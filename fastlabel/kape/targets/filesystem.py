"""
Auto-generated classes from the .tkape files for the FileSystem category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class EverythingVoidToolsEverythingVoidTools0(KapeTarget):
    """
    Copies out Everything.db
    """

    name: ClassVar[str] = "Everything (VoidTools)"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Everything\\")
    file_mask: ClassVar[str] = "Everything.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EverythingVoidToolsEverythingVoidToolsRunHistory1(KapeTarget):
    """
    Copies out a CSV containing the history of items ran from Everything's
    search results window
    """

    name: ClassVar[str] = "Everything (VoidTools) - Run History"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Everything\\"
    )
    file_mask: ClassVar[str] = "Run History.csv"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EverythingVoidToolsEverythingVoidToolsSearchHistory2(KapeTarget):
    """
    Copies out a CSV containing the history of items searched for within
    Everything with timestamps
    """

    name: ClassVar[str] = "Everything (VoidTools) - Search History"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Everything\\"
    )
    file_mask: ClassVar[str] = "Search History.csv"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EverythingVoidToolsEverythingVoidToolsinifile3(KapeTarget):
    """
    Copies out the .ini file for Everything
    """

    name: ClassVar[str] = "Everything (VoidTools) - .ini file"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Everything\\"
    )
    file_mask: ClassVar[str] = "Everything.ini"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EverythingVoidTools(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.2

    ID: d63046dd-1d8c-4f4f-acd0-4c1ea3415b0f

    Everything (VoidTools)
    """

    name: ClassVar[str] = "Everything (VoidTools)"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        EverythingVoidToolsEverythingVoidTools0,
        EverythingVoidToolsEverythingVoidToolsRunHistory1,
        EverythingVoidToolsEverythingVoidToolsSearchHistory2,
        EverythingVoidToolsEverythingVoidToolsinifile3,
    ]


