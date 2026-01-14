"""
Interactive shell mode for the TU Wien Companion CLI.

This module provides an advanced REPL (Read-Eval-Print Loop) shell interface
with command history, tab completion, and a clean prompt-based experience.
"""

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

# Command definitions organized by category
# Each command has: (description, category)
COMMAND_REGISTRY = {
    # Shell commands
    "help": ("Show available commands", "shell"),
    "exit": ("Exit the shell", "shell"),
    "quit": ("Exit the shell", "shell"),
    "clear": ("Clear the screen", "shell"),
    "interactive": ("Switch to menu mode", "shell"),

    # Account
    "login": ("Log in to TUWEL", "account"),
    "settings": ("Configure preferences", "account"),

    # Study
    "courses": ("List enrolled courses", "study"),
    "assignments": ("Show assignments", "study"),
    "checkmarks": ("Show Kreuzerlübungen status", "study"),
    "grades": ("Show grades (requires course_id)", "study"),
    "download": ("Download course materials (requires course_id)", "study"),
    "track-participation": ("Track exercise participation", "study"),
    "participation-stats": ("Show participation statistics", "study"),

    # Planning
    "dashboard": ("Show dashboard with events", "planning"),
    "weekly": ("Show weekly overview", "planning"),
    "timeline": ("Show unified timeline", "planning"),
    "todo": ("Show urgent tasks", "planning"),
    "rc": ("Quick status summary", "planning"),

    # Tools
    "unified-view": ("Unified TISS+TUWEL course view", "tools"),
    "tiss-course": ("Search TISS for course (requires number)", "tools"),
    "export-calendar": ("Export calendar to .ics", "tools"),
    "course-stats": ("Show course statistics", "tools"),
    "open-vowi": ("Open VoWi search", "tools"),
}

# Category display order and labels
CATEGORIES = {
    "shell": ("Shell", "yellow"),
    "account": ("Account", "cyan"),
    "study": ("Study", "green"),
    "planning": ("Planning & Deadlines", "blue"),
    "tools": ("Tools & Utilities", "magenta"),
}

# Custom style for the prompt
prompt_style = Style.from_dict({
    'prompt': 'ansigreen bold',
})


class ShellCompleter(Completer):
    """Custom completer for shell commands with better filtering."""

    def __init__(self):
        self.commands = list(COMMAND_REGISTRY.keys())

    def get_completions(self, document, complete_event):
        """Get completions for the current input."""
        word_before_cursor = document.get_word_before_cursor()

        for command in self.commands:
            if command.startswith(word_before_cursor):
                desc, _ = COMMAND_REGISTRY.get(command, ("", ""))
                yield Completion(
                    command,
                    start_position=-len(word_before_cursor),
                    display=command,
                    display_meta=desc
                )


def print_banner():
    """Print the shell welcome banner."""
    # Show compact summary if logged in
    from tiss_tuwel_cli.config import ConfigManager
    config = ConfigManager()

    summary_line = ""
    if config.get_tuwel_token():
        try:
            from tiss_tuwel_cli.cli.rc import get_summary_line
            summary_line = get_summary_line()
        except Exception:
            pass

    banner_text = """[bold cyan]TU Wien Companion Shell[/bold cyan]

[dim]help[/dim] - commands | [dim]interactive[/dim] - menu mode | [dim]exit[/dim] - quit
[dim]Tab[/dim] - completion | [dim]↑↓[/dim] - history"""

    console.print(Panel(banner_text, border_style="cyan", expand=False))

    if summary_line:
        console.print(summary_line)
    console.print()


def print_help():
    """Print help information showing all available commands."""
    table = Table(title="Commands", expand=False, show_header=True, header_style="bold cyan")
    table.add_column("Command", style="green", no_wrap=True, width=20)
    table.add_column("Description", style="white")

    # Group commands by category
    for cat_key, (cat_name, cat_style) in CATEGORIES.items():
        commands_in_cat = [
            (cmd, desc) for cmd, (desc, c) in COMMAND_REGISTRY.items() if c == cat_key
        ]

        if commands_in_cat:
            # Category header
            table.add_row(f"[bold {cat_style}]─── {cat_name} ───[/bold {cat_style}]", "")

            for cmd, desc in sorted(commands_in_cat):
                table.add_row(f"  {cmd}", desc)

    console.print(table)
    console.print()


