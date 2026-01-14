"""
RC command for shell startup integration.

This module provides a fast, one-liner command optimized for .bashrc/.zshrc
that shows a quick summary based on configured widgets.
"""

from datetime import datetime

from rich import print as rprint
from rich.console import Console

from tiss_tuwel_cli.config import ConfigManager

console = Console()
config = ConfigManager()

# Seconds in a day
SECONDS_PER_DAY = 86400


def get_summary_line(client=None) -> str:
    """
    Generate a one-line summary based on configured widgets.
    
    This function can be called with an existing client for efficiency,
    or without one to create its own.
    
    Args:
        client: Optional TuwelClient instance to reuse.
    
    Returns:
        A formatted one-line summary string.
    """
    widgets = config.get_setting("rc_widgets", ["deadlines", "todos", "exams"])

    if not widgets:
        return ""

    # Check if we have a token
    token = config.get_tuwel_token()
    if not token:
        return "[dim]Not logged in. Run:[/dim] tiss-tuwel-cli login"

    # Get or create client
    if client is None:
        from tiss_tuwel_cli.clients.tuwel import TuwelClient
        try:
            client = TuwelClient(token)
            # Quick validation
            client.get_site_info()
        except Exception:
            return "[dim]Session expired. Run:[/dim] tiss-tuwel-cli login"

    parts = []

    try:
        # Deadlines widget
        if "deadlines" in widgets:
            deadline_count = _count_deadlines(client)
            if deadline_count > 0:
                parts.append(f"📅 {deadline_count} deadline{'s' if deadline_count != 1 else ''}")

        # Todos widget
        if "todos" in widgets:
            urgent_count = _count_urgent_todos(client)
            if urgent_count > 0:
                parts.append(f"[red]⚠️ {urgent_count} urgent[/red]")

        # Exams widget
        if "exams" in widgets:
            exam_count = _count_exam_alerts(client)
            if exam_count > 0:
                parts.append(f"🎓 {exam_count} exam reg")

        # Progress widget
        if "progress" in widgets:
            progress = _get_progress(client)
            if progress:
                parts.append(f"✓ {progress}")

    except Exception:
        # Silently fail - rc command should never block shell startup
        pass

    if not parts:
        return "[green]✓ All clear[/green]"

    return " | ".join(parts)


def _count_deadlines(client) -> int:
    """Count deadlines in the next 7 days."""
    try:
        upcoming = client.get_upcoming_calendar()
        events = upcoming.get('events', [])

        now = datetime.now().timestamp()
        week_later = now + (7 * SECONDS_PER_DAY)

        count = sum(1 for e in events if now <= e.get('timestart', 0) <= week_later)
        return count
    except Exception:
        return 0


def _count_urgent_todos(client) -> int:
    """Count urgent todos (< 24h deadline, 0 ticked)."""
    try:
        checkmarks = client.get_checkmarks([])
        checkmarks_list = checkmarks.get('checkmarks', [])

        now = datetime.now().timestamp()
        tomorrow = now + SECONDS_PER_DAY
        urgent = 0

        for cm in checkmarks_list:
            deadline = cm.get('timeavailable', 0)
            if now <= deadline <= tomorrow:
                examples = cm.get('examples', [])
                checked = sum(1 for ex in examples if ex.get('checked'))
                if checked == 0 and len(examples) > 0:
                    urgent += 1

        return urgent
    except Exception:
        return 0


def _count_exam_alerts(client) -> int:
    """Count exam registrations opening soon or currently open."""
    try:
        from tiss_tuwel_cli.clients.tiss import TissClient
        from tiss_tuwel_cli.utils import extract_course_number, days_until

        tiss = TissClient()
        courses = client.get_enrolled_courses('inprogress')
        count = 0

        for course in courses[:5]:  # Limit to avoid slowness
            shortname = course.get('shortname', '')
            course_num = extract_course_number(shortname)
            if not course_num:
                continue

            try:
                exams = tiss.get_exam_dates(course_num)
                if not isinstance(exams, list):
                    continue

                for exam in exams:
                    reg_start = exam.get('registrationStart')
                    if reg_start:
                        days = days_until(reg_start)
                        if days is not None and -7 <= days <= 14:
                            count += 1
            except Exception:
                continue

        return count
    except Exception:
        return 0


def _get_progress(client) -> str:
    """Get checkmark progress as a string."""
    try:
        checkmarks = client.get_checkmarks([])
        checkmarks_list = checkmarks.get('checkmarks', [])

        total_checked = 0
        total_possible = 0

        for cm in checkmarks_list:
            examples = cm.get('examples', [])
            total_checked += sum(1 for ex in examples if ex.get('checked'))
            total_possible += len(examples)

        if total_possible > 0:
            pct = (total_checked / total_possible) * 100
            return f"{total_checked}/{total_possible} ({pct:.0f}%)"
        return ""
    except Exception:
        return ""


def rc():
    """
    Quick summary for shell startup (.bashrc/.zshrc).
    
    Outputs a single line with configured widgets. Fast and non-blocking.
    Add to your shell rc file: eval "$(tiss-tuwel-cli rc)"
    """
    summary = get_summary_line()
    if summary:
        rprint(summary)
