"""
Auto-generated classes from the .mkape files for the SUMDatabase category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class SumECmd(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: ac99af84-33b7-4f85-a9fa-146cd2fd6e31

    SumECmd: Process Microsoft User Access Logs
    """

    name: ClassVar[str] = "SumECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
