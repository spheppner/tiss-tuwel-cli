"""
Additional valuable features for the TU Wien Companion CLI.

This module provides advanced features that enhance the CLI experience:
- Calendar export (ICS format)
- Course statistics dashboard
- Study time estimator
- Assignment submission tracker
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
HOURS_PER_ASSIGNMENT = 3.0
HOURS_PER_CHECKMARK = 0.5
HOURS_PER_EVENT_PREP = 1.0


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


def estimate_study_time():
    """
    Estimate study time needed based on pending work.
    
    Analyzes pending assignments, checkmarks, and deadlines to provide
    an estimate of study time needed for the upcoming week.
    """
    from tiss_tuwel_cli.cli import get_tuwel_client
    
    client = get_tuwel_client()
    
    with console.status("[bold green]Analyzing workload...[/bold green]"):
        assignments_data = client.get_assignments()
        checkmarks_data = client.get_checkmarks([])
        calendar_data = client.get_upcoming_calendar()
    
    now = datetime.now().timestamp()
    week_later = now + (7 * 86400)
    
    # Count pending work this week
    courses_with_assignments = assignments_data.get('courses', [])
    
    assignments_this_week = []
    for course in courses_with_assignments:
        for assign in course.get('assignments', []):
            due = assign.get('duedate', 0)
            if now < due <= week_later:
                assignments_this_week.append({
                    'course': course.get('fullname', 'Unknown'),
                    'name': assign.get('name'),
                    'due': due
                })
    
    # Count incomplete checkmarks
    checkmarks_list = checkmarks_data.get('checkmarks', [])
    incomplete_checkmarks = []
    
    for cm in checkmarks_list:
        examples = cm.get('examples', [])
        unchecked = sum(1 for ex in examples if not ex.get('checked'))
        if unchecked > 0:
            incomplete_checkmarks.append({
                'course_id': cm.get('course'),
                'name': cm.get('name'),
                'unchecked': unchecked,
                'total': len(examples)
            })
    
    # Events this week
    events = calendar_data.get('events', [])
    events_this_week = [
        e for e in events
        if now < e.get('timestart', 0) <= week_later
    ]
    
    # Estimate time using configured constants
    assignment_time = len(assignments_this_week) * HOURS_PER_ASSIGNMENT
    checkmark_time = sum(cm['unchecked'] * HOURS_PER_CHECKMARK for cm in incomplete_checkmarks)
    event_prep_time = len(events_this_week) * HOURS_PER_EVENT_PREP
    
    total_estimated = assignment_time + checkmark_time + event_prep_time
    
    # Display
    rprint(Panel("[bold]Study Time Estimation for This Week[/bold]", expand=False))
    rprint()
    
    table = Table(title="Workload Analysis", expand=True)
    table.add_column("Category", style="cyan")
    table.add_column("Count", justify="center", style="white")
    table.add_column("Estimated Time", justify="right", style="yellow")
    
    table.add_row(
        "Assignments due",
        str(len(assignments_this_week)),
        f"{assignment_time:.0f}h"
    )
    table.add_row(
        "Checkmarks incomplete",
        str(sum(cm['unchecked'] for cm in incomplete_checkmarks)),
        f"{checkmark_time:.0f}h"
    )
    table.add_row(
        "Events/Deadlines",
        str(len(events_this_week)),
        f"{event_prep_time:.0f}h"
    )
    table.add_row(
        "[bold]Total Estimated[/bold]",
        "",
        f"[bold yellow]{total_estimated:.0f}h[/bold yellow]"
    )
    
    console.print(table)
    rprint()
    
    # Recommendations
    if total_estimated > 40:
        rprint("[bold red]⚠️ Heavy workload ahead![/bold red]")
        rprint("[dim]Consider prioritizing tasks and seeking help if needed.[/dim]")
    elif total_estimated > 20:
        rprint("[bold yellow]📚 Moderate workload[/bold yellow]")
        rprint("[dim]Plan your study sessions carefully.[/dim]")
    else:
        rprint("[bold green]✓ Manageable workload[/bold green]")
        rprint("[dim]Good time to get ahead or review material![/dim]")
    
    rprint()
    rprint("[dim]💡 Note: These are rough estimates. Actual time may vary based on")
    rprint("   difficulty, your familiarity with the material, and personal pace.[/dim]")


def compare_courses():
    """
    Compare workload and progress across all courses.
    
    Shows a comparative view of all current courses to help identify
    which courses need more attention.
    """
    from tiss_tuwel_cli.cli import config, get_tuwel_client
    
    client = get_tuwel_client()
    user_id = config.get_user_id()
    
    with console.status("[bold green]Analyzing all courses...[/bold green]"):
        courses = client.get_enrolled_courses('inprogress')
        assignments_data = client.get_assignments()
        checkmarks_data = client.get_checkmarks([])
        
        # Gather data for each course
        course_stats = []
        
        for course in courses:
            cid = course.get('id')
            stats = {
                'id': cid,
                'name': course.get('fullname', 'Unknown'),
                'code': course.get('shortname', ''),
                'pending_assignments': 0,
                'checkmark_completion': 0,
                'grade_pct': None
            }
            
            # Count pending assignments
            now = datetime.now().timestamp()
            courses_with_assignments = assignments_data.get('courses', [])
            course_assigns = next(
                (c for c in courses_with_assignments if c.get('id') == cid),
                None
            )
            if course_assigns:
                assigns = course_assigns.get('assignments', [])
                stats['pending_assignments'] = sum(
                    1 for a in assigns if a.get('duedate', 0) > now
                )
            
            # Calculate checkmark completion
            checkmarks_list = checkmarks_data.get('checkmarks', [])
            course_checkmarks = [cm for cm in checkmarks_list if cm.get('course') == cid]
            
            if course_checkmarks:
                total_checked = 0
                total_possible = 0
                
                for cm in course_checkmarks:
                    examples = cm.get('examples', [])
                    total_checked += sum(1 for ex in examples if ex.get('checked'))
                    total_possible += len(examples)
                
                if total_possible > 0:
                    stats['checkmark_completion'] = (total_checked / total_possible * 100)
            
            # Get grade if available
            if user_id:
                try:
                    from tiss_tuwel_cli.utils import parse_percentage, strip_html
                    
                    grades = client.get_user_grades_table(cid, user_id)
                    tables = grades.get('tables', [])
                    
                    if tables:
                        table_data = tables[0].get('tabledata', [])
                        for item in table_data:
                            raw_name = item.get('itemname', {}).get('content', '')
                            clean_name = strip_html(raw_name) if raw_name else ''
                            
                            if 'gesamt' in clean_name.lower() or 'total' in clean_name.lower():
                                percent_raw = item.get('percentage', {}).get('content', '')
                                pct = parse_percentage(strip_html(percent_raw))
                                if pct is not None:
                                    stats['grade_pct'] = pct
                                break
                except Exception:
                    pass
            
            course_stats.append(stats)
    
    # Display comparison
    rprint(Panel("[bold]Course Workload Comparison[/bold]", expand=False))
    rprint()
    
    table = Table(title="All Courses Overview", expand=True, show_header=True, header_style="bold cyan")
    table.add_column("Course", style="cyan", no_wrap=False)
    table.add_column("Pending\nAssignments", justify="center")
    table.add_column("Checkmark\nProgress", justify="center", no_wrap=False)
    table.add_column("Current\nGrade", justify="center")
    table.add_column("Status", justify="center")
    
    for stats in course_stats:
        # Determine status/priority
        priority_score = 0
        
        if stats['pending_assignments'] > 3:
            priority_score += 2
        elif stats['pending_assignments'] > 0:
            priority_score += 1
        
        if stats['checkmark_completion'] < 50:
            priority_score += 2
        elif stats['checkmark_completion'] < 80:
            priority_score += 1
        
        if stats['grade_pct'] and stats['grade_pct'] < 50:
            priority_score += 2
        elif stats['grade_pct'] and stats['grade_pct'] < 75:
            priority_score += 1
        
        # Status indicator
        if priority_score >= 4:
            status = "[bold red]⚠️ High[/bold red]"
        elif priority_score >= 2:
            status = "[yellow]⚡ Medium[/yellow]"
        else:
            status = "[green]✓ On Track[/green]"
        
        # Format columns
        assignments_str = (
            f"[red]{stats['pending_assignments']}[/red]"
            if stats['pending_assignments'] > 2
            else f"[yellow]{stats['pending_assignments']}[/yellow]"
            if stats['pending_assignments'] > 0
            else "[green]0[/green]"
        )
        
        # Create visual progress bar for checkmarks
        if stats['checkmark_completion'] > 0:
            completion = stats['checkmark_completion']
            bar_length = 10
            filled = int(completion / 100 * bar_length)
            bar = "█" * filled + "░" * (bar_length - filled)
            
            if completion >= 80:
                color = "green"
            elif completion >= 50:
                color = "yellow"
            else:
                color = "red"
            
            checkmark_str = f"[{color}]{bar}[/{color}] {completion:.0f}%"
        else:
            checkmark_str = "[dim]No data[/dim]"
        
        grade_str = (
            f"[green]{stats['grade_pct']:.0f}%[/green]"
            if stats['grade_pct'] and stats['grade_pct'] >= 75
            else f"[yellow]{stats['grade_pct']:.0f}%[/yellow]"
            if stats['grade_pct'] and stats['grade_pct'] >= 50
            else f"[red]{stats['grade_pct']:.0f}%[/red]"
            if stats['grade_pct']
            else "[dim]N/A[/dim]"
        )
        
        table.add_row(
            stats['name'],
            assignments_str,
            checkmark_str,
            grade_str,
            status
        )
    
    console.print(table)
    rprint()
    rprint("[dim]💡 Focus on courses with 'High' or 'Medium' status to stay on track.[/dim]")


def submission_tracker():
    """
    Track assignment submission status.
    
    Shows which assignments have been submitted and which are still pending,
    helping ensure nothing is missed.
    """
    from tiss_tuwel_cli.cli import get_tuwel_client
    
    client = get_tuwel_client()
    
    with console.status("[bold green]Fetching assignment status...[/bold green]"):
        assignments_data = client.get_assignments()
        courses_with_assignments = assignments_data.get('courses', [])
    
    if not courses_with_assignments:
        rprint("[yellow]No assignments found.[/yellow]")
        return
    
    rprint(Panel("[bold]Assignment Submission Tracker[/bold]", expand=False))
    rprint()
    
    now = datetime.now().timestamp()
    
    for course in courses_with_assignments:
        course_name = course.get('fullname', 'Unknown Course')
        assignments = course.get('assignments', [])
        
        if not assignments:
            continue
        
        rprint(f"[bold cyan]{course_name}[/bold cyan]")
        
        table = Table(expand=True, show_header=True, box=None)
        table.add_column("Assignment", style="white", no_wrap=False)
        table.add_column("Due Date", style="dim")
        table.add_column("Status", justify="center")
        
        for assign in assignments:
            name = assign.get('name', 'Unknown')
            due = assign.get('duedate', 0)
            
            from tiss_tuwel_cli.utils import timestamp_to_date
            due_str = timestamp_to_date(due)
            
            # Determine status based on due date
            if due == 0:
                status = "[dim]No deadline[/dim]"
            elif due < now:
                # Check if it's very old (>30 days) - likely completed
                if due < now - (30 * 86400):
                    status = "[dim]Closed[/dim]"
                else:
                    status = "[red]⚠️ Overdue[/red]"
            else:
                days_left = (due - now) / 86400
                if days_left < 1:
                    status = "[bold red]📌 Due Today![/bold red]"
                elif days_left < 3:
                    status = f"[yellow]⏰ {days_left:.0f}d left[/yellow]"
                else:
                    status = f"[green]✓ {days_left:.0f}d left[/green]"
            
            table.add_row(name, due_str, status)
        
        console.print(table)
        rprint()
    
    rprint("[dim]💡 Tip: Mark your calendar when you submit assignments to track your progress![/dim]")


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
