"""
Auto-generated classes from the .tkape files for the USBDevices category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class USBDevicesLogsSetupapilogXP0(KapeTarget):
    name: ClassVar[str] = "Setupapi.log XP"
    base_path: ClassVar[Path] = Path("C:\\Windows\\")
    file_mask: ClassVar[str] = "setupapi.log"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class USBDevicesLogsSetupapilogWin71(KapeTarget):
    name: ClassVar[str] = "Setupapi.log Win7+"
    base_path: ClassVar[Path] = Path("C:\\Windows\\inf\\")
    file_mask: ClassVar[str] = "setupapi.dev.log"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class USBDevicesLogsSetupapilogWin72(KapeTarget):
    name: ClassVar[str] = "Setupapi.log Win7+"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\inf\\")
    file_mask: ClassVar[str] = "setupapi.dev.log"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class USBDevicesLogs(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 07ee308f-c79a-47de-a431-c93ab34e4b66

    USB devices log files
    """

    name: ClassVar[str] = "USBDevicesLogs"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        USBDevicesLogsSetupapilogXP0,
        USBDevicesLogsSetupapilogWin71,
        USBDevicesLogsSetupapilogWin72,
    ]
