"""
Auto-generated classes from the .tkape files for the Execution category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class OfficeDiagnosticsOfficeDiagnostics0(KapeTarget):
    """
    Payloads for CVE-2022-30190 ('Follina') will be in this log
    """

    name: ClassVar[str] = "Office Diagnostics"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Diagnostics\\")
    regex: ClassVar[str] = r"(?s:PCW\.debugreport\.xml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OfficeDiagnosticsOfficeElevatedDiagnostics1(KapeTarget):
    """
    Payloads for CVE-2022-30190 ('Follina') will be in this log
    """

    name: ClassVar[str] = "Office Elevated Diagnostics"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\ElevatedDiagnostics\\"
    )
    regex: ClassVar[str] = r"(?s:PCW\.debugreport\.xml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OfficeDiagnostics(KapeTargetConfiguration):
    """
    Author: teddy-ROxPin

    Version: 1.0

    ID: 5ef604c2-e76b-40a0-9150-6b6715f2ebd7

    Office Diagnostics
    """

    name: ClassVar[str] = "OfficeDiagnostics"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        OfficeDiagnosticsOfficeDiagnostics0,
        OfficeDiagnosticsOfficeElevatedDiagnostics1,
    ]


class SRUMSRUM0(KapeTarget):
    name: ClassVar[str] = "SRUM"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\SRU\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SRUMSRUM1(KapeTarget):
    name: ClassVar[str] = "SRUM"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\SRU\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SRUMSOFTWAREregistryhive2(KapeTarget):
    name: ClassVar[str] = "SOFTWARE registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SOFTWARE)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SRUMSOFTWAREregistryhive3(KapeTarget):
    name: ClassVar[str] = "SOFTWARE registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SOFTWARE)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SRUMSOFTWAREregistrytransactionfiles4(KapeTarget):
    name: ClassVar[str] = "SOFTWARE registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SOFTWARE\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SRUMSOFTWAREregistrytransactionfiles5(KapeTarget):
    name: ClassVar[str] = "SOFTWARE registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SOFTWARE\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SRUM(KapeTargetConfiguration):
    """
    Author: Mark Hallman

    Version: 1.0

    ID: 9858f1fc-5e22-46a0-8bfd-c821ac9b4a13

    System Resource Usage Monitor (SRUM) Data
    """

    name: ClassVar[str] = "SRUM"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SRUMSRUM0,
        SRUMSRUM1,
        SRUMSOFTWAREregistryhive2,
        SRUMSOFTWAREregistryhive3,
        SRUMSOFTWAREregistrytransactionfiles4,
        SRUMSOFTWAREregistrytransactionfiles5,
    ]
