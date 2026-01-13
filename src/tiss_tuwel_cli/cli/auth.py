"""
Authentication commands for the TU Wien Companion CLI.

This module provides commands for logging in and configuring
TUWEL authentication tokens.
"""

import time
import typer
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeoutError
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress
from rich.prompt import Prompt

from tiss_tuwel_cli.clients.tuwel import TuwelClient
from tiss_tuwel_cli.config import ConfigManager
from tiss_tuwel_cli.utils import parse_mobile_token

console = Console()
config = ConfigManager()


def login(
    manual: bool = typer.Option(False, "--manual", help="Start manual login by pasting a token URL instead of automating."),
    debug: bool = typer.Option(False, "--debug", help="Enable debug mode with non-headless browser and verbose logs.")
):
    """
    [Automated] Launches a browser to log in and captures the TUWEL token automatically.
    
    This command uses Playwright to automate the TUWEL login process.
    It can store your credentials in a local config.json file for fully automated
    future logins.
    """
    if manual:
        manual_login()
        return

    try:
        # This is just to guide the user to install the browser extras
        from playwright.sync_api import sync_playwright
    except ImportError:
        rprint("[bold red]Playwright is not installed.[/bold red]")
        rprint("Please run: [green]pip install 'tiss-tuwel-cli[browser]'[/green]")
        rprint("After installation, run: [green]playwright install[/green] to set up the browsers.")
        return

    rprint("[yellow]Attempting automated TUWEL login...[/yellow]")

    user, passw = config.get_login_credentials()

    if not all([user, passw]):
        rprint("[cyan]No stored credentials found.[/cyan]")
        rprint("You can store your TUWEL credentials to enable fully automated logins.")

        save_creds = Prompt.ask("Store credentials for future logins?", choices=["y", "n"], default="y") == "y"

        if save_creds:
            rprint("[bold yellow]Warning:[/bold yellow] Credentials will be stored in plain text in your home directory.")
            rprint(f"Location: {config.config_file}")
            proceed = Prompt.ask("Continue?", choices=["y", "n"], default="y") == "y"
            if not proceed:
                rprint("[red]Aborted.[/red]")
                return

            user = Prompt.ask("Enter TUWEL Username")
            passw = Prompt.ask("Enter TUWEL Password", password=True)
            config.set_login_credentials(user, passw)
            rprint("[green]Credentials saved.[/green]")
        else:
            user = Prompt.ask("Enter TUWEL Username")
            passw = Prompt.ask("Enter TUWEL Password", password=True)

    with Progress() as progress:
        task = progress.add_task("[cyan]Logging in...", total=4)

        try:
            with sync_playwright() as p:
                storage_state_path = config.config_dir / "browser_state.json"

                if debug:
                    rprint("[bold magenta]DEBUG MODE ENABLED[/bold magenta]")

                browser = p.chromium.launch(headless=not debug)
                context = browser.new_context(storage_state=storage_state_path if storage_state_path.exists() else None)
                page = context.new_page()

                if debug:
                    # Log all requests and responses
                    page.on("request", lambda request: rprint(f"[magenta]>> Request: {request.method} {request.url}[/magenta]"))
                    page.on("response", lambda response: rprint(f"[magenta]<< Response: {response.status} {response.url}[/magenta]"))

                # 1. Go to login page
                progress.update(task, description="[cyan]Navigating to TUWEL...", advance=1)
                page.goto("https://tuwel.tuwien.ac.at/login/index.php")
                if debug:
                    rprint(f"[magenta]On page: {page.title()} ({page.url})[/magenta]")

                # If already logged in, we might be on the dashboard or a confirmation page
                is_logged_in = "dashboard" in page.url or "bereits als" in page.content()
                if is_logged_in:
                    progress.update(task, description="[cyan]Already logged in...", advance=3)
                    if debug:
                        rprint("[magenta]Dashboard URL or existing session detected, assuming already logged in.[/magenta]")
                else:
                    # 2. Click TU Wien Login button
                    progress.update(task, description="[cyan]Redirecting to IdP...", advance=1)
                    page.wait_for_selector('a:has-text("TU Wien Login")').click()
                    if debug:
                        page.wait_for_load_state('networkidle')
                        rprint(f"[magenta]On page: {page.title()} ({page.url})[/magenta]")

                    # 3. Fill and submit credentials
                    progress.update(task, description="[cyan]Submitting credentials...", advance=1)
                    page.fill('input[name="username"]', user)
                    page.fill('input[name="password"]', passw)
                    page.click('button:has-text("Log in")')
                    if debug:
                        page.wait_for_load_state('networkidle')
                        rprint(f"[magenta]On page: {page.title()} ({page.url})[/magenta]")

                # 4. Wait for the token page and capture the URL
                progress.update(task, description="[cyan]Capturing token...", advance=1)

                token_url = ""

                def on_request(request):
                    nonlocal token_url
                    if "moodlemobile://token=" in request.url:
                        token_url = request.url
                        if debug:
                            rprint(f"[bold green]>>> TOKEN URL CAPTURED: {request.url}[/bold green]")

                page.on("request", on_request)

                try:
                    page.goto("https://tuwel.tuwien.ac.at/admin/tool/mobile/launch.php?service=moodle_mobile_app&passport=student_api")
                except PlaywrightTimeoutError:
                    # This is expected if the page redirects to the custom protocol
                    if debug:
                        rprint("[magenta]Page.goto timed out as expected due to moodlemobile:// redirect.[/magenta]")
                    pass
                except Exception as e:
                    # Also ignore the ERR_ABORTED error which can happen
                    if "net::ERR_ABORTED" not in str(e):
                        raise e
                    if debug:
                        rprint(f"[magenta]Ignoring expected error: {e}[/magenta]")


                # Wait for the on_request handler to capture the token, polling instead of static wait
                wait_seconds = 30 if debug else 10
                if debug:
                    rprint(f"[magenta]Waiting for token capture for up to {wait_seconds}s...[/magenta]")

                end_time = time.time() + wait_seconds
                while time.time() < end_time:
                    if token_url:
                        if debug:
                            rprint("[magenta]Token found, proceeding immediately.[/magenta]")
                        break
                    page.wait_for_timeout(100)  # poll every 100ms

                if debug and not token_url:
                    rprint("[bold red]DEBUG: Timed out waiting for token.[/bold red]")
                    rprint("[bold red]Dumping page content:[/bold red]")
                    try:
                        rprint(page.content())
                    except Exception as e:
                        rprint(f"[bold red]Could not get page content: {e}[/bold red]")

                # Save the session state for the next run
                context.storage_state(path=storage_state_path)
                if debug:
                    rprint(f"[magenta]Browser state saved to {storage_state_path}[/magenta]")

                browser.close()

        except PlaywrightTimeoutError as e:
            rprint("[bold red]Login failed: Timed out waiting for a page element.[/bold red]")
            rprint("This could be due to a slow connection or a change in TUWEL's page structure.")
            if debug:
                rprint(f"[magenta]Playwright error: {e}[/magenta]")
            return
        except Exception as e:
            rprint(f"[bold red]An unexpected error occurred:[/bold red] {e}")
            return

    if not token_url:
        rprint("[bold red]Failed to capture the token URL.[/bold red]")
        rprint("It's possible the login failed or the page structure has changed.")
        return

    found_token = parse_mobile_token(token_url)

    if found_token:
        config.set_tuwel_token(found_token)
        rprint("[bold green]Token captured successfully![/bold green]")

        # Verify the token
        try:
            client = TuwelClient(found_token)
            info = client.get_site_info()
            config.set_user_id(info.get('userid', 0))
            rprint(f"Authenticated as [cyan]{info.get('fullname')}[/cyan] (ID: {info.get('userid')}).")
        except Exception as e:
            # Even if validation fails, save the token
            rprint(f"[yellow]Warning: Token captured but validation failed: {e}[/yellow]")
            rprint("[dim]The token was saved anyway. Try running [green]tiss-tuwel-cli dashboard[/green] "
                   "to see if it works.[/dim]")
    else:
        rprint("[red]Could not parse token from URL.[/red]")


