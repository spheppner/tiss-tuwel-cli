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
from tiss_tuwel_cli.cli import auth, courses, dashboard, features

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
app.command(name="track-participation")(courses.track_participation)
app.command(name="participation-stats")(courses.participation_stats)
app.command(name="open-vowi")(courses.open_vowi)

# Register new feature commands
app.command(name="export-calendar")(features.export_calendar)
app.command(name="course-stats")(features.course_statistics)
app.command(name="study-time")(features.estimate_study_time)
app.command(name="compare-courses")(features.compare_courses)
app.command(name="submission-tracker")(features.submission_tracker)
app.command(name="unified-view")(features.unified_course_view)


__all__ = ["app", "console", "config", "tiss", "get_tuwel_client"]
