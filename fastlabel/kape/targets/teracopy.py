"""
Auto-generated classes from the .tkape files for the TeraCopy category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class TeraCopyTeraCopy0(KapeTarget):
    name: ClassVar[str] = "TeraCopy"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\TeraCopy\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TeraCopy(KapeTargetConfiguration):
    """
    Author: Kevin Pagano

    Version: 1.0

    ID: 111ee9ac-f8b3-4026-a3c9-90f76b6b2cb4

    TeraCopy log history
    """

    name: ClassVar[str] = "TeraCopy"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [TeraCopyTeraCopy0]
