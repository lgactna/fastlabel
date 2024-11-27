"""
Auto-generated classes from the .mkape files for the ExifData category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class ExifTool(KapeModule):
    """
    Author: Lee Whitfield/esecrpm

    Version: 1.1

    ID: 75c32df2-8dad-4bbc-9230-2c3749fd6e2a

    Exiftool: process files
    """

    name: ClassVar[str] = "ExifTool"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
