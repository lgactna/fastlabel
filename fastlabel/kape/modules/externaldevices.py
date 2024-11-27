"""
Auto-generated classes from the .mkape files for the ExternalDevices category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class iTunesBackupReader(KapeModule):
    """
    Author: Jack Farley

    Version: 1.0

    ID: e2dbd037-69b5-476a-bbc6-9bcb737d76d4

    iTunes Backup Reader
    """

    name: ClassVar[str] = "iTunesBackupReader"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.DB]
