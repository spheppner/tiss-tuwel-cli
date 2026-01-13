"""
Dashboard command for the TU Wien Companion CLI.

This module provides the main dashboard view showing upcoming
events and deadlines from both TUWEL and TISS with enhanced visuals.
"""

from datetime import datetime

from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.progress import BarColumn, Progress, TextColumn
from rich.table import Table

from tiss_tuwel_cli.clients.tiss import TissClient
from tiss_tuwel_cli.utils import timestamp_to_date

console = Console()
tiss = TissClient()


def dashboard():
    """
    Overview of upcoming events with enhanced visuals.
    
    Shows upcoming TUWEL deadlines and TISS public events in a
    formatted view with color-coded urgency and progress indicators.
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

    # Display header
    console.print()
    console.print(Panel(
        "[bold cyan]📊 Your TU Wien Dashboard[/bold cyan]\n"
        "[dim]Showing upcoming deadlines and events from TUWEL and TISS[/dim]",
        border_style="cyan"
    ))
    console.print()

    # TUWEL Deadlines Table with urgency colors
    tuwel_table = Table(
        title="[bold blue]📅 Upcoming TUWEL Deadlines[/bold blue]",
        expand=True,
        show_header=True,
        header_style="bold cyan"
    )
    tuwel_table.add_column("Course", style="cyan", no_wrap=False)
    tuwel_table.add_column("Event", style="white", no_wrap=False)
    tuwel_table.add_column("Date", style="green")
    tuwel_table.add_column("Urgency", justify="center")

    now = datetime.now().timestamp()
    for event in events[:15]:  # Show more events
        event_time = event.get('timestart', 0)
        days_left = (event_time - now) / 86400

        # Determine urgency indicator
        if days_left < 0:
            urgency = "[red]⚠️ Overdue[/red]"
            date_style = "red"
        elif days_left < 1:
            urgency = "[bold red]🔥 Today![/bold red]"
            date_style = "bold red"
        elif days_left < 3:
            urgency = "[yellow]⏰ Soon[/yellow]"
            date_style = "yellow"
        elif days_left < 7:
            urgency = "[green]📌 This Week[/green]"
            date_style = "green"
        else:
            urgency = "[dim]✓ OK[/dim]"
            date_style = "dim"

        course_name = event.get('course', {}).get('shortname', 'Unknown')
        event_name = event.get('name', 'Unknown Event')
        date_str = timestamp_to_date(event_time)

        tuwel_table.add_row(
            course_name,
            event_name,
            f"[{date_style}]{date_str}[/{date_style}]",
            urgency
        )

    console.print(tuwel_table)
    console.print()

    # Study progress overview
    pending_assignments = 0
    try:
        # Get assignments for progress calculation
        assignments_data = client.get_assignments()
        total_assignments = 0

        for course in assignments_data.get('courses', []):
            for assignment in course.get('assignments', []):
                due = assignment.get('duedate', 0)
                if due > now - (30 * 86400):  # Not older than 30 days
                    total_assignments += 1
                    if due > now:
                        pending_assignments += 1

        if total_assignments > 0:
            completed = total_assignments - pending_assignments
            completion_pct = (completed / total_assignments) * 100

            # Create progress bar
            progress = Progress(
                TextColumn("[bold blue]{task.description}"),
                BarColumn(bar_width=40),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            )

            task = progress.add_task(
                "Assignment Completion",
                total=total_assignments,
                completed=completed
            )

            console.print(Panel(
                progress,
                title="📊 Study Progress",
                border_style="green"
            ))
            console.print()
    except Exception:
        # Progress is optional, don't fail if it errors
        pass

    # TISS Events Table with improved styling
    if isinstance(tiss_events, list) and len(tiss_events) > 0:
        tiss_table = Table(
            title="[bold yellow]🎓 TISS Public Events[/bold yellow]",
            expand=True,
            show_header=True,
            header_style="bold yellow"
        )
        tiss_table.add_column("Description", style="white", no_wrap=False)
        tiss_table.add_column("Time", style="green")
        for event in tiss_events[:5]:  # Show more events
            tiss_table.add_row(
                event.get('description', ''),
                event.get('begin', '')
            )
        console.print(tiss_table)
        console.print()

    # Quick tips panel
    tips = []
    if events:
        urgent_count = sum(1 for e in events if (e.get('timestart', 0) - now) < 86400)
        if urgent_count > 0:
            tips.append(f"🔥 You have {urgent_count} deadline(s) in the next 24 hours!")

    if pending_assignments > 5:
        tips.append(f"📚 {pending_assignments} assignments pending - consider prioritizing!")

    if tips:
        tip_text = "\n".join(tips)
        console.print(Panel(tip_text, title="💡 Quick Tips", border_style="yellow"))
        console.print()
