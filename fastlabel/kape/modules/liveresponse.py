"""
Auto-generated classes from the .mkape files for the LiveResponse category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class CrowdStrikeCrowdResponse(KapeModule):
    """
    Author: Mohamed El-Hadidi, Georg Lauenstein

    Version: 1.0

    ID: e137a1ed-5bfd-4ca3-9df1-c1d35624cbb2

    CrowdResponse is a lightweight Windows console application designed to aid
    in the gathering of system information for incident response and security
    engagements
    """

    name: ClassVar[str] = "CrowdStrike_CrowdResponse"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class KasperskyTDSSKiller(KapeModule):
    """
    Author: Mohamed El-Hadidi

    Version: 1.0

    ID: 38be1e67-e028-4bc0-ac50-376b7875be08

    Shows if the system have either rootkits or bootkits, TDSSKiller tool for
    detecting and removing rootkits and bootkits
    """

    name: ClassVar[str] = "Kaspersky_TDSSKiller"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class MagnetForensicsEDD(KapeModule):
    """
    Author: Mohamed El-Hadidi

    Version: 1.1

    ID: c7212da1-ed41-4560-95f7-1a2d99acc1f8

    Checks the local physical drives on a system for TrueCrypt, PGP, VeraCrypt,
    SafeBoot, or Bitlocker encrypted volumes
    """

    name: ClassVar[str] = "MagnetForensics_EDD"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class McAfeeStinger(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: c49d14fe-5b77-46d9-a058-ab90d5cc2edd

    McAfeeStinger scanner
    """

    name: ClassVar[str] = "McAfeeStinger"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.HTML]


class PowerShelllog4j(KapeModule):
    """
    Author: Jochen Meyer, Georg Lauenstein

    Version: 1.0

    ID: 94c6d3c1-25bc-4948-b626-f5f455f56b6a

    Find every Folder related to log4j core .jar extensions
    """

    name: ClassVar[str] = "PowerShell_log4j"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class LiveResponseNetSystemInfo(KapeModule):
    """
    Author: piesecurity, Andreas Hunkeler (@Karneades)

    Version: 1.1

    ID: be86ac26-4eea-4bcb-b5ae-9686ad0557c4

    Gathers Basic System Information Using the Net Command
    """

    name: ClassVar[str] = "LiveResponse_NetSystemInfo"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]


class LiveResponseNetworkDetails(KapeModule):
    """
    Author: Mike Cary

    Version: 1.0

    ID: 77b87364-39b1-46ff-b355-3d6fa8da9560

    Network Details
    """

    name: ClassVar[str] = "LiveResponse_NetworkDetails"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]


class LiveResponseProcessDetails(KapeModule):
    """
    Author: piesecurity

    Version: 1.0

    ID: 337a4733-5549-4d3e-818e-8c4c6b0381de

    Combination Module for LiveResponse. Gathering Running Process Details
    """

    name: ClassVar[str] = "LiveResponse_ProcessDetails"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]


class PowerShellDefenderExclusions(KapeModule):
    """
    Author: nov3mb3r

    Version: 1.0

    ID: 5a9ce674-0d3c-4c9a-9f53-d0130bb4aafb

    Windows Defender Exclusions
    """

    name: ClassVar[str] = "PowerShell_Defender_Exclusions"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class PowerShellDLLList(KapeModule):
    """
    Author: nov3mb3r

    Version: 1.0

    ID: 19e6448f-f94b-49a4-bc16-26080b7c0592

    DLL List
    """

    name: ClassVar[str] = "PowerShell_DLL_List"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class PowerShellNamedPipes(KapeModule):
    """
    Author: nov3mb3r

    Version: 1.0

    ID: f1f5f93d-d03b-45f4-bf72-7b8f9dc7ac23

    Named Pipes List
    """

    name: ClassVar[str] = "PowerShell_NamedPipes"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class PowerShellNetUserAdministrators(KapeModule):
    """
    Author: Andreas Hunkeler (@Karneades)

    Version: 1.0

    ID: 730cf14e-2680-447f-9853-e79ad3aa0e65

    Gathers Basic System Information Using the Net Command (members of local
    administrator group)
    """

    name: ClassVar[str] = "PowerShell_NetUserAdministrators"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class PowerShellParseScheduledTasks(KapeModule):
    """
    Author: Vikas Singh(@vikas891)

    Version: 1.0

    ID: ed6df81d-a90a-44ca-b322-1e02e72342dc

    Scheduled Task XMLs Parser
    """

    name: ClassVar[str] = "PowerShell_ParseScheduledTasks"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class PowerShellProcessListCimInstance(KapeModule):
    """
    Author: Markus Neis, Swisscom

    Version: 1.0

    ID: f5afb643-3a77-4e3e-a028-18cbeaf5c406

    Display running processes and context information
    """

    name: ClassVar[str] = "PowerShell_ProcessList_CimInstance"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]


