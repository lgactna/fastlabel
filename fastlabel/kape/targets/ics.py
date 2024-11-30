"""
Auto-generated classes from the .tkape files for the ICS category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class SiemensTIASiemensTIASettings0(KapeTarget):
    name: ClassVar[str] = "Siemens TIA Settings"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Siemens\\Automation\\Portal*\\Settings\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SiemensTIA(KapeTargetConfiguration):
    """
    Author: Olaf Schwarz (@b00010111)

    Version: 1.0

    ID: 0e43ebe5-cd5b-4487-ab41-66f46ebfc5c9

    Copy Siemens TIA Settings
    """

    name: ClassVar[str] = "SiemensTIA"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [SiemensTIASiemensTIASettings0]
