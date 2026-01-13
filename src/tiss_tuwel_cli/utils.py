"""
Utility functions for the TU Wien Companion CLI.

This module provides helper functions for date formatting, token parsing,
and other common operations used across the application.
"""

import base64
import html
import re
import urllib.parse
from datetime import datetime
from typing import Optional


def timestamp_to_date(ts: Optional[int]) -> str:
    """
    Convert a Unix timestamp to a human-readable date string.
    
    Args:
        ts: Unix timestamp in seconds, or None.
        
    Returns:
        Formatted date string (YYYY-MM-DD HH:MM), or "N/A" if input is None/falsy.
    
    Example:
        >>> timestamp_to_date(1704067200)
        '2024-01-01 00:00'
        >>> timestamp_to_date(None)
        'N/A'
    """
    if not ts:
        return "N/A"
    return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M')


def parse_mobile_token(token_string: str) -> Optional[str]:
    """
    Decode the token format used by Moodle Mobile.
    
    Handles the 'moodlemobile://token=BASE64...' URL format as well as
    raw base64 encoded token strings.
    
    The token format is: PASSPORT:::TOKEN:::PRIVATE (base64 encoded)
    
    Args:
        token_string: Either a moodlemobile:// URL or a raw base64 string.
        
    Returns:
        The extracted token string, or None if parsing fails.
    
    Example:
        >>> # With full URL
        >>> parse_mobile_token("moodlemobile://token=cGFzc3BvcnQ6Ojp0b2tlbjo6OnByaXZhdGU=")
        'token'
        >>> # With raw base64
        >>> parse_mobile_token("cGFzc3BvcnQ6Ojp0b2tlbjo6OnByaXZhdGU=")
        'token'
    """
    # Extract base64 part
    base64_message = token_string
    if "token=" in token_string:
        base64_message = token_string.split("token=")[1]

    # URL Decode (in case browser encoded special chars in base64)
    base64_message = urllib.parse.unquote(base64_message)

    try:
        # Base64 Decode
        message_bytes = base64.b64decode(base64_message)
        message = message_bytes.decode('ascii')

        # Extract middle part: PASSPORT:::TOKEN:::PRIVATE
        parts = message.split(':::')
        if len(parts) >= 2:
            return parts[1]
    except Exception:
        pass

    return None


def strip_html(html_string: str) -> str:
    """
    Remove HTML tags and decode HTML entities from a string.
    
    Args:
        html_string: String potentially containing HTML markup.
        
    Returns:
        Clean text with HTML tags removed and entities decoded.
    
    Example:
        >>> strip_html('<span class="test">Hello &amp; World</span>')
        'Hello & World'
        >>> strip_html('<i class="icon fa fa-check"></i>30,00')
        '30,00'
    """
    if not html_string:
        return ""

    # Remove all HTML tags
    text = re.sub(r'<[^>]+>', '', html_string)

    # Decode HTML entities (e.g., &ndash; &nbsp; &amp;)
    text = html.unescape(text)

    # Normalize whitespace
    text = ' '.join(text.split())

    return text.strip()


def parse_percentage(percent_str: str) -> Optional[float]:
    """
    Parse a percentage string to a float value.
    
    Args:
        percent_str: String containing a percentage (e.g., "85,50 %", "100.00%", "-").
        
    Returns:
        The percentage as a float (0-100), or None if not parseable.
    """
    if not percent_str or percent_str == '-':
        return None
    
    # Remove % sign and spaces
    cleaned = percent_str.replace('%', '').strip()
    # Handle European comma decimal separator
    cleaned = cleaned.replace(',', '.')
    
    try:
        return float(cleaned)
    except ValueError:
        return None


def extract_course_number(shortname: str) -> Optional[str]:
    """
    Extract a TISS course number from a TUWEL course shortname.
    
    TUWEL course shortnames often contain the TISS course number in various formats
    like "192.167-2024W" or "VU 192.167" or just embedded in the name.
    
    Args:
        shortname: The TUWEL course shortname.
        
    Returns:
        The course number in format "XXXXXX" (6 digits) or None if not found.
    
    Example:
        >>> extract_course_number("VU 192.167 - Maths")
        '192167'
        >>> extract_course_number("192167-2024W")
        '192167'
    """
    if not shortname:
        return None
    
    # Pattern 1: Match XXX.XXX format
    match = re.search(r'(\d{3})\.(\d{3})', shortname)
    if match:
        return match.group(1) + match.group(2)
    
    # Pattern 2: Match XXXXXX format (6 consecutive digits)
    match = re.search(r'\b(\d{6})\b', shortname)
    if match:
        return match.group(1)
    
    return None


def get_current_semester() -> str:
    """
    Get the current semester code based on the current date.

    TU Wien semesters follow this pattern:
    - Winter semester (W): October to February (spans two calendar years)
      - Oct-Dec: Uses current year (e.g., 2024W in October 2024)
      - Jan-Feb: Uses previous year (e.g., 2024W in January 2025)
    - Summer semester (S): March to September (e.g., 2024S)

    Returns:
        Semester code in format "YYYYS" or "YYYYW".

    Example:
        >>> # If current date is January 2024
        >>> get_current_semester()
        '2023W'
        >>> # If current date is October 2024
        >>> get_current_semester()
        '2024W'
    """
    now = datetime.now()
    year = now.year
    month = now.month

    if month >= 10:
        # October onwards is winter semester of this year
        return f"{year}W"
    elif month >= 3:
        # March to September is summer semester
        return f"{year}S"
    else:
        # January to February is still winter semester of previous year
        return f"{year - 1}W"


def days_until(date_str: str) -> Optional[int]:
    """
    Calculate days until a given date string.
    
    Args:
        date_str: Date in ISO format (YYYY-MM-DD) or datetime format.
        
    Returns:
        Number of days until the date, or None if parsing fails.
        Negative values mean the date is in the past.
    """
    if not date_str:
        return None
    
    try:
        # Try parsing ISO date
        if 'T' in date_str:
            target = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            target = target.replace(tzinfo=None)
        else:
            target = datetime.strptime(date_str[:10], '%Y-%m-%d')
        
        now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        delta = target - now
        return delta.days
    except (ValueError, AttributeError):
        return None
