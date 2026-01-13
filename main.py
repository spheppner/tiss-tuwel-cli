import json
import os
import requests
import typer
import base64
import urllib.parse
import time
from pathlib import Path
from typing import Optional, Dict, List, Any
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from rich import print as rprint
from rich.tree import Tree
from rich.text import Text

# ==========================================
# CONFIGURATION MANAGER
# ==========================================

CONFIG_DIR = Path.home() / ".tu_companion"
CONFIG_FILE = CONFIG_DIR / "config.json"


class ConfigManager:
    def __init__(self):
        self._ensure_config_exists()

    def _ensure_config_exists(self):
        if not CONFIG_DIR.exists():
            CONFIG_DIR.mkdir(parents=True)
        if not CONFIG_FILE.exists():
            self._save_config({})

    def _load_config(self) -> Dict:
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}

    def _save_config(self, config: Dict):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)

    def get_tuwel_token(self) -> Optional[str]:
        config = self._load_config()
        return config.get("tuwel_token")

    def set_tuwel_token(self, token: str):
        config = self._load_config()
        config["tuwel_token"] = token
        self._save_config(config)

    def get_user_id(self) -> Optional[int]:
        config = self._load_config()
        return config.get("tuwel_userid")

    def set_user_id(self, userid: int):
        config = self._load_config()
        config["tuwel_userid"] = userid
        self._save_config(config)


# ==========================================
# TISS API CLIENT
# ==========================================

class TissClient:
    """
    Client for interacting with the TISS Public API.
    """
    BASE_URL = "https://tiss.tuwien.ac.at/api"

    def _get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def get_course_details(self, course_number: str, semester: str) -> Dict:
        course_number = course_number.replace(".", "")
        return self._get(f"/course/{course_number}-{semester}")

    def get_exam_dates(self, course_number: str) -> List[Dict]:
        course_number = course_number.replace(".", "")
        return self._get(f"/course/{course_number}/examDates")

    def get_public_events(self) -> List[Dict]:
        today = datetime.now().strftime("%Y-%m-%d")
        params = {"from": today}
        return self._get("/event", params=params)


# ==========================================
# TUWEL (MOODLE) API CLIENT
# ==========================================

class TuwelClient:
    """
    Client for interacting with the TUWEL (Moodle) Web Service.
    """
    BASE_URL = "https://tuwel.tuwien.ac.at/webservice/rest/server.php"

    def __init__(self, token: str):
        self.token = token

    def _call(self, wsfunction: str, params: Optional[Dict[str, Any]] = None) -> Any:
        if params is None:
            params = {}

        payload = {
            "wstoken": self.token,
            "wsfunction": wsfunction,
            "moodlewsrestformat": "json",
        }
        payload.update(params)

        try:
            response = requests.post(self.BASE_URL, data=payload, timeout=15)
            response.raise_for_status()
            data = response.json()

            if isinstance(data, dict) and "exception" in data:
                # Silently handle some common exceptions or re-raise
                raise Exception(f"Moodle Error: {data.get('message')}")

            return data
        except requests.RequestException as e:
            raise Exception(f"Network Error: {str(e)}")

    def get_site_info(self) -> Dict:
        return self._call("core_webservice_get_site_info")

    def get_upcoming_calendar(self) -> Dict:
        return self._call("core_calendar_get_calendar_upcoming_view")

    def get_enrolled_courses(self, classification: str = 'inprogress') -> List[Dict]:
        # Classification: 'past', 'inprogress', or 'future'
        params = {"classification": classification, "sort": "fullname"}
        data = self._call("core_course_get_enrolled_courses_by_timeline_classification", params)
        return data.get('courses', [])

    def get_assignments(self) -> List[Dict]:
        courses = self.get_enrolled_courses()
        if not courses:
            return []

        # Build courseids[0]=123, courseids[1]=456...
        params = {}
        for i, cid in enumerate([c['id'] for c in courses]):
            params[f"courseids[{i}]"] = cid

        return self._call("mod_assign_get_assignments", params)

    def get_user_grades_table(self, course_id: int, user_id: int) -> Dict:
        """Fetches the grade report table structure."""
        params = {"courseid": course_id, "userid": user_id}
        return self._call("gradereport_user_get_grades_table", params)

    def get_checkmarks(self, course_ids: List[int]) -> List[Dict]:
        """Fetches 'Kreuzerlübung' (mod_checkmark) data."""
        params = {}
        # If course_ids is empty, we send no params to let Moodle fetch all (if supported),
        # otherwise we explicitly list them.
        for i, cid in enumerate(course_ids):
            params[f"courseids[{i}]"] = cid
        return self._call("mod_checkmark_get_checkmarks_by_courses", params)

    def download_file(self, file_url: str, output_path: Path):
        """Downloads a file from TUWEL, appending the token."""
        # Check if URL already has query params
        separator = "&" if "?" in file_url else "?"
        download_url = f"{file_url}{separator}token={self.token}"

        with requests.get(download_url, stream=True) as r:
            r.raise_for_status()
            with open(output_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)


