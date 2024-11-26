"""
Auto-generated classes from the .tkape files for the FileKnowledge category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class IrfanViewIrfanViewConfigurationFile0(KapeTarget):
    name: ClassVar[str] = "IrfanView Configuration File"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\IrfanView\\")
    regex: ClassVar[str] = r"(?s:i_view32\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class IrfanView(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 20c9d7ae-4efc-4eb0-b1c5-99504e1f6aac

    IrfanView
    """

    name: ClassVar[str] = "IrfanView"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [IrfanViewIrfanViewConfigurationFile0]


class PeaZipPeaZipConfigurationFiles0(KapeTarget):
    name: ClassVar[str] = "PeaZip Configuration Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\PeaZip\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class PeaZip(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 38efad53-1899-4b73-8a07-e8d12712f579

    PeaZip
    """

    name: ClassVar[str] = "PeaZip"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [PeaZipPeaZipConfigurationFiles0]


class SumatraPDFSumatraPDFSettingsSessionData0(KapeTarget):
    """
    Settings file which contains information about previous user session
    """

    name: ClassVar[str] = "SumatraPDF Settings - SessionData"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\SumatraPDF")
    regex: ClassVar[str] = r"(?s:SumatraPDF\-settings\.txt)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SumatraPDFSumatraPDFCache1(KapeTarget):
    """
    Folder contains a PNG snapshot of each PDF file the user had open at the
    time of last application close
    """

    name: ClassVar[str] = "SumatraPDF Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\SumatraPDF\\sumatrapdfcache"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SumatraPDF(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: c3a2d097-bca5-4ebe-83b2-db509c86883f

    SumatraPDF
    """

    name: ClassVar[str] = "SumatraPDF"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SumatraPDFSumatraPDFSettingsSessionData0,
        SumatraPDFSumatraPDFCache1,
    ]


class CertUtilSystemCryptnetUrlCache0(KapeTarget):
    name: ClassVar[str] = "System CryptnetUrlCache"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows\\System32\\config\\systemprofile\\AppData\\LocalLow\\Microsoft\\CryptnetUrlCache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CertUtilUserCryptnetUrlCache1(KapeTarget):
    name: ClassVar[str] = "User CryptnetUrlCache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\LocalLow\\Microsoft\\CryptnetUrlCache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CertUtilINetCache2(KapeTarget):
    name: ClassVar[str] = "INetCache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CertUtil(KapeTargetConfiguration):
    """
    Author: NVISO (@NVISOsecurity)

    Version: 1.0

    ID: ec903d15-64b5-4484-8786-94b2ad90bfb7

    Certutil
    """

    name: ClassVar[str] = "CertUtil"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        CertUtilSystemCryptnetUrlCache0,
        CertUtilUserCryptnetUrlCache1,
        CertUtilINetCache2,
    ]


class OfficeAutosaveWordAutosaveLocation0(KapeTarget):
    name: ClassVar[str] = "Word Autosave Location"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Word\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OfficeAutosaveExcelAutosaveLocation1(KapeTarget):
    name: ClassVar[str] = "Excel Autosave Location"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Excel\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OfficeAutosavePowerpointAutosaveLocation2(KapeTarget):
    name: ClassVar[str] = "Powerpoint Autosave Location"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Powerpoint\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OfficeAutosavePublisherAutosaveLocation3(KapeTarget):
    name: ClassVar[str] = "Publisher Autosave Location"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Publisher\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OfficeAutosave(KapeTargetConfiguration):
    """
    Author: Russ Taylor

    Version: 1.0

    ID: 71f1efe7-37be-4285-9896-11f0f6be2770

    Office Autosave
    """

    name: ClassVar[str] = "OfficeAutosave"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        OfficeAutosaveWordAutosaveLocation0,
        OfficeAutosaveExcelAutosaveLocation1,
        OfficeAutosavePowerpointAutosaveLocation2,
        OfficeAutosavePublisherAutosaveLocation3,
    ]


class OfficeDocumentCacheOfficeDocumentCache0(KapeTarget):
    name: ClassVar[str] = "Office Document Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Office\\*\\OfficeFileCache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OfficeDocumentCache(KapeTargetConfiguration):
    """
    Author: Banaanhangwagen

    Version: 1.0

    ID: 15e92d9c-b02d-4cdf-a86e-bafb3d25af5c

    Office Document Cache
    """

    name: ClassVar[str] = "OfficeDocumentCache"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        OfficeDocumentCacheOfficeDocumentCache0
    ]


class SnipAndSketchSnipSketch0(KapeTarget):
    """
    Pulls all temporary .png images generated by the Snip & Sketch screen
    capture tool built into Windows
    """

    name: ClassVar[str] = "Snip & Sketch"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\*\\AppData\\Local\\Packages\\Microsoft.ScreenSketch_8wekyb3d8bbwe\\TempState\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.png)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SnipAndSketch(KapeTargetConfiguration):
    """
    Author: Kevin Pagano

    Version: 1.0

    ID: b881c3bb-58b1-4e63-be1a-8159794e5a4b

    Snip & Sketch Cached Images
    """

    name: ClassVar[str] = "SnipAndSketch"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [SnipAndSketchSnipSketch0]


class ThumbCacheThumbcacheDB0(KapeTarget):
    name: ClassVar[str] = "Thumbcache DB"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\Explorer\\"
    )
    regex: ClassVar[str] = r"(?s:thumbcache_.*\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ThumbCache(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 1eec8849-b6eb-475b-a700-f4fb0055356d

    Thumbcache DB
    """

    name: ClassVar[str] = "ThumbCache"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [ThumbCacheThumbcacheDB0]


class WindowsIndexSearchWindowsIndexSearch0(KapeTarget):
    name: ClassVar[str] = "WindowsIndexSearch"
    base_path: ClassVar[Path] = Path(
        "C:\\programdata\\microsoft\\search\\data\\applications\\windows\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsIndexSearchGatherLogs1(KapeTarget):
    name: ClassVar[str] = "GatherLogs"
    base_path: ClassVar[Path] = Path(
        "C:\\programdata\\microsoft\\search\\data\\applications\\windows\\GatherLogs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsIndexSearch(KapeTargetConfiguration):
    """
    Author: Mark Hallman

    Version: 1.1

    ID: 9828b927-f955-464a-80fb-a48ce0101236

    Windows Index Search
    """

    name: ClassVar[str] = "WindowsIndexSearch"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WindowsIndexSearchWindowsIndexSearch0,
        WindowsIndexSearchGatherLogs1,
    ]
