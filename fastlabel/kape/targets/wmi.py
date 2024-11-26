"""
Auto-generated classes from the .tkape files for the WMI category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class MOFMOFfiles0(KapeTarget):
    name: ClassVar[str] = "MOF files"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.MOF)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MOF(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 4fc9820c-3d30-4a38-2e48-5e0b745a4b0c

    MOF files (WMI)
    """

    name: ClassVar[str] = "MOF"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [MOFMOFfiles0]
