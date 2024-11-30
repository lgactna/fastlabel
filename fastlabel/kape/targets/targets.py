"""
Auto-generated classes from the .tkape files for the Targets category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class KapeTriageAntivirus0(KapeTarget):
    name: ClassVar[str] = "Antivirus"
    base_path: ClassVar[Path] = Path("Antivirus.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriageEventLogs1(KapeTarget):
    name: ClassVar[str] = "EventLogs"
    base_path: ClassVar[Path] = Path("EventLogs.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriageEvidenceOfExecution2(KapeTarget):
    name: ClassVar[str] = "EvidenceOfExecution"
    base_path: ClassVar[Path] = Path("EvidenceOfExecution.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriageFileSystem3(KapeTarget):
    name: ClassVar[str] = "FileSystem"
    base_path: ClassVar[Path] = Path("FileSystem.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriageLNKFilesAndJumpLists4(KapeTarget):
    name: ClassVar[str] = "LNKFilesAndJumpLists"
    base_path: ClassVar[Path] = Path("LNKFilesAndJumpLists.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriagePowerShellConsole5(KapeTarget):
    name: ClassVar[str] = "PowerShellConsole"
    base_path: ClassVar[Path] = Path("PowerShellConsole.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriageRecycleBinInfoFiles6(KapeTarget):
    name: ClassVar[str] = "RecycleBin_InfoFiles"
    base_path: ClassVar[Path] = Path("RecycleBin_InfoFiles.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriageRegistryHives7(KapeTarget):
    name: ClassVar[str] = "RegistryHives"
    base_path: ClassVar[Path] = Path("RegistryHives.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriageRemoteAccess8(KapeTarget):
    name: ClassVar[str] = "RemoteAccess"
    base_path: ClassVar[Path] = Path("RemoteAdmin.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriageScheduledTasks9(KapeTarget):
    name: ClassVar[str] = "ScheduledTasks"
    base_path: ClassVar[Path] = Path("ScheduledTasks.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriageSRUM10(KapeTarget):
    name: ClassVar[str] = "SRUM"
    base_path: ClassVar[Path] = Path("SRUM.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriageSUM11(KapeTarget):
    name: ClassVar[str] = "SUM"
    base_path: ClassVar[Path] = Path("SUM.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriageWebBrowsers12(KapeTarget):
    name: ClassVar[str] = "WebBrowsers"
    base_path: ClassVar[Path] = Path("WebBrowsers.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriageWindowsTimeline13(KapeTarget):
    name: ClassVar[str] = "WindowsTimeline"
    base_path: ClassVar[Path] = Path("WindowsTimeline.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KapeTriage(KapeTargetConfiguration):
    """
    Author: Scott Downie

    Version: 4.0

    ID: a745b730-d6b7-4cb7-9847-4e896d9f3c52

    Kape Triage collections that will collect most of the files needed for a
    DFIR Investigation. This module pulls evidence from File System files,
    Registry Hives, Event Logs, Scheduled Tasks, Evidence of Execution, SRUM
    data, SUM data, Web Browser data (IE/Edge, Chrome, Mozilla history), LNK
    Files, Jump Lists, 3rd party remote access software logs, 3rd party
    antivirus software logs, Windows 10 Timeline database, and $I Recycle Bin
    data files.
    """

    name: ClassVar[str] = "KapeTriage"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        KapeTriageAntivirus0,
        KapeTriageEventLogs1,
        KapeTriageEvidenceOfExecution2,
        KapeTriageFileSystem3,
        KapeTriageLNKFilesAndJumpLists4,
        KapeTriagePowerShellConsole5,
        KapeTriageRecycleBinInfoFiles6,
        KapeTriageRegistryHives7,
        KapeTriageRemoteAccess8,
        KapeTriageScheduledTasks9,
        KapeTriageSRUM10,
        KapeTriageSUM11,
        KapeTriageWebBrowsers12,
        KapeTriageWindowsTimeline13,
    ]


class SOFELKEventLogs0(KapeTarget):
    name: ClassVar[str] = "EventLogs"
    base_path: ClassVar[Path] = Path("EventLogs.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SOFELKEvidenceOfExecution1(KapeTarget):
    name: ClassVar[str] = "EvidenceOfExecution"
    base_path: ClassVar[Path] = Path("EvidenceOfExecution.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SOFELKFileSystem2(KapeTarget):
    name: ClassVar[str] = "FileSystem"
    base_path: ClassVar[Path] = Path("FileSystem.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SOFELKLNKFilesAndJumpLists3(KapeTarget):
    name: ClassVar[str] = "LNKFilesAndJumpLists"
    base_path: ClassVar[Path] = Path("LNKFilesAndJumpLists.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SOFELKPrefetch4(KapeTarget):
    name: ClassVar[str] = "Prefetch"
    base_path: ClassVar[Path] = Path("Prefetch.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SOFELK(KapeTargetConfiguration):
    """
    Author: Tony Knutson and Andrew Rathbun

    Version: 1.1

    ID: bf220343-d374-4257-835f-b74ee8a47f78

    SOF-ELK related files of interest
    """

    name: ClassVar[str] = "SOFELK"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SOFELKEventLogs0,
        SOFELKEvidenceOfExecution1,
        SOFELKFileSystem2,
        SOFELKLNKFilesAndJumpLists3,
        SOFELKPrefetch4,
    ]
