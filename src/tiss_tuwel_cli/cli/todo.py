"""
Todo command for urgent checkmark alerts.
"""

from datetime import datetime

from rich import print as rprint
from rich.console import Console

from tiss_tuwel_cli.cli import get_tuwel_client
from tiss_tuwel_cli.utils import extract_course_number, format_course_name

console = Console()


def todo():
    """
    Check for urgent tasks, specifically upcoming checkmark deadlines with no ticks.
    """
    client = get_tuwel_client()

    with console.status("[bold green]Checking for urgent tasks...[/bold green]"):
        # 1. Fetch courses
        courses = client.get_enrolled_courses('inprogress')
        if not courses:
            rprint("[yellow]No courses found.[/yellow]")
            return

        course_ids = [c['id'] for c in courses]

        # 2. Fetch Checkmarks
        # Note: TuwelClient.get_checkmarks takes a list of IDs
        checkmarks_data = client.get_checkmarks(course_ids)
        checkmarks_list = checkmarks_data.get('checkmarks', [])

    urgent_items = []
    now = datetime.now().timestamp()

    # Create set of all course IDs involved
    # Ensure IDs are ints
    related_course_ids = list(set(int(cm.get('course')) for cm in checkmarks_list if cm.get('course')))

    # Resolve names
    course_names = {}

    # 1. Try existing course list
    missing_ids = set(related_course_ids)
    for c in courses:
        cid = c.get('id')
        if cid:
            cid = int(cid)
            if cid in missing_ids:
                # Format
                short = c.get('shortname', '')
                full = c.get('fullname', f"Course {cid}")
                num = extract_course_number(short)
                course_names[cid] = format_course_name(full, num)
                missing_ids.remove(cid)

    # 2. Fetch missing
    if missing_ids:
        try:
            ids_list = list(missing_ids)
            fetched = client.get_courses(ids_list)
            for c in fetched:
                cid = c.get('id')
                if cid:
                    cid = int(cid)
                    short = c.get('shortname', '')
                    full = c.get('fullname', f"Course {cid}")
                    num = extract_course_number(short)
                    course_names[cid] = format_course_name(full, num)
        except Exception:
            pass

    for cm in checkmarks_list:
        name = cm.get('name', 'Unknown')
        course_id = cm.get('course')
        if course_id:
            course_id = int(course_id)
        course_name = course_names.get(course_id, f"Course {course_id}")

        # Check deadline
        due_date = cm.get('duedate', 0)

        # Condition 1: Deadline is upcoming and less than 24 hours away
        # (check if logic matches 'upcoming' - so > now)
        if now < due_date < (now + 24 * 3600):

            # Condition 2: No examples ticked
            # 'examples' list contains dicts with 'checked' boolean
            examples = cm.get('examples', [])
            ticked_count = sum(1 for ex in examples if ex.get('checked'))

            if ticked_count == 0:
                # Calculate time left
                diff_seconds = due_date - now
                hours_left = int(diff_seconds / 3600)
                minutes_left = int((diff_seconds % 3600) / 60)

                urgent_items.append({
                    'course': course_name,
                    'name': name,
                    'time_str': f"{hours_left}h {minutes_left}m"
                })

    if urgent_items:
        for item in urgent_items:
            rprint(f"[bold red][URGENT][/bold red] You haven't ticked any examples for [bold]{item['name']}[/bold] in {item['course']}.")
            rprint(f"         Deadline in [bold red]{item['time_str']}[/bold red].")
    else:
        rprint("[green]No urgent checkmark alerts. You're good![/green]")
