"""
Auto-generated classes from the .mkape files for the SystemActivity category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class PowerShellGetDoSvc4n6(KapeModule):
    """
    Author: Gabriele Zambelli

    Version: 1.3

    ID: fc01eeb0-2e2d-4fbe-96b8-02a64933d466

    Get-DoSvc4n6: extracts (amongst others) public IP addresses from DoSvc
    EventTraceLogs
    """

    name: ClassVar[str] = "PowerShell_Get-DoSvc4n6"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class SRUMDump(KapeModule):
    """
    Author: Brian Maloney, Jay Houlden

    Version: 1.1

    ID: 8e0a2314-79e4-48f2-81ad-a0719e8af680

    SRUM-dump: Dump contents of the SRUM database
    """

    name: ClassVar[str] = "SRUMDump"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class TZWorksevtwalk64EventLogsScheduledTasks(KapeModule):
    """
    Author: Justin Price

    Version: 1.0

    ID: 5875f69b-4de1-418b-b306-db49b9fc0072

    Parses TaskScheduler-Operational event log using TZWorks evtwalk64
    """

    name: ClassVar[str] = "TZWorks_evtwalk64_EventLogs_ScheduledTasks"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
