"""
Auto-generated classes from the .tkape files for the FTP category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class FTPClientsFileZillaClient0(KapeTarget):
    name: ClassVar[str] = "FileZilla Client"
    base_path: ClassVar[Path] = Path("FileZillaClient.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FTPClientsFileZillaServer1(KapeTarget):
    name: ClassVar[str] = "FileZilla Server"
    base_path: ClassVar[Path] = Path("FileZillaServer.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FTPClientsWinSCP2(KapeTarget):
    name: ClassVar[str] = "WinSCP"
    base_path: ClassVar[Path] = Path("WinSCP.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FTPClients(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: b1f3e04d-6525-4a1a-9e19-82300ec1e3b7

    FTP Clients
    """

    name: ClassVar[str] = "FTPClients"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        FTPClientsFileZillaClient0,
        FTPClientsFileZillaServer1,
        FTPClientsWinSCP2,
    ]
