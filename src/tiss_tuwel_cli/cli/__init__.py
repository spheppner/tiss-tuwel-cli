"""
CLI commands for the TU Wien Companion.

This package contains the Typer-based CLI application and its commands
for interacting with TISS and TUWEL services.
"""

import typer
from rich import print as rprint
from rich.console import Console

from tiss_tuwel_cli.clients.tiss import TissClient
from tiss_tuwel_cli.clients.tuwel import TuwelClient
from tiss_tuwel_cli.config import ConfigManager

# Initialize the CLI application
app = typer.Typer(
    help="TU Wien Companion - TISS & TUWEL CLI",
    add_completion=False,
    invoke_without_command=True,
)

# Shared console and configuration instances
console = Console()
config = ConfigManager()
tiss = TissClient()


@app.callback()
def main(
        ctx: typer.Context,
        interactive: bool = typer.Option(
            False,
            "--interactive",
            "-i",
            help="Start in interactive menu mode",
        ),
):
    """
    TU Wien Companion - TISS & TUWEL CLI.

    Run without arguments to start an interactive shell.
    Use -i or --interactive to start in menu mode.
    """
    if interactive:
        from tiss_tuwel_cli.cli.interactive import interactive as run_interactive
        run_interactive()
        raise typer.Exit()
    elif ctx.invoked_subcommand is None:
        # No command and no interactive flag - start shell mode
        from tiss_tuwel_cli.cli.shell import start_shell
        start_shell()
        raise typer.Exit()


def get_tuwel_client(force_new_token: bool = False) -> TuwelClient:
    """
    Get an authenticated TUWEL client, automatically handling token validation and refresh.

    Args:
        force_new_token: If True, will force a new token to be fetched even if a valid one exists.

    Returns:
        An authenticated TuwelClient instance.

    Raises:
        typer.Exit: If no token can be obtained.
    """
    token = config.get_tuwel_token()

    # 1. If no token, try to log in
    if not token or force_new_token:
        user, _ = config.get_login_credentials()
        if user:
            rprint("[yellow]No valid token found. Attempting automatic re-login...[/yellow]")
            from tiss_tuwel_cli.cli.auth import _run_playwright_login_internal
            success = _run_playwright_login_internal(user, _, False) # silent=True -> debug=False
            if success:
                token = config.get_tuwel_token()
            else:
                rprint("[bold red]Error:[/bold red] Automatic login failed. Please run [green]tiss-tuwel-cli login[/green] manually.")
                raise typer.Exit()
        else:
            rprint("[bold red]Error:[/bold red] TUWEL token not found. Please run [green]tiss-tuwel-cli login[/green] first.")
            raise typer.Exit()

    client = TuwelClient(token)

    # 2. Validate existing token
    try:
        client.get_site_info()
    except Exception:
        # If validation fails, try to get a new token
        user, _ = config.get_login_credentials()
        if user:
            rprint("[yellow]Token is invalid or expired. Attempting automatic re-login...[/yellow]")
            from tiss_tuwel_cli.cli.auth import _run_playwright_login_internal
            success = _run_playwright_login_internal(user, _, False) # silent=True -> debug=False
            if success:
                new_token = config.get_tuwel_token()
                return TuwelClient(new_token)
            else:
                rprint("[bold red]Error:[/bold red] Automatic login failed. Please run [green]tiss-tuwel-cli login[/green] manually.")
                raise typer.Exit()
        else:
            rprint("[bold red]Error:[/bold red] Your TUWEL token is invalid. Please run [green]tiss-tuwel-cli login[/green] again.")
            raise typer.Exit()

    return client


# Import and register command modules
from tiss_tuwel_cli.cli import auth, courses, dashboard, features, timeline, todo

# Register commands
app.command()(auth.login)
app.command()(dashboard.dashboard)
app.command()(courses.courses)
app.command()(courses.assignments)
app.command()(courses.grades)
app.command()(courses.checkmarks)
app.command()(courses.download)
app.command()(courses.tiss_course)
app.command(name="track-participation")(courses.track_participation)
app.command(name="participation-stats")(courses.participation_stats)
app.command(name="open-vowi")(courses.open_vowi)

# Register new feature commands
app.command(name="export-calendar")(features.export_calendar)
app.command(name="course-stats")(features.course_statistics)
app.command(name="unified-view")(features.unified_course_view)

# New commands
app.command()(timeline.timeline)
app.command()(todo.todo)

__all__ = ["app", "console", "config", "tiss", "get_tuwel_client"]
