"""
Course-related commands for the TU Wien Companion CLI.

This module provides commands for listing courses, assignments,
grades, checkmarks, and downloading course materials.
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Optional

from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.tree import Tree

from tiss_tuwel_cli.clients.tiss import TissClient
from tiss_tuwel_cli.utils import timestamp_to_date

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
        enrolled_courses = data.get('courses', [])

    table = Table(title="Assignments")
    table.add_column("Course", style="cyan")
    table.add_column("Assignment", style="white")
    table.add_column("Due", style="red")
    table.add_column("Status", style="yellow")

    now = datetime.now().timestamp()
    for course in enrolled_courses:
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
    
    Displays the grade report for a specific course. If no course ID
    is provided, lists enrolled courses first.
    
    Args:
        course_id: The Moodle course ID to show grades for.
    """
    # Import here to avoid circular imports
    from tiss_tuwel_cli.cli import get_tuwel_client, config
    
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

    # Create a Tree for hierarchical display
    root_tree = Tree(f"[bold blue]Grades for Course {course_id}[/bold blue]")
    current_category = root_tree

    for item in table_data:
        # Extract text from the itemname dictionary
        raw_name = item.get('itemname', {}).get('content', 'Unknown')

        # Basic HTML stripping
        clean_name = raw_name.replace('<span class="gradeitemheader" title="', '').split('"')[0]
        if "class" in str(item.get('itemname')):
            clean_name = re.sub('<[^<]+?>', '', raw_name).strip()

        # Grade Values
        grade_val = item.get('grade', {}).get('content', '-').replace('&nbsp;', '')
        percent_val = item.get('percentage', {}).get('content', '-').replace('&nbsp;', '')
        range_val = item.get('range', {}).get('content', '-').replace('&nbsp;', '')

        # Formatting based on item type
        if "gesamt" in clean_name.lower() or "total" in clean_name.lower():
            # Category total
            text = Text(f"{clean_name}: {grade_val} ({percent_val})", style="bold yellow")
            current_category.add(text)
        elif grade_val != '-':
            # Grade item
            text = Text(f"{clean_name} | Grade: {grade_val} | Range: {range_val} | {percent_val}")
            if "0,00 %" in percent_val or "0.00 %" in percent_val:
                text.stylize("red")
            elif "100" in percent_val:
                text.stylize("green")
            current_category.add(text)
        else:
            # Category header or empty item
            if clean_name:
                text = Text(clean_name, style="bold cyan")
                current_category.add(text)

    console.print(root_tree)


def checkmarks():
    """
    Shows status of 'Kreuzerlübung' (mod_checkmark) exercises.
    
    Kreuzerlübungen are a TU Wien-specific exercise format where students
    mark which exercises they have completed before attending the lab session.
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

    table = Table(title="Kreuzerlübungen Overview")
    table.add_column("Course ID", style="cyan")
    table.add_column("Name", style="white")
    table.add_column("Examples Checked", style="green")
    table.add_column("Grade", style="magenta")
    table.add_column("Deadline", style="red")

    for cm in checkmarks_list:
        examples = cm.get('examples', [])
        checked_count = sum(1 for ex in examples if ex.get('checked'))
        total_count = len(examples)

        feedback = cm.get('feedback', {})
        grade = feedback.get('grade', '-')

        cutoff = cm.get('cutoffdate', 0)
        deadline = timestamp_to_date(cutoff) if cutoff else "No Deadline"

        table.add_row(
            str(cm.get('course')),
            cm.get('name'),
            f"{checked_count}/{total_count}",
            grade,
            deadline
        )

    console.print(table)


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
