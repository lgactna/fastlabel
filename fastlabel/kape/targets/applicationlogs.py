"""
Auto-generated classes from the .tkape files for the ApplicationLogs category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class EmsisoftEmsisoftScanLogs0(KapeTarget):
    """
    Can contain file detection and quarantine info
    """

    name: ClassVar[str] = "Emsisoft Scan Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Emsisoft\\Reports\\")
    regex: ClassVar[str] = r"(?s:scan.*\.txt)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Emsisoft(KapeTargetConfiguration):
    """
    Author: blueskycyber

    Version: 1.0

    ID: f810ea6e-eb10-4788-bff7-77bd83fe15d2

    Emsisoft Antivirus Logs
    """

    name: ClassVar[str] = "Emsisoft"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [EmsisoftEmsisoftScanLogs0]


class AmmyyAmmyyProgramData0(KapeTarget):
    """
    May not contain traditional log files, but presence of this folder may
    indicate historical usage
    """

    name: ClassVar[str] = "Ammyy Program Data"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Ammyy\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Ammyy(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: 606ad937-c32e-49ba-9403-3f1ce501a012

    Ammyy Data
    """

    name: ClassVar[str] = "Ammyy"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [AmmyyAmmyyProgramData0]


class KaseyaKaseyaLiveConnectLogsXP0(KapeTarget):
    """

    https://helpdesk.kaseya.com/hc/en-gb/articles/229009708-Live-Connect-Log-File-Locations
    """

    name: ClassVar[str] = "Kaseya Live Connect Logs (XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Kaseya\\Log\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaseyaKaseyaLiveConnectLogs1(KapeTarget):
    """

    https://helpdesk.kaseya.com/hc/en-gb/articles/229009708-Live-Connect-Log-File-Locations
    """

    name: ClassVar[str] = "Kaseya Live Connect Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Kaseya\\Log\\KaseyaLiveConnect\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaseyaKaseyaAgentEndpointServiceLogsXP2(KapeTarget):
    """

    https://helpdesk.kaseya.com/hc/en-gb/articles/229009708-Live-Connect-Log-File-Locations
    """

    name: ClassVar[str] = "Kaseya Agent Endpoint Service Logs (XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\All Users\\Application Data\\Kaseya\\Log\\Endpoint\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaseyaKaseyaAgentEndpointServiceLogs3(KapeTarget):
    """

    https://helpdesk.kaseya.com/hc/en-gb/articles/229009708-Live-Connect-Log-File-Locations
    """

    name: ClassVar[str] = "Kaseya Agent Endpoint Service Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Kaseya\\Log\\Endpoint\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaseyaKaseyaAgentServiceLog4(KapeTarget):
    """

    https://helpdesk.kaseya.com/hc/en-gb/articles/229009708-Live-Connect-Log-File-Locations
    """

    name: ClassVar[str] = "Kaseya Agent Service Log"
    base_path: ClassVar[Path] = Path("C:\\Program Files*\\Kaseya\\*\\")
    regex: ClassVar[str] = r"(?s:agentmon\.log.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaseyaKaseyaSetupLog5(KapeTarget):
    """
    https://helpdesk.kaseya.com/hc/en-gb/articles/229011448
    """

    name: ClassVar[str] = "Kaseya Setup Log"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Temp\\")
    regex: ClassVar[str] = r"(?s:KASetup\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaseyaKaseyaSetupLog6(KapeTarget):
    """
    https://helpdesk.kaseya.com/hc/en-gb/articles/229011448
    """

    name: ClassVar[str] = "Kaseya Setup Log"
    base_path: ClassVar[Path] = Path("C:\\Windows\\Temp\\")
    regex: ClassVar[str] = r"(?s:KASetup\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaseyaKaseyaSetupLog7(KapeTarget):
    """
    https://helpdesk.kaseya.com/hc/en-gb/articles/229011448
    """

    name: ClassVar[str] = "Kaseya Setup Log"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\Temp\\")
    regex: ClassVar[str] = r"(?s:KASetup\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaseyaKaseyaAgentEdgeServiceLogs8(KapeTarget):
    """

    https://www.huntress.com/blog/rapid-response-kaseya-vsa-mass-msp-ransomware-incident
    """

    name: ClassVar[str] = "Kaseya Agent Edge Service Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Kaseya\\Log\\KaseyaEdgeServices\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Kaseya(KapeTargetConfiguration):
    """
    Author: Drew Ervin and Andrew Rathbun

    Version: 1.1

    ID: bb83f860-5a10-4471-821e-9ef4ab6f856c

    Kaseya Data
    """

    name: ClassVar[str] = "Kaseya"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        KaseyaKaseyaLiveConnectLogsXP0,
        KaseyaKaseyaLiveConnectLogs1,
        KaseyaKaseyaAgentEndpointServiceLogsXP2,
        KaseyaKaseyaAgentEndpointServiceLogs3,
        KaseyaKaseyaAgentServiceLog4,
        KaseyaKaseyaSetupLog5,
        KaseyaKaseyaSetupLog6,
        KaseyaKaseyaSetupLog7,
        KaseyaKaseyaAgentEdgeServiceLogs8,
    ]