# ==========================================
# CLI APP
# ==========================================

app = typer.Typer(help="TU Wien Companion - TISS & TUWEL CLI")
console = Console()
config = ConfigManager()
tiss = TissClient()


def get_tuwel_client() -> TuwelClient:
    token = config.get_tuwel_token()
    if not token:
        rprint("[bold red]Error:[/bold red] TUWEL token not found. Please run [green]setup[/green] or [green]login[/green] first.")
        raise typer.Exit()
    return TuwelClient(token)


def timestamp_to_date(ts):
    if not ts: return "N/A"
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M')


def parse_mobile_token(token_string: str) -> Optional[str]:
    """
    Decodes the token format used by Moodle Mobile.
    Handles 'moodlemobile://token=BASE64...' OR just 'BASE64...'
    Logic based on provided SDK.
    """
    # 1. Extract base64 part
    base64_message = token_string
    if "token=" in token_string:
        base64_message = token_string.split("token=")[1]

    # 2. URL Decode (just in case browser encoded special chars in base64)
    base64_message = urllib.parse.unquote(base64_message)

    try:
        # 3. Base64 Decode
        message_bytes = base64.b64decode(base64_message)
        message = message_bytes.decode('ascii')

        # 4. Extract middle part: PASSPORT:::TOKEN:::PRIVATE
        parts = message.split(':::')
        if len(parts) >= 2:
            return parts[1]
    except Exception:
        pass

    return None


@app.command()
def login():
    """
    [Automated] Launches a browser to log in and captures the TUWEL token automatically.
    Requires Chrome or Firefox installed.
    """
    try:
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.common.exceptions import WebDriverException
    except ImportError:
        rprint("[bold red]Selenium is not installed.[/bold red]")
        rprint("Please run: [green]pip install selenium[/green]")
        return

    rprint("[yellow]Launching browser... Please log in to TUWEL in the opened window.[/yellow]")
    rprint("[dim]The window will close automatically once the token is detected.[/dim]")

    login_url = "https://tuwel.tuwien.ac.at/admin/tool/mobile/launch.php?service=moodle_mobile_app&passport=student_api"

    # Enable performance logging to catch the redirect URL even if the browser blocks it
    options = webdriver.ChromeOptions()
    options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = None
    try:
        try:
            driver = webdriver.Chrome(options=options)
        except WebDriverException:
            # Fallback to Firefox (logging works differently, this might be less reliable for Firefox)
            rprint("[yellow]Chrome not found, trying Firefox...[/yellow]")
            driver = webdriver.Firefox()

        driver.get(login_url)

        found_token = None

        # Poll loop
        while not found_token:
            # Check 1: Current URL (if browser successfully navigated)
            current_url = driver.current_url
            if "moodlemobile://token=" in current_url:
                found_token = parse_mobile_token(current_url)
                break

            # Check 2: Performance Logs (if browser blocked navigation to unknown protocol)
            # This is specific to Chrome-based browsers
            if hasattr(driver, 'get_log'):
                try:
                    logs = driver.get_log('performance')
                    for entry in logs:
                        message = json.loads(entry.get('message', '{}')).get('message', {})
                        # Look for Network.requestWillBeSent with the custom scheme
                        params = message.get('params', {})
                        req_url = params.get('request', {}).get('url', '')
                        doc_url = params.get('documentURL', '')

                        if "moodlemobile://token=" in req_url:
                            found_token = parse_mobile_token(req_url)
                            break
                        if "moodlemobile://token=" in doc_url:
                            found_token = parse_mobile_token(doc_url)
                            break
                except Exception:
                    pass

            if found_token:
                break

            time.sleep(1)

            # Stop if user closed browser
            try:
                # This throws exception if window is closed
                _ = driver.window_handles
            except Exception:
                rprint("[red]Browser closed by user.[/red]")
                return

    except Exception as e:
        rprint(f"[bold red]Automation failed:[/bold red] {e}")
        rprint("Please use the manual [green]setup[/green] command instead.")
        return
    finally:
        if driver:
            driver.quit()

    if found_token:
        config.set_tuwel_token(found_token)
        rprint("[bold green]Token captured successfully![/bold green]")

        # Verify
        try:
            client = TuwelClient(found_token)
            info = client.get_site_info()
            config.set_user_id(info.get('userid', 0))
            rprint(f"Authenticated as [cyan]{info.get('fullname')}[/cyan] (ID: {info.get('userid')}).")
        except Exception as e:
            # Even if validation fails, save the token. Access Control Exception
            # might mean we can't get site_info, but can fetch courses.
            rprint(f"[yellow]Warning: Token captured but validation failed: {e}[/yellow]")
            rprint("[dim]The token was saved anyway. Try running [green]python main.py dashboard[/green] to see if it works.[/dim]")
    else:
        rprint("[red]Could not capture token.[/red]")


