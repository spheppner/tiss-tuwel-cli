"""
Settings commands for the TU Wien Companion CLI.

This module provides commands for configuring user preferences,
running the setup wizard, and managing credentials.
"""

from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from tiss_tuwel_cli.config import ConfigManager

console = Console()
config = ConfigManager()

# Available widgets for the rc command
AVAILABLE_WIDGETS = {
    "deadlines": "📅 Upcoming deadlines count",
    "todos": "⚠️ Urgent todo alerts",
    "exams": "🎓 Exam registration alerts",
    "progress": "✓ Checkmark progress",
}


def settings():
    """
    Open the settings menu to configure preferences.
    """
    show_settings_menu()


def show_settings_menu():
    """Display the interactive settings menu."""
    while True:
        console.clear()
        console.print(Panel("[bold blue]Settings[/bold blue]", expand=False))
        console.print()

        # Show current settings
        current = config.get_settings()

        table = Table(title="Current Settings", expand=False)
        table.add_column("Setting", style="cyan")
        table.add_column("Value", style="white")

        table.add_row("Auto-login", "✓ Enabled" if current.get("auto_login") else "✗ Disabled")
        table.add_row("RC Widgets", ", ".join(current.get("rc_widgets", [])) or "None")
        table.add_row("Credentials saved", "✓ Yes" if config.has_credentials() else "✗ No")

        console.print(table)
        console.print()

        choices = [
            Choice(value="auto_login", name="🔐 Toggle Auto-Login"),
            Choice(value="widgets", name="📊 Configure RC Widgets"),
            Choice(value="wizard", name="🧙 Run Setup Wizard"),
            Separator(),
            Choice(value="clear_creds", name="🗑️ Delete Saved Credentials"),
            Choice(value="clear_token", name="🔓 Clear Auth Token"),
            Choice(value="reset", name="⚠️ Reset All Settings"),
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
        elif action == "auto_login":
            toggle_auto_login()
        elif action == "widgets":
            configure_widgets()
        elif action == "wizard":
            run_wizard()
        elif action == "clear_creds":
            clear_credentials()
        elif action == "clear_token":
            clear_token()
        elif action == "reset":
            reset_settings()


def toggle_auto_login():
    """Toggle the auto-login setting."""
    current = config.get_setting("auto_login", True)
    new_value = not current
    config.set_setting("auto_login", new_value)
    status = "enabled" if new_value else "disabled"
    rprint(f"[green]Auto-login {status}.[/green]")
    inquirer.text(message="Press Enter to continue...", default="").execute()


def configure_widgets():
    """Configure which widgets appear in the rc command."""
    current_widgets = config.get_setting("rc_widgets", [])

    console.print()
    rprint("[dim]Use [bold]Space[/bold] to toggle, [bold]Enter[/bold] to confirm[/dim]")
    console.print()

    choices = [
        Choice(value=key, name=desc, enabled=key in current_widgets)
        for key, desc in AVAILABLE_WIDGETS.items()
    ]

    selected = inquirer.checkbox(
        message="Select widgets (Space to toggle):",
        choices=choices,
        pointer="→",
        instruction="(Space=toggle, Enter=confirm)",
    ).execute()

    config.set_setting("rc_widgets", selected)
    rprint(f"\n[green]✓ Widgets: {', '.join(selected) if selected else 'None'}[/green]")
    inquirer.text(message="Press Enter to continue...", default="").execute()


def run_wizard():
    """Run the initial setup wizard."""
    console.clear()
    console.print(Panel("[bold blue]Setup Wizard[/bold blue]", expand=False))
    console.print()
    rprint("[cyan]Let's configure your TU Wien Companion.[/cyan]")
    console.print()

    # Step 1: Auto-login
    auto_login = inquirer.confirm(
        message="Enable automatic re-login when token expires?",
        default=True
    ).execute()
    config.set_setting("auto_login", auto_login)

    # Step 2: RC Widgets
    console.print()
    rprint("[cyan]What should appear in the quick status summary?[/cyan]")
    rprint("[dim]Use [bold]Space[/bold] to toggle selection, [bold]Enter[/bold] to confirm[/dim]")
    console.print()

    choices = [
        Choice(value=key, name=desc, enabled=True)
        for key, desc in AVAILABLE_WIDGETS.items()
    ]
    selected = inquirer.checkbox(
        message="Select widgets (Space to toggle):",
        choices=choices,
        pointer="→",
        instruction="(Space=toggle, Enter=confirm)",
    ).execute()
    config.set_setting("rc_widgets", selected)
    rprint(f"[green]✓ Selected: {', '.join(selected) if selected else 'None'}[/green]")

    # Step 3: Credentials
    if not config.has_credentials():
        save_creds = inquirer.confirm(
            message="Would you like to save login credentials for automated login?",
            default=False
        ).execute()

        if save_creds:
            from rich.prompt import Prompt
            rprint("\n[bold yellow]Warning:[/bold yellow] Credentials will be stored in plain text.")
            user = Prompt.ask("Enter TUWEL Username")
            passw = Prompt.ask("Enter TUWEL Password", password=True)
            config.set_login_credentials(user, passw)
            rprint("[green]Credentials saved.[/green]")

    config.set_setting("wizard_completed", True)
    console.print()
    rprint("[bold green]✓ Setup complete![/bold green]")
    inquirer.text(message="Press Enter to continue...", default="").execute()


def clear_credentials():
    """Delete saved login credentials."""
    confirm = inquirer.confirm(
        message="Are you sure you want to delete saved credentials?",
        default=False
    ).execute()

    if confirm:
        config.clear_credentials()
        rprint("[green]Credentials deleted.[/green]")
    else:
        rprint("[dim]Cancelled.[/dim]")

    inquirer.text(message="Press Enter to continue...", default="").execute()


def clear_token():
    """Clear the saved auth token."""
    confirm = inquirer.confirm(
        message="Are you sure you want to clear the auth token? You'll need to log in again.",
        default=False
    ).execute()

    if confirm:
        config.clear_token()
        rprint("[green]Auth token cleared.[/green]")
    else:
        rprint("[dim]Cancelled.[/dim]")

    inquirer.text(message="Press Enter to continue...", default="").execute()


def reset_settings():
    """Reset all settings to defaults."""
    confirm = inquirer.confirm(
        message="Are you sure you want to reset all settings?",
        default=False
    ).execute()

    if confirm:
        config.reset_settings()
        rprint("[green]Settings reset to defaults.[/green]")
    else:
        rprint("[dim]Cancelled.[/dim]")

    inquirer.text(message="Press Enter to continue...", default="").execute()