class LogMeInLogMeInProgramDataLogs0(KapeTarget):
    name: ClassVar[str] = "LogMeIn ProgramData Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\LogMeIn\\Logs\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LogMeInLogMeInApplicationEvents1(KapeTarget):
    """
    Contains LogMeIn entries, event source: LogMeIn
    """

    name: ClassVar[str] = "LogMeIn Application Events"
    base_path: ClassVar[Path] = Path("ApplicationEvents.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LogMeInLogMeInApplicationLogs2(KapeTarget):
    """
    Contains RemoteAssist (formerly GoToAssist), GoToMeeting, and other GoTo*
    logs
    """

    name: ClassVar[str] = "LogMeIn Application Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\temp\\LogMeInLogs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LogMeIn(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: 488e9de2-ecb6-4b27-88a3-719715147c33

    LogMeIn Data
    """

    name: ClassVar[str] = "LogMeIn"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        LogMeInLogMeInProgramDataLogs0,
        LogMeInLogMeInApplicationEvents1,
        LogMeInLogMeInApplicationLogs2,
    ]


class OpenVPNClientOpenVPNClientConfig0(KapeTarget):
    """
    Contains OpenVPN Configs (Profiles)
    """

    name: ClassVar[str] = "OpenVPN Client Config"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\OpenVPN\\config\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenVPNClientOpenVPNClientConfig1(KapeTarget):
    """
    Contains OpenVPN Configs(Profiles)
    """

    name: ClassVar[str] = "OpenVPN Client Config"
    base_path: ClassVar[Path] = Path("C:\\Program Files*\\OpenVPN\\config")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenVPNClientOpenVPNClientConfig2(KapeTarget):
    """
    Contains OpenVPN Logs for each Config(Profile)
    """

    name: ClassVar[str] = "OpenVPN Client Config"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\OpenVPN\\log\\")
    regex: ClassVar[str] = r"(?s:.*\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenVPNClient(KapeTargetConfiguration):
    """
    Author: Mathias Frank

    Version: 1.0

    ID: 03920e05-c794-46d1-b2cd-5e1febd0fdaf

    OpenVPN Client Config and Log
    """

    name: ClassVar[str] = "OpenVPNClient"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        OpenVPNClientOpenVPNClientConfig0,
        OpenVPNClientOpenVPNClientConfig1,
        OpenVPNClientOpenVPNClientConfig2,
    ]


class ProtonVPNProtonVPNConnectionLogs0(KapeTarget):
    """
    Locates ProtonVPN connection logs.
    """

    name: ClassVar[str] = "ProtonVPN - Connection Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\ProtonVPN\\Logs"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ProtonVPN(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 47dc8f4d-633d-4dcc-994d-2d62c3fa9c28

    ProtonVPN
    """

    name: ClassVar[str] = "ProtonVPN"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [ProtonVPNProtonVPNConnectionLogs0]


class RadminRadminServer32bitLog0(KapeTarget):
    """
    Contains Application Log entries such as service start and incomming
    connections.
    """

    name: ClassVar[str] = "Radmin Server 32bit Log"
    base_path: ClassVar[Path] = Path("C:\\Windows\\SysWOW64\\rserver30\\")
    regex: ClassVar[str] = r"(?s:Radm_log\.htm)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RadminRadminServer64bitLog1(KapeTarget):
    """
    Contains Application Log entries such as service start and incomming
    connections.
    """

    name: ClassVar[str] = "Radmin Server 64bit Log"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\rserver30\\")
    regex: ClassVar[str] = r"(?s:Radm_log\.htm)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RadminRadminServer32bitChats2(KapeTarget):
    """
    Previous chat logs
    """

    name: ClassVar[str] = "Radmin Server 32bit Chats"
    base_path: ClassVar[Path] = Path("C:\\Windows\\SysWOW64\\rserver30\\CHATLOGS\\*\\")
    regex: ClassVar[str] = r"(?s:.*\.htm)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RadminRadminServer64bitChats3(KapeTarget):
    """
    Previous chat logs
    """

    name: ClassVar[str] = "Radmin Server 64bit Chats"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\rserver30\\CHATLOGS\\*\\")
    regex: ClassVar[str] = r"(?s:.*\.htm)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RadminRadminViewerChats4(KapeTarget):
    """
    Previous chat logs
    """

    name: ClassVar[str] = "Radmin Viewer Chats"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Documents\\ChatLogs\\*\\")
    regex: ClassVar[str] = r"(?s:.*\.htm)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Radmin(KapeTargetConfiguration):
    """
    Author: Mathias Frank

    Version: 1.0

    ID: 432a2374-2310-461e-ad94-aaf07989aa46

    Radmin Server/Viewer Logs and Chats
    """

    name: ClassVar[str] = "Radmin"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RadminRadminServer32bitLog0,
        RadminRadminServer64bitLog1,
        RadminRadminServer32bitChats2,
        RadminRadminServer64bitChats3,
        RadminRadminViewerChats4,
    ]


