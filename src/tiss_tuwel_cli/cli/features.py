"""
Additional valuable features for the TU Wien Companion CLI.

This module provides advanced features that enhance the CLI experience:
- Calendar export (ICS format)
- Course statistics dashboard
- Calendar export (ICS format)
- Course statistics dashboard
- Course workload comparison
"""

import hashlib
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Study time estimation constants (in hours)
# Removed deprecated constants


def export_calendar(output_file: Optional[str] = None):
    """
    Export upcoming deadlines to ICS calendar format.
    
    Creates an ICS file that can be imported into calendar applications
    like Google Calendar, Apple Calendar, or Outlook.
    
    Args:
        output_file: Optional path for the output file. Defaults to
                    ~/Downloads/tuwel_calendar.ics
    """
    from tiss_tuwel_cli.cli import get_tuwel_client
    
    client = get_tuwel_client()
    
    with console.status("[bold green]Fetching calendar events...[/bold green]"):
        upcoming = client.get_upcoming_calendar()
        events = upcoming.get('events', [])
    
    if not events:
        rprint("[yellow]No upcoming events found to export.[/yellow]")
        return
    
    # Default output path
    if not output_file:
        output_file = str(Path.home() / "Downloads" / "tuwel_calendar.ics")
    
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Generate ICS content
    ics_lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//TU Wien Companion//TUWEL Calendar Export//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:TUWEL Deadlines",
        "X-WR-TIMEZONE:Europe/Vienna",
    ]
    
    for event in events:
        event_name = event.get('name', 'Unknown Event')
        course = event.get('course', {})
        course_name = course.get('fullname', course.get('shortname', ''))
        
        # Convert timestamp to datetime
        start_time = event.get('timestart', 0)
        if start_time:
            # Convert to UTC for proper ICS format
            dt = datetime.fromtimestamp(start_time, tz=timezone.utc)
            
            # Format for ICS (UTC with Z suffix)
            dtstart = dt.strftime('%Y%m%dT%H%M%SZ')
            dtend = (dt + timedelta(hours=1)).strftime('%Y%m%dT%H%M%SZ')
            
            # Generate stable unique ID using event properties
            event_id = event.get('id', 0)
            uid_base = f"{event_id}-{start_time}-{event_name}"
            uid_hash = hashlib.md5(uid_base.encode()).hexdigest()[:16]
            uid = f"tuwel-{uid_hash}@tuwel.tuwien.ac.at"
            
            # Add event
            ics_lines.extend([
                "BEGIN:VEVENT",
                f"UID:{uid}",
                f"DTSTAMP:{datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')}",
                f"DTSTART:{dtstart}",
                f"DTEND:{dtend}",
                f"SUMMARY:{event_name}",
                f"DESCRIPTION:Course: {course_name}",
                f"LOCATION:TUWEL",
                "STATUS:CONFIRMED",
                "END:VEVENT",
            ])
    
    ics_lines.append("END:VCALENDAR")
    
    # Write to file
    output_path.write_text('\n'.join(ics_lines))
    
    rprint(f"[bold green]✓ Calendar exported![/bold green]")
    rprint(f"[cyan]Location:[/cyan] {output_path}")
    rprint(f"[dim]Exported {len(events)} events[/dim]")
    rprint()
    rprint("[dim]💡 Import this file into Google Calendar, Apple Calendar, or Outlook.[/dim]")


