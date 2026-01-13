# tiss-tuwel-cli

A Python CLI tool for TU Wien students to interact with the public TISS API and TUWEL (Moodle) web services.

## Features

- **TUWEL Integration**:
  - View upcoming deadlines and calendar events
  - List enrolled courses (past, current, future)
  - View and track assignments
  - Access grade reports
  - Manage "Kreuzerlübungen" (checkmark exercises)
  - Download course materials

- **TISS Integration**:
  - Search course details
  - View exam dates and registration info
  - Access public university events

- **Smart Student Features** (Interactive Mode):
  - 🔔 **Exam Registration Alerts** - Get notified before exam registration opens
  - 📊 **Study Progress Tracking** - See completion rates for checkmarks and assignments
  - 📅 **Weekly Overview** - Plan your week with all upcoming deadlines
  - 🏆 **Grade Summary** - View grades across courses with Austrian grading scale
  - 💡 **Smart Tips** - Context-aware suggestions based on your academic situation

## Installation

```bash
# Clone the repository
git clone https://github.com/spheppner/tiss-tuwel-cli.git
cd tiss-tuwel-cli

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in dev mode
pip install -e ".[dev]"
# Or install normally
pip install -e "."
```

## Usage

### Interactive Mode

For a user-friendly menu-based experience, start the CLI in interactive mode:

```bash
tiss-tuwel-cli -i
# or
tiss-tuwel-cli --interactive
```

**Features of Interactive Mode:**
- **Keyboard Navigation** - Use arrow keys to navigate, Enter to select (no typing required)
- **Smart Dashboard** - See upcoming deadlines with color-coded urgency levels
- **🆕 Exam Registration Alerts** - Get notified when exam registration opens or is about to open
- **🆕 Study Progress Tracker** - Track your checkmark completion and pending assignments
- **🆕 Weekly Overview** - See all deadlines and events for the current week
- **🆕 Grade Summary** - View your grades across all courses with pass/fail indicators
- **🆕 Smart Tips** - Context-aware suggestions based on your deadlines and progress
- **Login from Menu** - Authenticate directly from the interactive menu
- **Course Browser** - Navigate through courses, view grades, assignments, and download materials
- **Kreuzerlübungen Overview** - Grouped by course with completion statistics

### Authentication

First, you need to authenticate with TUWEL:

```bash
# Automated login (requires Chrome or Firefox)
tiss-tuwel-cli login

# Manual token setup
tiss-tuwel-cli setup
```

### Commands

```bash
# View upcoming deadlines dashboard
tiss-tuwel-cli dashboard

# List enrolled courses
tiss-tuwel-cli courses                    # Current courses (default)
tiss-tuwel-cli courses --classification past
tiss-tuwel-cli courses --classification future

# View assignments
tiss-tuwel-cli assignments

# View grades for a course
tiss-tuwel-cli grades --course-id 12345

# View Kreuzerlübungen status
tiss-tuwel-cli checkmarks

# Download course materials
tiss-tuwel-cli download 12345

# Search TISS for course info
tiss-tuwel-cli tiss-course 192.167 --semester 2024W
```

### Alternative entry points

```bash
# Using the package module
python -m tiss_tuwel_cli dashboard

# Using the alias
tu-companion dashboard
```

## Project Structure

```
tiss-tuwel-cli/
├── src/
│   └── tiss_tuwel_cli/
│       ├── __init__.py          # Package initialization
│       ├── __main__.py          # Module entry point
│       ├── config.py            # Configuration management
│       ├── utils.py             # Utility functions
│       ├── clients/
│       │   ├── __init__.py
│       │   ├── tiss.py          # TISS API client
│       │   └── tuwel.py         # TUWEL (Moodle) API client
│       └── cli/
│           ├── __init__.py      # CLI app initialization
│           ├── auth.py          # Authentication commands
│           ├── dashboard.py     # Dashboard command
│           ├── courses.py       # Course-related commands
│           └── interactive.py   # Interactive menu mode
├── pyproject.toml               # Project configuration & dependencies
└── README.md
```

## Configuration

Configuration is stored in `~/.tu_companion/config.json` and includes:
- TUWEL authentication token
- User ID

## Dependencies

- **requests** - HTTP client for API requests
- **typer** - CLI framework
- **rich** - Terminal formatting and output
- **selenium** (optional) - Browser automation for login

## License

GNU GPL v3.0 License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
