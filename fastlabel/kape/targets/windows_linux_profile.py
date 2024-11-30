"""
Auto-generated classes from the .tkape files for the Windows Linux Profile category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class LinuxOnWindowsProfileFilesbashhistory0(KapeTarget):
    name: ClassVar[str] = ".bash_history"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\*\\LocalState\\rootfs\\home\\*\\"
    )
    file_mask: ClassVar[str] = ".bash_history"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LinuxOnWindowsProfileFilesbashlogout1(KapeTarget):
    name: ClassVar[str] = ".bash_logout"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\*\\LocalState\\rootfs\\home\\*\\"
    )
    file_mask: ClassVar[str] = ".bash_logout"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LinuxOnWindowsProfileFilesbashrc2(KapeTarget):
    name: ClassVar[str] = ".bashrc"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\*\\LocalState\\rootfs\\home\\*\\"
    )
    file_mask: ClassVar[str] = ".bashrc"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LinuxOnWindowsProfileFilesprofile3(KapeTarget):
    name: ClassVar[str] = ".profile"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\*\\LocalState\\rootfs\\home\\*\\"
    )
    file_mask: ClassVar[str] = ".profile"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LinuxOnWindowsProfileFiles(KapeTargetConfiguration):
    """
    Author: Troy Larson

    Version: 1.0

    ID: 9718a129-21f9-4354-a06f-2eddb112ab03

    Linux on Windows Profile Files
    """

    name: ClassVar[str] = "LinuxOnWindowsProfileFiles"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        LinuxOnWindowsProfileFilesbashhistory0,
        LinuxOnWindowsProfileFilesbashlogout1,
        LinuxOnWindowsProfileFilesbashrc2,
        LinuxOnWindowsProfileFilesprofile3,
    ]
