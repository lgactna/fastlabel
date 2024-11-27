"""
Auto-generated classes from the .mkape files for the SUM category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class PowerShellSumECmdSUMRepairAndParse(KapeModule):
    """
    Author: Matthew Arbaugh

    Version: 1.0

    ID: 92cc0f6c-4e41-4b1f-b250-4b016724f1c8

    Extract SUM data and repair with SumECmd
    """

    name: ClassVar[str] = "PowerShell_SumECmd_SUM-RepairAndParse"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
