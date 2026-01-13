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

# Define available commands that can be executed in the shell
SHELL_COMMANDS = {
    "help": "Show this help message",
    "exit": "Exit the shell",
    "quit": "Exit the shell",
    "clear": "Clear the screen",
    "login": "Automated login (browser)",
    "setup": "Manual token setup",
    "dashboard": "Show dashboard with upcoming events",
    "courses": "List enrolled courses",
    "assignments": "List assignments",
    "grades": "Show grades for a course",
    "checkmarks": "Show Kreuzerlübungen status",
    "download": "Download course materials",
    "tiss-course": "Search TISS for course details",
    "track-participation": "Track exercise participation",
    "participation-stats": "Show participation statistics",
    "open-vowi": "Open VoWi search",
    "export-calendar": "Export calendar to ICS",
    "course-stats": "Show course statistics",
    "unified-view": "Show unified TISS+TUWEL view",
    "interactive": "Start interactive menu mode",
}

# Custom style for the prompt
prompt_style = Style.from_dict({
    'prompt': 'ansigreen bold',
})


class ShellCompleter(Completer):
    """Custom completer for shell commands with better filtering."""

    def __init__(self):
        self.commands = list(SHELL_COMMANDS.keys())

    def get_completions(self, document, complete_event):
        """Get completions for the current input."""
        word_before_cursor = document.get_word_before_cursor()

        for command in self.commands:
            if command.startswith(word_before_cursor):
                yield Completion(
                    command,
                    start_position=-len(word_before_cursor),
                    display=command,
                    display_meta=SHELL_COMMANDS.get(command, "")
                )


def print_banner():
    """Print the shell welcome banner."""
    banner_text = """[bold cyan]TU Wien Companion - Interactive Shell[/bold cyan]

Type [yellow]help[/yellow] to see available commands
Type [yellow]exit[/yellow] or [yellow]quit[/yellow] to leave the shell
Type [yellow]interactive[/yellow] to enter the menu-based interactive mode

Press [dim]Tab[/dim] for command completion, [dim]↑↓[/dim] for command history"""

    console.print(Panel(banner_text, border_style="cyan", expand=False))
    console.print()


def print_help():
    """Print help information showing all available commands."""
    table = Table(title="Available Commands", expand=True, show_header=True, header_style="bold cyan")
    table.add_column("Command", style="green", no_wrap=True)
    table.add_column("Description", style="white")

    # Sort commands for better presentation
    sorted_commands = sorted(SHELL_COMMANDS.items())

    # Group special commands first
    special = []
    auth = []
    main = []
    advanced = []

    for cmd, desc in sorted_commands:
        if cmd in ["help", "exit", "quit", "clear"]:
            special.append((cmd, desc))
        elif cmd in ["login", "setup"]:
            auth.append((cmd, desc))
        elif cmd in ["dashboard", "courses", "assignments", "grades", "checkmarks",
                     "download", "tiss-course", "interactive"]:
            main.append((cmd, desc))
        else:
            advanced.append((cmd, desc))

    # Add sections with separators
    for cmd, desc in special:
        table.add_row(f"[bold yellow]{cmd}[/bold yellow]", desc)

    if auth:
        table.add_row("", "")
        table.add_row("[dim]Authentication[/dim]", "")
        for cmd, desc in auth:
            table.add_row(cmd, desc)

    if main:
        table.add_row("", "")
        table.add_row("[dim]Main Features[/dim]", "")
        for cmd, desc in main:
            table.add_row(cmd, desc)

    if advanced:
        table.add_row("", "")
        table.add_row("[dim]Advanced Features[/dim]", "")
        for cmd, desc in advanced:
            table.add_row(cmd, desc)

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
    # Parse command and arguments
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
        # Switch to the menu-based interactive mode
        from tiss_tuwel_cli.cli.interactive import interactive
        try:
            interactive()
        except KeyboardInterrupt:
            console.print("\n[dim]Returned to shell[/dim]")
        return True

    # Handle CLI commands by invoking typer app
    elif command in SHELL_COMMANDS:
        try:
            # Import the CLI app
            # Use typer's testing runner to execute commands
            # This is the recommended way to invoke Typer commands programmatically
            from typer.testing import CliRunner

            from tiss_tuwel_cli.cli import app

            runner = CliRunner()
            result = runner.invoke(app, [command] + args)

            # Print the output
            if result.output:
                console.print(result.output, end='')

            # If there was an error, show it
            if result.exit_code != 0:
                if result.exception and not isinstance(result.exception, SystemExit):
                    console.print(f"[red]Error: {result.exception}[/red]")
                elif not result.output:
                    # Command failed but produced no output or exception details
                    console.print(f"[red]Command failed with exit code {result.exit_code}[/red]")

        except KeyboardInterrupt:
            console.print("\n[yellow]Command interrupted[/yellow]")
        except Exception as e:
            console.print(f"[red]Error executing command: {e}[/red]")

        return True

    else:
        console.print(f"[red]Unknown command:[/red] {command}")
        console.print("[dim]Type[/dim] [yellow]help[/yellow] [dim]to see available commands[/dim]")
        return True


def start_shell():
    """
    Start the interactive shell REPL.

    This provides a command-line interface with advanced features like
    command history, tab completion, and a clean prompt experience.
    """
    # Print welcome banner
    print_banner()

    # Create prompt session with history and completion
    history = InMemoryHistory()
    completer = ShellCompleter()

    session: PromptSession = PromptSession(
        history=history,
        completer=completer,
        complete_while_typing=True,
        style=prompt_style,
    )

    # Main REPL loop
    while True:
        try:
            # Get user input with the fancy prompt
            user_input = session.prompt(
                [('class:prompt', '> ')],
                style=prompt_style
            )

            # Execute the command
            should_continue = execute_command(user_input)

            if not should_continue:
                console.print("[bold green]Goodbye![/bold green]")
                break

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully - don't exit, just show new prompt
            console.print()
            continue

        except EOFError:
            # Handle Ctrl+D - exit gracefully
            console.print("\n[bold green]Goodbye![/bold green]")
            break

        except Exception as e:
            console.print(f"[red]Unexpected error: {e}[/red]")
            console.print("[dim]Type[/dim] [yellow]help[/yellow] [dim]for usage information[/dim]")
