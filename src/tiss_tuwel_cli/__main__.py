"""
Entry point for running the package as a module.

This allows the CLI to be run with:
    python -m tiss_tuwel_cli

This is equivalent to running the installed CLI command.
"""

from tiss_tuwel_cli.cli import app

if __name__ == "__main__":
    app()
