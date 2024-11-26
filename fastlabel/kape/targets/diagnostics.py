"""
Auto-generated classes from the .tkape files for the Diagnostics category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class WindowsPowerDiagnosticsWindowsPowerDiagnostics0(KapeTarget):
    name: ClassVar[str] = "Windows Power Diagnostics"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Microsoft\\Windows\\Power Efficiency Diagnostics"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsPowerDiagnostics(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: eefa0401-8cae-4c65-84f4-c2bffd0805b7

    Windows Power Diagnostics
    """

    name: ClassVar[str] = "WindowsPowerDiagnostics"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WindowsPowerDiagnosticsWindowsPowerDiagnostics0
    ]
