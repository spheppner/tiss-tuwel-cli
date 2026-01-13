"""
TU Wien Companion - TISS & TUWEL CLI.

A Python CLI tool for TU Wien students to interact with the public TISS API
and TUWEL (Moodle) web services.

Example usage:
    # Setup authentication
    $ tiss-tuwel-cli login
    
    # View upcoming deadlines
    $ tiss-tuwel-cli dashboard
    
    # List enrolled courses
    $ tiss-tuwel-cli courses
"""

__version__ = "0.1.0"
__author__ = "TU Wien Companion Contributors"

from tiss_tuwel_cli.config import ConfigManager
from tiss_tuwel_cli.clients.tiss import TissClient
from tiss_tuwel_cli.clients.tuwel import TuwelClient

__all__ = [
    "ConfigManager",
    "TissClient", 
    "TuwelClient",
    "__version__",
]
