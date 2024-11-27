"""
Auto-generated classes from the .mkape files for the Antivirus category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class DHParser(KapeModule):
    """
    Author: Jordan Klepser

    Version: 1.1

    ID: 0256a455-1248-4e30-8175-727679189ddd

    Retrieve Defender DetectionHistory threat data into JSON
    """

    name: ClassVar[str] = "DHParser"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class SEPparser(KapeModule):
    """
    Author: Brian Maloney

    Version: 1.1

    ID: 073300a3-2d16-4bf5-b332-b038b571e95f

    Symantec Logs
    """

    name: ClassVar[str] = "SEPparser"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
