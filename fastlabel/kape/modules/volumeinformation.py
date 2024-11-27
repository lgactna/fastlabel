"""
Auto-generated classes from the .mkape files for the VolumeInformation category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class WindowsManageBDEBitLockerKeys(KapeModule):
    """
    Author: troyla@microsoft.com

    Version: 1.1

    ID: d30abed8-35f3-4fb6-ba47-5ffdad46c912

    Collect BitLocker recovery key for a volume
    """

    name: ClassVar[str] = "Windows_ManageBDE_BitLockerKeys"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsManageBDEBitLockerStatus(KapeModule):
    """
    Author: troyla@microsoft.com

    Version: 1.1

    ID: b069705b-13f0-42c7-86a2-4f310c3c651b

    Check for BitLocker volumes
    """

    name: ClassVar[str] = "Windows_ManageBDE_BitLockerStatus"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]
