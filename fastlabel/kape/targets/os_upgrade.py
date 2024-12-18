"""
Auto-generated classes from the .tkape files for the OS Upgrade category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class WindowsOSUpgradeArtifactsMigLogxml0(KapeTarget):
    name: ClassVar[str] = "MigLog.xml"
    base_path: ClassVar[Path] = Path("C:\\Windows\\Panther")
    file_mask: ClassVar[str] = "MigLog.xml"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsOSUpgradeArtifactsSetupactlog1(KapeTarget):
    name: ClassVar[str] = "Setupact.log"
    base_path: ClassVar[Path] = Path("C:\\Windows\\Panther")
    file_mask: ClassVar[str] = "Setupact.log"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsOSUpgradeArtifactsHumanReadablexml2(KapeTarget):
    name: ClassVar[str] = "HumanReadable.xml"
    base_path: ClassVar[Path] = Path("C:\\Windows\\Panther")
    file_mask: ClassVar[str] = "*HumanReadable.xml"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsOSUpgradeArtifactsFolderMoveLogtxt3(KapeTarget):
    name: ClassVar[str] = "FolderMoveLog.txt"
    base_path: ClassVar[Path] = Path("C:\\Windows\\Panther\\Rollback")
    file_mask: ClassVar[str] = "FolderMoveLog.txt"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsOSUpgradeArtifactsUpdateStoredb4(KapeTarget):
    name: ClassVar[str] = "Update Store.db"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\USOPrivate\\UpdateStore")
    file_mask: ClassVar[str] = "store.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsOSUpgradeArtifacts(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: e223d74f-7f36-46e8-b4ec-6d46f695a717

    Windows OS Upgrade Artifacts
    """

    name: ClassVar[str] = "WindowsOSUpgradeArtifacts"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WindowsOSUpgradeArtifactsMigLogxml0,
        WindowsOSUpgradeArtifactsSetupactlog1,
        WindowsOSUpgradeArtifactsHumanReadablexml2,
        WindowsOSUpgradeArtifactsFolderMoveLogtxt3,
        WindowsOSUpgradeArtifactsUpdateStoredb4,
    ]
