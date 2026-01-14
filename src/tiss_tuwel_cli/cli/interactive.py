"""
Interactive menu mode for the TU Wien Companion CLI.

This module provides an interactive, menu-based interface for using
all CLI features in a user-friendly way with keyboard navigation.
"""

import re
from datetime import datetime
from typing import Any, Dict, List, Optional

import requests
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from tiss_tuwel_cli.cli import get_tuwel_client
from tiss_tuwel_cli.clients.tiss import TissClient
from tiss_tuwel_cli.config import ConfigManager
from tiss_tuwel_cli.utils import (
    extract_course_number,
    parse_percentage,
    strip_html,
    timestamp_to_date,
)

console = Console()
config = ConfigManager()
tiss = TissClient()

# Constants for time calculations and thresholds
SECONDS_PER_DAY = 86400
EXAM_ALERT_DAYS_BEFORE = 14  # Show alerts for registrations opening within this many days
EXAM_ALERT_DAYS_AFTER = 7  # Show alerts for registrations that opened within this many days
MAX_COURSES_FOR_GRADES = 5  # Limit API calls when fetching grade summaries


class InteractiveMenu:
    """
    Interactive menu system for the CLI.
    
    Provides a clean, easy-to-use interface with keyboard navigation
    for navigating and using all CLI features interactively.
    """

    def __init__(self):
        """Initialize the interactive menu."""
        self._tuwel_client = None
        self._courses_cache: List[dict] = []
        self._user_info: Optional[dict] = None
        self._exam_alerts_cache: Optional[List[dict]] = None
        self._grade_summary_cache: Optional[Dict[str, Any]] = None

    def _get_tuwel_client(self):
        """Get or create the TUWEL client."""
        if self._tuwel_client is None:
            token = config.get_tuwel_token()
            if not token:
                return None
            from tiss_tuwel_cli.clients.tuwel import TuwelClient
            self._tuwel_client = TuwelClient(token)
        return self._tuwel_client

    def _is_authenticated(self) -> bool:
        """Check if user is authenticated."""
        return config.get_tuwel_token() is not None

    def _get_user_info(self) -> Optional[dict]:
        """Get cached user information."""
        if self._user_info is None:
            client = self._get_tuwel_client()
            if client:
                try:
                    self._user_info = client.get_site_info()
                except (Exception, KeyboardInterrupt):
                    # Authentication errors are handled gracefully in the UI
                    self._user_info = None
        return self._user_info

    def _get_exam_alerts(self) -> List[dict]:
        """Fetch exam alerts using shared logic."""
        if self._exam_alerts_cache is not None:
            return self._exam_alerts_cache

        client = self._get_tuwel_client()
        from tiss_tuwel_cli.cli.features import get_exam_alerts

        # Use shared logic
        self._exam_alerts_cache = get_exam_alerts(client, tiss)
        return self._exam_alerts_cache

    def _get_weekly_overview(self) -> List[dict]:
        """Get weekly events using shared logic."""
        client = self._get_tuwel_client()
        from tiss_tuwel_cli.cli.features import get_weekly_events
        return get_weekly_events(client)

    def _get_study_progress(self) -> Dict[str, Any]:
        """Get study progress using shared logic."""
        client = self._get_tuwel_client()
        from tiss_tuwel_cli.cli.features import get_study_progress
        return get_study_progress(client)

    def _get_grade_summary(self) -> Dict[str, Any]:
        """
        Get a summary of grades across all courses.
        
        Returns:
            Dictionary with grade statistics.
        """
        if self._grade_summary_cache is not None:
            return self._grade_summary_cache

        client = self._get_tuwel_client()
        user_id = config.get_user_id()

        if not client or not user_id:
            return {}

        try:
            courses = client.get_enrolled_courses('inprogress')

            course_grades = []
            for course in courses[:MAX_COURSES_FOR_GRADES]:
                try:
                    report = client.get_user_grades_table(course['id'], user_id)
                    tables = report.get('tables', [])
                    if tables:
                        table_data = tables[0].get('tabledata', [])
                        for item in table_data:
                            raw_name = item.get('itemname', {}).get('content', '')
                            clean_name = strip_html(raw_name) if raw_name else ''

                            # Look for course total
                            if 'gesamt' in clean_name.lower() or 'total' in clean_name.lower():
                                percent_raw = item.get('percentage', {}).get('content', '')
                                pct = parse_percentage(strip_html(percent_raw))
                                if pct is not None:
                                    course_grades.append({
                                        'course': course.get('shortname', ''),
                                        'percentage': pct,
                                    })
                                break
                except Exception:
                    continue

            self._grade_summary_cache = {
                'course_grades': course_grades,
                'average': (
                    sum(g['percentage'] for g in course_grades) / len(course_grades)
                    if course_grades else 0
                ),
            }
            return self._grade_summary_cache
        except Exception:
            return {}

    def _clear_screen(self):
        """Clear the console screen."""
        console.clear()

    def _print_header(self, title: str = "TU Wien Companion", subtitle: str = None):
        """Print the application header."""
        if subtitle:
            console.print(Panel(
                f"[bold blue]{title}[/bold blue]",
                subtitle=subtitle,
                expand=False
            ))
        else:
            console.print(Panel(
                f"[bold blue]{title}[/bold blue]",
                expand=False
            ))
        console.print()

    def _print_compact_summary(self):
        """Print a compact one-line summary using the rc module."""
        from tiss_tuwel_cli.cli.rc import get_summary_line
        client = self._get_tuwel_client()
        summary = get_summary_line(client)
        if summary:
            console.print(summary)
            console.print()

    def _show_settings(self):
        """Show the settings menu."""
        from tiss_tuwel_cli.cli.settings import show_settings_menu
        show_settings_menu()

    def _print_smart_dashboard(self):
        """Print an intelligent dashboard summary with exam alerts and smart features."""
        client = self._get_tuwel_client()
        if not client:
            return

        user_info = self._get_user_info()
        if user_info:
            name = user_info.get('fullname', 'Student')
            console.print(f"[dim]Welcome back,[/dim] [bold cyan]{name}[/bold cyan]")
            console.print()

        try:
            with console.status("[dim]Loading dashboard...[/dim]"):
                upcoming = client.get_upcoming_calendar()
                events = upcoming.get('events', [])[:5]
                exam_alerts = self._get_exam_alerts()
                progress = self._get_study_progress()

            # ============ EXAM REGISTRATION ALERTS ============
            if exam_alerts:
                console.print(Panel(
                    "[bold white on red] 🎓 EXAM REGISTRATION ALERTS [/bold white on red]",
                    expand=False,
                    border_style="red"
                ))
                for alert in exam_alerts[:3]:  # Show top 3 alerts
                    days = alert.get('days_to_registration', 0)
                    course = alert.get('course', '')
                    exam_date = alert.get('exam_date', 'TBD')
                    mode = alert.get('mode', '')

                    if days < 0:
                        # Registration is open now
                        status = "[bold green]OPEN NOW[/bold green]"
                        icon = "🟢"
                    elif days == 0:
                        status = "[bold yellow]OPENS TODAY[/bold yellow]"
                        icon = "🟡"
                    elif days <= 3:
                        status = f"[bold yellow]Opens in {days}d[/bold yellow]"
                        icon = "🟡"
                    else:
                        status = f"[dim]Opens in {days}d[/dim]"
                        icon = "📋"

                    console.print(f"  {icon} [bold]{course}[/bold]")
                    console.print(f"      Exam: {exam_date[:10] if exam_date else 'TBD'} ({mode})")
                    console.print(f"      Registration: {status}")
                console.print()

            # ============ STUDY PROGRESS OVERVIEW ============
            if progress:
                parts = []

                if progress.get('checkmarks_total', 0) > 0:
                    pct = progress.get('checkmarks_percentage', 0)
                    completed = progress.get('checkmarks_completed', 0)
                    total = progress.get('checkmarks_total', 0)

                    if pct >= 100:
                        bar_style = "green"
                    elif pct >= 50:
                        bar_style = "yellow"
                    else:
                        bar_style = "red"

                    parts.append(f"[{bar_style}]✓ Checkmarks: {completed}/{total} ({pct:.0f}%)[/{bar_style}]")

                pending = progress.get('pending_assignments', 0)
                overdue = progress.get('overdue_assignments', 0)

                if pending > 0:
                    parts.append(f"[cyan]📝 Pending: {pending} assignments[/cyan]")
                if overdue > 0:
                    parts.append(f"[red]⚠️ Overdue: {overdue}[/red]")

                if parts:
                    console.print("[bold]📊 Study Progress[/bold]")
                    for part in parts:
                        console.print(f"  {part}")
                    console.print()

            # ============ UPCOMING DEADLINES ============
            if events:
                console.print("[bold]📅 Upcoming Deadlines[/bold]")
                for event in events:
                    course = event.get('course', {}).get('shortname', '')
                    event_name = event.get('name', 'Unknown')
                    time = timestamp_to_date(event.get('timestart'))
                    # Color based on urgency
                    now = datetime.now().timestamp()
                    event_time = event.get('timestart', 0)
                    days_left = (event_time - now) / SECONDS_PER_DAY

                    if days_left < 1:
                        style = "bold red"
                        urgency = "⚠️ "
                    elif days_left < 3:
                        style = "yellow"
                        urgency = "⏰ "
                    else:
                        style = "green"
                        urgency = "   "

                    console.print(
                        f"  {urgency}[{style}]{time}[/{style}] [{style}]{course}[/{style}] - {event_name}"
                    )
                console.print()

            # ============ SMART TIPS ============
            tips = self._generate_smart_tips(exam_alerts, progress, events)
            if tips:
                console.print("[bold]💡 Tips[/bold]")
                for tip in tips[:2]:
                    console.print(f"  [dim]{tip}[/dim]")
                console.print()

        except (requests.RequestException, KeyError, TypeError):
            # Network or parsing errors are handled gracefully - dashboard is optional
            pass

    def _generate_smart_tips(
            self,
            exam_alerts: List[dict],
            progress: Dict[str, Any],
            events: List[dict]
    ) -> List[str]:
        """Generate context-aware tips for the student."""
        tips = []

        # Exam-related tips
        if exam_alerts:
            open_registrations = [a for a in exam_alerts if a.get('days_to_registration', 0) < 0]
            if open_registrations:
                tips.append(
                    f"🎓 Don't forget: {len(open_registrations)} exam registration(s) are open now!"
                )

        # Progress-related tips
        if progress:
            overdue = progress.get('overdue_assignments', 0)
            if overdue > 0:
                tips.append(f"📚 You have {overdue} overdue assignment(s). Consider catching up!")

            pct = progress.get('checkmarks_percentage', 0)
            if 0 < pct < 50:
                tips.append("✏️ Keep working on your checkmarks to meet participation requirements.")

        # Deadline-related tips
        if events:
            now = datetime.now().timestamp()
            urgent = [e for e in events if (e.get('timestart', 0) - now) < SECONDS_PER_DAY]
            if urgent:
                tips.append(f"⏰ You have {len(urgent)} deadline(s) in the next 24 hours!")

        # General tips (if no specific tips)
        if not tips:
            month = datetime.now().month
            if month in [1, 2, 6, 7]:
                tips.append("📖 Exam season! Good luck with your exams.")
            elif month in [10, 3]:
                tips.append("🎓 Start of semester - check your course registrations!")

        return tips

    def _wait_for_continue(self):
        """Wait for user to continue."""
        inquirer.text(message="Press Enter to continue...", default="").execute()

    def _get_courses(self, classification: str = 'inprogress') -> List[dict]:
        """Fetch and cache courses."""
        client = self._get_tuwel_client()
        if not client:
            return []
        with console.status(f"[bold green]Fetching {classification} courses...[/bold green]"):
            self._courses_cache = client.get_enrolled_courses(classification)
        return self._courses_cache

    def show_main_menu(self):
        """Display and handle the main menu with hierarchical sub-menus."""
        while True:
            self._clear_screen()
            self._print_header("TU Wien Companion", "Interactive Mode")

            # Show compact summary if authenticated
            if self._is_authenticated():
                self._print_compact_summary()

            # Build menu choices based on auth status
            choices = []

            if self._is_authenticated():
                choices.extend([
                    Separator("─── Main Menu ───"),
                    Choice(value="study", name="📚 Study"),
                    Choice(value="planning", name="📅 Planning & Deadlines"),
                    Choice(value="tools", name="🛠️ Tools & Utilities"),
                    Separator(),
                ])
            else:
                choices.append(Separator("─── Login Required ───"))

            choices.append(Choice(value="login", name="🔐 Account"))
            choices.append(Choice(value="settings", name="⚙️ Settings"))
            choices.append(Choice(value="quit", name="🚪 Quit"))

            action = inquirer.select(
                message="Select a category:",
                choices=choices,
                pointer="→",
                qmark="",
                amark="",
            ).execute()

            if action == "quit":
                self._clear_screen()
                rprint("[bold green]Goodbye![/bold green]")
                break
            elif action == "login":
                self._show_login_menu()
            elif action == "settings":
                self._show_settings()
            elif action == "study":
                self._show_study_menu()
            elif action == "planning":
                self._show_planning_menu()
            elif action == "tools":
                self._show_tools_menu()

    def _show_study_menu(self):
        """Show the Study sub-menu."""
        while True:
            self._clear_screen()
            self._print_header("Study", "Courses & Academics")

            choices = [
                Choice(value="courses", name="📚 My Courses"),
                Choice(value="assignments", name="📝 Assignments"),
                Choice(value="checkmarks", name="✅ Kreuzerlübungen"),
                Choice(value="grades", name="🏆 Grades"),
                Choice(value="participation", name="🎯 Exercise Participation"),
                Separator(),
                Choice(value="back", name="← Back"),
            ]

            action = inquirer.select(
                message="Select an option:",
                choices=choices,
                pointer="→",
                qmark="",
            ).execute()

            if action == "back":
                break
            elif action == "courses":
                self._show_courses_menu()
            elif action == "assignments":
                self._show_assignments()
            elif action == "checkmarks":
                self._show_checkmarks()
            elif action == "grades":
                self._show_grade_summary()
            elif action == "participation":
                self._show_participation_menu()

    def _show_planning_menu(self):
        """Show the Planning & Deadlines sub-menu."""
        while True:
            self._clear_screen()
            self._print_header("Planning", "Deadlines & Schedule")

            choices = [
                Choice(value="dashboard", name="📊 Dashboard"),
                Choice(value="weekly", name="📆 This Week"),
                Choice(value="timeline", name="📅 Unified Timeline"),
                Choice(value="todo", name="⚡ Urgent Tasks"),
                Separator(),
                Choice(value="back", name="← Back"),
            ]

            action = inquirer.select(
                message="Select an option:",
                choices=choices,
                pointer="→",
                qmark="",
            ).execute()

            if action == "back":
                break
            elif action == "dashboard":
                self._show_dashboard()
            elif action == "weekly":
                self._show_weekly_overview()
            elif action == "timeline":
                self._show_timeline()
            elif action == "todo":
                self._show_todo()

    def _show_tools_menu(self):
        """Show the Tools & Utilities sub-menu."""
        while True:
            self._clear_screen()
            self._print_header("Tools", "Utilities & Search")

            choices = [
                Choice(value="unified", name="🔗 Unified Course View (TISS+TUWEL)"),
                Choice(value="exams", name="🎓 Exam Registration"),
                Choice(value="export_cal", name="📅 Export Calendar"),
                Choice(value="tiss", name="🔍 Search TISS"),
                Separator(),
                Choice(value="back", name="← Back"),
            ]

            action = inquirer.select(
                message="Select an option:",
                choices=choices,
                pointer="→",
                qmark="",
            ).execute()

            if action == "back":
                break
            elif action == "unified":
                self._show_unified_view()
            elif action == "exams":
                self._show_exam_registration()
            elif action == "export_cal":
                self._export_calendar()
            elif action == "tiss":
                self._show_tiss_search()

    def _show_login_menu(self):
        """Show login options."""
        self._clear_screen()
        self._print_header("Authentication")

        if self._is_authenticated():
            user_info = self._get_user_info()
            if user_info:
                console.print(f"[green]✓ Logged in as:[/green] [bold]{user_info.get('fullname')}[/bold]")
                console.print()

        choices = [
            Choice(value="auto", name="🤖 Fully Automated Login"),
            Choice(value="hybrid", name="🌐 Hybrid Login (Browser opens, manual click, auto-capture)"),
            Choice(value="manual", name="📋 Manual Setup (Paste Token)"),
            Separator(),
            Choice(value="back", name="← Back"),
        ]

        action = inquirer.select(
            message="Choose login method:",
            choices=choices,
            pointer="→",
            qmark="",
        ).execute()

        if action == "auto":
            self._do_automated_login()
        elif action == "hybrid":
            self._do_hybrid_login()
        elif action == "manual":
            self._do_manual_setup()

    def _do_automated_login(self):
        """Perform automated browser login."""
        self._clear_screen()
        self._print_header("Automated Login")

        from tiss_tuwel_cli.cli.auth import login
        try:
            login(False, False, False)
            # Refresh user info
            self._tuwel_client = None
            self._user_info = None
        except Exception as e:
            rprint(f"[red]Error: {e}[/red]")

        self._wait_for_continue()

    def _do_hybrid_login(self):
        """Perform hybrid browser login (manual click, auto-capture)."""
        self._clear_screen()
        self._print_header("Hybrid Login")

        from tiss_tuwel_cli.cli.auth import hybrid_login
        try:
            hybrid_login()
            # Refresh user info
            self._tuwel_client = None
            self._user_info = None
        except Exception as e:
            rprint(f"[red]Error: {e}[/red]")

        self._wait_for_continue()

    def _do_manual_setup(self):
        """Perform manual token setup."""
        self._clear_screen()
        self._print_header("Manual Setup")

        from tiss_tuwel_cli.cli.auth import manual_login
        try:
            manual_login()
            # Refresh user info
            self._tuwel_client = None
            self._user_info = None
        except Exception as e:
            rprint(f"[red]Error: {e}[/red]")

        self._wait_for_continue()

    def _show_dashboard(self):
        """Show the full dashboard view."""
        self._clear_screen()
        self._print_header("Dashboard")

        from tiss_tuwel_cli.cli.dashboard import dashboard as show_dashboard
        try:
            show_dashboard()
        except Exception as e:
            rprint(f"[red]Error loading dashboard: {e}[/red]")

        self._wait_for_continue()

    def _show_courses_menu(self):
        """Show the courses menu with keyboard navigation."""
        while True:
            self._clear_screen()
            self._print_header("My Courses")

            action = inquirer.select(
                message="Select course category:",
                choices=[
                    Choice(value="inprogress", name="📗 Current Courses"),
                    Choice(value="past", name="📕 Past Courses"),
                    Choice(value="future", name="📘 Future Courses"),
                    Separator(),
                    Choice(value="back", name="← Back"),
                ],
                pointer="→",
                qmark="",
            ).execute()

            if action == "back":
                break
            else:
                self._show_course_list(action)

    def _show_course_list(self, classification: str):
        """Show list of courses with selection."""
        courses = self._get_courses(classification)

        if not courses:
            self._clear_screen()
            rprint(f"[yellow]No {classification} courses found.[/yellow]")
            self._wait_for_continue()
            return

        while True:
            self._clear_screen()
            self._print_header(f"Courses ({classification.capitalize()})")

            # Build course choices
            choices = []
            for course in courses:
                cid = course.get('id')
                from tiss_tuwel_cli.utils import format_course_name
                shortname = course.get('shortname', '')
                fullname = course.get('fullname', '')
                # Truncate if too long
                if len(fullname) > 50:
                    fullname = fullname[:47] + "..."
                num = extract_course_number(shortname)
                display_name = format_course_name(fullname, num)

                # Truncate if too long (keeping it readable)
                if len(display_name) > 60:
                    display_name = display_name[:57] + "..."

                choices.append(Choice(
                    value=course,
                    name=display_name
                ))

            choices.append(Separator())
            choices.append(Choice(value="back", name="← Back"))

            selected = inquirer.select(
                message="Select a course:",
                choices=choices,
                pointer="→",
                qmark="",
            ).execute()

            if selected == "back":
                break
            else:
                self._show_course_details(selected)

    def _show_course_details(self, course: dict):
        """Show details and actions for a specific course with TISS integration."""
        course_id = course.get('id')
        course_name = course.get('fullname', 'Unknown Course')
        shortname = course.get('shortname', '')

        # Format name consistently
        from tiss_tuwel_cli.utils import format_course_name
        course_num = extract_course_number(shortname)
        display_name = format_course_name(course_name, course_num)

        while True:
            self._clear_screen()
            self._print_header(display_name or "Course Details")

            # Build course info panel with TISS data if available
            info_text = f"[bold]{display_name}[/bold]\n"
            info_text += f"[dim]Course ID: {course_id}[/dim]"

            # Try to extract course number and fetch TISS data
            course_num = extract_course_number(shortname)
            tiss_data = None
            if course_num:
                try:
                    from tiss_tuwel_cli.utils import get_current_semester
                    semester = get_current_semester()
                    tiss_data = tiss.get_course_details(course_num, semester)

                    if tiss_data and 'error' not in tiss_data:
                        info_text += f"\n[dim]TISS Number: {course_num}[/dim]"

                        # Add ECTS and type info
                        ects = tiss_data.get('ects')
                        course_type = tiss_data.get('courseType', {})
                        type_name = course_type.get('name') if isinstance(course_type, dict) else None

                        if ects:
                            info_text += f"\n💎 ECTS: [cyan]{ects}[/cyan]"
                        if type_name:
                            info_text += f" | Type: [cyan]{type_name}[/cyan]"
                except Exception:
                    # Silently ignore TISS fetch errors
                    pass

            console.print(Panel(info_text, title="📚 Course Information"))
            console.print()

            # Show exam dates if available
            if course_num and tiss_data:
                try:
                    exams = tiss.get_exam_dates(course_num)
                    if isinstance(exams, list) and exams:
                        console.print("[bold]📅 Upcoming Exams:[/bold]")
                        for exam in exams[:3]:  # Show up to 3 exams
                            exam_date = exam.get('date', 'N/A')
                            mode = exam.get('mode', 'Unknown')
                            console.print(f"  • {exam_date} - {mode}")
                        console.print()
                except Exception:
                    pass

            # Build action menu with new options
            choices = [
                Choice(value="grades", name="📊 View Grades"),
                Choice(value="assignments", name="📝 View Assignments"),
                Choice(value="download", name="📥 Download Materials"),
                Separator("─── External Links ───"),
                Choice(value="vowi", name="📖 Open in VoWi"),
                Choice(value="tuwel", name="🌐 Open in TUWEL"),
            ]

            # Add TISS link if course number is available
            if course_num:
                choices.append(Choice(value="tiss", name="🔍 Open in TISS"))

            choices.extend([
                Separator(),
                Choice(value="back", name="← Back"),
            ])

            action = inquirer.select(
                message="What would you like to do?",
                choices=choices,
                pointer="→",
                qmark="",
            ).execute()

            if action == "back":
                break
            elif action == "grades":
                self._show_course_grades(course_id)
            elif action == "assignments":
                self._show_course_assignments(course_id, course_name)
            elif action == "download":
                self._download_course_materials(course_id)
            elif action == "vowi":
                self._open_vowi_for_course(course_name)
            elif action == "tuwel":
                self._open_tuwel_course(course_id)
            elif action == "tiss" and course_num:
                self._open_tiss_course(course_num)

    def _show_course_grades(self, course_id: int):
        """Show grades for a specific course in a clean table format."""
        self._clear_screen()
        self._print_header("Grades")

        client = self._get_tuwel_client()
        user_id = config.get_user_id()

        if not client or not user_id:
            rprint("[red]Error: Not authenticated properly.[/red]")
            self._wait_for_continue()
            return

        with console.status("[bold green]Fetching grades...[/bold green]"):
            try:
                report = client.get_user_grades_table(course_id, user_id)
            except Exception as e:
                rprint(f"[red]Error loading grades: {e}[/red]")
                self._wait_for_continue()
                return

        tables = report.get('tables', [])
        if not tables:
            rprint("[yellow]No grades found for this course.[/yellow]")
            self._wait_for_continue()
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
        self._wait_for_continue()

    def _show_course_assignments(self, course_id: int, course_name: str):
        """Show assignments for a specific course."""
        self._clear_screen()
        self._print_header(f"Assignments - {course_name}")

        from tiss_tuwel_cli.cli.courses import assignments as show_assignments
        try:
            show_assignments(course_id=course_id)
        except Exception as e:
            rprint(f"[red]Error loading assignments: {e}[/red]")

        self._wait_for_continue()

    def _download_course_materials(self, course_id: int):
        """Download materials from a course."""
        self._clear_screen()
        self._print_header("Download Materials")

        confirm = inquirer.confirm(
            message=f"Download all materials from course {course_id}?",
            default=False
        ).execute()

        if confirm:
            from tiss_tuwel_cli.cli.courses import download
            try:
                download(course_id=course_id)
            except Exception as e:
                rprint(f"[red]Error downloading materials: {e}[/red]")

        self._wait_for_continue()

    def _show_assignments(self):
        """Show all assignments."""
        self._clear_screen()
        self._print_header("All Assignments")

        from tiss_tuwel_cli.cli.courses import assignments as show_assignments
        try:
            show_assignments()
        except Exception as e:
            rprint(f"[red]Error loading assignments: {e}[/red]")

        self._wait_for_continue()

    def _show_checkmarks(self):
        """Show Kreuzerlübungen status."""
        self._clear_screen()
        self._print_header("Kreuzerlübungen")

        from tiss_tuwel_cli.cli.courses import checkmarks as show_checkmarks
        try:
            show_checkmarks()
        except Exception as e:
            rprint(f"[red]Error loading checkmarks: {e}[/red]")

        self._wait_for_continue()

    def _show_exam_registration(self):
        """Show detailed exam registration information."""
        self._clear_screen()
        self._print_header("Exam Registration")

        with console.status("[bold green]Fetching exam information...[/bold green]"):
            # Force refresh of exam alerts
            self._exam_alerts_cache = None
            alerts = self._get_exam_alerts()

        if not alerts:
            rprint("[yellow]No upcoming exam registrations found for your courses.[/yellow]")
            rprint()
            rprint("[dim]This feature checks TISS for exam dates on your current TUWEL courses.[/dim]")
            rprint("[dim]Make sure your course shortnames contain the TISS course number (e.g., '104.633').[/dim]")
            self._wait_for_continue()
            return

        # Group by status
        open_now = [a for a in alerts if a.get('days_to_registration', 0) < 0]
        opening_soon = [a for a in alerts if 0 <= a.get('days_to_registration', 0) <= 7]
        upcoming = [a for a in alerts if a.get('days_to_registration', 0) > 7]

        if open_now:
            console.print(Panel(
                "[bold green]🟢 Registration Open Now[/bold green]",
                expand=False
            ))
            table = Table(expand=True)
            table.add_column("Course", style="white", no_wrap=False)
            table.add_column("Exam Date", style="cyan")
            table.add_column("Mode", style="dim")
            table.add_column("Closes", style="yellow")

            for alert in open_now:
                reg_end = alert.get('registration_end', '')
                closes = reg_end[:10] if reg_end else 'Unknown'
                table.add_row(
                    alert.get('course', ''),
                    alert.get('exam_date', 'TBD')[:10] if alert.get('exam_date') else 'TBD',
                    alert.get('mode', 'Unknown'),
                    closes
                )
            console.print(table)
            console.print()

        if opening_soon:
            console.print(Panel(
                "[bold yellow]🟡 Opening This Week[/bold yellow]",
                expand=False
            ))
            table = Table(expand=True)
            table.add_column("Course", style="white", no_wrap=False)
            table.add_column("Exam Date", style="cyan")
            table.add_column("Opens In", style="yellow", justify="right")

            for alert in opening_soon:
                days = alert.get('days_to_registration', 0)
                if days == 0:
                    opens_in = "Today!"
                else:
                    opens_in = f"{days} days"
                table.add_row(
                    alert.get('course', ''),
                    alert.get('exam_date', 'TBD')[:10] if alert.get('exam_date') else 'TBD',
                    opens_in
                )
            console.print(table)
            console.print()

        if upcoming:
            console.print(Panel(
                "[bold dim]📋 Coming Up[/bold dim]",
                expand=False
            ))
            table = Table(expand=True)
            table.add_column("Course", style="dim", no_wrap=False)
            table.add_column("Exam Date", style="dim")
            table.add_column("Registration Opens", style="dim")

            for alert in upcoming[:5]:
                table.add_row(
                    alert.get('course', ''),
                    alert.get('exam_date', 'TBD')[:10] if alert.get('exam_date') else 'TBD',
                    alert.get('registration_start', 'TBD')[:10] if alert.get('registration_start') else 'TBD'
                )
            console.print(table)
            console.print()

        rprint("[dim]💡 Tip: Visit TISS to complete your exam registration.[/dim]")
        self._wait_for_continue()

    def _show_weekly_overview(self):
        """Show events and deadlines for the current week using shared dashboard logic."""
        self._clear_screen()
        # Header is printed by the function

        from tiss_tuwel_cli.cli.dashboard import weekly_overview
        try:
            weekly_overview()
        except Exception as e:
            rprint(f"[red]Error loading weekly overview: {e}[/red]")

        self._wait_for_continue()

    def _show_grade_summary(self):
        """Show grades summary."""
        self._clear_screen()
        self._print_header("My Grades")

        from tiss_tuwel_cli.cli.courses import grades as show_grades
        try:
            show_grades()
        except Exception as e:
            rprint(f"[red]Error loading grades: {e}[/red]")

        self._wait_for_continue()

    def _show_participation_menu(self):
        """Show participation tracking menu."""
        from tiss_tuwel_cli.participation_tracker import ParticipationTracker

        tracker = ParticipationTracker()

        while True:
            self._clear_screen()
            self._print_header("Exercise Participation Tracker")

            # Show summary
            all_courses = tracker.get_all_courses()
            if all_courses:
                rprint("[bold]📊 Tracked Courses[/bold]")
                for course_id, data in all_courses.items():
                    stats = tracker.calculate_probability(course_id)
                    if stats:
                        prob = stats['adjusted_probability']
                        prob_color = "red" if prob > 50 else "yellow" if prob > 30 else "green"
                        rprint(
                            f"  [{prob_color}]•[/{prob_color}] {stats['course_name']} "
                            f"(ID: {course_id}) - {stats['times_called']}/{stats['total_sessions']} - "
                            f"[{prob_color}]{prob:.0f}% chance[/{prob_color}]"
                        )
                rprint()
            else:
                rprint("[dim]No participation data recorded yet.[/dim]")
                rprint()

            choices = [
                Choice(value="record", name="✏️  Record Session Participation"),
                Choice(value="stats", name="📊 View Detailed Statistics"),
                Choice(value="group", name="👥 Set Group Size"),
                Separator(),
                Choice(value="back", name="← Back"),
            ]

            action = inquirer.select(
                message="Select an option:",
                choices=choices,
                pointer="→",
                qmark="",
            ).execute()

            if action == "back":
                break
            elif action == "record":
                self._record_participation()
            elif action == "stats":
                self._view_participation_stats()
            elif action == "group":
                self._set_group_size()

    def _record_participation(self):
        """Record a participation event."""
        # Get course list
        client = self._get_tuwel_client()
        if not client:
            return

        with console.status("[bold green]Fetching courses...[/bold green]"):
            courses = client.get_enrolled_courses('inprogress')

        if not courses:
            rprint("[yellow]No current courses found.[/yellow]")
            self._wait_for_continue()
            return

        # Select course
        course_choices = [
            Choice(
                value=course,
                name=f"[{course.get('id')}] {course.get('fullname', 'Unknown')}"
            )
            for course in courses
        ]

        selected_course = inquirer.select(
            message="Select course:",
            choices=course_choices,
            pointer="→",
        ).execute()

        # Enter exercise name
        exercise_name = inquirer.text(
            message="Exercise name/number (e.g., 'Exercise 3'):",
        ).execute()

        if not exercise_name:
            return

        # Were you called?
        was_called = inquirer.confirm(
            message="Were you called to present?",
            default=False
        ).execute()

        # Delegate to shared command
        from tiss_tuwel_cli.cli.courses import track_participation
        self._clear_screen()
        track_participation(
            course_id=selected_course.get('id'),
            exercise_name=exercise_name,
            was_called=was_called
        )

        self._wait_for_continue()

    def _view_participation_stats(self):
        """View detailed participation statistics."""
        from tiss_tuwel_cli.participation_tracker import ParticipationTracker

        self._clear_screen()
        self._print_header("Participation Statistics")

        tracker = ParticipationTracker()
        all_courses = tracker.get_all_courses()

        if not all_courses:
            rprint("[yellow]No participation data found.[/yellow]")
            self._wait_for_continue()
            return

        # Select course
        course_choices = [
            Choice(
                value=course_id,
                name=f"{data.get('course_name', f'Course {course_id}')} (ID: {course_id})"
            )
            for course_id, data in all_courses.items()
        ]

        selected_id = inquirer.select(
            message="Select course:",
            choices=course_choices,
            pointer="→",
        ).execute()

        # Delegate to shared command
        from tiss_tuwel_cli.cli.courses import participation_stats
        self._clear_screen()
        participation_stats(course_id=selected_id)

        self._wait_for_continue()

    def _set_group_size(self):
        """Set the group size for a course."""
        from tiss_tuwel_cli.participation_tracker import ParticipationTracker

        self._clear_screen()
        self._print_header("Set Group Size")

        tracker = ParticipationTracker()
        all_courses = tracker.get_all_courses()

        if not all_courses:
            rprint("[yellow]No participation data found. Record a session first.[/yellow]")
            self._wait_for_continue()
            return

        # Select course
        course_choices = [
            Choice(
                value=course_id,
                name=f"{data.get('course_name', f'Course {course_id}')} (current: {data.get('group_size', 1)})"
            )
            for course_id, data in all_courses.items()
        ]

        selected_id = inquirer.select(
            message="Select course:",
            choices=course_choices,
            pointer="→",
        ).execute()

        # Get new group size
        group_size = inquirer.number(
            message="Average group size (number of students):",
            min_allowed=1,
            max_allowed=100,
            default=10
        ).execute()

        if group_size:
            tracker.set_group_size(selected_id, int(group_size))
            rprint(f"[green]✓ Group size updated to {int(group_size)}[/green]")

        self._wait_for_continue()

    def _show_timeline(self):
        """Show unified timeline."""
        self._clear_screen()
        from tiss_tuwel_cli.cli.timeline import timeline
        timeline(export=False)
        self._wait_for_continue()

    def _show_todo(self):
        """Show urgent tasks."""
        self._clear_screen()
        from tiss_tuwel_cli.cli.todo import todo
        todo()
        self._wait_for_continue()

    def _export_calendar(self):
        """Export calendar to ICS."""
        self._clear_screen()
        self._print_header("Export Calendar")

        # Use simple timeline export now
        from tiss_tuwel_cli.cli.timeline import timeline
        try:
            timeline(export=True)
        except Exception as e:
            rprint(f"[red]Export failed: {e}[/red]")

        self._wait_for_continue()

    def _open_vowi_for_course(self, course_title: str):
        """Open VoWi search for a course in the browser."""
        import webbrowser
        from tiss_tuwel_cli.utils import get_vowi_search_url

        self._clear_screen()
        self._print_header("Open VoWi")

        url = get_vowi_search_url(course_title)
        console.print(f"[cyan]Opening VoWi search for:[/cyan] {course_title}")
        console.print(f"[dim]URL: {url}[/dim]")
        console.print()

        try:
            webbrowser.open(url)
            console.print("[green]✓ Opened in browser[/green]")
        except Exception as e:
            console.print(f"[red]Error opening browser: {e}[/red]")
            console.print(f"[yellow]Please open this URL manually:[/yellow] {url}")

        self._wait_for_continue()

    def _open_tuwel_course(self, course_id: int):
        """Open TUWEL course page in the browser."""
        import webbrowser
        from tiss_tuwel_cli.utils import get_tuwel_course_url

        self._clear_screen()
        self._print_header("Open TUWEL Course")

        url = get_tuwel_course_url(course_id)
        console.print(f"[cyan]Opening TUWEL course page...[/cyan]")
        console.print(f"[dim]URL: {url}[/dim]")
        console.print()

        try:
            webbrowser.open(url)
            console.print("[green]✓ Opened in browser[/green]")
        except Exception as e:
            console.print(f"[red]Error opening browser: {e}[/red]")
            console.print(f"[yellow]Please open this URL manually:[/yellow] {url}")

        self._wait_for_continue()

    def _open_tiss_course(self, course_number: str):
        """Open TISS course page in the browser."""
        import webbrowser
        from tiss_tuwel_cli.utils import get_tiss_course_url, get_current_semester

        self._clear_screen()
        self._print_header("Open TISS Course")

        semester = get_current_semester()
        url = get_tiss_course_url(course_number, semester)
        console.print(f"[cyan]Opening TISS course page...[/cyan]")
        console.print(f"[dim]Course: {course_number}, Semester: {semester}[/dim]")
        console.print(f"[dim]URL: {url}[/dim]")
        console.print()

        try:
            webbrowser.open(url)
            console.print("[green]✓ Opened in browser[/green]")
        except Exception as e:
            console.print(f"[red]Error opening browser: {e}[/red]")
            console.print(f"[yellow]Please open this URL manually:[/yellow] {url}")

        self._wait_for_continue()

    def _show_unified_view(self):
        """Show unified TISS+TUWEL course view."""
        self._clear_screen()
        self._print_header("Unified Course View (TISS + TUWEL)")

        from tiss_tuwel_cli.cli.features import unified_course_view
        try:
            unified_course_view()
        except Exception as e:
            rprint(f"[red]Error: {e}[/red]")

        self._wait_for_continue()

    def _show_tiss_search(self):
        """Show TISS course search interface."""
        self._clear_screen()
        self._print_header("TISS Course Search")

        def validate_course_number(text: str) -> bool:
            """Validate TISS course number format (e.g., 104.633 or 104633)."""
            if not text:
                return False
            # Accept formats like "104.633", "104633", etc.
            pattern = r'^\d{3}\.?\d{3}$'
            return bool(re.match(pattern, text.strip()))

        course_number = inquirer.text(
            message="Course number (e.g., 104.633):",
            validate=validate_course_number,
            invalid_message="Please enter a valid course number (e.g., 104.633)",
        ).execute()

        if not course_number:
            return

        current_year = datetime.now().year
        current_month = datetime.now().month
        default_semester = f"{current_year}W" if current_month >= 9 else f"{current_year}S"

        semester = inquirer.text(
            message="Semester (e.g., 2025W, 2024S):",
            default=default_semester,
        ).execute()

        console.print()

        from tiss_tuwel_cli.cli.courses import tiss_course
        try:
            tiss_course(course_number=course_number, semester=semester)
        except Exception as e:
            rprint(f"[red]Error searching TISS: {e}[/red]")

        self._wait_for_continue()


