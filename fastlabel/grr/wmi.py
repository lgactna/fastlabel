"""
Auto-generated classes from the YAML declarations in wmi.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class WMIAccountUsersDomain(GRRArtifactBase):
    """
    Fill out user AD domain information based on username.

    We expect this artifact to be collected with WindowsRegistryProfiles to
    supply the rest of the user information. This artifact optimizes retrieval
    of user information by limiting the WMI query to users for which we have a
    username for. Specifically this solves the issue that in a domain setting,
    querying for all users via WMI will give you the list of all local and
    domain accounts which means a large data transfer from an Active Directory
    server. This artifact relies on having the users.username field populated in
    the knowledge base. Unfortunately even limiting by username this query can
    be slow, and this artifact runs it for each user present on the system.

    Reference URLs:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa394507(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "query": "SELECT * FROM Win32_UserAccount WHERE name='%%users.username%%'"
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIAntivirusProduct(GRRArtifactBase):
    """
    Enumerate the registered antivirus.
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "base_object": "winmgmts:\\root\\SecurityCenter2",
                "query": "SELECT * FROM AntivirusProduct",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMICCMRUA(GRRArtifactBase):
    """
    Enumerate instances of CCM_RecentlyUsedApps.

    Reference URLs: https://forensics.wiki/windows#ccm-recentlyusedapps
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "base_object": "winmgmts:\\root\\ccm\\SoftwareMeteringAgent",
                "query": "SELECT * FROM CCM_RecentlyUsedApps",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIComputerSystemProduct(GRRArtifactBase):
    """
    Computer System Product including Identifiying number queried from WMI.

    Reference URLs:
    http://msdn.microsoft.com/en-us/library/aa394105(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {"query": "SELECT * FROM Win32_ComputerSystemProduct"},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIDNSClientCache(GRRArtifactBase):
    """
    DNS client cache via Windows Management Instrumentation (WMI).

    Reference URLs:
    https://docs.microsoft.com/en-us/previous-versions/windows/desktop/dnsclientcimprov/msft-dnsclientcache
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "base_object": "winmgmts:\\root\\StandardCimv2",
                "query": "SELECT * from MSFT_DNSClientCache",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIDrivers(GRRArtifactBase):
    """
    Installed drivers via Windows Management Instrumentation (WMI).
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "query": "SELECT DisplayName, Description, InstallDate, Name, PathName, Status, State, ServiceType from Win32_SystemDriver"
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIEnumerateASEC(GRRArtifactBase):
    """
    Enumerate instances of ActiveScriptEventConsumer.
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "base_object": "winmgmts:\\root\\subscription",
                "query": "SELECT * FROM ActiveScriptEventConsumer",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIEnumerateCLEC(GRRArtifactBase):
    """
    Enumerate instances of CommandLineEventConsumer.
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "base_object": "winmgmts:\\root\\subscription",
                "query": "SELECT * FROM CommandLineEventConsumer",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIHotFixes(GRRArtifactBase):
    """
    Installed hotfixes via Windows Management Instrumentation (WMI).
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {"query": "SELECT * from Win32_QuickFixEngineering"},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIInstalledSoftware(GRRArtifactBase):
    """
    Installed software via Windows Management Instrumentation (WMI).
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "query": "SELECT Name, Vendor, Description, InstallDate, InstallDate2, Version from Win32_Product"
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMILastBootupTime(GRRArtifactBase):
    """
    Last system boot time (UTC) retrieved from WMI.

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/aa394239(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {"query": "SELECT LastBootUpTime FROM Win32_OperatingSystem"},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMILogicalDisks(GRRArtifactBase):
    """
    Disk information via Windows Management Instrumentation (WMI).

    Reference URLs:
    http://msdn.microsoft.com/en-us/library/aa394173(v=vs.85).aspx
    """

    SOURCES = [
        {"type": "WMI", "attributes": {"query": "SELECT * FROM Win32_LogicalDisk"}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMILoggedOnSessions(GRRArtifactBase):
    """
    Logged on users queried from WMI.
    """

    SOURCES = [
        {"type": "WMI", "attributes": {"query": "SELECT * FROM Win32_LogonSession"}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMILoggedOnUsers(GRRArtifactBase):
    """
    Logged on users queried from WMI.
    """

    SOURCES = [
        {"type": "WMI", "attributes": {"query": "SELECT * FROM Win32_LoggedonUser"}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMILoginUsers(GRRArtifactBase):
    """
    Login Users via Windows Management Instrumentation (WMI).

    This WMI query may take a long time to complete when run on a domain and
    will create load on a domain controller.
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "query": 'SELECT * from Win32_GroupUser where Name = "login_users"'
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMINetNeighbors(GRRArtifactBase):
    """
    TCP/IP neighbors via Windows Management Instrumentation (WMI).

    Reference URLs:
    https://docs.microsoft.com/en-us/previous-versions/windows/desktop/nettcpipprov/msft-netneighbor
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "base_object": "winmgmts:\\root\\StandardCimv2",
                "query": "SELECT * from MSFT_NetNeighbor",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMINetTCPConnections(GRRArtifactBase):
    """
    TCP connections via Windows Management Instrumentation (WMI).

    Reference URLs:
    https://docs.microsoft.com/en-us/previous-versions/windows/desktop/nettcpipprov/msft-nettcpconnection
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "base_object": "winmgmts:\\root\\StandardCimv2",
                "query": "SELECT * from MSFT_NetTCPConnection",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMINetUDPEndpoints(GRRArtifactBase):
    """
    UDP endpoints via Windows Management Instrumentation (WMI).

    Reference URLs:
    https://docs.microsoft.com/en-us/previous-versions/windows/desktop/nettcpipprov/msft-netudpendpoint
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "base_object": "winmgmts:\\root\\StandardCimv2",
                "query": "SELECT * from MSFT_NetUDPEndpoint",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIOperatingSystem(GRRArtifactBase):
    """
    Operating system installed on the computer via Windows Management
    Instrumentation (WMI).

    Reference URLs:
    https://docs.microsoft.com/en-us/windows/desktop/cimwin32prov/win32-operatingsystem
    """

    SOURCES = [
        {"type": "WMI", "attributes": {"query": "SELECT * from Win32_OperatingSystem"}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIPhysicalMemory(GRRArtifactBase):
    """
    Physical memory information via Windows Management Instrumentation (WMI).

    Reference URLs:
    http://msdn.microsoft.com/en-us/library/aa394347%28v=vs.85%29.aspx
    """

    SOURCES = [
        {"type": "WMI", "attributes": {"query": "SELECT * from Win32_PhysicalMemory"}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIProcessList(GRRArtifactBase):
    """
    Process listing via Windows Management Instrumentation (WMI).
    """

    SOURCES = [{"type": "WMI", "attributes": {"query": "SELECT * from Win32_Process"}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIProfileUsersHomeDir(GRRArtifactBase):
    """
    Get user homedir from Win32_UserProfile based on a known user's SID.

    This artifact relies on having the SID field users.sid populated in the
    knowledge base. We expect it to be collected with WindowsRegistryProfiles to
    supply the rest of the user information.

    Reference URLs:
    http://msdn.microsoft.com/en-us/library/windows/desktop/ee886409(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "query": "SELECT * FROM Win32_UserProfile WHERE SID='%%users.sid%%'"
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIScheduledTasks(GRRArtifactBase):
    """
    Scheduled tasks that are registered on the computer via Windows Management
    Instrumentation (WMI).

    Reference URLs:
    https://wutils.com/wmi/root/microsoft/windows/taskscheduler/msft_scheduledtask/
    """

    SOURCES = [
        {
            "type": "WMI",
            "attributes": {
                "base_object": "winmgmts:\\root\\Microsoft\\Windows\\TaskScheduler",
                "query": "SELECT * from MSFT_ScheduledTask",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIServices(GRRArtifactBase):
    """
    Services queried from WMI.
    """

    SOURCES = [{"type": "WMI", "attributes": {"query": "SELECT * FROM Win32_Service"}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIStartupCommands(GRRArtifactBase):
    """
    Commands that run automatically when a user logs onto the computer system
    via Windows Management Instrumentation (WMI).

    Reference URLs:
    https://docs.microsoft.com/en-us/windows/desktop/cimwin32prov/win32-startupcommand
    """

    SOURCES = [
        {"type": "WMI", "attributes": {"query": "SELECT * from Win32_StartupCommand"}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIUsers(GRRArtifactBase):
    """
    Users via Windows Management Instrumentation (WMI).

    Note that in a domain setup, this will probably return all users in the
    domain which will be expensive and slow. Consider limiting by SID like
    WMIProfileUsersHomeDir.

    Reference URLs:
    http://msdn.microsoft.com/en-us/library/windows/desktop/aa394507(v=vs.85).aspx
    """

    SOURCES = [
        {"type": "WMI", "attributes": {"query": "SELECT * FROM Win32_UserAccount"}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WMIVolumeShadowCopies(GRRArtifactBase):
    """
    A List of Volume Shadow Copies from WMI.
    """

    SOURCES = [
        {"type": "WMI", "attributes": {"query": "SELECT * FROM Win32_ShadowCopy"}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None
