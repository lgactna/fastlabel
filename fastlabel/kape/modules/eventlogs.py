"""
Auto-generated classes from the .mkape files for the EventLogs category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class WinlogbeatALL(KapeModule):
    """
    Author: Thomas DIOT (Qazeer)

    Version: 1.0

    ID: a059c70b-2615-47ce-a45c-75a377eb4fc7

    Winlogbeat - Parse all EVTX files (and all their events) to JSON.
    """

    name: ClassVar[str] = "Winlogbeat_ALL"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class Hayabusa(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 0976ccf9-b7f8-4e5d-9bf7-96ba3b051db8

    Hayabusa a timeline generator for Windows event logs
    """

    name: ClassVar[str] = "Hayabusa"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]


class Chainsaw(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 2.0

    ID: e5912d52-6b31-4480-9255-8c5433326d85

    Chainsaw - Rapidly Search and Hunt through Windows Event Logs
    """

    name: ClassVar[str] = "Chainsaw"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]


class EvtxHussar(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: baeb5700-a62f-4b8f-b47a-3a9c8545cbe3

    EvtxHussar
    """

    name: ClassVar[str] = "EvtxHussar"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]


class ZircoliteScan(KapeModule):
    """
    Author: Pedro Sanchez Cordero

    Version: 1.0

    ID: c89231d3-ef95-49e8-81b1-01bdc17e46bb

    zircolite - A standalone SIGMA-based detection tool for EVTX, Auditd and
    Sysmon for Linux logs
    """

    name: ClassVar[str] = "Zircolite_Scan"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class ZircoliteUpdate(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 19461b7a-a558-4662-93e6-63e6a126dca9

    zircolite - Update Zircolite rules
    """

    name: ClassVar[str] = "Zircolite_Update"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class NirSoftFullEventLogViewAllEventLogs(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 123e00c7-b7d0-4e48-9a93-6c49c29d6e82

    Parses all event logs using Nirsoft FullEventLogView.exe
    """

    name: ClassVar[str] = "NirSoft_FullEventLogView_AllEventLogs"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class NirSoftFullEventLogViewApplication(KapeModule):
    """
    Author: Barrie Hill

    Version: 1.0

    ID: 505019ce-2fae-4a87-bcf5-cc663c60b030

    Parses Application event log using Nirsoft FullEventLogView.exe
    """

    name: ClassVar[str] = "NirSoft_FullEventLogView_Application"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class NirSoftFullEventLogViewPowerShellOperational(KapeModule):
    """
    Author: Barrie Hill

    Version: 1.0

    ID: 3189c1e4-a76d-4bd6-a16b-a7e7fb821635

    Parses PowerShell-Operational event log using Nirsoft FullEventLogView.exe
    """

    name: ClassVar[str] = "NirSoft_FullEventLogView_PowerShell-Operational"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class NirSoftFullEventLogViewPrintServiceOperational(KapeModule):
    """
    Author: Barrie Hill

    Version: 1.0

    ID: 10c90348-bf0d-436d-815b-e3c63ae6218e

    Parses Microsoft-Windows-PrintService%4Operational event log using Nirsoft
    FullEventLogView.exe
    """

    name: ClassVar[str] = "NirSoft_FullEventLogView_PrintService-Operational"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class NirSoftFullEventLogViewScheduledTasks(KapeModule):
    """
    Author: Hadar Yudovich

    Version: 1.0

    ID: 8e04da5a-7ee4-4ef6-a4e0-4c68aca39af0

    Parses TaskScheduler event log using Nirsoft FullEventLogView.exe
    """

    name: ClassVar[str] = "NirSoft_FullEventLogView_ScheduledTasks"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class NirSoftFullEventLogViewSecurity(KapeModule):
    """
    Author: Barrie Hill

    Version: 1.0

    ID: 6f9da2e0-0c7c-4147-9a02-58622e4c1b34

    Parses Security event log using Nirsoft FullEventLogView.exe
    """

    name: ClassVar[str] = "NirSoft_FullEventLogView_Security"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class NirSoftFullEventLogViewSystem(KapeModule):
    """
    Author: Barrie Hill

    Version: 1.0

    ID: bb628207-56cc-4293-aa6a-2073d406c8cb

    Parses System event log using Nirsoft FullEventLogView.exe
    """

    name: ClassVar[str] = "NirSoft_FullEventLogView_System"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class NirSoftTurnedOnTimesView(KapeModule):
    """
    Author: Thomas DIOT

    Version: 1.0

    ID: 95549abe-f13a-4c8c-bccb-8dbb7fdbe83a

    Uses Nirsoft TurnedOnTimesViewtime to determine time ranges the system was
    turned on
    """

    name: ClassVar[str] = "NirSoft_TurnedOnTimesView"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class hayabusaEventStatistics(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.1

    ID: f3fb3648-1ccb-458c-80e2-261818803bda

    Hayabusa a timeline generator for Windows event logs - Event Statistics
    """

    name: ClassVar[str] = "hayabusa_EventStatistics"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class hayabusaLiveResponse(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.2

    ID: 9696412c-c973-4fd4-a426-06318011b8ba

    Hayabusa a timeline generator for Windows event logs - Live
    """

    name: ClassVar[str] = "hayabusa_LiveResponse"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class hayabusaLogonSummary(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.1

    ID: 2dd36453-d175-4b54-b98f-9cdf492859ce

    Hayabusa a timeline generator for Windows event logs - Logon Summary
    """

    name: ClassVar[str] = "hayabusa_LogonSummary"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class hayabusaOfflineEventLogs(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.2

    ID: 49f9cd2d-3da5-4349-a9aa-c2b450582ccc

    Hayabusa a timeline generator for Windows event logs - Offline
    """

    name: ClassVar[str] = "hayabusa_OfflineEventLogs"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class hayabusaUpdateRules(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: cd547400-e8cb-4339-9a50-818327fe059b

    Hayabusa a timeline generator for Windows event logs - Update Rules
    """

    name: ClassVar[str] = "hayabusa_UpdateRules"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.NONE]


class EvtxECmd(KapeModule):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 1b66f0e2-2ccf-467d-ae15-a2b3dc59df08

    EvtxECmd: process event log files
    """

    name: ClassVar[str] = "EvtxECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.XML,
        KapeExportFormat.JSON,
    ]


class EvtxECmdRDP(KapeModule):
    """
    Author: Mark Hallman

    Version: 1.1

    ID: d6ddc918-feb1-47b6-8e51-e9c50936ec75

    EvtxECmd: process RDP-related event log files
    """

    name: ClassVar[str] = "EvtxECmd_RDP"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.XML,
        KapeExportFormat.JSON,
    ]
