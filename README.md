# 🦉 TU Wien Companion CLI

**Because clicking through 17 submenus to find out if you passed Linear Algebra is not efficient O(1) access.**

> **TL;DR:** A Python CLI tool that merges TISS and TUWEL into a single, beautiful terminal interface. Stop context-switching. Start procrastinating efficiently.

## 🤔 Why?

As a TU Wien informatics student, your life is a constant state of:
- Checking TISS for exam dates.
- Checking TUWEL for homework deadlines.
- Forgetting to tick your **Kreuzerl** because the module was hidden in "Section 4 > General > Important > New > Final".
- Manually downloading `slides_v2_final_FINAL.pdf` one by one.

**No more.** This tool brings the API (and the pain) directly to your terminal, formatted with [Rich](https://github.com/Textualize/rich) for that cyberpunk-hacker-aesthetic you crave.

## ✨ Features

- **📅 Unified Timeline**: See your **TUWEL deadlines** and **TISS exams** in one chronological list. Never miss a deadline again.
- **⚡ Urgent Todo Checks**: The `todo` command nags you about upcoming "Kreuzerlübungen" submissions if you haven't ticked anything yet.
- **🎲 Participation Tracking**: Track your exercise frequency and estimate your chances of being called.
- **💾 Data Hoarding**: Download all course files recursively.

## 📦 Installation

Requires Python 3.8+ (because f-strings are life).

```bash
# Clone the repository
git clone https://github.com/spheppner/tiss-tuwel-cli.git
cd tiss-tuwel-cli

# Create a venv (don't pollute your global site-packages, you animal)
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies in editable mode
pip install -e "."
```

## 🔐 Authentication (The Fun Part)

We need your TUWEL Web Service Token. You have two options:

### Option A: The "I trust code" way (Automated) 🤖

Requires Chrome or Firefox. Launches a browser, lets you SSO login, and sniffs the token from the network traffic like a digital bloodhound.
It uses a dedicated profile, so your session persists across runs!

```bash
tiss-tuwel-cli login
```

### Option B: The "Paranoid" way (Manual) 🕵️

If you prefer to dig through Developer Tools yourself or automated login fails.
Run `setup`, follow the instructions to generate the `moodlemobile://` token URL, and paste it into the terminal.

```bash
tiss-tuwel-cli setup
```

## 🚀 Usage

### `dashboard`
Your daily stand-up. Shows upcoming deadlines, calendar events, and helpful tips.

```bash
tiss-tuwel-cli dashboard
```

### `timeline`
**The Master View.** Merges all active TUWEL assignments/events and TISS exam dates into a single timeline.
Export to `.ics` to sync with your real calendar!

```bash
tiss-tuwel-cli timeline
tiss-tuwel-cli timeline --export  # Saves to ~/Downloads/unified_timeline.ics
```

### `todo`
**The MVP Feature 👑**. The Kreuzerlübung Nag.
Checks specifically for:
1. Deadlines < 24 hours
2. **AND** 0 ticked examples

Ideally, this output is empty. If it's not, **you need to act immediately.**

```bash
tiss-tuwel-cli todo
```

### `courses`
List everything you are currently suffering through (enrolled courses).

```bash
tiss-tuwel-cli courses
```

### `assignments`
Lists all active assignments. Highlights deadlines so you can panic appropriately.

```bash
tiss-tuwel-cli assignments
```

### `checkmarks`
Shows how many examples you've ticked vs. total for all your courses. Prevents the "I solved it but forgot to tick it" fail condition.

```bash
tiss-tuwel-cli checkmarks
```

### `grades [course_id]`
Fetches the deeply nested, confusing grade table from TUWEL and renders it as a beautiful, readable tree.

```bash
tiss-tuwel-cli grades 12345
```

### `download [course_id]`
The Data Hoarder Special. Recursively crawls a course and downloads every file resource to your local `Downloads/Tuwel/` folder.
Perfect for offline studying (lol) or archiving materials before they vanish.

```bash
tiss-tuwel-cli download 12345
```

### `tiss-course [number] [semester]`
Queries the TISS public API for course info and upcoming exam dates. Now with XML parsing for those legacy endpoints.

```bash
tiss-tuwel-cli tiss-course 185.A91 2025W
```

### Interactive Mode
Prefer a menu because remembering commands is hard? We got you.

```bash
tiss-tuwel-cli -i
```
Navigate through your courses, view grades, and check deadlines with a TUI.

## 🐛 Known Issues & Quirks

- **"Access Control Exception"**: Moodle hates us. If login throws this, ignore it. If the token is saved, most features usually work anyway.
- **TISS Limitations**: The TISS public API is read-only. We can't register you for exams yet (mostly because we don't want to accidentally deregister you from your Bachelor thesis).
- **Windows**: If the TUI looks weird, try using Windows Terminal instead of the legacy CMD.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Credits
- TUWEL API info from [student-api-documentation](https://github.com/tuwel-api/student-api-documentation).
- TISS API info from [tiss public-api](https://tiss.tuwien.ac.at/api/dokumentation).