def manual_login():
    """
    [Manual] Configure TUWEL token by pasting the redirect URL.
    
    This command guides you through manually obtaining and configuring
    your TUWEL authentication token. Use this if the automated login
    doesn't work.
    """
    console.print(Panel("[bold blue]TU Wien Companion Login[/bold blue]", expand=False))
    rprint("1. Go to: [link]https://tuwel.tuwien.ac.at/admin/tool/mobile/launch.php"
           "?service=moodle_mobile_app&passport=student_api[/link]")
    rprint("2. Login and wait for the 'Address not understood' or failed redirect page.")
    rprint("3. Copy the [bold]entire URL[/bold] from the address bar (starting with moodlemobile://) or find it in the developer console or in the network tab.")

    user_input = Prompt.ask("Paste URL or Token")

    token = parse_mobile_token(user_input)

    # If parsing failed, maybe they pasted the raw token directly?
    if not token and ":::" not in user_input and "token=" not in user_input:
        token = user_input

    if not token:
        rprint("[bold red]Invalid input format.[/bold red]")
        return

    try:
        client = TuwelClient(token)
        info = client.get_site_info()
        user_id = info.get('userid', 0)
        config.set_tuwel_token(token)
        config.set_user_id(user_id)
        rprint(f"[bold green]Success![/bold green] Authenticated as [cyan]{info.get('fullname')}[/cyan].")
    except Exception as e:
        rprint(f"[bold red]Authentication failed:[/bold red] {e}")
