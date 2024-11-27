"""
Auto-generated classes from the .mkape files for the RemoteAccess category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class LogParserDetailedNetworkShareAccess(KapeModule):
    """
    Author: Brian Maloney/@sbousseaden

    Version: 1.0

    ID: 2d3f0292-d302-4d4a-b292-f8fbd58b8498

    LogParser Security event 5145
    """

    name: ClassVar[str] = "LogParser_DetailedNetworkShareAccess"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class LogParserRDPUsageEvents(KapeModule):
    """
    Author: Brian Maloney (idea by @0x47617279), Thomas DIOT (Qazeer)

    Version: 1.1

    ID: 058b60b0-6d1e-4b1b-8426-7418e40b6a4f

    LogParser RDP Usage
    Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational
    21,22,23,24,25,39,40 and
    Microsoft-Windows-TerminalServices-RemoteConnectionManager%4Operational 1149
    """

    name: ClassVar[str] = "LogParser_RDPUsageEvents"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class LogParserSMBServerAnonymousLogons(KapeModule):
    """
    Author: Hadar Yudovich, Thomas DIOT (Qazeer)

    Version: 1.1

    ID: 7f4fed47-cd92-4a94-a2c0-b937ea218bc8

    LogParser Microsoft-Windows-SMBServer-Security event 551
    """

    name: ClassVar[str] = "LogParser_SMBServerAnonymousLogons"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
