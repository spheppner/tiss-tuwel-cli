"""
Dashboard command for the TU Wien Companion CLI.

This module provides the main dashboard view showing upcoming
events and deadlines from both TUWEL and TISS.
"""

from rich import print as rprint
from rich.console import Console
from rich.table import Table

from tiss_tuwel_cli.clients.tiss import TissClient
from tiss_tuwel_cli.utils import timestamp_to_date

console = Console()
tiss = TissClient()


def dashboard():
    """
    Overview of upcoming events.
    
    Shows upcoming TUWEL deadlines and TISS public events in a
    formatted table view.
    """
    # Import here to avoid circular imports
    from tiss_tuwel_cli.cli import get_tuwel_client
    
    client = get_tuwel_client()
    with console.status("[bold green]Fetching data...[/bold green]"):
        try:
            upcoming = client.get_upcoming_calendar()
            events = upcoming.get('events', [])
            tiss_events = tiss.get_public_events()
        except Exception as e:
            rprint(f"[bold red]Error:[/bold red] {e}")
            return

    # TUWEL Deadlines Table
    tuwel_table = Table(title="[bold blue]Upcoming TUWEL Deadlines[/bold blue]", expand=True)
    tuwel_table.add_column("Course", style="cyan")
    tuwel_table.add_column("Event", style="white")
    tuwel_table.add_column("Date", style="green")

    for event in events:
        tuwel_table.add_row(
            event.get('course', {}).get('shortname', 'Unknown'),
            event.get('name'),
            timestamp_to_date(event.get('timestart'))
        )

    console.print(tuwel_table)
    rprint("\n")

    # TISS Events Table
    if isinstance(tiss_events, list) and len(tiss_events) > 0:
        tiss_table = Table(title="[bold yellow]TISS Public Events[/bold yellow]", expand=True)
        tiss_table.add_column("Description", style="white")
        tiss_table.add_column("Time", style="green")
        for event in tiss_events[:3]:
            tiss_table.add_row(event.get('description', ''), event.get('begin', ''))
        console.print(tiss_table)
