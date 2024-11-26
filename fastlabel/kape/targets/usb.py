"""
Auto-generated classes from the .tkape files for the USB category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class USBDetectiveUSBDevicesLogs0(KapeTarget):
    name: ClassVar[str] = "USBDevicesLogs"
    base_path: ClassVar[Path] = Path("USBDevicesLogs.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class USBDetectiveRegistryHives1(KapeTarget):
    name: ClassVar[str] = "RegistryHives"
    base_path: ClassVar[Path] = Path("RegistryHives.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class USBDetectiveEventLogs2(KapeTarget):
    name: ClassVar[str] = "Event Logs"
    base_path: ClassVar[Path] = Path("EventLogs.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class USBDetectiveLNKFilesAndJumplists3(KapeTarget):
    name: ClassVar[str] = "LNKFilesAndJumplists"
    base_path: ClassVar[Path] = Path("LNKFilesAndJumplists.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class USBDetectiveAmcache4(KapeTarget):
    name: ClassVar[str] = "Amcache"
    base_path: ClassVar[Path] = Path("Amcache.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class USBDetective(KapeTargetConfiguration):
    """
    Author: Kevin Pagano

    Version: 1.0

    ID: 6c3f8a69-f529-4201-a00e-067f6db7be8e

    Collects files that can be input into USB Detective for parsing
    """

    name: ClassVar[str] = "USBDetective"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        USBDetectiveUSBDevicesLogs0,
        USBDetectiveRegistryHives1,
        USBDetectiveEventLogs2,
        USBDetectiveLNKFilesAndJumplists3,
        USBDetectiveAmcache4,
    ]