class PowerShellProcessListWMI(KapeModule):
    """
    Author: piesecurity

    Version: 1.0

    ID: d9bf9198-72e4-4f01-8ec9-e8ec4e322c06

    Display a running process list with a variety of fields
    """

    name: ClassVar[str] = "PowerShell_ProcessList_WMI"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]


class PowerShellProcessCmdline(KapeModule):
    """
    Author: nov3mb3r

    Version: 1.0

    ID: 92039073-8cb7-4b82-86de-1911fd8e317a

    Process Commandline
    """

    name: ClassVar[str] = "PowerShell_Process_Cmdline"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class PowerShellStartupCommands(KapeModule):
    """
    Author: nov3mb3r

    Version: 1.0

    ID: 67733d63-8052-4abf-b85e-450bbd368e36

    Commands on Startup
    """

    name: ClassVar[str] = "PowerShell_Startup_Commands"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class PowerShellWMIRepositoryAuditing(KapeModule):
    """
    Author: Andreas Hunkeler (@Karneades)

    Version: 1.0

    ID: cebffd14-901a-44fd-9960-e3a781acc1d9

    Collect WMI repository information
    """

    name: ClassVar[str] = "PowerShell_WMIRepositoryAuditing"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsARPCache(KapeModule):
    """
    Author: Mike Cary

    Version: 1.0

    ID: 6d4ea3be-f634-4809-b7d8-db0d22800737

    ARPCache
    """

    name: ClassVar[str] = "Windows_ARPCache"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsDNSCache(KapeModule):
    """
    Author: Mike Cary

    Version: 1.0

    ID: b5df17b0-29d2-448f-bdaa-ec221bee29b6

    DNSCache
    """

    name: ClassVar[str] = "Windows_DNSCache"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsGpResult(KapeModule):
    """
    Author: NVISO (@NVISOsecurity)

    Version: 0.1

    ID: 4dc75767-5c10-4ec5-b5d6-ba332f92070f

    gpresult
    """

    name: ClassVar[str] = "Windows_GpResult"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsIPConfig(KapeModule):
    """
    Author: Mike Cary

    Version: 1.0

    ID: 5afdfd6b-5ebb-4545-9980-88e6f421e508

    IPConfig
    """

    name: ClassVar[str] = "Windows_IPConfig"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsMsInfo(KapeModule):
    """
    Author: NVISO (@NVISOsecurity)

    Version: 0.1

    ID: a282bf61-d47b-456c-8b37-a4d455c3e122

    msinfo
    """

    name: ClassVar[str] = "Windows_MsInfo"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsnbtstatNetBIOSCache(KapeModule):
    """
    Author: Mike Cary

    Version: 1.0

    ID: d0309794-03b1-40bf-bbdd-12fe77f5e0a6

    NBTStat_NETBIOS_Cache
    """

    name: ClassVar[str] = "Windows_nbtstat_NetBIOSCache"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsnbtstatNetBIOSSessions(KapeModule):
    """
    Author: Mike Cary

    Version: 1.0

    ID: 340d77a6-a9bd-400b-b3b6-bdd5a2085e3c

    NBTStat_NETBIOS_Sessions
    """

    name: ClassVar[str] = "Windows_nbtstat_NetBIOSSessions"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class Windowsnetshportproxy(KapeModule):
    """
    Author: Andreas Hunkeler (@Karneades)

    Version: 1.0

    ID: a7e6344e-2680-447f-223e-e79ad3aa0e65

    PortProxy configuration
    """

    name: ClassVar[str] = "Windows_netsh_portproxy"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsNetStat(KapeModule):
    """
    Author: Mike Cary

    Version: 1.0

    ID: ea773d1a-0a69-432d-ab3a-45a0d87374b8

    NetStat
    """

    name: ClassVar[str] = "Windows_NetStat"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsNetAccounts(KapeModule):
    """
    Author: piesecurity

    Version: 1.0

    ID: 6ec49720-1afc-4b89-9454-1398430cb31f

    Gathers Basic System Information Using the Net Command (Accounts)
    """

    name: ClassVar[str] = "Windows_Net_Accounts"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsNetFile(KapeModule):
    """
    Author: piesecurity

    Version: 1.0

    ID: fb732a7a-e5f3-484e-95dd-d49cdac29391

    Gathers Basic System Information Using the Net Command (File)
    """

    name: ClassVar[str] = "Windows_Net_File"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsNetLocalGroup(KapeModule):
    """
    Author: piesecurity

    Version: 1.0

    ID: a9789a17-1061-4a66-b5da-419223bb6c09

    Gathers Basic System Information Using the Net Command (LocalGroup)
    """

    name: ClassVar[str] = "Windows_Net_LocalGroup"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsNetSession(KapeModule):
    """
    Author: piesecurity

    Version: 1.0

    ID: 878ca28e-aa20-4e2e-b3d4-2a30402057d6

    Gathers Basic System Information Using the Net Command (Session)
    """

    name: ClassVar[str] = "Windows_Net_Session"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsNetShare(KapeModule):
    """
    Author: piesecurity

    Version: 1.0

    ID: aba1ed38-d670-4db1-be70-bebb0a6a4ef3

    Gathers Basic System Information Using the Net Command (Share)
    """

    name: ClassVar[str] = "Windows_Net_Share"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsNetStart(KapeModule):
    """
    Author: piesecurity

    Version: 1.0

    ID: aa1b7b54-2e33-486c-9b4d-eb467e9e6ea3

    Gathers Basic System Information Using the Net Command (Running Services)
    """

    name: ClassVar[str] = "Windows_Net_Start"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsNetUse(KapeModule):
    """
    Author: piesecurity

    Version: 1.0

    ID: 979b4a71-abf8-4f0b-9b94-51e9c1384888

    Gathers Basic System Information Using the Net Command (Use)
    """

    name: ClassVar[str] = "Windows_Net_Use"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsNetUser(KapeModule):
    """
    Author: piesecurity

    Version: 1.0

    ID: 12589aca-921f-42a0-8806-5174bfa511fd

    Gathers Basic System Information Using the Net Command (User)
    """

    name: ClassVar[str] = "Windows_Net_User"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsqwinstaRDPSessions(KapeModule):
    """
    Author: piesecurity

    Version: 1.0

    ID: 7407dd38-cd98-4981-b9ee-d6ae1e306db0

    Display information about Active Remote Desktop Services sessions. - Query
    Windows Station
    """

    name: ClassVar[str] = "Windows_qwinsta_RDPSessions"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class WindowsRoutingTable(KapeModule):
    """
    Author: Mike Cary

    Version: 1.0

    ID: 8aaad838-be9e-43d4-8643-145ceaa4208b

    RoutingTable
    """

    name: ClassVar[str] = "Windows_RoutingTable"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class Windowsschtasks(KapeModule):
    """
    Author: Brian Maloney

    Version: 1.1

    ID: 66d26feb-6dd7-4b12-b88b-b43ee17cd2c7

    Displays all scheduled tasks
    """

    name: ClassVar[str] = "Windows_schtasks"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.XML,
    ]


