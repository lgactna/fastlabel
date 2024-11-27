"""
Auto-generated classes from the .mkape files for the SRUM category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class PowerShellSrumECmdSRUMRepairAndParse(KapeModule):
    """
    Author: Matthew Arbaugh

    Version: 1.0

    ID: a03a3be0-0101-42cc-a639-484ab24e0018

    Extract SRUM data and repair with SrumECmd
    """

    name: ClassVar[str] = "PowerShell_SrumECmd_SRUM-RepairAndParse"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
