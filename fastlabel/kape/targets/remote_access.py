"""
Auto-generated classes from the .tkape files for the Remote Access category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class RemoteUtilitiesappRemoteUtilitiesConnectionLogs0(KapeTarget):
    """
    Includes connection log files
    """

    name: ClassVar[str] = "RemoteUtilities Connection Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Program Files*\\Remote Utilities - Host\\Logs"
    )
    regex: ClassVar[str] = r"(?s:rut_log_.*\.html)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteUtilitiesappRemoteUtilitiesInstallLog1(KapeTarget):
    """
    Includes Install log file
    """

    name: ClassVar[str] = "RemoteUtilities Install Log"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Remote Utilities")
    regex: ClassVar[str] = r"(?s:install\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteUtilitiesapp(KapeTargetConfiguration):
    """
    Author: Ryan McVicar

    Version: 1.0

    ID: 55733479-dd80-4958-a0a8-0d1c1392f494

    Remote Utilities
    """

    name: ClassVar[str] = "RemoteUtilities_app"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RemoteUtilitiesappRemoteUtilitiesConnectionLogs0,
        RemoteUtilitiesappRemoteUtilitiesInstallLog1,
    ]


class UltraviewerUltraViewerLogs0(KapeTarget):
    """
    Includes all files related to UltraViewer chat, connections, and recordings
    """

    name: ClassVar[str] = "UltraViewer Logs"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\UltraViewer")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UltraviewerUltraViewerLogs1(KapeTarget):
    """
    UltraViewer Service log file
    """

    name: ClassVar[str] = "UltraViewer Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Program Files*\\UltraViewer\\UltraViewerService_log.txt"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UltraviewerUltraViewerLogs2(KapeTarget):
    """
    UltraViewer Service level connection log
    """

    name: ClassVar[str] = "UltraViewer Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Program Files*\\UltraViewer\\ConnectionLog.Log"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Ultraviewer(KapeTargetConfiguration):
    """
    Author: Ryan McVicar

    Version: 1.1

    ID: 992869b7-f262-4058-98d4-623ca2383a66

    UltraViewer
    """

    name: ClassVar[str] = "Ultraviewer"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        UltraviewerUltraViewerLogs0,
        UltraviewerUltraViewerLogs1,
        UltraviewerUltraViewerLogs2,
    ]
