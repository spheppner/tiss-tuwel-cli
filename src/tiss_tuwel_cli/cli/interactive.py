"""
Interactive menu mode for the TU Wien Companion CLI.

This module provides an interactive, menu-based interface for using
all CLI features in a user-friendly way with keyboard navigation.
"""

from datetime import datetime
from typing import Any, Dict, List, Optional

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from tiss_tuwel_cli.config import ConfigManager
from tiss_tuwel_cli.utils import strip_html, timestamp_to_date

console = Console()
config = ConfigManager()


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
                except Exception:
                    pass
        return self._user_info

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
        """Print an intelligent dashboard summary."""
        client = self._get_tuwel_client()
        if not client:
            return

        user_info = self._get_user_info()
        if user_info:
            name = user_info.get('fullname', 'Student')
            console.print(f"[dim]Welcome back,[/dim] [bold cyan]{name}[/bold cyan]")
            console.print()

        try:
            # Fetch upcoming events
            with console.status("[dim]Loading dashboard...[/dim]"):
                upcoming = client.get_upcoming_calendar()
                events = upcoming.get('events', [])[:5]

            if events:
                console.print("[bold]📅 Upcoming Deadlines[/bold]")
                for event in events:
                    course = event.get('course', {}).get('shortname', '')
                    name = event.get('name', 'Unknown')
                    time = timestamp_to_date(event.get('timestart'))
                    # Color based on urgency
                    now = datetime.now().timestamp()
                    event_time = event.get('timestart', 0)
                    days_left = (event_time - now) / 86400

                    if days_left < 1:
                        style = "bold red"
                        urgency = "⚠️ "
                    elif days_left < 3:
                        style = "yellow"
                        urgency = "⏰ "
                    else:
                        style = "green"
                        urgency = "   "

                    console.print(f"  {urgency}[{style}]{time}[/{style}] [{style}]{course}[/{style}] - {name}")
                console.print()
        except Exception:
            pass

    def _wait_for_continue(self):
        """Wait for user to continue."""
        inquirer.confirm(message="Press Enter to continue...", default=True).execute()

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
                    Choice(value="assignments", name="📝 Assignments"),
                    Choice(value="checkmarks", name="✅ Kreuzerlübungen"),
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
            elif action == "assignments":
                self._show_assignments()
            elif action == "checkmarks":
                self._show_checkmarks()
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
                # Regular grade item
                style = ""
                if "0,00" in percent_val or "0.00" in percent_val:
                    style = "red"
                elif "100" in percent_val:
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
                        days_left = (due - now) / 86400
                        if days_left < 1:
                            status = "[bold red]Due Soon![/bold red]"
                        elif days_left < 3:
                            status = "[yellow]Due in {:.0f}d[/yellow]".format(days_left)
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

    def _show_tiss_search(self):
        """Show TISS course search interface."""
        self._clear_screen()
        self._print_header("TISS Course Search")

        course_number = inquirer.text(
            message="Course number (e.g., 192.167):",
            validate=lambda x: len(x) > 0,
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