def execute_command(command_line: str) -> bool:
    """
    Execute a shell command.

    Args:
        command_line: The full command line entered by the user

    Returns:
        True to continue the shell, False to exit
    """
    parts = command_line.strip().split()
    if not parts:
        return True

    command = parts[0].lower()
    args = parts[1:] if len(parts) > 1 else []

    # Handle built-in shell commands
    if command in ["exit", "quit"]:
        return False

    elif command == "help":
        print_help()
        return True

    elif command == "clear":
        console.clear()
        return True

    elif command == "interactive":
        from tiss_tuwel_cli.cli.interactive import interactive
        try:
            interactive()
        except KeyboardInterrupt:
            console.print("\n[dim]Returned to shell[/dim]")
        return True

    # Handle CLI commands directly (not via CliRunner for better output)
    elif command in COMMAND_REGISTRY:
        try:
            _execute_cli_command(command, args)
        except KeyboardInterrupt:
            console.print("\n[yellow]Interrupted[/yellow]")
        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
        return True

    else:
        console.print(f"[red]Unknown command:[/red] {command}")
        console.print("[dim]Type [yellow]help[/yellow] to see available commands[/dim]")
        return True


def _execute_cli_command(command: str, args: list):
    """
    Execute a CLI command directly for better Rich output support.
    
    This avoids the CliRunner which captures output as plain text,
    losing Rich formatting.
    """
    # Map commands to their handler functions
    if command == "login":
        from tiss_tuwel_cli.cli.auth import login
        login(False, False, False)

    elif command == "settings":
        from tiss_tuwel_cli.cli.settings import show_settings_menu
        show_settings_menu()

    elif command == "dashboard":
        from tiss_tuwel_cli.cli.dashboard import dashboard
        dashboard()

    elif command == "courses":
        from tiss_tuwel_cli.cli.courses import courses
        courses()

    elif command == "assignments":
        from tiss_tuwel_cli.cli.courses import assignments
        assignments()

    elif command == "checkmarks":
        from tiss_tuwel_cli.cli.courses import checkmarks
        checkmarks()

    elif command == "grades":
        from tiss_tuwel_cli.cli.courses import grades
        course_id = int(args[0]) if args else None
        if course_id:
            grades(course_id=course_id)
        else:
            console.print("[yellow]Usage: grades <course_id>[/yellow]")

    elif command == "download":
        from tiss_tuwel_cli.cli.courses import download
        course_id = int(args[0]) if args else None
        if course_id:
            download(course_id=course_id)
        else:
            console.print("[yellow]Usage: download <course_id>[/yellow]")

    elif command == "timeline":
        from tiss_tuwel_cli.cli.timeline import timeline
        timeline()

    elif command == "todo":
        from tiss_tuwel_cli.cli.todo import todo
        todo()

    elif command == "rc":
        from tiss_tuwel_cli.cli.rc import rc
        rc()

    elif command == "weekly":
        from tiss_tuwel_cli.cli.dashboard import weekly_overview
        weekly_overview()

    elif command == "tiss-course":
        from tiss_tuwel_cli.cli.courses import tiss_course
        if len(args) >= 1:
            course_num = args[0]
            semester = args[1] if len(args) > 1 else None
            tiss_course(course_number=course_num, semester=semester)
        else:
            console.print("[yellow]Usage: tiss-course <number> [semester][/yellow]")

    elif command == "unified-view":
        from tiss_tuwel_cli.cli.features import unified_course_view
        unified_course_view()

    elif command == "export-calendar":
        from tiss_tuwel_cli.cli.features import export_calendar
        export_calendar()

    elif command == "course-stats":
        from tiss_tuwel_cli.cli.features import course_statistics
        course_statistics()

    elif command == "track-participation":
        from tiss_tuwel_cli.cli.courses import track_participation
        track_participation()

    elif command == "participation-stats":
        from tiss_tuwel_cli.cli.courses import participation_stats
        participation_stats()

    elif command == "open-vowi":
        from tiss_tuwel_cli.cli.courses import open_vowi
        query = " ".join(args) if args else None
        open_vowi(query=query)

    else:
        # Fallback to CliRunner for any unhandled commands
        from typer.testing import CliRunner
        from tiss_tuwel_cli.cli import app

        runner = CliRunner()
        result = runner.invoke(app, [command] + args)
        if result.output:
            console.print(result.output, end='')


def start_shell():
    """
    Start the interactive shell REPL.

    Provides a command-line interface with command history,
    tab completion, and a clean prompt experience.
    """
    print_banner()

    history = InMemoryHistory()
    completer = ShellCompleter()

    session: PromptSession = PromptSession(
        history=history,
        completer=completer,
        complete_while_typing=True,
        style=prompt_style,
    )

    while True:
        try:
            user_input = session.prompt(
                [('class:prompt', '> ')],
                style=prompt_style
            )

            should_continue = execute_command(user_input)

            if not should_continue:
                console.print("[bold green]Goodbye![/bold green]")
                break

        except KeyboardInterrupt:
            console.print()
            continue

        except EOFError:
            console.print("\n[bold green]Goodbye![/bold green]")
            break

        except Exception as e:
            console.print(f"[red]Error: {e}[/red]")
