"""
Course-related commands for the TU Wien Companion CLI.

This module provides commands for listing courses, assignments,
grades, checkmarks, and downloading course materials.
"""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from tiss_tuwel_cli.clients.tiss import TissClient
from tiss_tuwel_cli.utils import parse_percentage, strip_html, timestamp_to_date

console = Console()
tiss = TissClient()


def courses(classification: str = 'inprogress'):
    """
    List enrolled courses.
    
    Shows all courses the user is enrolled in, filtered by their status.
    
    Args:
        classification: Filter by course status.
            - 'past': Completed courses
            - 'inprogress': Currently active courses (default)
            - 'future': Upcoming courses
    """
    # Import here to avoid circular imports
    from tiss_tuwel_cli.cli import get_tuwel_client

    client = get_tuwel_client()
    with console.status(f"[bold green]Fetching {classification} courses...[/bold green]"):
        enrolled_courses = client.get_enrolled_courses(classification)

    table = Table(title=f"Enrolled Courses ({classification})")
    table.add_column("ID", justify="right", style="dim")
    table.add_column("Shortname", style="cyan")
    table.add_column("Fullname")

    for course in enrolled_courses:
        table.add_row(str(course.get('id')), course.get('shortname'), course.get('fullname'))
    console.print(table)


def assignments():
    """
    List assignments.
    
    Shows all assignments from enrolled courses, including their
    due dates and current status.
    """
    # Import here to avoid circular imports
    from tiss_tuwel_cli.cli import get_tuwel_client

    client = get_tuwel_client()
    with console.status("[bold green]Fetching assignments...[/bold green]"):
        data = client.get_assignments()
        courses_with_assignments = data.get('courses', [])

    table = Table(title="Assignments")
    table.add_column("Course", style="cyan")
    table.add_column("Assignment", style="white")
    table.add_column("Due", style="red")
    table.add_column("Status", style="yellow")

    now = datetime.now().timestamp()
    for course in courses_with_assignments:
        for assign in course.get('assignments', []):
            due = assign.get('duedate', 0)
            if due < now - (30 * 86400):
                continue  # Skip old assignments

            status = "Closed" if due < now else "Open"
            table.add_row(
                course.get('shortname'),
                assign.get('name'),
                timestamp_to_date(due),
                status
            )
    console.print(table)


def grades(course_id: Optional[int] = None):
    """
    Show grades.
    
    Displays the grade report for a specific course in a clean table format.
    If no course ID is provided, lists enrolled courses first.
    
    Args:
        course_id: The Moodle course ID to show grades for.
    """
    # Import here to avoid circular imports
    from tiss_tuwel_cli.cli import config, get_tuwel_client

    client = get_tuwel_client()
    user_id = config.get_user_id()

    if not course_id:
        rprint("[bold yellow]Please provide a course ID. Listing active courses:[/bold yellow]")
        courses(classification='inprogress')
        return

    with console.status("[bold green]Fetching detailed grades...[/bold green]"):
        report = client.get_user_grades_table(course_id, user_id)

    tables = report.get('tables', [])
    if not tables:
        rprint("[red]No grade table found for this course.[/red]")
        return

    table_data = tables[0].get('tabledata', [])

    # Create a clean table
    table = Table(title=f"Grades for Course {course_id}", expand=True)
    table.add_column("Item", style="white", no_wrap=False)
    table.add_column("Grade", justify="right", style="cyan")
    table.add_column("Range", justify="center", style="dim")
    table.add_column("Percentage", justify="right", style="green")

    for item in table_data:
        # Extract text from the itemname dictionary
        raw_name = item.get('itemname', {}).get('content', '')
        if not raw_name:
            continue

        # Clean HTML from the name
        clean_name = strip_html(raw_name)
        if not clean_name:
            continue

        # Grade Values - clean HTML from all values
        grade_raw = item.get('grade', {}).get('content', '-')
        grade_val = strip_html(grade_raw) if grade_raw else '-'

        percent_raw = item.get('percentage', {}).get('content', '-')
        percent_val = strip_html(percent_raw) if percent_raw else '-'

        range_raw = item.get('range', {}).get('content', '-')
        range_val = strip_html(range_raw) if range_raw else '-'

        # Determine row style
        if "gesamt" in clean_name.lower() or "total" in clean_name.lower():
            # Category total - highlight
            table.add_row(
                f"[bold yellow]▸ {clean_name}[/bold yellow]",
                f"[bold yellow]{grade_val}[/bold yellow]",
                range_val,
                f"[bold yellow]{percent_val}[/bold yellow]"
            )
        elif grade_val != '-' and grade_val.strip():
            # Regular grade item - use numeric comparison for styling
            style = ""
            pct = parse_percentage(percent_val)
            if pct is not None:
                if pct == 0.0:
                    style = "red"
                elif pct >= 100.0:
                    style = "green"

            if style:
                table.add_row(
                    f"  [{style}]{clean_name}[/{style}]",
                    f"[{style}]{grade_val}[/{style}]",
                    range_val,
                    f"[{style}]{percent_val}[/{style}]"
                )
            else:
                table.add_row(f"  {clean_name}", grade_val, range_val, percent_val)
        else:
            # Category header or pending item
            if clean_name.strip():
                table.add_row(
                    f"[bold cyan]{clean_name}[/bold cyan]",
                    "[dim]-[/dim]",
                    range_val if range_val != '-' else "",
                    "[dim]-[/dim]"
                )

    console.print(table)