@app.command()
def setup():
    """
    [Manual] Configure TUWEL token by pasting the redirect URL.
    """
    console.print(Panel("[bold blue]TU Wien Companion Setup[/bold blue]", expand=False))
    rprint("1. Go to: [link]https://tuwel.tuwien.ac.at/admin/tool/mobile/launch.php?service=moodle_mobile_app&passport=student_api[/link]")
    rprint("2. Login and wait for the 'Address not understood' or failed redirect page.")
    rprint("3. Copy the [bold]entire URL[/bold] from the address bar (starting with moodlemobile://).")

    user_input = Prompt.ask("Paste URL or Token")

    token = parse_mobile_token(user_input)

    # If parsing failed, maybe they pasted the raw token directly?
    if not token and ":::" not in user_input and "token=" not in user_input:
        token = user_input

    if not token:
        rprint("[bold red]Invalid input format.[/bold red]")
        return

    try:
        client = TuwelClient(token)
        info = client.get_site_info()
        user_id = info.get('userid', 0)
        config.set_tuwel_token(token)
        config.set_user_id(user_id)
        rprint(f"[bold green]Success![/bold green] Authenticated as [cyan]{info.get('fullname')}[/cyan].")
    except Exception as e:
        rprint(f"[bold red]Authentication failed:[/bold red] {e}")


@app.command()
def dashboard():
    """Overview of upcoming events."""
    client = get_tuwel_client()
    with console.status("[bold green]Fetching data...[/bold green]"):
        try:
            upcoming = client.get_upcoming_calendar()
            events = upcoming.get('events', [])
            tiss_events = tiss.get_public_events()
        except Exception as e:
            rprint(f"[bold red]Error:[/bold red] {e}")
            return

    tuwel_table = Table(title="[bold blue]Upcoming TUWEL Deadlines[/bold blue]", expand=True)
    tuwel_table.add_column("Course", style="cyan")
    tuwel_table.add_column("Event", style="white")
    tuwel_table.add_column("Date", style="green")

    for event in events:
        tuwel_table.add_row(
            event.get('course', {}).get('shortname', 'Unknown'),
            event.get('name'),
            timestamp_to_date(event.get('timestart'))
        )

    console.print(tuwel_table)
    rprint("\n")

    # TISS data logic could be expanded here
    if isinstance(tiss_events, list) and len(tiss_events) > 0:
        tiss_table = Table(title="[bold yellow]TISS Public Events[/bold yellow]", expand=True)
        tiss_table.add_column("Description", style="white")
        tiss_table.add_column("Time", style="green")
        for event in tiss_events[:3]:
            tiss_table.add_row(event.get('description', ''), event.get('begin', ''))
        console.print(tiss_table)


