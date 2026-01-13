"""
Interactive menu mode for the TU Wien Companion CLI.

This module provides an interactive, menu-based interface for using
all CLI features in a user-friendly way.
"""

from typing import List, Optional

from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.prompt import IntPrompt, Prompt
from rich.table import Table

console = Console()


class InteractiveMenu:
    """
    Interactive menu system for the CLI.
    
    Provides a clean, easy-to-use interface for navigating
    and using all CLI features interactively.
    """

    def __init__(self):
        """Initialize the interactive menu."""
        self._tuwel_client = None
        self._courses_cache: List[dict] = []

    def _get_tuwel_client(self):
        """Get or create the TUWEL client."""
        if self._tuwel_client is None:
            from tiss_tuwel_cli.cli import get_tuwel_client
            self._tuwel_client = get_tuwel_client()
        return self._tuwel_client

    def _clear_screen(self):
        """Clear the console screen."""
        console.clear()

    def _print_header(self, title: str = "TU Wien Companion"):
        """Print the application header."""
        console.print(Panel(
            f"[bold blue]{title}[/bold blue]",
            subtitle="Interactive Mode",
            expand=False
        ))
        console.print()

    def _print_menu_options(self, options: List[tuple]):
        """
        Print a list of menu options.
        
        Args:
            options: List of (key, label) tuples.
        """
        for key, label in options:
            console.print(f"  [cyan][{key}][/cyan] {label}")
        console.print()

    def _wait_for_enter(self):
        """Wait for user to press Enter."""
        console.print()
        Prompt.ask("[dim]Press Enter to continue[/dim]", default="")

    def _get_courses(self, classification: str = 'inprogress') -> List[dict]:
        """
        Fetch and cache courses.
        
        Args:
            classification: Course classification (past, inprogress, future).
            
        Returns:
            List of course dictionaries.
        """
        client = self._get_tuwel_client()
        with console.status(f"[bold green]Fetching {classification} courses...[/bold green]"):
            self._courses_cache = client.get_enrolled_courses(classification)
        return self._courses_cache

    def _select_course(self) -> Optional[dict]:
        """
        Display course selection menu and return selected course.
        
        Returns:
            Selected course dictionary, or None if cancelled.
        """
        courses = self._get_courses()

        if not courses:
            rprint("[yellow]No courses found.[/yellow]")
            self._wait_for_enter()
            return None

        table = Table(title="Select a Course")
        table.add_column("#", justify="right", style="dim")
        table.add_column("ID", justify="right", style="cyan")
        table.add_column("Shortname", style="green")
        table.add_column("Fullname")

        for i, course in enumerate(courses, 1):
            table.add_row(
                str(i),
                str(course.get('id')),
                course.get('shortname', ''),
                course.get('fullname', '')
            )

        console.print(table)
        console.print()
        console.print("[dim]Enter 0 to go back[/dim]")

        while True:
            try:
                choice = IntPrompt.ask("Select course number", default=0)
                if choice == 0:
                    return None
                if 1 <= choice <= len(courses):
                    return courses[choice - 1]
                rprint("[red]Invalid selection. Please try again.[/red]")
            except (ValueError, KeyboardInterrupt):
                return None

    def show_main_menu(self):
        """Display and handle the main menu."""
        while True:
            self._clear_screen()
            self._print_header()

            options = [
                ("1", "📊 Dashboard - View upcoming events"),
                ("2", "📚 My Courses - Browse enrolled courses"),
                ("3", "📝 Assignments - View all assignments"),
                ("4", "✅ Kreuzerlübungen - Check exercise status"),
                ("5", "🔍 Search TISS - Look up course information"),
                ("q", "Quit"),
            ]

            self._print_menu_options(options)

            choice = Prompt.ask("Select an option", choices=["1", "2", "3", "4", "5", "q"], default="q")

            if choice == "1":
                self._show_dashboard()
            elif choice == "2":
                self._show_courses_menu()
            elif choice == "3":
                self._show_assignments()
            elif choice == "4":
                self._show_checkmarks()
            elif choice == "5":
                self._show_tiss_search()
            elif choice.lower() == "q":
                self._clear_screen()
                rprint("[bold green]Goodbye![/bold green]")
                break

    def _show_dashboard(self):
        """Show the dashboard view."""
        self._clear_screen()
        self._print_header("Dashboard")

        # Import and call the dashboard function
        from tiss_tuwel_cli.cli.dashboard import dashboard as show_dashboard
        try:
            show_dashboard()
        except Exception as e:
            rprint(f"[red]Error loading dashboard: {e}[/red]")

        self._wait_for_enter()

    def _show_courses_menu(self):
        """Show the courses menu."""
        while True:
            self._clear_screen()
            self._print_header("My Courses")

            options = [
                ("1", "📗 Current courses (in progress)"),
                ("2", "📕 Past courses"),
                ("3", "📘 Future courses"),
                ("b", "Back to main menu"),
            ]

            self._print_menu_options(options)

            choice = Prompt.ask("Select an option", choices=["1", "2", "3", "b"], default="b")

            classification = None
            if choice == "1":
                classification = "inprogress"
            elif choice == "2":
                classification = "past"
            elif choice == "3":
                classification = "future"
            elif choice.lower() == "b":
                break

            if classification:
                self._show_course_list(classification)

    def _show_course_list(self, classification: str):
        """
        Show list of courses with options.
        
        Args:
            classification: Course classification.
        """
        courses = self._get_courses(classification)

        if not courses:
            rprint(f"[yellow]No {classification} courses found.[/yellow]")
            self._wait_for_enter()
            return

        while True:
            self._clear_screen()
            self._print_header(f"Courses ({classification})")

            table = Table()
            table.add_column("#", justify="right", style="dim")
            table.add_column("ID", justify="right", style="cyan")
            table.add_column("Shortname", style="green")
            table.add_column("Fullname")

            for i, course in enumerate(courses, 1):
                table.add_row(
                    str(i),
                    str(course.get('id')),
                    course.get('shortname', ''),
                    course.get('fullname', '')
                )

            console.print(table)
            console.print()
            console.print("[dim]Enter a course number to view details, or 0 to go back[/dim]")

            try:
                choice = IntPrompt.ask("Select course", default=0)
                if choice == 0:
                    break
                if 1 <= choice <= len(courses):
                    self._show_course_details(courses[choice - 1])
                else:
                    rprint("[red]Invalid selection.[/red]")
            except (ValueError, KeyboardInterrupt):
                break

    def _show_course_details(self, course: dict):
        """
        Show details and actions for a specific course.
        
        Args:
            course: Course dictionary.
        """
        course_id = course.get('id')
        course_name = course.get('fullname', 'Unknown Course')

        while True:
            self._clear_screen()
            self._print_header(course.get('shortname', 'Course'))

            console.print(Panel(
                f"[bold]{course_name}[/bold]\n"
                f"[dim]Course ID: {course_id}[/dim]",
                title="Course Details"
            ))
            console.print()

            options = [
                ("1", "📊 View Grades"),
                ("2", "📝 View Assignments"),
                ("3", "📥 Download Materials"),
                ("b", "Back"),
            ]

            self._print_menu_options(options)

            choice = Prompt.ask("Select an option", choices=["1", "2", "3", "b"], default="b")

            if choice == "1":
                self._show_course_grades(course_id)
            elif choice == "2":
                self._show_course_assignments(course_id, course_name)
            elif choice == "3":
                self._download_course_materials(course_id)
            elif choice.lower() == "b":
                break

    def _show_course_grades(self, course_id: int):
        """
        Show grades for a specific course.
        
        Args:
            course_id: The course ID.
        """
        self._clear_screen()
        self._print_header("Grades")

        from tiss_tuwel_cli.cli.courses import grades as show_grades
        try:
            show_grades(course_id=course_id)
        except Exception as e:
            rprint(f"[red]Error loading grades: {e}[/red]")

        self._wait_for_enter()

    def _show_course_assignments(self, course_id: int, course_name: str):
        """
        Show assignments for a specific course.
        
        Args:
            course_id: The course ID.
            course_name: The course name for display.
        """
        self._clear_screen()
        self._print_header(f"Assignments - {course_name}")

        # Show all assignments (filtered display would require API changes)
        from tiss_tuwel_cli.cli.courses import assignments as show_assignments
        try:
            show_assignments()
        except Exception as e:
            rprint(f"[red]Error loading assignments: {e}[/red]")

        self._wait_for_enter()

    def _download_course_materials(self, course_id: int):
        """
        Download materials from a course.
        
        Args:
            course_id: The course ID.
        """
        self._clear_screen()
        self._print_header("Download Materials")

        confirm = Prompt.ask(
            f"Download all materials from course {course_id}?",
            choices=["y", "n"],
            default="n"
        )

        if confirm.lower() == "y":
            from tiss_tuwel_cli.cli.courses import download
            try:
                download(course_id=course_id)
            except Exception as e:
                rprint(f"[red]Error downloading materials: {e}[/red]")

        self._wait_for_enter()

    def _show_assignments(self):
        """Show all assignments."""
        self._clear_screen()
        self._print_header("Assignments")

        from tiss_tuwel_cli.cli.courses import assignments as show_assignments
        try:
            show_assignments()
        except Exception as e:
            rprint(f"[red]Error loading assignments: {e}[/red]")

        self._wait_for_enter()

    def _show_checkmarks(self):
        """Show Kreuzerlübungen status."""
        self._clear_screen()
        self._print_header("Kreuzerlübungen")

        from tiss_tuwel_cli.cli.courses import checkmarks as show_checkmarks
        try:
            show_checkmarks()
        except Exception as e:
            rprint(f"[red]Error loading checkmarks: {e}[/red]")

        self._wait_for_enter()

    def _show_tiss_search(self):
        """Show TISS course search interface."""
        self._clear_screen()
        self._print_header("TISS Course Search")

        console.print("[dim]Enter course number (e.g., 192.167) and semester (e.g., 2024W)[/dim]")
        console.print()

        course_number = Prompt.ask("Course number", default="")
        if not course_number:
            return

        semester = Prompt.ask("Semester (e.g., 2024W, 2024S)", default="2024W")

        console.print()

        from tiss_tuwel_cli.cli.courses import tiss_course
        try:
            tiss_course(course_number=course_number, semester=semester)
        except Exception as e:
            rprint(f"[red]Error searching TISS: {e}[/red]")

        self._wait_for_enter()


def interactive():
    """
    Start interactive mode.
    
    Launches a user-friendly menu-based interface for interacting
    with all CLI features. Navigate through your courses, view grades,
    assignments, and more.
    """
    menu = InteractiveMenu()
    try:
        menu.show_main_menu()
    except KeyboardInterrupt:
        rprint("\n[bold green]Goodbye![/bold green]")
