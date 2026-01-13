"""
Interactive menu mode for the TU Wien Companion CLI.

This module provides an interactive, menu-based interface for using
all CLI features in a user-friendly way with keyboard navigation.
"""

import re
from collections import defaultdict
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

from tiss_tuwel_cli.clients.tiss import TissClient
from tiss_tuwel_cli.config import ConfigManager
from tiss_tuwel_cli.utils import (
    days_until,
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
EXAM_ALERT_DAYS_AFTER = 7   # Show alerts for registrations that opened within this many days
MAX_COURSES_FOR_GRADES = 5   # Limit API calls when fetching grade summaries


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
        """
        Fetch upcoming exam registration alerts for ongoing courses.
        
        Checks TISS for exam dates where registration is starting soon
        or currently open for courses the user is enrolled in.
        
        Returns:
            List of alert dictionaries with course info and registration details.
        """
        if self._exam_alerts_cache is not None:
            return self._exam_alerts_cache
        
        self._exam_alerts_cache = []
        
        # Get current courses
        client = self._get_tuwel_client()
        if not client:
            return []
        
        try:
            courses = client.get_enrolled_courses('inprogress')
        except Exception:
            return []
        
        # For each course, try to extract course number and fetch exam dates
        for course in courses:
            shortname = course.get('shortname', '')
            course_num = extract_course_number(shortname)
            
            if not course_num:
                continue
            
            try:
                exams = tiss.get_exam_dates(course_num)
                if isinstance(exams, dict) and 'error' in exams:
                    continue
                if not isinstance(exams, list):
                    continue
                
                for exam in exams:
                    reg_start = exam.get('registrationStart')
                    reg_end = exam.get('registrationEnd')
                    exam_date = exam.get('date')
                    
                    if reg_start:
                        days_to_reg = days_until(reg_start)
                        days_to_exam = days_until(exam_date) if exam_date else None
                        
                        # Alert if registration starts within configured days
                        # or is currently open (reg_start passed but reg_end not)
                        if days_to_reg is not None:
                            if -EXAM_ALERT_DAYS_AFTER <= days_to_reg <= EXAM_ALERT_DAYS_BEFORE:
                                alert = {
                                    'course': shortname,
                                    'course_fullname': course.get('fullname', shortname),
                                    'exam_date': exam_date,
                                    'registration_start': reg_start,
                                    'registration_end': reg_end,
                                    'days_to_registration': days_to_reg,
                                    'days_to_exam': days_to_exam,
                                    'mode': exam.get('mode', 'Unknown'),
                                }
                                self._exam_alerts_cache.append(alert)
            except Exception:
                # Skip courses that fail - don't let one failure break the loop
                continue
        
        # Sort by registration start date (soonest first)
        self._exam_alerts_cache.sort(
            key=lambda x: x.get('days_to_registration', 999)
        )
        
        return self._exam_alerts_cache

    def _get_weekly_overview(self) -> List[dict]:
        """
        Get events and deadlines for the upcoming week.
        
        Returns:
            List of events happening in the next 7 days.
        """
        client = self._get_tuwel_client()
        if not client:
            return []
        
        try:
            upcoming = client.get_upcoming_calendar()
            events = upcoming.get('events', [])

            # Filter to next 7 days
            now = datetime.now().timestamp()
            week_later = now + (7 * SECONDS_PER_DAY)
            
            weekly = []
            for event in events:
                event_time = event.get('timestart', 0)
                if now <= event_time <= week_later:
                    weekly.append(event)
            
            return weekly
        except Exception:
            return []

    def _get_study_progress(self) -> Dict[str, Any]:
        """
        Calculate overall study progress across all courses.
        
        Returns:
            Dictionary with progress statistics.
        """
        client = self._get_tuwel_client()
        if not client:
            return {}
        
        try:
            # Get checkmarks data for completion tracking
            checkmarks_data = client.get_checkmarks([])
            checkmarks_list = checkmarks_data.get('checkmarks', [])
            
            total_checked = 0
            total_possible = 0
            
            for cm in checkmarks_list:
                examples = cm.get('examples', [])
                total_checked += sum(1 for ex in examples if ex.get('checked'))
                total_possible += len(examples)
            
            # Get assignments for pending work
            assignments_data = client.get_assignments()
            courses_with_assignments = assignments_data.get('courses', [])
            
            now = datetime.now().timestamp()
            pending_assignments = 0
            overdue_assignments = 0
            
            for course in courses_with_assignments:
                for assign in course.get('assignments', []):
                    due = assign.get('duedate', 0)
                    if due > now:
                        pending_assignments += 1
                    elif due > now - (7 * SECONDS_PER_DAY):
                        # Overdue within last week
                        overdue_assignments += 1
            
            return {
                'checkmarks_completed': total_checked,
                'checkmarks_total': total_possible,
                'checkmarks_percentage': (
                    (total_checked / total_possible * 100) if total_possible > 0 else 0
                ),
                'pending_assignments': pending_assignments,
                'overdue_assignments': overdue_assignments,
            }
        except Exception:
            return {}

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
        """Display and handle the main menu."""
        while True:
            self._clear_screen()
            self._print_header("TU Wien Companion", "Interactive Mode")

            # Show smart dashboard if authenticated
            if self._is_authenticated():
                self._print_smart_dashboard()

            # Build menu choices based on auth status
            choices = []

            if self._is_authenticated():
                choices.extend([
                    Choice(value="courses", name="📚 My Courses"),
                    Choice(value="dashboard", name="📊 Dashboard"),
                    Choice(value="exams", name="🎓 Exam Registration"),
                    Choice(value="weekly", name="📆 This Week"),
                    Choice(value="assignments", name="📝 Assignments"),
                    Choice(value="checkmarks", name="✅ Kreuzerlübungen"),
                    Choice(value="participation", name="🎯 Exercise Participation"),
                    Choice(value="grades", name="🏆 Grade Summary"),
                    Separator("─── Advanced Features ───"),
                    Choice(value="compare", name="📊 Compare All Courses"),
                    Choice(value="study_time", name="⏱️ Study Time Estimator"),
                    Choice(value="export_cal", name="📅 Export Calendar"),
                    Choice(value="submissions", name="📌 Submission Tracker"),
                    Separator(),
                    Choice(value="tiss", name="🔍 Search TISS"),
                    Separator(),
                ])
            else:
                choices.append(Separator("─── Login Required ───"))

            choices.append(Choice(value="login", name="🔐 Login / Setup"))
            choices.append(Separator())
            choices.append(Choice(value="quit", name="🚪 Quit"))

            action = inquirer.select(
                message="Select an option:",
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
            elif action == "courses":
                self._show_courses_menu()
            elif action == "dashboard":
                self._show_dashboard()
            elif action == "exams":
                self._show_exam_registration()
            elif action == "weekly":
                self._show_weekly_overview()
            elif action == "assignments":
                self._show_assignments()
            elif action == "checkmarks":
                self._show_checkmarks()
            elif action == "participation":
                self._show_participation_menu()
            elif action == "grades":
                self._show_grade_summary()
            elif action == "compare":
                self._show_course_comparison()
            elif action == "study_time":
                self._show_study_time_estimate()
            elif action == "export_cal":
                self._export_calendar()
            elif action == "submissions":
                self._show_submission_tracker()
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
            Choice(value="auto", name="🌐 Automated Login (Browser)"),
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
        elif action == "manual":
            self._do_manual_setup()

    def _do_automated_login(self):
        """Perform automated browser login."""
        self._clear_screen()
        self._print_header("Automated Login")

        from tiss_tuwel_cli.cli.auth import login
        try:
            login()
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

        from tiss_tuwel_cli.cli.auth import setup
        try:
            setup()
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
                shortname = course.get('shortname', '')
                fullname = course.get('fullname', '')
                # Truncate if too long
                if len(fullname) > 50:
                    fullname = fullname[:47] + "..."
                choices.append(Choice(
                    value=course,
                    name=f"[{cid}] {shortname} - {fullname}"
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
        """Show details and actions for a specific course."""
        course_id = course.get('id')
        course_name = course.get('fullname', 'Unknown Course')
        shortname = course.get('shortname', '')

        while True:
            self._clear_screen()
            self._print_header(shortname or "Course Details")

            console.print(Panel(
                f"[bold]{course_name}[/bold]\n"
                f"[dim]Course ID: {course_id}[/dim]",
                title="📚 Course Information"
            ))
            console.print()

            action = inquirer.select(
                message="What would you like to do?",
                choices=[
                    Choice(value="grades", name="📊 View Grades"),
                    Choice(value="assignments", name="📝 View Assignments"),
                    Choice(value="download", name="📥 Download Materials"),
                    Separator(),
                    Choice(value="back", name="← Back"),
                ],
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
        self._print_header("Assignments")

        client = self._get_tuwel_client()
        if not client:
            rprint("[red]Error: Not authenticated.[/red]")
            self._wait_for_continue()
            return

        with console.status("[bold green]Fetching assignments...[/bold green]"):
            try:
                data = client.get_assignments()
            except Exception as e:
                rprint(f"[red]Error: {e}[/red]")
                self._wait_for_continue()
                return

        courses_with_assignments = data.get('courses', [])

        # Find assignments for this specific course
        table = Table(title=f"Assignments - {course_name[:40]}...", expand=True)
        table.add_column("Assignment", style="white", no_wrap=False)
        table.add_column("Due Date", style="green", justify="right")
        table.add_column("Status", justify="center")

        now = datetime.now().timestamp()
        found = False

        for course in courses_with_assignments:
            if course.get('id') == course_id:
                for assign in course.get('assignments', []):
                    found = True
                    due = assign.get('duedate', 0)
                    name = assign.get('name', 'Unknown')

                    if due < now:
                        status = "[red]Closed[/red]"
                    else:
                        days_left = (due - now) / SECONDS_PER_DAY
                        if days_left < 1:
                            status = "[bold red]Due Soon![/bold red]"
                        elif days_left < 3:
                            status = f"[yellow]Due in {days_left:.0f}d[/yellow]"
                        else:
                            status = "[green]Open[/green]"

                    table.add_row(name, timestamp_to_date(due), status)

        if found:
            console.print(table)
        else:
            rprint("[yellow]No assignments found for this course.[/yellow]")

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
        """Show Kreuzerlübungen status with clean, grouped view."""
        self._clear_screen()
        self._print_header("Kreuzerlübungen")

        client = self._get_tuwel_client()
        if not client:
            rprint("[red]Error: Not authenticated.[/red]")
            self._wait_for_continue()
            return

        with console.status("[bold green]Fetching Kreuzerlübungen...[/bold green]"):
            try:
                checkmarks_data = client.get_checkmarks([])
                checkmarks_list = checkmarks_data.get('checkmarks', [])
            except Exception as e:
                rprint(f"[red]Error fetching checkmarks: {e}[/red]")
                self._wait_for_continue()
                return

        if not checkmarks_list:
            rprint("[yellow]No Kreuzerlübungen found in your courses.[/yellow]")
            self._wait_for_continue()
            return

        # Group by course
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

        # Display grouped by course
        for course_id, data in courses_data.items():
            total_checked = data['total_checked']
            total_possible = data['total_possible']
            completion_pct = (total_checked / total_possible * 100) if total_possible > 0 else 0

            # Create summary panel
            avg_grade = data['total_grade'] / data['graded_count'] if data['graded_count'] > 0 else 0

            summary = f"[bold]Course {course_id}[/bold]\n"
            summary += f"Completion: {total_checked}/{total_possible} ({completion_pct:.0f}%)"
            if data['graded_count'] > 0:
                summary += f" | Avg Grade: {avg_grade:.1f}"

            console.print(Panel(summary, expand=True))

            # Create exercise table
            table = Table(expand=True, show_header=True, header_style="bold")
            table.add_column("Exercise", style="white", no_wrap=False)
            table.add_column("Checked", justify="center", style="cyan")
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
            console.print()

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
            rprint("[dim]Make sure your course shortnames contain the TISS course number (e.g., '192.167').[/dim]")
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
        """Show events and deadlines for the current week."""
        self._clear_screen()
        self._print_header("This Week")

        weekly = self._get_weekly_overview()

        if not weekly:
            rprint("[yellow]No events or deadlines in the next 7 days.[/yellow]")
            rprint()
            rprint("[green]🎉 Enjoy your free week![/green]")
            self._wait_for_continue()
            return

        # Group by day
        by_day: Dict[str, List[dict]] = defaultdict(list)

        for event in weekly:
            event_time = event.get('timestart', 0)
            day = datetime.fromtimestamp(event_time).strftime('%A, %b %d')
            by_day[day].append(event)

        now = datetime.now().timestamp()

        for day, events in by_day.items():
            console.print(f"[bold cyan]📅 {day}[/bold cyan]")
            for event in events:
                course = event.get('course', {}).get('shortname', '')
                event_name = event.get('name', 'Unknown')
                event_time = event.get('timestart', 0)
                time_str = datetime.fromtimestamp(event_time).strftime('%H:%M')

                days_left = (event_time - now) / SECONDS_PER_DAY
                if days_left < 1:
                    style = "bold red"
                elif days_left < 2:
                    style = "yellow"
                else:
                    style = "white"

                console.print(f"   [{style}]{time_str}[/{style}] [{style}]{course}[/{style}] - {event_name}")
            console.print()

        # Summary
        total = len(weekly)
        urgent = sum(1 for e in weekly if (e.get('timestart', 0) - now) < SECONDS_PER_DAY)
        rprint(f"[dim]Total: {total} events/deadlines this week")
        if urgent > 0:
            rprint(f"[bold red]⚠️ {urgent} in the next 24 hours![/bold red]")

        self._wait_for_continue()

    def _show_grade_summary(self):
        """Show a summary of grades across all courses."""
        self._clear_screen()
        self._print_header("Grade Summary")

        with console.status("[bold green]Fetching grades...[/bold green]"):
            # Force refresh
            self._grade_summary_cache = None
            summary = self._get_grade_summary()

        course_grades = summary.get('course_grades', [])
        avg = summary.get('average', 0)

        if not course_grades:
            rprint("[yellow]No grade data found for your current courses.[/yellow]")
            rprint()
            rprint("[dim]Grades will appear here once they are published in TUWEL.[/dim]")
            self._wait_for_continue()
            return

        console.print(Panel(
            f"[bold]📊 Overall Average: {avg:.1f}%[/bold]",
            expand=False,
            border_style="green" if avg >= 70 else "yellow" if avg >= 50 else "red"
        ))
        console.print()

        table = Table(title="Course Grades", expand=True)
        table.add_column("Course", style="white", no_wrap=False)
        table.add_column("Grade %", justify="right")
        table.add_column("Status", justify="center")

        for grade in course_grades:
            pct = grade.get('percentage', 0)
            course = grade.get('course', '')

            if pct >= 87.5:
                status = "[bold green]Excellent (1)[/bold green]"
                pct_style = "green"
            elif pct >= 75:
                status = "[green]Good (2)[/green]"
                pct_style = "green"
            elif pct >= 62.5:
                status = "[yellow]Satisfactory (3)[/yellow]"
                pct_style = "yellow"
            elif pct >= 50:
                status = "[yellow]Sufficient (4)[/yellow]"
                pct_style = "yellow"
            else:
                status = "[red]Fail (5)[/red]"
                pct_style = "red"

            table.add_row(
                course,
                f"[{pct_style}]{pct:.1f}%[/{pct_style}]",
                status
            )

        console.print(table)
        console.print()
        rprint(f"[dim]📊 Showing grades from {len(course_grades)} course(s)[/dim]")

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
        from tiss_tuwel_cli.participation_tracker import ParticipationTracker
        
        self._clear_screen()
        self._print_header("Record Participation")
        
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
        
        # Record it
        tracker = ParticipationTracker()
        tracker.record_participation(
            course_id=selected_course.get('id'),
            course_name=selected_course.get('fullname', f"Course {selected_course.get('id')}"),
            exercise_name=exercise_name,
            was_called=was_called
        )
        
        # Show updated stats
        stats = tracker.calculate_probability(selected_course.get('id'))
        if stats:
            self._clear_screen()
            self._print_header("Recorded!")
            
            status = "[green]✓ Called[/green]" if was_called else "[dim]○ Not called[/dim]"
            rprint(f"[bold]{exercise_name}[/bold] - {status}")
            rprint(f"[bold cyan]{stats['course_name']}[/bold cyan]")
            rprint()
            rprint(f"Total sessions: {stats['total_sessions']}")
            rprint(f"Times called: {stats['times_called']}")
            rprint(f"Next call probability: [yellow]{stats['adjusted_probability']:.1f}%[/yellow]")
        
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
        
        # Show detailed stats
        stats = tracker.calculate_probability(selected_id)
        if stats:
            self._clear_screen()
            from tiss_tuwel_cli.cli.courses import _display_detailed_stats
            _display_detailed_stats(stats)
        
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

    def _show_course_comparison(self):
        """Show course comparison view."""
        self._clear_screen()
        self._print_header("Course Comparison")
        
        from tiss_tuwel_cli.cli.features import compare_courses
        try:
            compare_courses()
        except Exception as e:
            rprint(f"[red]Error: {e}[/red]")
        
        self._wait_for_continue()

    def _show_study_time_estimate(self):
        """Show study time estimation."""
        self._clear_screen()
        self._print_header("Study Time Estimator")
        
        from tiss_tuwel_cli.cli.features import estimate_study_time
        try:
            estimate_study_time()
        except Exception as e:
            rprint(f"[red]Error: {e}[/red]")
        
        self._wait_for_continue()

    def _export_calendar(self):
        """Export calendar to ICS."""
        self._clear_screen()
        self._print_header("Export Calendar")
        
        from tiss_tuwel_cli.cli.features import export_calendar
        try:
            export_calendar()
        except Exception as e:
            rprint(f"[red]Error: {e}[/red]")
        
        self._wait_for_continue()

    def _show_submission_tracker(self):
        """Show submission tracker."""
        self._clear_screen()
        self._print_header("Assignment Submission Tracker")
        
        from tiss_tuwel_cli.cli.features import submission_tracker
        try:
            submission_tracker()
        except Exception as e:
            rprint(f"[red]Error: {e}[/red]")
        
        self._wait_for_continue()

    def _show_tiss_search(self):
        """Show TISS course search interface."""
        self._clear_screen()
        self._print_header("TISS Course Search")

        def validate_course_number(text: str) -> bool:
            """Validate TISS course number format (e.g., 192.167 or 192167)."""
            if not text:
                return False
            # Accept formats like "192.167", "192167", etc.
            pattern = r'^\d{3}\.?\d{3}$'
            return bool(re.match(pattern, text.strip()))

        course_number = inquirer.text(
            message="Course number (e.g., 192.167):",
            validate=validate_course_number,
            invalid_message="Please enter a valid course number (e.g., 192.167)",
        ).execute()

        if not course_number:
            return

        current_year = datetime.now().year
        current_month = datetime.now().month
        default_semester = f"{current_year}W" if current_month >= 9 else f"{current_year}S"

        semester = inquirer.text(
            message="Semester (e.g., 2024W, 2024S):",
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
    Start interactive mode.
    
    Launches a user-friendly menu-based interface with keyboard navigation
    for interacting with all CLI features. Navigate through your courses,
    view grades, assignments, and more using arrow keys.
    """
    menu = InteractiveMenu()
    try:
        menu.show_main_menu()
    except KeyboardInterrupt:
        rprint("\n[bold green]Goodbye![/bold green]")
    except Exception as e:
        rprint(f"\n[red]Error: {e}[/red]")
