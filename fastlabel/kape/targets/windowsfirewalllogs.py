"""
Auto-generated classes from the .tkape files for the WindowsFirewallLogs category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class WindowsFirewallWindowsFirewallLogs0(KapeTarget):
    name: ClassVar[str] = "Windows Firewall Logs"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\LogFiles\\Firewall\\")
    file_mask: ClassVar[str] = "pfirewall.*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsFirewallWindowsFirewallLogs1(KapeTarget):
    name: ClassVar[str] = "Windows Firewall Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\LogFiles\\Firewall\\"
    )
    file_mask: ClassVar[str] = "pfirewall.*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsFirewall(KapeTargetConfiguration):
    """
    Author: Mike Cary

    Version: 1.0

    ID: e1c2040e-c1b4-47ef-973f-73a54c5e87ca

    Windows Firewall Logs
    """

    name: ClassVar[str] = "WindowsFirewall"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WindowsFirewallWindowsFirewallLogs0,
        WindowsFirewallWindowsFirewallLogs1,
    ]
