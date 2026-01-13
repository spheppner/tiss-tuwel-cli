"""
Todo command for urgent checkmark alerts.
"""

from datetime import datetime

from rich import print as rprint
from rich.console import Console

from tiss_tuwel_cli.cli import get_tuwel_client

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

    for cm in checkmarks_list:
        name = cm.get('name', 'Unknown')
        course_id = cm.get('course')
        # Find course name
        course_name = next((c['fullname'] for c in courses if c['id'] == course_id), f"Course {course_id}")

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