@app.command()
def courses(classification: str = 'inprogress'):
    """List enrolled courses."""
    client = get_tuwel_client()
    with console.status(f"[bold green]Fetching {classification} courses...[/bold green]"):
        courses = client.get_enrolled_courses(classification)

    table = Table(title=f"Enrolled Courses ({classification})")
    table.add_column("ID", justify="right", style="dim")
    table.add_column("Shortname", style="cyan")
    table.add_column("Fullname")

    for course in courses:
        table.add_row(str(course.get('id')), course.get('shortname'), course.get('fullname'))
    console.print(table)


@app.command()
def assignments():
    """List assignments."""
    client = get_tuwel_client()
    with console.status("[bold green]Fetching assignments...[/bold green]"):
        data = client.get_assignments()
        courses = data.get('courses', [])

    table = Table(title="Assignments")
    table.add_column("Course", style="cyan")
    table.add_column("Assignment", style="white")
    table.add_column("Due", style="red")
    table.add_column("Status", style="yellow")

    now = datetime.now().timestamp()
    for course in courses:
        for assign in course.get('assignments', []):
            due = assign.get('duedate', 0)
            if due < now - (30 * 86400): continue  # Skip old

            status = "Closed" if due < now else "Open"
            table.add_row(course.get('shortname'), assign.get('name'), timestamp_to_date(due), status)
    console.print(table)


@app.command()
def grades(course_id: Optional[int] = None):
    """
    Show grades. If no ID provided, lists courses first.
    """
    client = get_tuwel_client()
    user_id = config.get_user_id()

    if not course_id:
        rprint("[bold yellow]Please provide a course ID. Listing active courses:[/bold yellow]")
        courses(classification='inprogress')
        return

    with console.status("[bold green]Fetching detailed grades...[/bold green]"):
        report = client.get_user_grades_table(course_id, user_id)

    tables = report.get('tables', [])
    if not tables:
        rprint("[red]No grade table found for this course.[/red]")
        return

    # The API returns HTML-rich data in 'tabledata'. We need to extract meaningful text.
    # Structure: tables -> tabledata -> itemname, grade, percentage, feedback, etc.

    table_data = tables[0].get('tabledata', [])

    # Create a Tree for hierarchical display
    root_tree = Tree(f"[bold blue]Grades for Course {course_id}[/bold blue]")

    # Simple recursive-like parsing based on indentation logic usually found in Moodle
    # Moodle API flattens the table but often keeps order.
    # itemname content often contains class="column-itemname item"

    current_category = root_tree

    for item in table_data:
        # Extract text from the itemname dictionary
        raw_name = item.get('itemname', {}).get('content', 'Unknown')

        # Very basic HTML stripping (placeholder for a real parser like BeautifulSoup)
        # In a real app, use bs4. Here we do simple cleanup for CLI speed.
        clean_name = raw_name.replace('<span class="gradeitemheader" title="', '').split('"')[0]
        if "class" in str(item.get('itemname')):
            # Fallback cleanup
            import re
            clean_name = re.sub('<[^<]+?>', '', raw_name).strip()

        # Grade Values
        grade_val = item.get('grade', {}).get('content', '-').replace('&nbsp;', '')
        percent_val = item.get('percentage', {}).get('content', '-').replace('&nbsp;', '')
        range_val = item.get('range', {}).get('content', '-').replace('&nbsp;', '')

        # Formatting
        if "gesamt" in clean_name.lower() or "total" in clean_name.lower():
            # It's a category total
            text = Text(f"{clean_name}: {grade_val} ({percent_val})", style="bold yellow")
            current_category.add(text)
        elif grade_val != '-':
            # It's a grade item
            text = Text(f"{clean_name} | Grade: {grade_val} | Range: {range_val} | {percent_val}")
            if "0,00 %" in percent_val or "0.00 %" in percent_val:
                text.stylize("red")
            elif "100" in percent_val:
                text.stylize("green")
            current_category.add(text)
        else:
            # Likely a category header or empty item
            if clean_name:
                text = Text(clean_name, style="bold cyan")
                current_category.add(text)

    console.print(root_tree)