class FileSystemMFT0(KapeTarget):
    name: ClassVar[str] = "$MFT"
    base_path: ClassVar[Path] = Path("$MFT.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileSystemLogFile1(KapeTarget):
    name: ClassVar[str] = "$LogFile"
    base_path: ClassVar[Path] = Path("$LogFile.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileSystemJ2(KapeTarget):
    name: ClassVar[str] = "$J"
    base_path: ClassVar[Path] = Path("$J.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileSystemSDS3(KapeTarget):
    name: ClassVar[str] = "$SDS"
    base_path: ClassVar[Path] = Path("$SDS.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileSystemBoot4(KapeTarget):
    name: ClassVar[str] = "$Boot"
    base_path: ClassVar[Path] = Path("$Boot.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileSystemT5(KapeTarget):
    name: ClassVar[str] = "$T"
    base_path: ClassVar[Path] = Path("$T.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileSystem(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 2bd97ef7-5fbf-4427-8ca2-ffb15d545b00

    File system metadata
    """

    name: ClassVar[str] = "FileSystem"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        FileSystemMFT0,
        FileSystemLogFile1,
        FileSystemJ2,
        FileSystemSDS3,
        FileSystemBoot4,
        FileSystemT5,
    ]


class BootBoot0(KapeTarget):
    name: ClassVar[str] = "$Boot"
    base_path: ClassVar[Path] = Path("C:\\")
    file_mask: ClassVar[str] = "$Boot"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Boot(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 9f24d727-fcf0-492d-97cc-108472eb4e00

    $Boot
    """

    name: ClassVar[str] = "$Boot"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [BootBoot0]


class JJ0(KapeTarget):
    name: ClassVar[str] = "$J"
    base_path: ClassVar[Path] = Path("C:\\$Extend\\")
    file_mask: ClassVar[str] = "$UsnJrnl:$J"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JMax1(KapeTarget):
    name: ClassVar[str] = "$Max"
    base_path: ClassVar[Path] = Path("C:\\$Extend\\")
    file_mask: ClassVar[str] = "$UsnJrnl:$Max"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JJ2(KapeTarget):
    """
    This is for the use case when you're running this Target against a mounted
    VHDX with these files already pulled from a live system. The above Targets
    are looking for the files as an ADS whereas once they are already pulled
    they no longer match the ADS criteria and therefore are missed
    """

    name: ClassVar[str] = "$J"
    base_path: ClassVar[Path] = Path("C:\\$Extend\\")
    file_mask: ClassVar[str] = "$J"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JMax3(KapeTarget):
    """
    This is for the use case when you're running this Target against a mounted
    VHDX with these files already pulled from a live system. The above Targets
    are looking for the files as an ADS whereas once they are already pulled
    they no longer match the ADS criteria and therefore are missed
    """

    name: ClassVar[str] = "$Max"
    base_path: ClassVar[Path] = Path("C:\\$Extend\\")
    file_mask: ClassVar[str] = "$Max"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class J(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman and Andrew Rathbun

    Version: 1.1

    ID: 2a9c6f80-250b-42a6-9d29-90cb0a20f7be

    $J
    """

    name: ClassVar[str] = "$J"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [JJ0, JMax1, JJ2, JMax3]


class LogFileLogFile0(KapeTarget):
    name: ClassVar[str] = "$LogFile"
    base_path: ClassVar[Path] = Path("C:\\")
    file_mask: ClassVar[str] = "$LogFile"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LogFile(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: b98612e0-f679-400a-954f-c0b2bc86147b

    $LogFile
    """

    name: ClassVar[str] = "$LogFile"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [LogFileLogFile0]


class MFTMFT0(KapeTarget):
    name: ClassVar[str] = "$MFT"
    base_path: ClassVar[Path] = Path("C:\\")
    file_mask: ClassVar[str] = "$MFT"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MFT(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 2b3d01e2-25e1-4079-a630-6cb6e2069456

    $MFT
    """

    name: ClassVar[str] = "$MFT"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [MFTMFT0]


class MFTMirrMFTMirr0(KapeTarget):
    """
    $MFTMirr is a redundant copy of the first four (4) records of the MFT.
    """

    name: ClassVar[str] = "$MFTMirr"
    base_path: ClassVar[Path] = Path("C:\\")
    file_mask: ClassVar[str] = "$MFTMirr"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MFTMirr(KapeTargetConfiguration):
    """
    Author: Teo Kia Meng

    Version: 1.0

    ID: 8fce369c-a773-41c4-8ca3-ba9df1f72ba0

    $MFTMirr
    """

    name: ClassVar[str] = "$MFTMirr"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [MFTMirrMFTMirr0]


class SDSSDS0(KapeTarget):
    name: ClassVar[str] = "$SDS"
    base_path: ClassVar[Path] = Path("C:\\")
    file_mask: ClassVar[str] = "$Secure:$SDS"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SDSSDS1(KapeTarget):
    """
    This is for the use case when you're running this Target against a mounted
    VHDX with these files already pulled from a live system. The above Target is
    looking for the files as an ADS whereas once they are already pulled they no
    longer match the ADS criteria and therefore are missed
    """

    name: ClassVar[str] = "$SDS"
    base_path: ClassVar[Path] = Path("C:\\")
    file_mask: ClassVar[str] = "$Secure_$SDS"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SDS(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman and Andrew Rathbun

    Version: 1.1

    ID: 72d56db2-b8da-4830-a2e7-37437c90e18f

    $SDS
    """

    name: ClassVar[str] = "$SDS"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [SDSSDS0, SDSSDS1]


class TT0(KapeTarget):
    name: ClassVar[str] = "$T"
    base_path: ClassVar[Path] = Path("C:\\$Extend\\$RmMetadata\\$TxfLog\\")
    file_mask: ClassVar[str] = "$Tops:$T"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TT1(KapeTarget):
    """
    This is for the use case when you're running this Target against a mounted
    VHDX with these files already pulled from a live system. The above Target is
    looking for the files as an ADS whereas once they are already pulled they no
    longer match the ADS criteria and therefore are missed
    """

    name: ClassVar[str] = "$T"
    base_path: ClassVar[Path] = Path("C:\\$Extend\\$RmMetadata\\$TxfLog\\")
    file_mask: ClassVar[str] = "$T"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class T(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman and Andrew Rathbun

    Version: 1.1

    ID: 8c568aa0-9a67-4035-9720-1423770bc29a

    $T
    """

    name: ClassVar[str] = "$T"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [TT0, TT1]


class RDPCacheRDPCacheFiles0(KapeTarget):
    name: ClassVar[str] = "RDP Cache Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Terminal Server Client\\Cache\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RDPCacheWindowsoldRDPCacheFiles1(KapeTarget):
    name: ClassVar[str] = "Windows.old RDP Cache Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Users\\%user%\\AppData\\Local\\Microsoft\\Terminal Server Client\\Cache\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RDPCacheRDPCacheFiles2(KapeTarget):
    name: ClassVar[str] = "RDP Cache Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Microsoft\\Terminal Server Client\\Cache\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RDPCache(KapeTargetConfiguration):
    """
    Author: Hadar Yudovich

    Version: 1.1

    ID: 527a5de1-fb71-4efd-9701-89a30ea908e3

    RDP Cache Files
    """

    name: ClassVar[str] = "RDPCache"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RDPCacheRDPCacheFiles0,
        RDPCacheWindowsoldRDPCacheFiles1,
        RDPCacheRDPCacheFiles2,
    ]
