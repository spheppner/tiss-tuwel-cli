"""
TISS (TU Wien Information Systems and Services) API client.

This module provides a client for interacting with the public TISS API
to fetch course information, exam dates, and public events.

API Documentation: https://tiss.tuwien.ac.at/api
"""

from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

import requests


class TissAPIError(Exception):
    """Custom exception for TISS API errors."""
    pass


class TissClient:
    """
    Client for interacting with the TISS Public API.
    
    TISS (TU Wien Information Systems and Services) provides public endpoints
    for accessing course information, exam schedules, and university events.
    
    Attributes:
        BASE_URL: The base URL for the TISS API.
        timeout: Request timeout in seconds.
    
    Example:
        >>> client = TissClient()
        >>> course = client.get_course_details("192.167", "2025W")
        >>> exams = client.get_exam_dates("192.167")
    """

    BASE_URL = "https://tiss.tuwien.ac.at/api"

    def __init__(self, timeout: int = 10):
        """
        Initialize the TISS client.
        
        Args:
            timeout: Request timeout in seconds (default: 10).
        """
        self.timeout = timeout

    def _get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Any:
        """
        Make a GET request to the TISS API.
        
        Args:
            endpoint: API endpoint path (e.g., "/course/123456-2025W").
            params: Optional query parameters.
            
        Returns:
            JSON response as a dictionary or list.

        Raises:
            TissAPIError: On API errors or parsing failures.
        """
        url = f"{self.BASE_URL}{endpoint}"
        try:
            # Try to get JSON first, but TISS often returns XML despite Request headers
            # Note: We don't force Accept: application/json anymore as it caused 500 errors
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # The TISS API returns 404 if no events are found in the given timeframe.
            # We'll catch this specific case and return an empty list to prevent an error.
            if e.response.status_code == 404 and "/event" in endpoint:
                return []
            raise TissAPIError(str(e))
        except requests.RequestException as e:
            raise TissAPIError(str(e))

        # Handle empty responses
        if not response.content or not response.text.strip():
            raise TissAPIError("Empty response from TISS API")

        # Try JSON parsing
        try:
            return response.json()
        except ValueError as json_e:
            # Fallback: Try XML parsing
            try:
                import xml.etree.ElementTree as ET
                root = ET.fromstring(response.content)

                # Namespaces found in the TISS response
                ns = {
                    '': 'https://tiss.tuwien.ac.at/api/schemas/course/v10',
                    'ns2': 'https://tiss.tuwien.ac.at/api/schemas/i18n/v10'
                }

                # The root might be <tuvienna>, we need to find <course> inside it
                # Note: find() with default namespace requires explicit namespace URI in path or strict Usage
                # We'll try finding 'course' with the namespace
                course_elem = root.find(f"{{{ns['']}}}course")
                # If not found directly, maybe root IS the course or different structure, try relative find
                if course_elem is None:
                    course_elem = root.find('course')  # Try without NS if previous failed
                if course_elem is None:
                    # Maybe root is the course itself (unlikely based on provided XML but possible)
                    course_elem = root

                result = {}

                # Helper to get text from element with namespace
                def get_text(elem, tag, namespace=ns['']):
                    # Try with namespace first
                    sub = elem.find(f"{{{namespace}}}{tag}")
                    if sub is not None:
                        return sub.text
                    # Try without namespace for robustness
                    sub = elem.find(tag)
                    if sub is not None:
                        return sub.text
                    return None

                # Parse course details
                result['courseNumber'] = get_text(course_elem, 'courseNumber')
                result['semester'] = get_text(course_elem, 'semesterCode')
                result['courseType'] = get_text(course_elem, 'courseType')
                result['ects'] = get_text(course_elem, 'ects')  # Might be missing in XML
                if not result['ects']:
                    # Fallback to weekly hours if ECTS invalid
                    result['ects'] = get_text(course_elem, 'weeklyHours') + "h" if get_text(course_elem, 'weeklyHours') else None

                # Parse Title (localized)
                title_elem = course_elem.find(f"{{{ns['']}}}title")
                if title_elem is not None:
                    result['title'] = {
                        'en': get_text(title_elem, 'en', ns['ns2']),
                        'de': get_text(title_elem, 'de', ns['ns2'])
                    }
                else:
                    # Fallback if title element not found standard way
                    result['title'] = {'en': 'Unknown Course', 'de': 'Unbekannter Kurs'}

                return result
            except Exception as xml_e:
                # Raise a clear error if both JSON and XML fail
                raise TissAPIError(f"Failed to parse TISS response. JSON error: {str(json_e)}. XML error: {str(xml_e)}")
        except requests.RequestException as e:
            raise TissAPIError(str(e))

    def get_course_details(self, course_number: str, semester: str) -> Dict[str, Any]:
        """
        Fetch details for a specific course.
        
        Args:
            course_number: Course number (e.g., "192.167" or "192167").
            semester: Semester code (e.g., "2025W" for winter, "2024S" for summer).
            
        Returns:
            Dictionary containing course details including title, ECTS, and type.

        Raises:
            TissAPIError: On API errors.

        Example:
            >>> client = TissClient()
            >>> details = client.get_course_details("192.167", "2025W")
            >>> print(details.get('title', {}).get('en'))
        """
        course_number = course_number.replace(".", "")
        return self._get(f"/course/{course_number}-{semester}")

    def get_exam_dates(self, course_number: str) -> List[Dict[str, Any]]:
        """
        Fetch upcoming exam dates for a course.
        
        Args:
            course_number: Course number (e.g., "192.167" or "192167").
            
        Returns:
            List of exam dictionaries containing date, mode, and registration info.

        Raises:
            TissAPIError: On API errors.

        Example:
            >>> client = TissClient()
            >>> exams = client.get_exam_dates("192.167")
            >>> for exam in exams:
            ...     print(f"{exam.get('date')}: {exam.get('mode')}")
        """
        course_number = course_number.replace(".", "")
        return self._get(f"/course/{course_number}/examDates")

    def get_public_events(self) -> List[Dict[str, Any]]:
        """
        Fetch public university events starting from today.
        
        Returns:
            List of event dictionaries containing description and timing info.

        Raises:
            TissAPIError: On API errors.

        Example:
            >>> client = TissClient()
            >>> events = client.get_public_events()
            >>> for event in events[:5]:
            ...     print(event.get('description'))
        """
        today = datetime.now().strftime("%Y-%m-%d")
        future = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
        params = {"from": today, "to": future}
        return self._get("/event", params=params)
