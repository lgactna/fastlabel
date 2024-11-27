"""
Auto-generated classes from the .mkape files for the Webservers category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class LogParserApacheAccessLogs(KapeModule):
    """
    Author: Hadar Yudovich

    Version: 1.0

    ID: 631ac549-9ddf-48ea-b95b-ca4678230df6

    LogParser Apache Access Log
    """

    name: ClassVar[str] = "LogParser_ApacheAccessLogs"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
