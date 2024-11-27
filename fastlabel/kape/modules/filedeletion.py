"""
Auto-generated classes from the .mkape files for the FileDeletion category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class RBCmd(KapeModule):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 7ef84a6b-5115-45bb-aa5b-2249a3237e75

    RBCmd: process recycle bin artifacts
    """

    name: ClassVar[str] = "RBCmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
