"""
Auto-generated classes from the .tkape files for the Nessus category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class NessusNessusLogs0(KapeTarget):
    name: ClassVar[str] = "Nessus Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Tenable\\Nessus\\conf")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NessusNessusLogs1(KapeTarget):
    name: ClassVar[str] = "Nessus Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Tenable\\Nessus\\nessus\\logs\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Nessus(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: eceacdb8-28ac-4ddd-8214-a52deee12c7f

    Nessus
    """

    name: ClassVar[str] = "Nessus"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [NessusNessusLogs0, NessusNessusLogs1]