def course_statistics(course_id: Optional[int] = None):
    """
    Show detailed statistics for a course.
    
    Displays comprehensive statistics including progress, deadlines,
    completion rates, and time-based analytics.
    
    Args:
        course_id: Optional course ID. If not provided, shows a list to choose from.
    """
    from tiss_tuwel_cli.cli import config, get_tuwel_client
    
    client = get_tuwel_client()
    user_id = config.get_user_id()
    
    if not course_id:
        with console.status("[bold green]Fetching courses...[/bold green]"):
            courses = client.get_enrolled_courses('inprogress')
        
        if not courses:
            rprint("[yellow]No current courses found.[/yellow]")
            return
        
        rprint("[bold]Select a course:[/bold]")
        table = Table()
        table.add_column("ID", style="dim")
        table.add_column("Course", style="cyan")
        
        for course in courses:
            table.add_row(str(course.get('id')), course.get('fullname', 'Unknown'))
        
        console.print(table)
        return
    
    # Fetch comprehensive data
    with console.status("[bold green]Analyzing course data...[/bold green]"):
        try:
            # Get course info
            courses = client.get_enrolled_courses('inprogress')
            course_info = next((c for c in courses if c.get('id') == course_id), None)
            
            if not course_info:
                rprint(f"[red]Course {course_id} not found.[/red]")
                return
            
            # Get various data points
            grades_data = client.get_user_grades_table(course_id, user_id) if user_id else {}
            assignments_data = client.get_assignments()
            checkmarks_data = client.get_checkmarks([])
            calendar_data = client.get_upcoming_calendar()
            
        except Exception as e:
            rprint(f"[red]Error fetching course data: {e}[/red]")
            return
    
    # Display comprehensive statistics
    course_name = course_info.get('fullname', 'Unknown Course')
    
    rprint(Panel(
        f"[bold cyan]{course_name}[/bold cyan]\n"
        f"[dim]Course ID: {course_id} | Code: {course_info.get('shortname', 'N/A')}[/dim]",
        title="📊 Course Statistics"
    ))
    rprint()
    
    # === GRADE ANALYSIS ===
    tables = grades_data.get('tables', [])
    if tables and tables[0].get('tabledata'):
        table_data = tables[0].get('tabledata', [])
        
        # Find total/gesamt grade
        from tiss_tuwel_cli.utils import parse_percentage, strip_html
        
        for item in table_data:
            raw_name = item.get('itemname', {}).get('content', '')
            clean_name = strip_html(raw_name) if raw_name else ''
            
            if 'gesamt' in clean_name.lower() or 'total' in clean_name.lower():
                percent_raw = item.get('percentage', {}).get('content', '')
                pct = parse_percentage(strip_html(percent_raw))
                
                if pct is not None:
                    # Grade display
                    if pct >= 87.5:
                        grade = "1 (Excellent)"
                        color = "green"
                    elif pct >= 75:
                        grade = "2 (Good)"
                        color = "green"
                    elif pct >= 62.5:
                        grade = "3 (Satisfactory)"
                        color = "yellow"
                    elif pct >= 50:
                        grade = "4 (Sufficient)"
                        color = "yellow"
                    else:
                        grade = "5 (Fail)"
                        color = "red"
                    
                    rprint(Panel(
                        f"Current Grade: [{color}]{pct:.1f}%[/{color}] - [{color}]{grade}[/{color}]",
                        title="🎯 Performance"
                    ))
                    rprint()
                break
    
    # === ASSIGNMENTS ===
    courses_with_assignments = assignments_data.get('courses', [])
    course_assignments = next(
        (c for c in courses_with_assignments if c.get('id') == course_id),
        None
    )
    
    if course_assignments:
        assigns = course_assignments.get('assignments', [])
        now = datetime.now().timestamp()
        
        pending = [a for a in assigns if a.get('duedate', 0) > now]
        completed = [a for a in assigns if a.get('duedate', 0) <= now]
        
        rprint("[bold]📝 Assignments[/bold]")
        rprint(f"  Pending: [yellow]{len(pending)}[/yellow]")
        rprint(f"  Completed: [green]{len(completed)}[/green]")
        rprint(f"  Total: [cyan]{len(assigns)}[/cyan]")
        rprint()
    
    # === CHECKMARKS ===
    checkmarks_list = checkmarks_data.get('checkmarks', [])
    course_checkmarks = [cm for cm in checkmarks_list if cm.get('course') == course_id]
    
    if course_checkmarks:
        total_checked = 0
        total_possible = 0
        
        for cm in course_checkmarks:
            examples = cm.get('examples', [])
            total_checked += sum(1 for ex in examples if ex.get('checked'))
            total_possible += len(examples)
        
        completion = (total_checked / total_possible * 100) if total_possible > 0 else 0
        
        rprint("[bold]✅ Kreuzerlübungen[/bold]")
        rprint(f"  Completion: [cyan]{total_checked}/{total_possible}[/cyan] ([yellow]{completion:.0f}%[/yellow])")
        rprint()
    
    # === UPCOMING EVENTS ===
    events = calendar_data.get('events', [])
    course_events = [
        e for e in events
        if e.get('course', {}).get('id') == course_id
    ]
    
    if course_events:
        rprint("[bold]📅 Upcoming Deadlines[/bold]")
        for event in course_events[:5]:
            from tiss_tuwel_cli.utils import timestamp_to_date
            date_str = timestamp_to_date(event.get('timestart'))
            event_name = event.get('name', 'Unknown')
            rprint(f"  • {date_str} - {event_name}")
        rprint()
    
    rprint("[dim]💡 Tip: Use this information to plan your study time effectively![/dim]")







