"""
Auto-generated classes from the .mkape files for the GitHub category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class BitsParser(KapeModule):
    """
    Author: Pedro Sanchez Cordero (conexioninversa)

    Version: 1.0

    ID: acdc62ed-b1a1-426f-8d5e-e53687284410

    Tool to parse Windows Background Intelligent Transfer Service database files
    """

    name: ClassVar[str] = "BitsParser"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]
