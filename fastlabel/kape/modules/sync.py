"""
Auto-generated classes from the .mkape files for the Sync category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class ToolSync(KapeModule):
    """
    Author: Andrew Rathbun, Andreas Hunkeler (@Karneades)

    Version: 1.0

    ID: 8d0a44a4-fa8e-443b-8f6e-8711ce2acd12

    Sync for new Maps, Batch Files, Targets and Modules
    """

    name: ClassVar[str] = "!!ToolSync"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]
