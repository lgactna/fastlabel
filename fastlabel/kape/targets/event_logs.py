"""
Auto-generated classes from the .tkape files for the Event Logs category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class BasicCollectionEventLogs0(KapeTarget):
    name: ClassVar[str] = "Event Logs"
    base_path: ClassVar[Path] = Path("EventLogs.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BasicCollectionEvidenceofExecution1(KapeTarget):
    name: ClassVar[str] = "Evidence of Execution"
    base_path: ClassVar[Path] = Path("EvidenceOfExecution.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BasicCollectionFileSystem2(KapeTarget):
    name: ClassVar[str] = "File System"
    base_path: ClassVar[Path] = Path("FileSystem.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BasicCollectionLNKFilesAndJumpLists3(KapeTarget):
    name: ClassVar[str] = "LNKFilesAndJumpLists"
    base_path: ClassVar[Path] = Path("LNKFilesAndJumpLists.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BasicCollectionPowerShellConsole4(KapeTarget):
    name: ClassVar[str] = "PowerShellConsole"
    base_path: ClassVar[Path] = Path("PowerShellConsole.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BasicCollectionRecycleBinInfoFiles5(KapeTarget):
    name: ClassVar[str] = "RecycleBin InfoFiles"
    base_path: ClassVar[Path] = Path("RecycleBin_InfoFiles.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BasicCollectionRegistryHives6(KapeTarget):
    name: ClassVar[str] = "RegistryHives"
    base_path: ClassVar[Path] = Path("RegistryHives.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BasicCollectionScheduledTasks7(KapeTarget):
    name: ClassVar[str] = "ScheduledTasks"
    base_path: ClassVar[Path] = Path("ScheduledTasks.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BasicCollectionSRUM8(KapeTarget):
    name: ClassVar[str] = "SRUM"
    base_path: ClassVar[Path] = Path("SRUM.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BasicCollectionThumbCache9(KapeTarget):
    name: ClassVar[str] = "ThumbCache"
    base_path: ClassVar[Path] = Path("Thumbcache.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BasicCollectionUSBDevicesLogs10(KapeTarget):
    name: ClassVar[str] = "USBDevicesLogs"
    base_path: ClassVar[Path] = Path("USBDevicesLogs.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BasicCollectionWindowsIndexSearch11(KapeTarget):
    name: ClassVar[str] = "WindowsIndexSearch"
    base_path: ClassVar[Path] = Path("WindowsIndexSearch.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BasicCollection(KapeTargetConfiguration):
    """
    Author: Phill Moore

    Version: 1.1

    ID: 83b99299-2d84-4844-af25-c727d3440b19

    Basic Collection
    """

    name: ClassVar[str] = "!BasicCollection"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        BasicCollectionEventLogs0,
        BasicCollectionEvidenceofExecution1,
        BasicCollectionFileSystem2,
        BasicCollectionLNKFilesAndJumpLists3,
        BasicCollectionPowerShellConsole4,
        BasicCollectionRecycleBinInfoFiles5,
        BasicCollectionRegistryHives6,
        BasicCollectionScheduledTasks7,
        BasicCollectionSRUM8,
        BasicCollectionThumbCache9,
        BasicCollectionUSBDevicesLogs10,
        BasicCollectionWindowsIndexSearch11,
    ]


class MiniTimelineCollectionEventLogs0(KapeTarget):
    name: ClassVar[str] = "Event Logs"
    base_path: ClassVar[Path] = Path("EventLogs.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MiniTimelineCollectionFileSystem1(KapeTarget):
    name: ClassVar[str] = "File System"
    base_path: ClassVar[Path] = Path("FileSystem.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MiniTimelineCollectionRegistryHives2(KapeTarget):
    name: ClassVar[str] = "RegistryHives"
    base_path: ClassVar[Path] = Path("RegistryHives.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MiniTimelineCollection(KapeTargetConfiguration):
    """
    Author: Mari DeGrazia

    Version: 1.0

    ID: 02e131d6-7784-4302-9495-75536423e414

    MFT, Registry and Event Logs to generate a mini timeline
    """

    name: ClassVar[str] = "MiniTimelineCollection"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        MiniTimelineCollectionEventLogs0,
        MiniTimelineCollectionFileSystem1,
        MiniTimelineCollectionRegistryHives2,
    ]
