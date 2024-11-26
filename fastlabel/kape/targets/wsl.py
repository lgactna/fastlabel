"""
Auto-generated classes from the .tkape files for the WSL category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class WSLDebian0(KapeTarget):
    name: ClassVar[str] = "Debian"
    base_path: ClassVar[Path] = Path("Debian.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WSLUbuntu1(KapeTarget):
    name: ClassVar[str] = "Ubuntu"
    base_path: ClassVar[Path] = Path("Ubuntu.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WSLKali2(KapeTarget):
    name: ClassVar[str] = "Kali"
    base_path: ClassVar[Path] = Path("Kali.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WSLopenSUSE3(KapeTarget):
    name: ClassVar[str] = "openSUSE"
    base_path: ClassVar[Path] = Path("openSUSE.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WSLSUSELinuxEnterpriseServer4(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server"
    base_path: ClassVar[Path] = Path("SUSELinuxEnterpriseServer.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WSL(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 6f1d49c3-e558-4d59-bf33-5ce8bb611102

    All Windows Subsystem for Linux targets
    """

    name: ClassVar[str] = "WSL"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WSLDebian0,
        WSLUbuntu1,
        WSLKali2,
        WSLopenSUSE3,
        WSLSUSELinuxEnterpriseServer4,
    ]
