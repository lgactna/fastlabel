"""
Auto-generated classes from the .mkape files for the Remote Access category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class BMCToolsRDPBitmapCacheParser(KapeModule):
    """
    Author: dingtoffee

    Version: 1.1

    ID: fcb0083d-11d7-4305-9577-2379cd243bd0

    BMC-Tools: RDP Bitmap Cache parser
    """

    name: ClassVar[str] = "BMC-Tools_RDPBitmapCacheParser"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.NONE]