def interactive():
    """
    Launch the interactive menu-driven mode.
    """
    console.print(Panel("[bold blue]TU Wien Companion[/bold blue]\n[dim]Interactive Mode[/dim]", expand=False))

    try:
        client = get_tuwel_client()
        info = client.get_site_info()
        console.print(f"\nWelcome back, {info.get('fullname')}\n")

    except Exception as e:
        console.print(f"\n[bold red]Error:[/bold red] {e}")
        return

    menu = InteractiveMenu()

    # Check for first run
    if not config.get_setting("wizard_completed"):
        from tiss_tuwel_cli.cli.settings import run_wizard
        console.print(Panel("[bold green]Welcome to TU Wien Companion![/bold green]\n\nSince this is your first time, let's set things up.", expand=False))
        if inquirer.confirm("Start setup wizard now?", default=True).execute():
            run_wizard()
        else:
            # Mark as completed even if skipped to avoid nagging, or maybe we want to nag?
            # User said "make the user go through", but skipping is usually polite.
            # Let's nag next time if they skip.
            pass

    # Print compact summary
    from tiss_tuwel_cli.cli.rc import get_summary_line
    summary = get_summary_line()
    if summary:
        console.print(summary)
        console.print()

    while True:
        choices = [
            Separator("─── Main Menu ───"),
            Choice(value="study", name="📚 Study"),
            Choice(value="planning", name="📅 Planning & Deadlines"),
            Choice(value="tools", name="🛠️ Tools & Utilities"),
            Separator(),
            Choice(value="login", name="🔐 Account"),
            Choice(value="settings", name="⚙️ Settings"),
            Choice(value="quit", name="🚪 Quit"),
        ]

        action = inquirer.select(
            message="Select a category:",
            choices=choices,
            pointer="→",
            qmark="",
            amark="",
        ).execute()

        if action == "quit":
            console.print("[bold green]Goodbye![/bold green]")
            break
        elif action == "login":
            menu._show_login_menu()
        elif action == "settings":
            menu._show_settings()
        elif action == "study":
            menu._show_study_menu()
        elif action == "planning":
            menu._show_planning_menu()
        elif action == "tools":
            menu._show_tools_menu()
