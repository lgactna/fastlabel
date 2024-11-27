"""
Auto-generated classes from the .mkape files for the DirectoryLister category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class Snap2HTML(KapeModule):
    """
    Author: Dennis Reneau

    Version: 1.0

    ID: 0ca2b18d-b886-497c-a57a-ea4442c878e2

    Directory Lister - HTML Browser
    """

    name: ClassVar[str] = "Snap2HTML"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.HTML]
