"""
Auto-generated classes from the .tkape files for the Executables category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class AssetAdvisorLogAssetAdvisorLog0(KapeTarget):
    name: ClassVar[str] = "Asset Advisor Log"
    base_path: ClassVar[Path] = Path("C:\\Windows\\CCM\\Logs\\AssetAdvisor.log")
    file_mask: ClassVar[str] = "EncapsulationLogging.hve"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AssetAdvisorLog(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 700413f8-703b-44fb-9192-8830ac84b6b0

    Asset Advisor Log
    """

    name: ClassVar[str] = "AssetAdvisorLog"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [AssetAdvisorLogAssetAdvisorLog0]


class EncapsulationLoggingEncapsulationLogging0(KapeTarget):
    name: ClassVar[str] = "EncapsulationLogging"
    base_path: ClassVar[Path] = Path("C:\\Windows\\Appcompat\\Programs\\")
    file_mask: ClassVar[str] = "EncapsulationLogging.hve"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EncapsulationLoggingEncapsulationLogging1(KapeTarget):
    name: ClassVar[str] = "EncapsulationLogging"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\Appcompat\\Programs\\")
    file_mask: ClassVar[str] = "EncapsulationLogging.hve"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EncapsulationLoggingEncapsulationLoggingLogs2(KapeTarget):
    name: ClassVar[str] = "EncapsulationLogging Logs"
    base_path: ClassVar[Path] = Path("C:\\Windows\\Appcompat\\Programs\\")
    file_mask: ClassVar[str] = "EncapsulationLogging.hve.log*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EncapsulationLoggingEncapsulationLoggingLogs3(KapeTarget):
    name: ClassVar[str] = "EncapsulationLogging Logs"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\Appcompat\\Programs\\")
    file_mask: ClassVar[str] = "EncapsulationLogging.hve.log*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EncapsulationLogging(KapeTargetConfiguration):
    """
    Author: Troy Larson

    Version: 1.0

    ID: 7c328d9b-4a10-459d-b8b3-36d81686bc74

    EncapsulationLogging
    """

    name: ClassVar[str] = "EncapsulationLogging"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        EncapsulationLoggingEncapsulationLogging0,
        EncapsulationLoggingEncapsulationLogging1,
        EncapsulationLoggingEncapsulationLoggingLogs2,
        EncapsulationLoggingEncapsulationLoggingLogs3,
    ]


class SDBSDBFiles0(KapeTarget):
    name: ClassVar[str] = "SDB Files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\apppatch\\Custom\\")
    file_mask: ClassVar[str] = "*.sdb"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SDBSDBFiles1(KapeTarget):
    name: ClassVar[str] = "SDB Files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\apppatch\\Custom\\")
    file_mask: ClassVar[str] = "*.sdb"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SDBSDBFilesx642(KapeTarget):
    name: ClassVar[str] = "SDB Files x64"
    base_path: ClassVar[Path] = Path("C:\\Windows\\apppatch\\Custom\\Custom64\\")
    file_mask: ClassVar[str] = "*.sdb"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SDBSDBFilesx643(KapeTarget):
    name: ClassVar[str] = "SDB Files x64"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\apppatch\\Custom\\Custom64\\"
    )
    file_mask: ClassVar[str] = "*.sdb"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SDB(KapeTargetConfiguration):
    """
    Author: Troy Larson

    Version: 1.0

    ID: 99e82a85-e4d4-4139-930c-7eea9a45452f

    Shim SDB FIles
    """

    name: ClassVar[str] = "SDB"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SDBSDBFiles0,
        SDBSDBFiles1,
        SDBSDBFilesx642,
        SDBSDBFilesx643,
    ]


class WERWERFiles0(KapeTarget):
    name: ClassVar[str] = "WER Files"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Microsoft\\Windows\\WER\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WERCrashDumps1(KapeTarget):
    name: ClassVar[str] = "Crash Dumps"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\CrashDumps\\")
    file_mask: ClassVar[str] = "*.dmp"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WERCrashDumps2(KapeTarget):
    name: ClassVar[str] = "Crash Dumps"
    base_path: ClassVar[Path] = Path("C:\\Windows\\")
    file_mask: ClassVar[str] = "*.dmp"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WERCrashDumps3(KapeTarget):
    name: ClassVar[str] = "Crash Dumps"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\")
    file_mask: ClassVar[str] = "*.dmp"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WER(KapeTargetConfiguration):
    """
    Author: Troy Larson

    Version: 1.0

    ID: 03106a1c-e1f8-4075-abdb-f9c83078347d

    Windows Error Reporting
    """

    name: ClassVar[str] = "WER"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WERWERFiles0,
        WERCrashDumps1,
        WERCrashDumps2,
        WERCrashDumps3,
    ]
