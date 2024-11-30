"""
Auto-generated classes from the .tkape files for the Software category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class AteraAgentAteraAgentinifiles0(KapeTarget):
    """
    Collects logs for AteraAgent
    """

    name: ClassVar[str] = "AteraAgent .ini files"
    base_path: ClassVar[Path] = Path("C:\\Program Files\\ATERA Networks\\AteraAgent")
    file_mask: ClassVar[str] = "*.ini"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AteraAgentAteraAgentLogs1(KapeTarget):
    """
    Collects logs for AteraAgent
    """

    name: ClassVar[str] = "AteraAgent Logs"
    base_path: ClassVar[Path] = Path("C:\\Program Files\\ATERA Networks\\AteraAgent")
    file_mask: ClassVar[str] = "*.txt"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AteraAgentAteraAgentLogs2(KapeTarget):
    """
    Collects logs for AteraAgent
    """

    name: ClassVar[str] = "AteraAgent Logs"
    base_path: ClassVar[Path] = Path("C:\\Program Files\\ATERA Networks\\AteraAgent")
    file_mask: ClassVar[str] = "*.db"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AteraAgentAteraAgentLogs3(KapeTarget):
    """
    Collects logs for AteraAgent
    """

    name: ClassVar[str] = "AteraAgent Logs"
    base_path: ClassVar[Path] = Path("C:\\Program Files\\ATERA Networks\\AteraAgent")
    file_mask: ClassVar[str] = "*.config"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AteraAgentAteraAgentLogs4(KapeTarget):
    """
    Collects logs for AteraAgent
    """

    name: ClassVar[str] = "AteraAgent Logs"
    base_path: ClassVar[Path] = Path("C:\\Program Files\\ATERA Networks\\AteraAgent")
    file_mask: ClassVar[str] = "*.cfg"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AteraAgent(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: ca980fbe-fe64-490c-ac94-0bcdd8e8bce1

    AteraAgent
    """

    name: ClassVar[str] = "AteraAgent"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        AteraAgentAteraAgentinifiles0,
        AteraAgentAteraAgentLogs1,
        AteraAgentAteraAgentLogs2,
        AteraAgentAteraAgentLogs3,
        AteraAgentAteraAgentLogs4,
    ]


class SplashtopSplashtopLogFiles0(KapeTarget):
    """
    Collects logs for Splashtop
    """

    name: ClassVar[str] = "Splashtop Log Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Program Files*\\Splashtop\\Splashtop Remote\\Server\\log"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SplashtopSplashtopLogFilesinProgramData1(KapeTarget):
    """
    Collects logs for Splashtop
    """

    name: ClassVar[str] = "Splashtop Log Files in ProgramData"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Splashtop\\Temp\\log")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Splashtop(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun, Yogesh Khatri

    Version: 1.0

    ID: 940c768b-b32c-4b4b-82d7-68385ff470c8

    Splashtop
    """

    name: ClassVar[str] = "Splashtop"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SplashtopSplashtopLogFiles0,
        SplashtopSplashtopLogFilesinProgramData1,
    ]
