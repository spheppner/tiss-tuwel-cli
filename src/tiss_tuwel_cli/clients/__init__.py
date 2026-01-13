"""
API clients for TU Wien services.

This package contains client implementations for interacting with
TISS and TUWEL (Moodle) web services.
"""

from tiss_tuwel_cli.clients.tiss import TissClient
from tiss_tuwel_cli.clients.tuwel import TuwelClient

__all__ = ["TissClient", "TuwelClient"]
