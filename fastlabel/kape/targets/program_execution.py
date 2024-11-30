"""
Auto-generated classes from the .tkape files for the Program Execution category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class SyscacheSyscache0(KapeTarget):
    name: ClassVar[str] = "Syscache"
    base_path: ClassVar[Path] = Path("C:\\System Volume Information\\")
    file_mask: ClassVar[str] = "Syscache.hve"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SyscacheSyscachetransactionfiles1(KapeTarget):
    name: ClassVar[str] = "Syscache transaction files"
    base_path: ClassVar[Path] = Path("C:\\System Volume Information\\")
    file_mask: ClassVar[str] = "Syscache.hve.LOG*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Syscache(KapeTargetConfiguration):
    """
    Author: Phill Moore

    Version: 1.0

    ID: d4665b13-9953-4cf0-bdc4-6fcb7a37842f

    syscache.hve
    """

    name: ClassVar[str] = "Syscache"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SyscacheSyscache0,
        SyscacheSyscachetransactionfiles1,
    ]
