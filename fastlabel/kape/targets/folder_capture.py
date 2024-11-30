"""
Auto-generated classes from the .tkape files for the Folder capture category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class XPRestorePointsSystemVolumeInformation0(KapeTarget):
    name: ClassVar[str] = "System Volume Information"
    base_path: ClassVar[Path] = Path("C:\\System Volume Information\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class XPRestorePoints(KapeTargetConfiguration):
    """
    Author: Phill Moore

    Version: 1.0

    ID: 07f57a75-f9d9-42f3-842c-bd7e5abbb569

    XP Restore Points - System Volume Information directory
    """

    name: ClassVar[str] = "XPRestorePoints"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        XPRestorePointsSystemVolumeInformation0
    ]
