"""
Authentication commands for the TU Wien Companion CLI.

This module provides commands for logging in and configuring
TUWEL authentication tokens.
"""

import json
import time

from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from tiss_tuwel_cli.config import ConfigManager
from tiss_tuwel_cli.clients.tuwel import TuwelClient
from tiss_tuwel_cli.utils import parse_mobile_token

console = Console()
config = ConfigManager()


def login():
    """
    [Automated] Launches a browser to log in and captures the TUWEL token automatically.
    
    Requires Chrome or Firefox installed with the corresponding WebDriver.
    This command opens a browser window where you can log in to TUWEL,
    and automatically captures the authentication token.
    """
    try:
        from selenium import webdriver
        from selenium.common.exceptions import WebDriverException
    except ImportError:
        rprint("[bold red]Selenium is not installed.[/bold red]")
        rprint("Please run: [green]pip install selenium[/green]")
        rprint("Or install with browser extras: [green]pip install tiss-tuwel-cli[browser][/green]")
        return

    rprint("[yellow]Launching browser... Please log in to TUWEL in the opened window.[/yellow]")
    rprint("[dim]The window will close automatically once the token is detected.[/dim]")

    login_url = "https://tuwel.tuwien.ac.at/admin/tool/mobile/launch.php?service=moodle_mobile_app&passport=student_api"

    # Enable performance logging to catch the redirect URL even if the browser blocks it
    options = webdriver.ChromeOptions()
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = None
    try:
        try:
            driver = webdriver.Chrome(options=options)
        except WebDriverException:
            # Fallback to Firefox (logging works differently, this might be less reliable)
            rprint("[yellow]Chrome not found, trying Firefox...[/yellow]")
            driver = webdriver.Firefox()

        driver.get(login_url)

        found_token = None

        # Poll loop to detect the token
        while not found_token:
            # Check 1: Current URL (if browser successfully navigated)
            current_url = driver.current_url
            if "moodlemobile://token=" in current_url:
                found_token = parse_mobile_token(current_url)
                break

            # Check 2: Performance Logs (if browser blocked navigation to unknown protocol)
            # This is specific to Chrome-based browsers
            if hasattr(driver, 'get_log'):
                try:
                    logs = driver.get_log('performance')
                    for entry in logs:
                        message = json.loads(entry.get('message', '{}')).get('message', {})
                        # Look for Network.requestWillBeSent with the custom scheme
                        params = message.get('params', {})
                        req_url = params.get('request', {}).get('url', '')
                        doc_url = params.get('documentURL', '')

                        if "moodlemobile://token=" in req_url:
                            found_token = parse_mobile_token(req_url)
                            break
                        if "moodlemobile://token=" in doc_url:
                            found_token = parse_mobile_token(doc_url)
                            break
                except Exception:
                    pass

            if found_token:
                break

            time.sleep(1)

            # Stop if user closed browser
            try:
                # This throws exception if window is closed
                _ = driver.window_handles
            except Exception:
                rprint("[red]Browser closed by user.[/red]")
                return

    except Exception as e:
        rprint(f"[bold red]Automation failed:[/bold red] {e}")
        rprint("Please use the manual [green]setup[/green] command instead.")
        return
    finally:
        if driver:
            driver.quit()

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
        rprint("[red]Could not capture token.[/red]")


def setup():
    """
    [Manual] Configure TUWEL token by pasting the redirect URL.
    
    This command guides you through manually obtaining and configuring
    your TUWEL authentication token. Use this if the automated login
    doesn't work.
    """
    console.print(Panel("[bold blue]TU Wien Companion Setup[/bold blue]", expand=False))
    rprint("1. Go to: [link]https://tuwel.tuwien.ac.at/admin/tool/mobile/launch.php"
           "?service=moodle_mobile_app&passport=student_api[/link]")
    rprint("2. Login and wait for the 'Address not understood' or failed redirect page.")
    rprint("3. Copy the [bold]entire URL[/bold] from the address bar (starting with moodlemobile://).")

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
