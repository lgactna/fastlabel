"""
Auto-generated classes from the .mkape files for the WMI category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class WMIParser(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: ab1d6a09-450a-464a-aebc-7f415035404d

    WMI-Parser - parses the WMI object database looking for persistence
    """

    name: ClassVar[str] = "WMI-Parser"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.NONE]
