"""
Auto-generated classes from the .mkape files for the --module category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class KAPEAutomation(KapeModule):
    """
    Author: Brian Maloney

    Version: 1.0

    ID: 06cfa868-31f3-43e9-826a-abd199987770

    Module to run for KAPE automation
    """

    name: ClassVar[str] = "KAPE_Automation"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.NONE]