def checkmarks():
    """
    Shows status of 'Kreuzerlübung' (mod_checkmark) exercises.
    
    Kreuzerlübungen are a TU Wien-specific exercise format where students
    mark which exercises they have completed before attending the lab session.
    Displays exercises grouped by course with summary statistics.
    """
    # Import here to avoid circular imports
    from tiss_tuwel_cli.cli import get_tuwel_client

    client = get_tuwel_client()

    with console.status("[bold green]Looking for checkmark exercises...[/bold green]"):
        try:
            # Fetch ALL checkmarks by passing empty list
            checkmarks_data = client.get_checkmarks([])
            checkmarks_list = checkmarks_data.get('checkmarks', [])
        except Exception as e:
            rprint(f"[bold red]Error fetching checkmarks:[/bold red] {e}")
            rprint("[dim]This may be due to a bug in the mod_checkmark plugin on TUWEL.[/dim]")
            return

    if not checkmarks_list:
        rprint("[yellow]No Kreuzerlübungen found in your active courses.[/yellow]")
        return

    # Group checkmarks by course
    courses_data: Dict[int, Dict[str, Any]] = {}
    for cm in checkmarks_list:
        course_id = cm.get('course')
        if course_id not in courses_data:
            courses_data[course_id] = {
                'exercises': [],
                'total_checked': 0,
                'total_possible': 0,
                'total_grade': 0.0,
                'graded_count': 0
            }

        examples = cm.get('examples', [])
        checked = sum(1 for ex in examples if ex.get('checked'))
        total = len(examples)

        feedback = cm.get('feedback', {})
        grade_str = feedback.get('grade', '-')

        courses_data[course_id]['exercises'].append({
            'name': cm.get('name'),
            'checked': checked,
            'total': total,
            'grade': grade_str,
            'deadline': cm.get('cutoffdate', 0)
        })

        courses_data[course_id]['total_checked'] += checked
        courses_data[course_id]['total_possible'] += total

        if grade_str and grade_str != '-':
            try:
                courses_data[course_id]['total_grade'] += float(grade_str)
                courses_data[course_id]['graded_count'] += 1
            except ValueError:
                pass

    # Display grouped by course with summary
    rprint(Panel("[bold]Kreuzerlübungen Overview[/bold]", expand=False))
    rprint()

    for course_id, data in courses_data.items():
        total_checked = data['total_checked']
        total_possible = data['total_possible']
        completion_pct = (total_checked / total_possible * 100) if total_possible > 0 else 0
        avg_grade = data['total_grade'] / data['graded_count'] if data['graded_count'] > 0 else 0

        # Summary header for the course
        summary = f"[bold cyan]Course {course_id}[/bold cyan] | "
        summary += f"Completion: [green]{total_checked}/{total_possible}[/green] ({completion_pct:.0f}%)"
        if data['graded_count'] > 0:
            summary += f" | Avg Grade: [magenta]{avg_grade:.1f}[/magenta]"
        rprint(summary)

        # Exercise table for this course
        table = Table(expand=True, show_header=True, header_style="bold", box=None)
        table.add_column("Exercise", style="white", no_wrap=False)
        table.add_column("Checked", justify="center")
        table.add_column("Grade", justify="right", style="magenta")
        table.add_column("Deadline", style="dim")

        for ex in data['exercises']:
            checked_str = f"{ex['checked']}/{ex['total']}"
            if ex['checked'] == ex['total']:
                checked_str = f"[green]{checked_str} ✓[/green]"
            elif ex['checked'] > 0:
                checked_str = f"[yellow]{checked_str}[/yellow]"
            else:
                checked_str = f"[red]{checked_str}[/red]"

            deadline = timestamp_to_date(ex['deadline']) if ex['deadline'] else "No deadline"

            table.add_row(
                ex['name'],
                checked_str,
                str(ex['grade']),
                deadline
            )

        console.print(table)
        rprint()  # Space between courses


