"""
Auto-generated classes from the .tkape files for the WBEM category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class WBEMWBEM0(KapeTarget):
    name: ClassVar[str] = "WBEM"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\wbem\\Repository\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WBEMWBEM1(KapeTarget):
    name: ClassVar[str] = "WBEM"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\wbem\\Repository\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WBEM(KapeTargetConfiguration):
    """
    Author: Mark Hallman

    Version: 1.0

    ID: e985f5e3-f951-4e13-8099-a2a6877355cb

    Web-Based Enterprise Management (WBEM)
    """

    name: ClassVar[str] = "WBEM"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [WBEMWBEM0, WBEMWBEM1]
