"""
Auto-generated classes from the .tkape files for the Notifications category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class WindowsNotificationsDBWindows10NotificationDB0(KapeTarget):
    name: ClassVar[str] = "Windows 10 Notification DB"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\Notifications\\"
    )
    regex: ClassVar[str] = r"(?s:wpndatabase\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsNotificationsDBWindows10NotificationDB1(KapeTarget):
    name: ClassVar[str] = "Windows 10 Notification DB"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\Notifications\\"
    )
    regex: ClassVar[str] = r"(?s:appdb\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsNotificationsDB(KapeTargetConfiguration):
    """
    Author: Hadar Yudovich

    Version: 1.0

    ID: a5c3308d-8941-43c4-a295-b906a59bc895

    Windows 10 Notification DB
    """

    name: ClassVar[str] = "WindowsNotificationsDB"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WindowsNotificationsDBWindows10NotificationDB0,
        WindowsNotificationsDBWindows10NotificationDB1,
    ]
