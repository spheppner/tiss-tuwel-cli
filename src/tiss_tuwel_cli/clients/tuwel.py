"""
TUWEL (Moodle) API client.

This module provides a client for interacting with the TUWEL web service,
which is TU Wien's Moodle-based learning management system.

TUWEL provides access to courses, assignments, grades, calendar events,
and other educational resources.
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

import requests


class TuwelClient:
    """
    Client for interacting with the TUWEL (Moodle) Web Service.
    
    TUWEL is TU Wien's learning management system based on Moodle.
    This client provides methods to access courses, assignments, grades,
    calendar events, and download course materials.
    
    Attributes:
        BASE_URL: The base URL for the TUWEL web service API.
        token: The authentication token for API requests.
        timeout: Request timeout in seconds.
    
    Example:
        >>> client = TuwelClient("your_token_here")
        >>> courses = client.get_enrolled_courses()
        >>> for course in courses:
        ...     print(course['fullname'])
    """

    BASE_URL = "https://tuwel.tuwien.ac.at/webservice/rest/server.php"

    def __init__(self, token: str, timeout: int = 15):
        """
        Initialize the TUWEL client.
        
        Args:
            token: TUWEL authentication token obtained via mobile app login flow.
            timeout: Request timeout in seconds (default: 15).
        """
        self.token = token
        self.timeout = timeout

    def _call(self, wsfunction: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """
        Make a POST request to the TUWEL web service.
        
        Args:
            wsfunction: The Moodle web service function name.
            params: Optional additional parameters for the function.
            
        Returns:
            JSON response from the API.
            
        Raises:
            Exception: On network errors or Moodle API exceptions.
        """
        if params is None:
            params = {}

        payload = {
            "wstoken": self.token,
            "wsfunction": wsfunction,
            "moodlewsrestformat": "json",
        }
        payload.update(params)

        try:
            response = requests.post(self.BASE_URL, data=payload, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            if isinstance(data, dict) and "exception" in data:
                raise Exception(f"Moodle Error: {data.get('message')}")

            return data
        except requests.RequestException as e:
            raise Exception(f"Network Error: {str(e)}")

    def get_site_info(self) -> Dict[str, Any]:
        """
        Get information about the TUWEL site and authenticated user.
        
        Returns:
            Dictionary containing site information including:
            - userid: The authenticated user's ID
            - fullname: The user's full name
            - sitename: The site name
            
        Example:
            >>> client = TuwelClient(token)
            >>> info = client.get_site_info()
            >>> print(f"Logged in as: {info['fullname']}")
        """
        return self._call("core_webservice_get_site_info")

    def get_upcoming_calendar(self) -> Dict[str, Any]:
        """
        Get upcoming calendar events and deadlines.
        
        Returns:
            Dictionary containing 'events' list with upcoming calendar items.
            
        Example:
            >>> client = TuwelClient(token)
            >>> calendar = client.get_upcoming_calendar()
            >>> for event in calendar.get('events', []):
            ...     print(event['name'])
        """
        return self._call("core_calendar_get_calendar_upcoming_view")

    def get_enrolled_courses(self, classification: str = 'inprogress') -> List[Dict[str, Any]]:
        """
        Get courses the user is enrolled in.
        
        Args:
            classification: Filter courses by timeline status.
                - 'past': Completed courses
                - 'inprogress': Currently active courses (default)
                - 'future': Upcoming courses
                
        Returns:
            List of course dictionaries containing id, shortname, and fullname.
            
        Example:
            >>> client = TuwelClient(token)
            >>> courses = client.get_enrolled_courses('inprogress')
            >>> for course in courses:
            ...     print(f"{course['shortname']}: {course['fullname']}")
        """
        params = {"classification": classification, "sort": "fullname"}
        data = self._call("core_course_get_enrolled_courses_by_timeline_classification", params)
        return data.get('courses', [])

    def get_assignments(self) -> Dict[str, Any]:
        """
        Get assignments from all enrolled courses.
        
        Returns:
            Dictionary containing 'courses' list, each with 'assignments' list.
            
        Example:
            >>> client = TuwelClient(token)
            >>> data = client.get_assignments()
            >>> for course in data.get('courses', []):
            ...     for assignment in course.get('assignments', []):
            ...         print(assignment['name'])
        """
        courses = self.get_enrolled_courses()
        if not courses:
            return {"courses": []}

        # Build courseids[0]=123, courseids[1]=456...
        params = {}
        for i, cid in enumerate([c['id'] for c in courses]):
            params[f"courseids[{i}]"] = cid

        return self._call("mod_assign_get_assignments", params)

    def get_user_grades_table(self, course_id: int, user_id: int) -> Dict[str, Any]:
        """
        Fetch the grade report table structure for a course.
        
        Args:
            course_id: The Moodle course ID.
            user_id: The Moodle user ID.
            
        Returns:
            Dictionary containing 'tables' list with grade information.
            
        Example:
            >>> client = TuwelClient(token)
            >>> grades = client.get_user_grades_table(12345, 67890)
            >>> tables = grades.get('tables', [])
        """
        params = {"courseid": course_id, "userid": user_id}
        return self._call("gradereport_user_get_grades_table", params)

    def get_checkmarks(self, course_ids: List[int]) -> Dict[str, Any]:
        """
        Fetch 'Kreuzerlübung' (mod_checkmark) exercise data.
        
        Kreuzerlübungen are a TU Wien-specific exercise format where students
        mark which exercises they have completed.
        
        Args:
            course_ids: List of course IDs to fetch checkmarks from.
                       Pass empty list to fetch from all courses.
            
        Returns:
            Dictionary containing 'checkmarks' list with exercise status.
            
        Example:
            >>> client = TuwelClient(token)
            >>> data = client.get_checkmarks([])  # All courses
            >>> for cm in data.get('checkmarks', []):
            ...     print(cm['name'])
        """
        params = {}
        for i, cid in enumerate(course_ids):
            params[f"courseids[{i}]"] = cid
        return self._call("mod_checkmark_get_checkmarks_by_courses", params)

    def get_course_contents(self, course_id: int) -> List[Dict[str, Any]]:
        """
        Fetch the contents/resources of a course.
        
        Args:
            course_id: The Moodle course ID.
            
        Returns:
            List of section dictionaries containing modules and resources.
            
        Example:
            >>> client = TuwelClient(token)
            >>> contents = client.get_course_contents(12345)
            >>> for section in contents:
            ...     for module in section.get('modules', []):
            ...         print(module['name'])
        """
        return self._call("core_course_get_contents", {"courseid": course_id})

    def download_file(self, file_url: str, output_path: Path) -> None:
        """
        Download a file from TUWEL.
        
        The authentication token is automatically appended to the URL.
        
        Args:
            file_url: The file URL from TUWEL (from course contents).
            output_path: Local path where the file should be saved.
            
        Raises:
            requests.HTTPError: On download failure.
            
        Example:
            >>> client = TuwelClient(token)
            >>> client.download_file(
            ...     "https://tuwel.tuwien.ac.at/pluginfile.php/...",
            ...     Path("./lecture.pdf")
            ... )
        """
        # Check if URL already has query params
        separator = "&" if "?" in file_url else "?"
        download_url = f"{file_url}{separator}token={self.token}"

        with requests.get(download_url, stream=True) as r:
            r.raise_for_status()
            with open(output_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
