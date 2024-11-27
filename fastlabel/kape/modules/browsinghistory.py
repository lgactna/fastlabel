"""
Auto-generated classes from the .mkape files for the BrowsingHistory category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class ObsidianForensicsHindsight(KapeModule):
    """
    Author: Mike Cary

    Version: 1.1

    ID: d9661ea6-3369-41d0-8807-904f00edcbf4

    Hindsight - Chrome browser parsing
    """

    name: ClassVar[str] = "ObsidianForensics_Hindsight"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.XLSX,
        KapeExportFormat.JSON,
    ]


class NirSoftBrowsingHistoryView(KapeModule):
    """
    Author: Mike Cary

    Version: 1.0

    ID: 53d5bea2-b3d3-4a60-8844-be898390adc1

    Browsing History View - Nirsoft
    """

    name: ClassVar[str] = "NirSoft_BrowsingHistoryView"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.HTML,
    ]
