"""
Auto-generated classes from the .mkape files for the PowerShellHistory category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class PowerShellMoveKAPEConsoleHosthistory(KapeModule):
    """
    Author: Andrew Rathbun and Matt Arbaugh

    Version: 1.0

    ID: e57584ec-0c9a-49cf-9ac5-7d42c7570fae

    Move-KAPEConsoleHost_history.ps1 - Moves the ConsoleHost_history.txt file
    into the Modules output for better visibility
    """

    name: ClassVar[str] = "PowerShell_Move-KAPEConsoleHost_history"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]