def unified_course_view(course_id: Optional[int] = None):
    """
    Show a unified view combining TISS and TUWEL data for courses.
    
    Displays course information from both platforms side-by-side, showing:
    - TISS: Course details, ECTS, type, exam dates
    - TUWEL: Assignments, grades, progress
    
    Args:
        course_id: Optional specific course ID. If omitted, shows all current courses.
    """
    from tiss_tuwel_cli.cli import get_tuwel_client
    from tiss_tuwel_cli.clients.tiss import TissClient
    from tiss_tuwel_cli.utils import extract_course_number, get_current_semester, timestamp_to_date
    
    client = get_tuwel_client()
    tiss = TissClient()
    
    if course_id:
        # Show single course
        with console.status("[bold green]Fetching course data...[/bold green]"):
            courses = [c for c in client.get_enrolled_courses('inprogress') if c.get('id') == course_id]
            if not courses:
                rprint(f"[red]Course ID {course_id} not found in current courses.[/red]")
                return
    else:
        # Show all courses
        with console.status("[bold green]Fetching courses...[/bold green]"):
            courses = client.get_enrolled_courses('inprogress')
    
    if not courses:
        rprint("[yellow]No courses found.[/yellow]")
        return
    
    semester = get_current_semester()
    
    for course in courses:
        cid = course.get('id')
        fullname = course.get('fullname', 'Unknown')
        shortname = course.get('shortname', '')
        
        # Extract course number and try to fetch TISS data
        course_num = extract_course_number(shortname)
        
        console.print()
        console.print(f"[bold cyan]{'=' * 80}[/bold cyan]")
        console.print(f"[bold white]{fullname}[/bold white]")
        console.print(f"[dim]TUWEL ID: {cid} | Code: {shortname}[/dim]")
        console.print()
        
        # Create side-by-side panels
        tiss_content = ""
        tuwel_content = ""
        
        # Fetch TISS data
        if course_num:
            tiss_content += f"[bold]Course Number:[/bold] {course_num}\n"
            try:
                details = tiss.get_course_details(course_num, semester)
                if details and 'error' not in details:
                    ects = details.get('ects', 'N/A')
                    course_type = details.get('courseType', {})
                    type_name = course_type.get('name') if isinstance(course_type, dict) else 'N/A'
                    
                    tiss_content += f"[bold]ECTS:[/bold] {ects}\n"
                    tiss_content += f"[bold]Type:[/bold] {type_name}\n"
                    
                    # Get exam dates
                    exams = tiss.get_exam_dates(course_num)
                    if isinstance(exams, list) and exams:
                        tiss_content += f"\n[bold cyan]📅 Upcoming Exams:[/bold cyan]\n"
                        for exam in exams[:3]:
                            date = exam.get('date', 'N/A')
                            mode = exam.get('mode', 'Unknown')
                            tiss_content += f"  • {date} - {mode}\n"
                    else:
                        tiss_content += "\n[dim]No exam dates available[/dim]"
                else:
                    tiss_content += "[dim]Course details not found in TISS[/dim]"
            except Exception as e:
                tiss_content += f"[dim]Error fetching TISS data: {str(e)[:50]}[/dim]"
        else:
            tiss_content = "[dim]Course number not found\nCannot fetch TISS data[/dim]"
        
        # Fetch TUWEL data - assignments
        try:
            assignments_data = client.get_assignments()
            course_assignments = []
            for c in assignments_data.get('courses', []):
                if c.get('id') == cid:
                    course_assignments = c.get('assignments', [])
                    break
            
            if course_assignments:
                now = datetime.now().timestamp()
                pending = [a for a in course_assignments if a.get('duedate', 0) > now]
                overdue = [a for a in course_assignments if a.get('duedate', 0) < now and a.get('duedate', 0) > now - (30*86400)]
                
                tuwel_content += f"[bold cyan]📝 Assignments:[/bold cyan]\n"
                tuwel_content += f"  Pending: [yellow]{len(pending)}[/yellow]\n"
                tuwel_content += f"  Overdue: [red]{len(overdue)}[/red]\n"
                
                if pending:
                    tuwel_content += "\n[bold]Next Deadlines:[/bold]\n"
                    for a in sorted(pending, key=lambda x: x.get('duedate', 0))[:3]:
                        name = a.get('name', 'Unknown')
                        due_str = timestamp_to_date(a.get('duedate'))
                        tuwel_content += f"  • {name}\n    [dim]{due_str}[/dim]\n"
            else:
                tuwel_content += "[bold cyan]📝 Assignments:[/bold cyan]\n"
                tuwel_content += "[dim]No assignments found[/dim]\n"
            
            # Try to get checkmarks
            try:
                checkmarks_data = client.get_checkmarks([cid])
                checkmarks = checkmarks_data.get('checkmarks', [])
                if checkmarks:
                    total_checked = 0
                    total_possible = 0
                    for cm in checkmarks:
                        examples = cm.get('examples', [])
                        total_checked += sum(1 for ex in examples if ex.get('checked'))
                        total_possible += len(examples)
                    
                    if total_possible > 0:
                        pct = (total_checked / total_possible * 100)
                        tuwel_content += f"\n[bold cyan]✅ Checkmarks:[/bold cyan]\n"
                        tuwel_content += f"  Progress: {total_checked}/{total_possible} ([green]{pct:.0f}%[/green])\n"
            except Exception:
                pass  # Checkmarks not available for all courses
                
        except Exception as e:
            tuwel_content += f"[dim]Error fetching TUWEL data: {str(e)[:50]}[/dim]"
        
        # Display side-by-side panels
        from rich.columns import Columns
        
        tiss_panel = Panel(tiss_content, title="🔍 TISS Data", border_style="cyan", expand=True)
        tuwel_panel = Panel(tuwel_content, title="📚 TUWEL Data", border_style="green", expand=True)
        
        console.print(Columns([tiss_panel, tuwel_panel], equal=True, expand=True))
    
    console.print()
    console.print(f"[bold cyan]{'=' * 80}[/bold cyan]")
    console.print()
    rprint("[dim]💡 Use this view to see all information about your courses at a glance![/dim]")
