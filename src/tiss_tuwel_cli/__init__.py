"""
TU Wien Companion - TISS & TUWEL CLI.

A Python CLI tool for TU Wien students to interact with the public TISS API
and TUWEL (Moodle) web services.

Example usage:
    # Setup authentication
    $ tiss-tuwel-cli login
    
    # View upcoming deadlines
    $ tiss-tuwel-cli timeline
"""

from .clients.tiss import TissClient
from .clients.tuwel import TuwelClient, TuwelAPIError
from .config import ConfigManager

__all__ = [
    "TissClient",
    "TuwelClient",
    "TuwelAPIError",
    "ConfigManager",
]