@app.command()
def checkmarks():
    """
    Shows status of 'Kreuzerlübung' (mod_checkmark) exercises.
    """
    client = get_tuwel_client()

    with console.status("[bold green]Looking for checkmark exercises...[/bold green]"):
        try:
            # Try fetching ALL checkmarks by passing empty list (if plugin supports it)
            # This avoids the "stdClass given" error which happens when passing specific IDs
            # due to a server-side bug in mod_checkmark.
            checkmarks_data = client.get_checkmarks([])
            checkmarks_list = checkmarks_data.get('checkmarks', [])
        except Exception as e:
            # Fallback: Error handling if the empty list approach also fails
            rprint(f"[bold red]Error fetching checkmarks:[/bold red] {e}")
            rprint("[dim]This may be due to a bug in the mod_checkmark plugin on TUWEL.[/dim]")
            return

    if not checkmarks_list:
        rprint("[yellow]No Kreuzerlübungen found in your active courses.[/yellow]")
        return

    table = Table(title="Kreuzerlübungen Overview")
    table.add_column("Course ID", style="cyan")  # Using ID as shortname map isn't available without extra call
    table.add_column("Name", style="white")
    table.add_column("Examples Checked", style="green")
    table.add_column("Grade", style="magenta")
    table.add_column("Deadline", style="red")

    for cm in checkmarks_list:
        examples = cm.get('examples', [])
        checked_count = sum(1 for ex in examples if ex.get('checked'))
        total_count = len(examples)

        feedback = cm.get('feedback', {})
        grade = feedback.get('grade', '-')

        cutoff = cm.get('cutoffdate', 0)
        deadline = timestamp_to_date(cutoff) if cutoff else "No Deadline"

        table.add_row(
            str(cm.get('course')),
            cm.get('name'),
            f"{checked_count}/{total_count}",
            grade,
            deadline
        )

    console.print(table)


@app.command()
def download(course_id: int):
    """
    Download all resources (files) from a specific course.
    Files are saved to Downloads/Tuwel/<Course_ID>
    """
    client = get_tuwel_client()

    # 1. Fetch course contents
    with console.status(f"[bold green]Fetching course {course_id} contents...[/bold green]"):
        contents = client._call("core_course_get_contents", {"courseid": course_id})

    if not contents:
        rprint("[red]No content found or access denied.[/red]")
        return

    # 2. Prepare download directory
    dl_dir = Path.home() / "Downloads" / "Tuwel" / str(course_id)
    dl_dir.mkdir(parents=True, exist_ok=True)
    rprint(f"Downloading to: [blue]{dl_dir}[/blue]")

    # 3. Iterate and download
    count = 0
    for section in contents:
        for module in section.get('modules', []):
            # We look for resources, folders, or anything with 'contents' (files)
            if 'contents' in module:
                for file_info in module['contents']:
                    if file_info.get('type') == 'file':
                        file_url = file_info.get('fileurl')
                        file_name = file_info.get('filename')
                        if file_url and file_name:
                            rprint(f" - Downloading {file_name}...")
                            try:
                                client.download_file(file_url, dl_dir / file_name)
                                count += 1
                            except Exception as e:
                                rprint(f"   [red]Failed:[/red] {e}")

    rprint(f"[bold green]Done! Downloaded {count} files.[/bold green]")


@app.command()
def tiss_course(course_number: str, semester: str = "2024W"):
    """Search TISS for course details and exams."""
    with console.status(f"[bold green]Searching TISS...[/bold green]"):
        details = tiss.get_course_details(course_number, semester)
        exams = tiss.get_exam_dates(course_number)

    if "error" in details:
        rprint(f"[bold red]Error:[/bold red] {details['error']}")
        return

    rprint(Panel(f"[bold blue]{details.get('title', {}).get('en', 'Unknown Title')}[/bold blue]\n"
                 f"ECTS: {details.get('ects', 'N/A')} | Type: {details.get('courseType', 'N/A')}",
                 title="Course Info"))

    if exams and isinstance(exams, list):
        t = Table(title="Exams")
        t.add_column("Date", style="green")
        t.add_column("Mode", style="white")
        t.add_column("Registration", style="dim")
        for e in exams:
            t.add_row(e.get('date', 'N/A'), e.get('mode', 'N/A'), e.get('registrationStart', 'N/A'))
        console.print(t)
    else:
        rprint("[yellow]No future exam dates found.[/yellow]")


if __name__ == "__main__":
    app()
