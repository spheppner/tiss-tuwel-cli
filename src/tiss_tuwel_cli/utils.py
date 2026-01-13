"""
Utility functions for the TU Wien Companion CLI.

This module provides helper functions for date formatting, token parsing,
and other common operations used across the application.
"""

import base64
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