class WindowsSystemInfo(KapeModule):
    """
    Author: piesecurity

    Version: 1.0

    ID: e4263b9f-cc93-434a-b56f-d3d7cc205e4b

    Gathers Basic System Information
    """

    name: ClassVar[str] = "Windows_SystemInfo"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class log4jscanner(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: 625db471-45bd-4b3b-a60f-97a376168a94

    Vulnerability scanner and mitigation patch for Log4j2 CVE-2021-44228
    """

    name: ClassVar[str] = "log4j-scanner"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class LokiLiveResponse(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: e93f1052-4d8f-4b63-b680-2af845e95a98

    Loki - Simple IOC and Incident Response Scanner - Live Response
    """

    name: ClassVar[str] = "Loki_LiveResponse"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.LOG]


class PowerShellGetInjectedThread(KapeModule):
    """
    Author: piesecurity

    Version: 1.1

    ID: c3998d96-fa6f-44db-9bb3-4cc66259a09c

    Get-InjectedThread
    """

    name: ClassVar[str] = "PowerShell_Get-InjectedThread"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class PowerShellGetNetworkConnection(KapeModule):
    """
    Author: Hadar Yudovich

    Version: 1.1

    ID: 814f00f5-b8c0-4bef-8439-b75bd90c1459

    Get-NetworkConnection including timestamps
    """

    name: ClassVar[str] = "PowerShell_Get-NetworkConnection"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]


