"""
CLI commands for the TU Wien Companion.

This package contains the Typer-based CLI application and its commands
for interacting with TISS and TUWEL services.
"""

import typer
from rich.console import Console
from rich import print as rprint

from tiss_tuwel_cli.config import ConfigManager
from tiss_tuwel_cli.clients.tiss import TissClient
from tiss_tuwel_cli.clients.tuwel import TuwelClient

# Initialize the CLI application
app = typer.Typer(
    help="TU Wien Companion - TISS & TUWEL CLI",
    add_completion=False,
)

# Shared console and configuration instances
console = Console()
config = ConfigManager()
tiss = TissClient()


def get_tuwel_client() -> TuwelClient:
    """
    Get an authenticated TUWEL client.
    
    Returns:
        An authenticated TuwelClient instance.
        
    Raises:
        typer.Exit: If no TUWEL token is configured.
    """
    token = config.get_tuwel_token()
    if not token:
        rprint("[bold red]Error:[/bold red] TUWEL token not found. "
               "Please run [green]setup[/green] or [green]login[/green] first.")
        raise typer.Exit()
    return TuwelClient(token)


# Import and register command modules
from tiss_tuwel_cli.cli import auth
from tiss_tuwel_cli.cli import courses
from tiss_tuwel_cli.cli import dashboard

# Register commands from submodules
app.command()(auth.login)
app.command()(auth.setup)
app.command()(dashboard.dashboard)
app.command()(courses.courses)
app.command()(courses.assignments)
app.command()(courses.grades)
app.command()(courses.checkmarks)
app.command()(courses.download)
app.command()(courses.tiss_course)


__all__ = ["app", "console", "config", "tiss", "get_tuwel_client"]
