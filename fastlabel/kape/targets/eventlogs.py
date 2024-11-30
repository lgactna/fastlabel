"""
Auto-generated classes from the .tkape files for the EventLogs category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class CombinedLogsWindowsEventLogs0(KapeTarget):
    name: ClassVar[str] = "Windows Event Logs"
    base_path: ClassVar[Path] = Path("EventLogs.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CombinedLogsEventTraceLogs1(KapeTarget):
    name: ClassVar[str] = "Event Trace Logs"
    base_path: ClassVar[Path] = Path("EventTraceLogs.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CombinedLogsPowerShellConsoleLog2(KapeTarget):
    name: ClassVar[str] = "PowerShell Console Log"
    base_path: ClassVar[Path] = Path("PowerShellConsole.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CombinedLogsWindowsFirewallLog3(KapeTarget):
    name: ClassVar[str] = "Windows Firewall Log"
    base_path: ClassVar[Path] = Path("WindowsFirewall.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CombinedLogsUSBDevicesLogs4(KapeTarget):
    name: ClassVar[str] = "USBDevicesLogs"
    base_path: ClassVar[Path] = Path("USBDevicesLogs.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CombinedLogs(KapeTargetConfiguration):
    """
    Author: Mike Cary, Mark Hallman added the USBDevicelogs target

    Version: 1.1

    ID: d4fdd600-15b1-4b78-bc77-88e724861d8d

    Collect Event logs, Trace logs, Windows Firewall and PowerShell console
    """

    name: ClassVar[str] = "CombinedLogs"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        CombinedLogsWindowsEventLogs0,
        CombinedLogsEventTraceLogs1,
        CombinedLogsPowerShellConsoleLog2,
        CombinedLogsWindowsFirewallLog3,
        CombinedLogsUSBDevicesLogs4,
    ]


class ApplicationEventsApplicationEventLogXP0(KapeTarget):
    name: ClassVar[str] = "Application Event Log XP"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    file_mask: ClassVar[str] = "AppEvent.evt"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ApplicationEventsApplicationEventLogXP1(KapeTarget):
    name: ClassVar[str] = "Application Event Log XP"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    file_mask: ClassVar[str] = "AppEvent.evt"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ApplicationEventsApplicationEventLogWin72(KapeTarget):
    name: ClassVar[str] = "Application Event Log Win7+"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\winevt\\logs\\")
    file_mask: ClassVar[str] = "application.evtx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ApplicationEventsApplicationEventLogWin73(KapeTarget):
    name: ClassVar[str] = "Application Event Log Win7+"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\winevt\\logs\\"
    )
    file_mask: ClassVar[str] = "application.evtx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ApplicationEvents(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: 2da16dbf-ea47-448e-a00f-fc442c3109ba

    Windows Application Event Log
    """

    name: ClassVar[str] = "ApplicationEvents"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ApplicationEventsApplicationEventLogXP0,
        ApplicationEventsApplicationEventLogXP1,
        ApplicationEventsApplicationEventLogWin72,
        ApplicationEventsApplicationEventLogWin73,
    ]


class EventLogsRDPEventlogsWin70(KapeTarget):
    name: ClassVar[str] = "Event logs Win7+"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\winevt\\logs\\")
    file_mask: ClassVar[str] = "System.evtx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventLogsRDPEventlogsWin71(KapeTarget):
    name: ClassVar[str] = "Event logs Win7+"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\winevt\\logs\\"
    )
    file_mask: ClassVar[str] = "System.evtx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventLogsRDPEventlogsWin72(KapeTarget):
    name: ClassVar[str] = "Event logs Win7+"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\winevt\\logs\\")
    file_mask: ClassVar[str] = "Security.evtx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventLogsRDPEventlogsWin73(KapeTarget):
    name: ClassVar[str] = "Event logs Win7+"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\winevt\\logs\\"
    )
    file_mask: ClassVar[str] = "Security.evtx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventLogsRDPEventlogsWin74(KapeTarget):
    name: ClassVar[str] = "Event logs Win7+"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx"
    )
    file_mask: ClassVar[str] = (
        "Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx"
    )
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventLogsRDPEventlogsWin75(KapeTarget):
    name: ClassVar[str] = "Event logs Win7+"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\winevt\\Logs\\")
    file_mask: ClassVar[str] = (
        "Microsoft-Windows-TerminalServices-RemoteConnectionManager%4Operational.evtx"
    )
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventLogsRDP(KapeTargetConfiguration):
    """
    Author: Mark Hallman

    Version: 1.0

    ID: 2e79fc64-816c-439a-8b7f-93dd59bf2711

    Collect Win7+ RDP related Event logs
    """

    name: ClassVar[str] = "EventLogs-RDP"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        EventLogsRDPEventlogsWin70,
        EventLogsRDPEventlogsWin71,
        EventLogsRDPEventlogsWin72,
        EventLogsRDPEventlogsWin73,
        EventLogsRDPEventlogsWin74,
        EventLogsRDPEventlogsWin75,
    ]


