"""
Unified Timeline command merging TUWEL events and TISS exams.
"""

from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from tiss_tuwel_cli.cli import get_tuwel_client
from tiss_tuwel_cli.clients.tiss import TissClient
from tiss_tuwel_cli.utils import extract_course_number, timestamp_to_date

console = Console()

def timeline(export: bool = False, output: Optional[str] = None):
    """
    Show a unified timeline of TUWEL assignments and TISS exams.
    
    Args:
        export: If True, export the timeline to an .ics file.
        output: Optional output path for the .ics file.
    """
    client = get_tuwel_client()
    tiss = TissClient()

    with console.status("[bold green]Fetching data...[/bold green]"):
        # 1. Fetch TUWEL Calendar (Upcoming view)
        upcoming = client.get_upcoming_calendar()
        tuwel_events = upcoming.get('events', [])
        
        # 2. Fetch Enrolled Courses (to map to TISS)
        courses = client.get_enrolled_courses('inprogress')
        
        # 3. Fetch TISS Exams for each course
        tiss_exams = []
        for course in courses:
            shortname = course.get('shortname', '')
            course_num = extract_course_number(shortname)
            if course_num:
                exams = tiss.get_exam_dates(course_num)
                if isinstance(exams, list):
                    for exam in exams:
                        # Enrich with course info
                        exam['course_name'] = course.get('fullname', shortname)
                        exam['course_short'] = shortname
                        exam['source'] = 'TISS'
                        tiss_exams.append(exam)

    # 4. Merge Events
    timeline_events = []
    
    # Process TUWEL events
    for event in tuwel_events:
        start_ts = event.get('timestart', 0)
        course = event.get('course', {})
        timeline_events.append({
            'timestamp': start_ts,
            'date_str': timestamp_to_date(start_ts),
            'name': event.get('name', 'Unknown Event'),
            'course': course.get('fullname', 'Unknown Course'),
            'source': 'TUWEL',
            'raw': event
        })

    # Process TISS exams
    for exam in tiss_exams:
        date_str = exam.get('date', '') # Format usually ISO YYYY-MM-DDThh:mm:ss
        course_name = exam.get('course_name', 'Unknown')
        mode = exam.get('mode', 'Exam')
        
        try:
            # TISS dates are usually ISO-like
            if 'T' in date_str:
                dt = datetime.fromisoformat(date_str)
                ts = dt.timestamp()
                formatted_date = dt.strftime('%Y-%m-%d %H:%M')
            else:
                # Fallback if format is different
                ts = 0 
                formatted_date = date_str
            
            if ts > datetime.now().timestamp(): # Only future exams
                timeline_events.append({
                    'timestamp': ts,
                    'date_str': formatted_date,
                    'name': f"Exam ({mode})",
                    'course': course_name,
                    'source': 'TISS',
                    'raw': exam
                })
        except Exception:
            pass # Skip if date parsing fails

    # 5. Sort by timestamp
    timeline_events.sort(key=lambda x: x['timestamp'])

    # 6. Display or Export
    if export:
        _export_timeline(timeline_events, output)
    else:
        _display_timeline(timeline_events)

def _display_timeline(events):
    if not events:
        rprint("[yellow]No upcoming events found.[/yellow]")
        return

    rprint(Panel("[bold]Unified Timeline (TUWEL + TISS)[/bold]", expand=False))
    rprint()

    now = datetime.now().timestamp()

    for event in events:
        ts = event['timestamp']
        days_diff = (ts - now) / 86400
        
        if days_diff < 0:
            continue # Should fitlered out, but just in case
            
        time_text = ""
        if days_diff < 1:
            hours_diff = (ts - now) / 3600
            time_text = f"In {int(hours_diff)} hours"
            color = "red"
        elif days_diff < 2:
            time_text = "Tomorrow"
            color = "yellow"
        else:
            time_text = f"In {int(days_diff)} days"
            color = "green" if days_diff > 7 else "yellow"

        source_tag = f"[blue](TISS)[/blue]" if event['source'] == 'TISS' else f"[magenta](TUWEL)[/magenta]"
        
        rprint(f"[{color}]{time_text}[/{color}]: [bold]{event['name']}[/bold] {source_tag}")
        rprint(f"  [dim]{event['course']} | {event['date_str']}[/dim]")
        rprint()

def _export_timeline(events, output_file):
    # Re-use logic from features.py export_calendar but adapted for merged list
    import hashlib
    
    if not output_file:
        output_file = str(Path.home() / "Downloads" / "unified_timeline.ics")
    
    output_path = Path(output_file)
    
    ics_lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//TU Wien Companion//Unified Timeline//EN",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:Uni Timeline",
    ]
    
    for event in events:
        ts = event['timestamp']
        dt = datetime.fromtimestamp(ts, tz=timezone.utc)
        dtstart = dt.strftime('%Y%m%dT%H%M%SZ')
        dtend = (dt.replace(minute=dt.minute + 60)).strftime('%Y%m%dT%H%M%SZ') # 1 hr duration dummy
        
        uid_base = f"{event['name']}-{ts}"
        uid_hash = hashlib.md5(uid_base.encode()).hexdigest()[:16]
        
        ics_lines.extend([
            "BEGIN:VEVENT",
            f"UID:timeline-{uid_hash}",
            f"DTSTART:{dtstart}",
            f"DTEND:{dtend}",
            f"SUMMARY:{event['name']} ({event['source']})",
            f"DESCRIPTION:{event['course']}",
            "END:VEVENT"
        ])

    ics_lines.append("END:VCALENDAR")
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text('\n'.join(ics_lines))
    rprint(f"[bold green]✓ Timeline exported to {output_path}[/bold green]")
