"""
Auto-generated classes from the .tkape files for the Persistence category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class BITSBITSfiles0(KapeTarget):
    name: ClassVar[str] = "BITS files"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Microsoft\\Network\\Downloader\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BITS(KapeTargetConfiguration):
    """
    Author: Jos Clephas

    Version: 1.0

    ID: bd55a936-7c4d-46a5-b7bb-a4e4064683d2

    Microsoft BITS (Background Intelligent Transer Service) persistent files
    """

    name: ClassVar[str] = "BITS"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [BITSBITSfiles0]


class ScheduledTasksatjob0(KapeTarget):
    name: ClassVar[str] = "at .job"
    base_path: ClassVar[Path] = Path("C:\\Windows\\Tasks\\")
    file_mask: ClassVar[str] = "*.job"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ScheduledTasksatjob1(KapeTarget):
    name: ClassVar[str] = "at .job"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\Tasks\\")
    file_mask: ClassVar[str] = "*.job"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ScheduledTasksatSchedLgUtxt2(KapeTarget):
    name: ClassVar[str] = "at SchedLgU.txt"
    base_path: ClassVar[Path] = Path("C:\\Windows\\")
    file_mask: ClassVar[str] = "SchedLgU.txt"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ScheduledTasksatSchedLgUtxt3(KapeTarget):
    name: ClassVar[str] = "at SchedLgU.txt"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\")
    file_mask: ClassVar[str] = "SchedLgU.txt"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ScheduledTasksXML4(KapeTarget):
    name: ClassVar[str] = "XML"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\Tasks\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ScheduledTasksXML5(KapeTarget):
    name: ClassVar[str] = "XML"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\Tasks\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ScheduledTasks(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: e5dc4367-2e6b-49bf-a90a-d4c1598bbe28

    Scheduled tasks (*.job and XML)
    """

    name: ClassVar[str] = "ScheduledTasks"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ScheduledTasksatjob0,
        ScheduledTasksatjob1,
        ScheduledTasksatSchedLgUtxt2,
        ScheduledTasksatSchedLgUtxt3,
        ScheduledTasksXML4,
        ScheduledTasksXML5,
    ]


class StartupFoldersUserstartupfolders0(KapeTarget):
    name: ClassVar[str] = "User startup folders"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class StartupFoldersSystemwidestartupfolder1(KapeTarget):
    name: ClassVar[str] = "System-wide startup folder"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\StartUp"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class StartupFolders(KapeTargetConfiguration):
    """
    Author: Jason Ballard

    Version: 1.0

    ID: 95408ecb-0adb-4a13-8b3d-a36e7f70b6b6

    Startup Folders
    """

    name: ClassVar[str] = "StartupFolders"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        StartupFoldersUserstartupfolders0,
        StartupFoldersSystemwidestartupfolder1,
    ]


class StartupInfoStartupInfoXMLFiles0(KapeTarget):
    name: ClassVar[str] = "StartupInfo XML Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows\\System32\\WDI\\LogFiles\\StartupInfo\\"
    )
    file_mask: ClassVar[str] = "*.xml"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class StartupInfoStartupInfoXMLFiles1(KapeTarget):
    name: ClassVar[str] = "StartupInfo XML Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\WDI\\LogFiles\\StartupInfo\\"
    )
    file_mask: ClassVar[str] = "*.xml"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class StartupInfo(KapeTargetConfiguration):
    """
    Author: Hadar Yudovich

    Version: 1.0

    ID: 9bb477a3-fa6f-410d-8646-c3f987c147ce

    StartupInfo XML Files
    """

    name: ClassVar[str] = "StartupInfo"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        StartupInfoStartupInfoXMLFiles0,
        StartupInfoStartupInfoXMLFiles1,
    ]
