"""
Auto-generated classes from the .mkape files for the AccountUsage category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class LogParserLogonLogoffEvents(KapeModule):
    """
    Author: Brian Maloney (idea by @0x47617279)

    Version: 1.1

    ID: 659a8666-4e35-436e-8a6f-69814ec4bfbe

    LogParser Security events
    4624,4625,4634,4647,4648,4772,4778,4779,4800,4801,4802,4803
    """

    name: ClassVar[str] = "LogParser_LogonLogoffEvents"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
