"""
Auto-generated classes from the .mkape files for the SRUMDatabase category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class SrumECmd(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: a0fac3f5-ee99-4973-b3ea-4cffc87da48d

    SrumECmd: SRUM Parser
    """

    name: ClassVar[str] = "SrumECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
