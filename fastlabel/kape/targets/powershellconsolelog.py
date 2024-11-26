"""
Auto-generated classes from the .tkape files for the PowerShellConsoleLog category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class PowerShellConsolePowerShellConsoleLog0(KapeTarget):
    name: ClassVar[str] = "PowerShell Console Log"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Windows\\PowerShell\\PSReadline\\"
    )
    regex: ClassVar[str] = r"(?s:ConsoleHost_history\.txt)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class PowerShellConsole(KapeTargetConfiguration):
    """
    Author: Mike Cary

    Version: 1.0

    ID: efa4332a-89eb-430c-ab61-006a9e6620d7

    PowerShell Console Log File
    """

    name: ClassVar[str] = "PowerShellConsole"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [PowerShellConsolePowerShellConsoleLog0]
