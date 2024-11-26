"""
Auto-generated classes from the .tkape files for the LNKFiles category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class LNKFilesAndJumpListsLNKFilesfromRecent0(KapeTarget):
    """
    Also includes automatic and custom jumplist directories
    """

    name: ClassVar[str] = "LNK Files from Recent"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Windows\\Recent\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LNKFilesAndJumpListsLNKFilesfromMicrosoftOfficeRecent1(KapeTarget):
    name: ClassVar[str] = "LNK Files from Microsoft Office Recent"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Office\\Recent\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LNKFilesAndJumpListsStartMenuLNKFiles2(KapeTarget):
    name: ClassVar[str] = "Start Menu LNK Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs"
    )
    regex: ClassVar[str] = r"(?s:.*\.LNK)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LNKFilesAndJumpListsLNKFilesfromRecentXP3(KapeTarget):
    name: ClassVar[str] = "LNK Files from Recent (XP)"
    base_path: ClassVar[Path] = Path("C:\\Documents and Settings\\%user%\\Recent\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LNKFilesAndJumpListsDesktopLNKFilesXP4(KapeTarget):
    name: ClassVar[str] = "Desktop LNK Files XP"
    base_path: ClassVar[Path] = Path("C:\\Documents and Settings\\%user%\\Desktop\\")
    regex: ClassVar[str] = r"(?s:.*\.LNK)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LNKFilesAndJumpListsDesktopLNKFiles5(KapeTarget):
    name: ClassVar[str] = "Desktop LNK Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Desktop\\")
    regex: ClassVar[str] = r"(?s:.*\.LNK)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LNKFilesAndJumpListsRestorepointLNKFilesXP6(KapeTarget):
    name: ClassVar[str] = "Restore point LNK Files XP"
    base_path: ClassVar[Path] = Path("C:\\System Volume Information\\_restore*\\RP*\\")
    regex: ClassVar[str] = r"(?s:.*\.LNK)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LNKFilesAndJumpListsLNKFilesfromCProgramData7(KapeTarget):
    name: ClassVar[str] = "LNK Files from C:\\ProgramData"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.LNK)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LNKFilesAndJumpLists(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman, Andrew Rathbun, Yogesh Khatri

    Version: 1.3

    ID: 2e354bdc-e418-438e-8439-c21c83c64e90

    LNK Files and jump lists
    """

    name: ClassVar[str] = "LNKFilesAndJumpLists"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        LNKFilesAndJumpListsLNKFilesfromRecent0,
        LNKFilesAndJumpListsLNKFilesfromMicrosoftOfficeRecent1,
        LNKFilesAndJumpListsStartMenuLNKFiles2,
        LNKFilesAndJumpListsLNKFilesfromRecentXP3,
        LNKFilesAndJumpListsDesktopLNKFilesXP4,
        LNKFilesAndJumpListsDesktopLNKFiles5,
        LNKFilesAndJumpListsRestorepointLNKFilesXP6,
        LNKFilesAndJumpListsLNKFilesfromCProgramData7,
    ]