def download(course_id: int):
    """
    Download all resources (files) from a specific course.
    
    Files are saved to ~/Downloads/Tuwel/<Course_ID>/
    
    Args:
        course_id: The Moodle course ID to download files from.
    """
    # Import here to avoid circular imports
    from tiss_tuwel_cli.cli import get_tuwel_client

    client = get_tuwel_client()

    # Fetch course contents
    with console.status(f"[bold green]Fetching course {course_id} contents...[/bold green]"):
        contents = client.get_course_contents(course_id)

    if not contents:
        rprint("[red]No content found or access denied.[/red]")
        return

    # Prepare download directory
    dl_dir = Path.home() / "Downloads" / "Tuwel" / str(course_id)
    dl_dir.mkdir(parents=True, exist_ok=True)
    rprint(f"Downloading to: [blue]{dl_dir}[/blue]")

    # Iterate and download files
    count = 0
    for section in contents:
        for module in section.get('modules', []):
            if 'contents' in module:
                for file_info in module['contents']:
                    if file_info.get('type') == 'file':
                        file_url = file_info.get('fileurl')
                        file_name = file_info.get('filename')
                        if file_url and file_name:
                            rprint(f" - Downloading {file_name}...")
                            try:
                                client.download_file(file_url, dl_dir / file_name)
                                count += 1
                            except Exception as e:
                                rprint(f"   [red]Failed:[/red] {e}")

    rprint(f"[bold green]Done! Downloaded {count} files.[/bold green]")


def tiss_course(course_number: str, semester: str = "2024W"):
    """
    Search TISS for course details and exams.
    
    Args:
        course_number: The TISS course number (e.g., "192.167").
        semester: Semester code (e.g., "2024W" for winter, "2024S" for summer).
    """
    with console.status("[bold green]Searching TISS...[/bold green]"):
        details = tiss.get_course_details(course_number, semester)
        exams = tiss.get_exam_dates(course_number)

    if "error" in details:
        rprint(f"[bold red]Error:[/bold red] {details['error']}")
        return

    rprint(Panel(
        f"[bold blue]{details.get('title', {}).get('en', 'Unknown Title')}[/bold blue]\n"
        f"ECTS: {details.get('ects', 'N/A')} | Type: {details.get('courseType', 'N/A')}",
        title="Course Info"
    ))

    if exams and isinstance(exams, list):
        t = Table(title="Exams")
        t.add_column("Date", style="green")
        t.add_column("Mode", style="white")
        t.add_column("Registration", style="dim")
        for e in exams:
            t.add_row(e.get('date', 'N/A'), e.get('mode', 'N/A'), e.get('registrationStart', 'N/A'))
        console.print(t)
    else:
        rprint("[yellow]No future exam dates found.[/yellow]")
