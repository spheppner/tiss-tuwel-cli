"""
Configuration management for the TU Wien Companion CLI.

This module handles persistent storage of user configuration including
TUWEL authentication tokens and user IDs.
"""

import json
from pathlib import Path
from typing import Dict, Optional

# Default configuration directory and file paths
CONFIG_DIR = Path.home() / ".tu_companion"
CONFIG_FILE = CONFIG_DIR / "config.json"


class ConfigManager:
    """
    Manages persistent configuration for the CLI application.
    
    Configuration is stored in JSON format at ~/.tu_companion/config.json
    
    Attributes:
        config_dir: Path to the configuration directory.
        config_file: Path to the configuration file.
    
    Example:
        >>> config = ConfigManager()
        >>> config.set_tuwel_token("my_token")
        >>> token = config.get_tuwel_token()
    """

    def __init__(self, config_dir: Optional[Path] = None, config_file: Optional[Path] = None):
        """
        Initialize the configuration manager.

        Args:
            config_dir: Optional custom configuration directory path.
            config_file: Optional custom configuration file path.
        """
        self.config_dir = config_dir or CONFIG_DIR
        self.config_file = config_file or CONFIG_FILE
        self._ensure_config_exists()

    def _ensure_config_exists(self) -> None:
        """Create configuration directory and file if they don't exist."""
        if not self.config_dir.exists():
            self.config_dir.mkdir(parents=True)
        if not self.config_file.exists():
            self._save_config({})

    def _load_config(self) -> Dict:
        """
        Load configuration from the JSON file.

        Returns:
            Dictionary containing the configuration, or empty dict on error.
        """
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}

    def _save_config(self, config: Dict) -> None:
        """
        Save configuration to the JSON file.
        
        Args:
            config: Dictionary containing the configuration to save.
        """
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)

    def get_tuwel_token(self) -> Optional[str]:
        """
        Get the stored TUWEL authentication token.
        
        Returns:
            The TUWEL token string, or None if not configured.
        """
        config = self._load_config()
        return config.get("tuwel_token")

    def set_tuwel_token(self, token: str) -> None:
        """
        Store the TUWEL authentication token.
        
        Args:
            token: The TUWEL token to store.
        """
        config = self._load_config()
        config["tuwel_token"] = token
        self._save_config(config)

    def get_user_id(self) -> Optional[int]:
        """
        Get the stored TUWEL user ID.
        
        Returns:
            The user ID integer, or None if not configured.
        """
        config = self._load_config()
        return config.get("tuwel_userid")

    def set_user_id(self, userid: int) -> None:
        """
        Store the TUWEL user ID.
        
        Args:
            userid: The user ID to store.
        """
        config = self._load_config()
        config["tuwel_userid"] = userid
        self._save_config(config)

    def get_login_credentials(self) -> tuple[Optional[str], Optional[str]]:
        """
        Get TUWEL login credentials from the config file.

        Returns:
            A tuple containing (username, password), or (None, None) if not set.
        """
        config = self._load_config()
        return config.get("tuwel_user"), config.get("tuwel_pass")

    def set_login_credentials(self, user: str, passw: str) -> None:
        """
        Save TUWEL login credentials to the config file.

        Args:
            user: The TUWEL username.
            passw: The TUWEL password.
        """
        config = self._load_config()
        config["tuwel_user"] = user
        config["tuwel_pass"] = passw
        self._save_config(config)
