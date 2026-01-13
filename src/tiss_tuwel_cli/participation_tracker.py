"""
Participation tracking for exercise sessions (Übungen).

This module provides functionality to track when students are called to
present exercises at the board and calculate the probability of being
called in future sessions.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Data file for participation history
PARTICIPATION_FILE = Path.home() / ".tu_companion" / "participation_history.json"

# Probability calculation constants
ADJUSTMENT_FACTOR = 0.5  # Factor for adjusting probability based on fairness (0.0 to 1.0)


class ParticipationTracker:
    """
    Track participation in exercise sessions.
    
    For exercise courses where students are randomly called to present
    solutions at the board, this tracker maintains history and calculates
    probabilities of being called in future sessions.
    """

    def __init__(self, data_file: Optional[Path] = None):
        """
        Initialize the participation tracker.
        
        Args:
            data_file: Optional custom path for the data file.
        """
        self.data_file = data_file or PARTICIPATION_FILE
        self._ensure_data_exists()

    def _ensure_data_exists(self) -> None:
        """Create data directory and file if they don't exist."""
        self.data_file.parent.mkdir(parents=True, exist_ok=True)
        if not self.data_file.exists():
            self._save_data({})

    def _load_data(self) -> Dict:
        """
        Load participation history from the JSON file.
        
        Returns:
            Dictionary with course participation data.
        """
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}

    def _save_data(self, data: Dict) -> None:
        """
        Save participation history to the JSON file.
        
        Args:
            data: Dictionary containing the participation data to save.
        """
        with open(self.data_file, 'w') as f:
            json.dump(data, f, indent=4)

    def record_participation(
        self,
        course_id: int,
        course_name: str,
        exercise_name: str,
        was_called: bool,
        date: Optional[str] = None
    ) -> None:
        """
        Record a participation event for an exercise session.
        
        Args:
            course_id: The course ID.
            course_name: The full name of the course.
            exercise_name: Name of the exercise (e.g., "Exercise 3").
            was_called: True if the student was called, False otherwise.
            date: Optional date string (ISO format), defaults to today.
        """
        data = self._load_data()
        course_key = str(course_id)
        
        if course_key not in data:
            data[course_key] = {
                'course_name': course_name,
                'group_size': 1,  # Default, can be updated
                'sessions': []
            }
        
        # Update course name in case it changed
        data[course_key]['course_name'] = course_name
        
        session_date = date or datetime.now().strftime('%Y-%m-%d')
        data[course_key]['sessions'].append({
            'date': session_date,
            'exercise': exercise_name,
            'was_called': was_called
        })
        
        self._save_data(data)

    def set_group_size(self, course_id: int, group_size: int) -> None:
        """
        Set or update the group size for a course.
        
        Args:
            course_id: The course ID.
            group_size: Average number of students in the exercise groups.
        """
        data = self._load_data()
        course_key = str(course_id)
        
        if course_key in data:
            data[course_key]['group_size'] = group_size
            self._save_data(data)

    def get_course_data(self, course_id: int) -> Optional[Dict]:
        """
        Get all participation data for a specific course.
        
        Args:
            course_id: The course ID.
            
        Returns:
            Dictionary with course participation data, or None if not found.
        """
        data = self._load_data()
        return data.get(str(course_id))

    def get_all_courses(self) -> Dict[int, Dict]:
        """
        Get participation data for all tracked courses.
        
        Returns:
            Dictionary mapping course IDs to their participation data.
        """
        data = self._load_data()
        return {int(k): v for k, v in data.items()}

    def calculate_probability(self, course_id: int) -> Optional[Dict]:
        """
        Calculate the probability of being called in the next session.
        
        This uses a simple model based on:
        - Number of times already called
        - Total number of sessions attended
        - Group size
        
        The probability is adjusted to be fair: if you haven't been called
        much relative to the average, your probability increases.
        
        Args:
            course_id: The course ID.
            
        Returns:
            Dictionary with probability statistics, or None if no data.
        """
        course_data = self.get_course_data(course_id)
        if not course_data:
            return None
        
        sessions = course_data.get('sessions', [])
        if not sessions:
            return None
        
        group_size = course_data.get('group_size', 1)
        if group_size < 1:
            group_size = 1
        
        total_sessions = len(sessions)
        times_called = sum(1 for s in sessions if s.get('was_called', False))
        
        # Base probability (uniform random selection)
        base_prob = 1.0 / group_size
        
        # Expected number of calls up to this point
        expected_calls = total_sessions / group_size
        
        # Adjustment factor: if called less than expected, increase probability
        # if called more than expected, decrease probability
        if expected_calls > 0:
            adjustment = (expected_calls - times_called) / expected_calls
            # Clamp adjustment to reasonable range (-1 to 1)
            adjustment = max(-1, min(1, adjustment))
            
            # Adjusted probability with bounds [0, 1]
            adjusted_prob = base_prob * (1 + adjustment * ADJUSTMENT_FACTOR)
            adjusted_prob = max(0.0, min(1.0, adjusted_prob))
        else:
            adjusted_prob = base_prob
        
        return {
            'course_id': course_id,
            'course_name': course_data.get('course_name', f'Course {course_id}'),
            'total_sessions': total_sessions,
            'times_called': times_called,
            'group_size': group_size,
            'base_probability': base_prob * 100,  # As percentage
            'adjusted_probability': adjusted_prob * 100,  # As percentage
            'expected_calls': expected_calls,
            'sessions': sessions[-5:]  # Last 5 sessions
        }

    def delete_course_data(self, course_id: int) -> bool:
        """
        Delete all participation data for a course.
        
        Args:
            course_id: The course ID to delete.
            
        Returns:
            True if data was deleted, False if course not found.
        """
        data = self._load_data()
        course_key = str(course_id)
        
        if course_key in data:
            del data[course_key]
            self._save_data(data)
            return True
        return False
