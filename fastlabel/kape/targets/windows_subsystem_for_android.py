"""
Auto-generated classes from the .tkape files for the Windows Subsystem for Android category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class WindowsSubsystemforAndroidDiagnosticLogsforWSA0(KapeTarget):
    """
    Filenames should be %timestamp%.log
    """

    name: ClassVar[str] = "Diagnostic Logs for WSA"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\\LocalState\\diagnostics\\logcat\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsSubsystemforAndroidAppdownloadartifactsPNG1(KapeTarget):
    """
    Will provide examiners with indicators of which apps were downloaded
    """

    name: ClassVar[str] = "App download artifacts (PNG)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\\LocalCache\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.png)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsSubsystemforAndroidAppdownloadartifactsICO2(KapeTarget):
    """
    Will provide examiners with indicators of which apps were downloaded WHEN
    since .ico files appear immediately when download of an application
    completes
    """

    name: ClassVar[str] = "App download artifacts (ICO)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\\LocalCache\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.ico)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsSubsystemforAndroidAppcompatdbjson3(KapeTarget):
    """
    Grabs the appcompatdb.json, unknown exactly what this is but further
    relevance could be uncovered after more research is conducted
    """

    name: ClassVar[str] = "Appcompatdb.json"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\\LocalState\\"
    )
    regex: ClassVar[str] = r"(?s:appcompatdb\.json)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsSubsystemforAndroiduserdatavhdx4(KapeTarget):
    """
    Grabs the user's data which appears to be stored in a VHDX
    """

    name: ClassVar[str] = "userdata.vhdx"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\MicrosoftCorporationII.WindowsSubsystemForAndroid_8wekyb3d8bbwe\\LocalCache\\"
    )
    regex: ClassVar[str] = r"(?s:userdata\.vhdx)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsSubsystemforAndroid(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 0e0b5f71-6e93-444e-8109-7a0c902f8361

    Windows Subsystem for Android (WSA)
    """

    name: ClassVar[str] = "WindowsSubsystemforAndroid"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WindowsSubsystemforAndroidDiagnosticLogsforWSA0,
        WindowsSubsystemforAndroidAppdownloadartifactsPNG1,
        WindowsSubsystemforAndroidAppdownloadartifactsICO2,
        WindowsSubsystemforAndroidAppcompatdbjson3,
        WindowsSubsystemforAndroiduserdatavhdx4,
    ]