class ScreenConnectScreenConnectSessionDatabase0(KapeTarget):
    """
    SQLite database with session information
    """

    name: ClassVar[str] = "ScreenConnect Session Database"
    base_path: ClassVar[Path] = Path("C:\\Program Files*\\ScreenConnect\\App_Data\\")
    regex: ClassVar[str] = r"(?s:Session\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ScreenConnectScreenConnectSessionDatabase1(KapeTarget):
    """
    Contains each user's last authenticated time
    """

    name: ClassVar[str] = "ScreenConnect Session Database"
    base_path: ClassVar[Path] = Path("C:\\Program Files*\\ScreenConnect\\App_Data\\")
    regex: ClassVar[str] = r"(?s:User\.xml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ScreenConnectScreenConnectApplicationEvents2(KapeTarget):
    """
    Contains ScreenConnect entries, source: ScreenConnect Client
    """

    name: ClassVar[str] = "ScreenConnect Application Events"
    base_path: ClassVar[Path] = Path("ApplicationEvents.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ScreenConnectScreenConnectUserConfig3(KapeTarget):
    """
    Contains server domain and IP info
    """

    name: ClassVar[str] = "ScreenConnect User Config"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\ScreenConnect Client*\\")
    regex: ClassVar[str] = r"(?s:user\.config)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ScreenConnect(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: 26c80b79-b3c0-4378-abe8-a5a6c9aebb4f

    ScreenConnect Data (now known as ConnectWise Control)
    """

    name: ClassVar[str] = "ScreenConnect"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ScreenConnectScreenConnectSessionDatabase0,
        ScreenConnectScreenConnectSessionDatabase1,
        ScreenConnectScreenConnectApplicationEvents2,
        ScreenConnectScreenConnectUserConfig3,
    ]


class VNCLogsRealVNCLog0(KapeTarget):
    """
    https://www.realvnc.com/en/connect/docs/logging.html#logging
    """

    name: ClassVar[str] = "RealVNC Log"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\RealVNC\\")
    regex: ClassVar[str] = r"(?s:vncserver\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VNCLogsRealVNCApplicationLogs1(KapeTarget):
    """
    Contains RealVNC entries, event source: VNC Server
    """

    name: ClassVar[str] = "RealVNC Application Logs"
    base_path: ClassVar[Path] = Path("ApplicationEvents.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VNCLogs(KapeTargetConfiguration):
    """
    Author: Phill Moore

    Version: 1.1

    ID: b98dab2e-81f3-472e-a22a-05269ad16270

    VNC Logs
    """

    name: ClassVar[str] = "VNCLogs"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        VNCLogsRealVNCLog0,
        VNCLogsRealVNCApplicationLogs1,
    ]


class RemoteAdminAmmyy0(KapeTarget):
    name: ClassVar[str] = "Ammyy"
    base_path: ClassVar[Path] = Path("Ammyy.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminAnyDesk1(KapeTarget):
    name: ClassVar[str] = "AnyDesk"
    base_path: ClassVar[Path] = Path("AnyDesk.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminChromeRemoteDesktop2(KapeTarget):
    name: ClassVar[str] = "Chrome Remote Desktop"
    base_path: ClassVar[Path] = Path("ApplicationEvents.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminKaseya3(KapeTarget):
    name: ClassVar[str] = "Kaseya"
    base_path: ClassVar[Path] = Path("Kaseya.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminLogMeIn4(KapeTarget):
    name: ClassVar[str] = "LogMeIn"
    base_path: ClassVar[Path] = Path("LogMeIn.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminmRemoteNG5(KapeTarget):
    name: ClassVar[str] = "mRemoteNG"
    base_path: ClassVar[Path] = Path("mRemoteNG.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminRadmin6(KapeTarget):
    """
    Radmin Server and Viewer Logs and Chats
    """

    name: ClassVar[str] = "Radmin"
    base_path: ClassVar[Path] = Path("Radmin.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminRDPCache7(KapeTarget):
    """
    Contains data cached during recent RDP sessions
    """

    name: ClassVar[str] = "RDP Cache"
    base_path: ClassVar[Path] = Path("RDPCache.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminRDPLogs8(KapeTarget):
    """
    Contains Windows Event Logs related to RDP
    """

    name: ClassVar[str] = "RDP Logs"
    base_path: ClassVar[Path] = Path("RDPLogs.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminRemoteUtilities9(KapeTarget):
    """
    Contains logs related to the App RemoteUtilities
    """

    name: ClassVar[str] = "Remote Utilities"
    base_path: ClassVar[Path] = Path("RemoteUtilities_app.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminScreenConnectConnectWiseControl10(KapeTarget):
    name: ClassVar[str] = "ScreenConnect (ConnectWise Control)"
    base_path: ClassVar[Path] = Path("ScreenConnect.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminSplashtop11(KapeTarget):
    name: ClassVar[str] = "Splashtop"
    base_path: ClassVar[Path] = Path("Splashtop.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminSupremoRemoteDesktopControl12(KapeTarget):
    name: ClassVar[str] = "Supremo Remote Desktop Control"
    base_path: ClassVar[Path] = Path("SupremoRemoteDesktop.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminTeamViewer13(KapeTarget):
    name: ClassVar[str] = "TeamViewer"
    base_path: ClassVar[Path] = Path("TeamViewerLogs.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminUltraViewer14(KapeTarget):
    name: ClassVar[str] = "UltraViewer"
    base_path: ClassVar[Path] = Path("UltraViewer.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdminVNC15(KapeTarget):
    name: ClassVar[str] = "VNC"
    base_path: ClassVar[Path] = Path("VNCLogs.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RemoteAdmin(KapeTargetConfiguration):
    """
    Author: Drew Ervin, Mathias Frank, Andrew Rathbun

    Version: 1.7

    ID: 31cf5a4e-c44c-4457-b11f-74dca73e141b

    Composite target for files related to remote administration tools
    """

    name: ClassVar[str] = "RemoteAdmin"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RemoteAdminAmmyy0,
        RemoteAdminAnyDesk1,
        RemoteAdminChromeRemoteDesktop2,
        RemoteAdminKaseya3,
        RemoteAdminLogMeIn4,
        RemoteAdminmRemoteNG5,
        RemoteAdminRadmin6,
        RemoteAdminRDPCache7,
        RemoteAdminRDPLogs8,
        RemoteAdminRemoteUtilities9,
        RemoteAdminScreenConnectConnectWiseControl10,
        RemoteAdminSplashtop11,
        RemoteAdminSupremoRemoteDesktopControl12,
        RemoteAdminTeamViewer13,
        RemoteAdminUltraViewer14,
        RemoteAdminVNC15,
    ]
