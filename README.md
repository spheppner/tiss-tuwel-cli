# tiss-tuwel-cli

A Python CLI tool for TU Wien students to interact with the public TISS API and TUWEL (Moodle) web services.

## Features

- **TUWEL Integration**:
  - View upcoming deadlines and calendar events
  - List enrolled courses (past, current, future) with full titles
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

- **🆕 Exercise Participation Tracking**:
  - 🎯 **Call Probability Calculator** - Track when you're called to present exercises
  - 📈 **Fair Probability Estimation** - Calculate your chances of being called next time
  - 📊 **Historical Analysis** - View participation history per course
  - 👥 **Group Size Configuration** - Adjust calculations based on exercise group size

- **🆕 Advanced Features**:
  - 📊 **Course Comparison** - Compare workload and progress across all courses at a glance
  - ⏱️ **Study Time Estimator** - Get estimates of study time needed based on pending work
  - 📅 **Calendar Export** - Export all deadlines to ICS format (Google Calendar, Outlook, etc.)
  - 📌 **Submission Tracker** - Track assignment submission status to never miss a deadline
  - 📈 **Detailed Course Statistics** - View comprehensive stats for individual courses

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
- **🆕 Exercise Participation Tracker** - Track and predict when you'll be called to present
- **🆕 Advanced Analytics** - Compare courses, estimate study time, export calendars, and more
- **Login from Menu** - Authenticate directly from the interactive menu
- **Course Browser** - Navigate through courses with full titles, view grades, assignments, and download materials
- **Kreuzerlübungen Overview** - Grouped by course with full names and completion statistics

### Authentication

First, you need to authenticate with TUWEL:

```bash
# Automated login (requires Chrome or Firefox)
tiss-tuwel-cli login

# Manual token setup
tiss-tuwel-cli setup
```

### Commands

#### Basic Commands

```bash
# View upcoming deadlines dashboard
tiss-tuwel-cli dashboard

# List enrolled courses (shows full course titles)
tiss-tuwel-cli courses                    # Current courses (default)
tiss-tuwel-cli courses --classification past
tiss-tuwel-cli courses --classification future

# View assignments
tiss-tuwel-cli assignments

# View grades for a course
tiss-tuwel-cli grades --course-id 12345

# View Kreuzerlübungen status (with course titles)
tiss-tuwel-cli checkmarks

# Download course materials
tiss-tuwel-cli download 12345

# Search TISS for course info
tiss-tuwel-cli tiss-course 192.167 --semester 2024W
```

#### Exercise Participation Tracking

For courses where students are called randomly to present exercises:

```bash
# Record participation in an exercise session
tiss-tuwel-cli track-participation 12345 "Exercise 3" --was-called
tiss-tuwel-cli track-participation 12345 "Exercise 4"  # Not called this time

# Set group size for better probability calculations
tiss-tuwel-cli track-participation 12345 "Exercise 5" --group-size 15

# View participation statistics and call probabilities
tiss-tuwel-cli participation-stats                    # All courses
tiss-tuwel-cli participation-stats --course-id 12345  # Specific course
```

**How it works:**
- Records when you attend exercise sessions and whether you were called
- Calculates probability using fair selection model (adjusted based on history)
- If you've been called less than average, probability increases
- Helps you prepare more for sessions where you're more likely to be called

#### Advanced Features

```bash
# Compare workload across all courses
tiss-tuwel-cli compare-courses

# Estimate study time needed this week
tiss-tuwel-cli study-time

# Export calendar to ICS format (for Google Calendar, Outlook, etc.)
tiss-tuwel-cli export-calendar
tiss-tuwel-cli export-calendar --output-file ~/my-calendar.ics

# View detailed course statistics
tiss-tuwel-cli course-stats --course-id 12345

# Track assignment submissions
tiss-tuwel-cli submission-tracker
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
│       ├── __init__.py                # Package initialization
│       ├── __main__.py                # Module entry point
│       ├── config.py                  # Configuration management
│       ├── utils.py                   # Utility functions
│       ├── participation_tracker.py   # Exercise participation tracking
│       ├── clients/
│       │   ├── __init__.py
│       │   ├── tiss.py                # TISS API client
│       │   └── tuwel.py               # TUWEL (Moodle) API client
│       └── cli/
│           ├── __init__.py            # CLI app initialization
│           ├── auth.py                # Authentication commands
│           ├── dashboard.py           # Dashboard command
│           ├── courses.py             # Course-related commands
│           ├── features.py            # Advanced feature commands
│           └── interactive.py         # Interactive menu mode
├── pyproject.toml                     # Project configuration & dependencies
└── README.md
```

## Configuration

Configuration is stored in `~/.tu_companion/` and includes:
- `config.json` - TUWEL authentication token and user ID
- `participation_history.json` - Exercise participation tracking data (created when first used)

## Dependencies

- **requests** - HTTP client for API requests
- **typer** - CLI framework
- **rich** - Terminal formatting and output
- **InquirerPy** - Interactive prompts and menus
- **selenium** - Browser automation for login

## Use Cases

### Exercise Participation Tracking
Perfect for courses like "Übungen" where:
- Only one student per group is called to present each week
- You want to estimate your chances of being called next time
- You need to know how much to prepare based on probability

### Study Planning
Use the advanced features to:
- **Compare courses** - See which courses need more attention
- **Estimate time** - Plan your study schedule for the week
- **Export calendar** - Sync all deadlines with your calendar app
- **Track submissions** - Never miss an assignment deadline

## License

GNU GPL v3.0 License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