class PowerShellNetscan(KapeModule):
    """
    Author: nov3mb3r

    Version: 1.0

    ID: c1847d86-3fa9-492b-ae09-8c90173ec222

    Network scan of process connections
    """

    name: ClassVar[str] = "PowerShell_Netscan"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class PowerShellSigned(KapeModule):
    """
    Author: Pedro Sanchez Cordero (conexioninversa)

    Version: 1.0

    ID: 2fec6f40-c36f-4faa-8b42-c997e494d92b

    PowerShell_Signing
    """

    name: ClassVar[str] = "PowerShell_Signed"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class NirSoftUSBDeview(KapeModule):
    """
    Author: NVISO (@NVISOsecurity)

    Version: 1.0

    ID: 9a23e756-3f18-4448-95c6-65d411f8c70b

    USBDeview - Nirsoft
    """

    name: ClassVar[str] = "NirSoft_USBDeview"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class SysInternalsAutoruns(KapeModule):
    """
    Author: Andy Furnas, Encoding updates by piesecurity, Andreas Hunkeler
    (@Karneades)

    Version: 1.4

    ID: c95e71bd-7abb-48c3-abae-f48b9ff19dec

    Autoruns reports Explorer shell extensions, toolbars, browser helper
    objects, Winlogon notifications, auto-start services, and much more.
    """

    name: ClassVar[str] = "SysInternals_Autoruns"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class SysInternalsHandle(KapeModule):
    """
    Author: Andy Furnas

    Version: 1.0

    ID: de522157-2cde-46ff-b1b0-d2201fba6554

    Handle is a utility that displays information about open handles for any
    process in the system.
    """

    name: ClassVar[str] = "SysInternals_Handle"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class SysInternalsPsFile(KapeModule):
    """
    Author: Andy Furnas

    Version: 1.0

    ID: 79cca355-160d-4a61-951d-e295a8c0d8bb

    PsFile is a command-line utility that shows a list of files on a system that
    are opened remotely, and it also allows you to close opened files either by
    name or by a file identifier.
    """

    name: ClassVar[str] = "SysInternals_PsFile"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class SysInternalsPsInfo(KapeModule):
    """
    Author: Andy Furnas

    Version: 1.0

    ID: 9e89b787-bc97-4e96-b72e-195a390ede98

    PsInfo is a command-line tool that gathers key information about the local
    or remote Windows NT/2000 system, including the type of installation, kernel
    build, registered organization and owner, number of processors and their
    type, amount of physical memory, the install date of the system, and if its
    a trial version, the expiration date.
    """

    name: ClassVar[str] = "SysInternals_PsInfo"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class SysInternalsPsList(KapeModule):
    """
    Author: Andy Furnas

    Version: 1.0

    ID: fa3aa32a-0091-4650-9485-ad87891b8751

    Shows statistics for all running processes
    """

    name: ClassVar[str] = "SysInternals_PsList"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class SysInternalsPsLoggedOn(KapeModule):
    """
    Author: Andy Furnas

    Version: 1.0

    ID: 7b71f318-468e-4616-9ed2-dfd750b6b960

    PsLoggedOn is an applet that displays both the locally logged on users and
    users logged on via resources for either the local computer, or a remote
    one.
    """

    name: ClassVar[str] = "SysInternals_PsLoggedOn"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class SysInternalsPsService(KapeModule):
    """
    Author: Andy Furnas

    Version: 1.0

    ID: b5af1e38-2a78-4538-8430-83b8a60e02c4

    Display the configured services (both running and stopped) on the local
    system.
    """

    name: ClassVar[str] = "SysInternals_PsService"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class SysInternalsPsTree(KapeModule):
    """
    Author: piesecurity

    Version: 1.0

    ID: df6c02c1-d4b9-4e84-a4f6-7dd3f67a319d

    Shows a basic process tree for all running processes
    """

    name: ClassVar[str] = "SysInternals_PsTree"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class SysInternalsTcpvcon(KapeModule):
    """
    Author: Andy Furnas

    Version: 1.0

    ID: 528beed4-5703-454b-a4e8-879b8daecfd5

    TCPView provides a more informative and conveniently presented subset of the
    Netstat program that ships with Windows.
    """

    name: ClassVar[str] = "SysInternals_Tcpvcon"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
