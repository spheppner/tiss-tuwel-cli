"""
TISS (TU Wien Information Systems and Services) API client.

This module provides a client for interacting with the public TISS API
to fetch course information, exam dates, and public events.

API Documentation: https://tiss.tuwien.ac.at/api
"""

from datetime import datetime
from typing import Any, Dict, List, Optional

import requests


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
        >>> course = client.get_course_details("192.167", "2024W")
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
            endpoint: API endpoint path (e.g., "/course/123456-2024W").
            params: Optional query parameters.
            
        Returns:
            JSON response as a dictionary or list, or error dictionary on failure.
        """
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()

            # Handle empty responses
            if not response.content or not response.text.strip():
                return {"error": "Empty response from TISS API"}

            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}
        except ValueError as e:
            # JSONDecodeError is a subclass of ValueError
            return {"error": f"Invalid JSON response: {str(e)}"}

    def get_course_details(self, course_number: str, semester: str) -> Dict[str, Any]:
        """
        Fetch details for a specific course.
        
        Args:
            course_number: Course number (e.g., "192.167" or "192167").
            semester: Semester code (e.g., "2024W" for winter, "2024S" for summer).
            
        Returns:
            Dictionary containing course details including title, ECTS, and type.
            Returns {"error": "..."} on failure.
        
        Example:
            >>> client = TissClient()
            >>> details = client.get_course_details("192.167", "2024W")
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
            Returns {"error": "..."} on failure.
        
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
            Returns {"error": "..."} on failure.
        
        Example:
            >>> client = TissClient()
            >>> events = client.get_public_events()
            >>> for event in events[:5]:
            ...     print(event.get('description'))
        """
        today = datetime.now().strftime("%Y-%m-%d")
        params = {"from": today}
        return self._get("/event", params=params)
