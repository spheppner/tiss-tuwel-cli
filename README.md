# tiss-tuwel-cli

**The ultimate power tool for TU Wien students.** 🚀

A modern, feature-rich CLI that unifies TISS and TUWEL into a single, powerful command-line interface. Stop clicking through slow websites and get everything you need instantly.

## Why use this?

- **Unified Timeline**: See your **TUWEL deadlines** and **TISS exams** in one chronological list. Never miss a deadline again.
- **Smart Alerts**: The `todo` command nags you about upcoming "Kreuzerlübungen" submissions if you haven't ticked anything yet.
- **Persistent Login**: Log in once, and stay logged in. No more daily token refreshing.
- **Participation Tracking**: Track your exercise frequency and estimate your chances of being called.
- **Fast & Beautiful**: Built with modern terminal UI, it's faster than the browser and looks great.

## ✨ New Features

### 📅 Unified Timeline
Available via `timeline` command.
Merges all your upcoming:
- TUWEL Assignments
- TUWEL Calendar Events
- TISS Exam Dates

Sorts them chronologically and tells you exactly how much time you have left.
_Supports exporting to .ics for your calendar app!_

### 🚨 Urgent Todo Checks
Available via `todo` command.
Checks specifically for:
- Deadline < 24 hours
- **AND** 0 ticked examples (Kreuzerlübungen)

Ideally, this output is empty. If it's not, **you need to act due to imminent submission deadlines.**

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
```

## Usage

### Authentication (One-time setup)

```bash
# Launches a browser window to capture your session.
# Your login persists, so you rarely need to do this again!
tiss-tuwel-cli login
```

### Essential Commands

```bash
# 📅 The Master View: All deadlines and exams
tiss-tuwel-cli timeline
tiss-tuwel-cli timeline --export # Save to .ics

# 🚨 Am I forgetting something vital?
tiss-tuwel-cli todo

# 📊 Dashboard: Quick overview of upcoming week
tiss-tuwel-cli dashboard

# 📚 List all your courses
tiss-tuwel-cli courses
```

### Interactive Mode

Prefer a menu? We got you.

```bash
tiss-tuwel-cli -i
```

Navigate through your courses, view grades, and check deadlines with a TUI (Text User Interface).

### Advanced: Participation Tracking

For "Übungen" where you are called randomly:

```bash
# Record that you were called
tiss-tuwel-cli track-participation 12345 "Exercise 3" --was-called

# See your stats and probability of being called next
tiss-tuwel-cli participation-stats
```

## Project Structure

```
tiss-tuwel-cli/
├── src/
│   └── tiss_tuwel_cli/
│       ├── clients/           # API clients for TISS and TUWEL
│       ├── cli/               # CLI commands and menus
│       │   ├── timeline.py    # Unified timeline logic
│       │   ├── todo.py        # Urgent todo checker
│       │   └── ...
│       └── ...
```

## License

GNU GPL v3.0 License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### TUWEL API Docs

Information taken from [student-api-documentation repo](https://github.com/tuwel-api/student-api-documentation).

### TISS API Docs

Information taken from [tiss public-api](https://tiss.tuwien.ac.at/api/dokumentation)