class EventLogsEventlogsXP0(KapeTarget):
    name: ClassVar[str] = "Event logs XP"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    file_mask: ClassVar[str] = "*.evt"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventLogsEventlogsWin71(KapeTarget):
    name: ClassVar[str] = "Event logs Win7+"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\winevt\\logs\\")
    file_mask: ClassVar[str] = "*.evtx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventLogsEventlogsWin72(KapeTarget):
    name: ClassVar[str] = "Event logs Win7+"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\winevt\\logs\\"
    )
    file_mask: ClassVar[str] = "*.evtx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventLogs(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: d95784d9-bd1c-472b-aeef-de5d9ecc7aaa

    Event logs
    """

    name: ClassVar[str] = "EventLogs"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        EventLogsEventlogsXP0,
        EventLogsEventlogsWin71,
        EventLogsEventlogsWin72,
    ]


class RDPLogsRemoteConnectionManagerEventLogs0(KapeTarget):
    name: ClassVar[str] = "RemoteConnectionManager Event Logs"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\winevt\\logs\\")
    file_mask: ClassVar[str] = (
        "Microsoft-Windows-TerminalServices-RemoteConnectionManager*"
    )
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RDPLogsRemoteConnectionManagerEventLogs1(KapeTarget):
    name: ClassVar[str] = "RemoteConnectionManager Event Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\winevt\\logs\\"
    )
    file_mask: ClassVar[str] = (
        "Microsoft-Windows-TerminalServices-RemoteConnectionManager*"
    )
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RDPLogsLocalSessionManagerEventLogs2(KapeTarget):
    name: ClassVar[str] = "LocalSessionManager Event Logs"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\winevt\\logs\\")
    file_mask: ClassVar[str] = "Microsoft-Windows-TerminalServices-LocalSessionManager*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RDPLogsLocalSessionManagerEventLogs3(KapeTarget):
    name: ClassVar[str] = "LocalSessionManager Event Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\winevt\\logs\\"
    )
    file_mask: ClassVar[str] = "Microsoft-Windows-TerminalServices-LocalSessionManager*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RDPLogsRDPClientEventLogs4(KapeTarget):
    name: ClassVar[str] = "RDPClient Event Logs"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\winevt\\logs\\")
    file_mask: ClassVar[str] = "Microsoft-Windows-TerminalServices-RDPClient*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RDPLogsRDPClientEventLogs5(KapeTarget):
    name: ClassVar[str] = "RDPClient Event Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\winevt\\logs\\"
    )
    file_mask: ClassVar[str] = "Microsoft-Windows-TerminalServices-RDPClient*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RDPLogsRDPCoreTSEventLogs6(KapeTarget):
    """
    Can be used to correlate RDP logon failures by originating IP
    """

    name: ClassVar[str] = "RDPCoreTS Event Logs"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\winevt\\logs\\")
    file_mask: ClassVar[str] = "Microsoft-Windows-RemoteDesktopServices-RdpCoreTS*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RDPLogsRDPCoreTSEventLogs7(KapeTarget):
    """
    Can be used to correlate RDP logon failures by originating IP
    """

    name: ClassVar[str] = "RDPCoreTS Event Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\winevt\\logs\\"
    )
    file_mask: ClassVar[str] = "Microsoft-Windows-RemoteDesktopServices-RdpCoreTS*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RDPLogs(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: 6fa6ac8c-d940-4658-9c61-fdad4cf6416b

    RDP Logs
    """

    name: ClassVar[str] = "RDPLogs"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RDPLogsRemoteConnectionManagerEventLogs0,
        RDPLogsRemoteConnectionManagerEventLogs1,
        RDPLogsLocalSessionManagerEventLogs2,
        RDPLogsLocalSessionManagerEventLogs3,
        RDPLogsRDPClientEventLogs4,
        RDPLogsRDPClientEventLogs5,
        RDPLogsRDPCoreTSEventLogs6,
        RDPLogsRDPCoreTSEventLogs7,
    ]
