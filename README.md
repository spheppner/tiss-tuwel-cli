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

## Installation

### From PyPI (recommended)

```bash
pip install tiss-tuwel-cli
```

### With browser automation support

For automated login via browser:

```bash
pip install tiss-tuwel-cli[browser]
```

### Development installation

```bash
# Clone the repository
git clone https://github.com/spheppner/tiss-tuwel-cli.git
cd tiss-tuwel-cli

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

## Usage

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
│           └── courses.py       # Course-related commands
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

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
