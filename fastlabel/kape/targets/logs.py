"""
Auto-generated classes from the .tkape files for the Logs category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class ConfluenceLogsConfluenceWikiLogFiles0(KapeTarget):
    name: ClassVar[str] = "Confluence Wiki Log Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Atlassian\\Application Data\\Confluence\\logs\\"
    )
    file_mask: ClassVar[str] = "*.log*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ConfluenceLogsConfluenceWikiLogFiles1(KapeTarget):
    name: ClassVar[str] = "Confluence Wiki Log Files"
    base_path: ClassVar[Path] = Path("C:\\Program Files\\Atlassian\\Confluence\\logs\\")
    file_mask: ClassVar[str] = "*.log"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ConfluenceLogs(KapeTargetConfiguration):
    """
    Author: Eric Capuano

    Version: 1.0

    ID: 317b3814-b383-4bcf-97a2-3b3d1c5f8ca0

    Confluence Log Files
    """

    name: ClassVar[str] = "ConfluenceLogs"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ConfluenceLogsConfluenceWikiLogFiles0,
        ConfluenceLogsConfluenceWikiLogFiles1,
    ]


class ExchangeClientAccessExchangeclientaccesslogfiles0(KapeTarget):
    """
    Highly dependent on Exchange configuration
    """

    name: ClassVar[str] = "Exchange client access log files"
    base_path: ClassVar[Path] = Path(
        "C:\\Program Files\\Microsoft\\Exchange Server\\*\\Logging\\"
    )
    file_mask: ClassVar[str] = "*.log"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ExchangeClientAccess(KapeTargetConfiguration):
    """
    Author: Keith Twombley

    Version: 1.0

    ID: 9e802154-53eb-4cc9-9cca-d2e39f3227d7

    Exchange Client Access Log Files
    """

    name: ClassVar[str] = "ExchangeClientAccess"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ExchangeClientAccessExchangeclientaccesslogfiles0
    ]


class ExchangeTransportExchangeTransportRoleslogfiles0(KapeTarget):
    """
    Highly dependent on Exchange configuration
    """

    name: ClassVar[str] = "Exchange TransportRoles log files"
    base_path: ClassVar[Path] = Path(
        "C:\\Program Files\\Microsoft\\Exchange Server\\*\\TransportRoles\\Logs\\"
    )
    file_mask: ClassVar[str] = "*.log"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ExchangeTransport(KapeTargetConfiguration):
    """
    Author: Keith Twombley

    Version: 1.0

    ID: 9bc0a453-50ab-46e8-a424-09dc7022c4a4

    Exchange Transport Log Files
    """

    name: ClassVar[str] = "ExchangeTransport"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ExchangeTransportExchangeTransportRoleslogfiles0
    ]


class FileZillaClientFileZillaXMLLogFiles0(KapeTarget):
    name: ClassVar[str] = "FileZilla XML Log Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\FileZilla\\")
    file_mask: ClassVar[str] = "*.xml*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileZillaClientFileZillaSQLite3LogFiles1(KapeTarget):
    name: ClassVar[str] = "FileZilla SQLite3 Log Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\FileZilla\\")
    file_mask: ClassVar[str] = "*.sqlite3*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileZillaClient(KapeTargetConfiguration):
    """
    Author: Dennis Reneau

    Version: 1.0

    ID: f7eaa0d5-0b15-4578-b411-ac4226e13a7f

    FileZilla XML and SQLite Log Files
    """

    name: ClassVar[str] = "FileZillaClient"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        FileZillaClientFileZillaXMLLogFiles0,
        FileZillaClientFileZillaSQLite3LogFiles1,
    ]


class FileZillaServerFileZillaServerXMLLogFiles0(KapeTarget):
    name: ClassVar[str] = "FileZilla Server XML Log Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\FileZilla Server\\"
    )
    file_mask: ClassVar[str] = "*.xml*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileZillaServerFileZillaLogFiles1(KapeTarget):
    name: ClassVar[str] = "FileZilla Log Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Program Files (x86)\\FileZilla Server\\Logs\\"
    )
    file_mask: ClassVar[str] = "*.log*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileZillaServer(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 1292ff24-aae0-4bab-8e11-d040c4aaf1b5

    FileZilla Server Logs
    """

    name: ClassVar[str] = "FileZillaServer"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        FileZillaServerFileZillaServerXMLLogFiles0,
        FileZillaServerFileZillaLogFiles1,
    ]


class TablacusExplorerTablacusExplorerrememberxml0(KapeTarget):
    name: ClassVar[str] = "Tablacus Explorer - remember.xml"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Temp\\*\\config"
    )
    file_mask: ClassVar[str] = "remember.xml"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TablacusExplorerTablacusExplorerwindowxml1(KapeTarget):
    name: ClassVar[str] = "Tablacus Explorer - window.xml"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Temp\\*\\config"
    )
    file_mask: ClassVar[str] = "window.xml"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TablacusExplorerTablacusExplorerwindow1xml2(KapeTarget):
    name: ClassVar[str] = "Tablacus Explorer - window1.xml"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Temp\\*\\config"
    )
    file_mask: ClassVar[str] = "window1.xml"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TablacusExplorer(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 0dc0d6c0-3385-4621-886e-0bda8f97cbc4

    Tablacus Explorer
    """

    name: ClassVar[str] = "TablacusExplorer"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        TablacusExplorerTablacusExplorerrememberxml0,
        TablacusExplorerTablacusExplorerwindowxml1,
        TablacusExplorerTablacusExplorerwindow1xml2,
    ]


class WinSCPWinSCPinifile0(KapeTarget):
    name: ClassVar[str] = "WinSCP (.ini file)"
    base_path: ClassVar[Path] = Path("C:\\")
    file_mask: ClassVar[str] = "WinSCP.ini"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WinSCP(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: acd134fb-6f0b-446e-a781-3a9b6411488d

    WinSCP
    """

    name: ClassVar[str] = "WinSCP"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [WinSCPWinSCPinifile0]


class ExchangeExchangeclientaccesslogfiles0(KapeTarget):
    name: ClassVar[str] = "Exchange client access log files"
    base_path: ClassVar[Path] = Path("ExchangeClientAccess.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ExchangeExchangeTransportRoleslogfiles1(KapeTarget):
    name: ClassVar[str] = "Exchange TransportRoles log files"
    base_path: ClassVar[Path] = Path("ExchangeTransport.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Exchange(KapeTargetConfiguration):
    """
    Author: Keith Twombley

    Version: 1.0

    ID: 1b54aafe-5074-4d45-b129-29107ce7f863

    Exchange Log Files
    """

    name: ClassVar[str] = "Exchange"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ExchangeExchangeclientaccesslogfiles0,
        ExchangeExchangeTransportRoleslogfiles1,
    ]


class WebServersApacheAccessLogs0(KapeTarget):
    name: ClassVar[str] = "Apache Access Logs"
    base_path: ClassVar[Path] = Path("ApacheAccessLog.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WebServersIISLogs1(KapeTarget):
    name: ClassVar[str] = "IIS Logs"
    base_path: ClassVar[Path] = Path("IISLogFiles.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WebServersNGINXLogs2(KapeTarget):
    name: ClassVar[str] = "NGINX Logs"
    base_path: ClassVar[Path] = Path("NGINXLogs.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WebServersMSSQLErrorLogs3(KapeTarget):
    name: ClassVar[str] = "MSSQL Error Logs"
    base_path: ClassVar[Path] = Path("MSSQLErrorLog.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WebServers(KapeTargetConfiguration):
    """
    Author: Eric Capuano

    Version: 1.0

    ID: 38de27ae-5047-404b-a7e1-3c99071724d5

    Logs from all known web server applications and supporting services
    """

    name: ClassVar[str] = "WebServers"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WebServersApacheAccessLogs0,
        WebServersIISLogs1,
        WebServersNGINXLogs2,
        WebServersMSSQLErrorLogs3,
    ]


class IISLogFilesIISlogfiles0(KapeTarget):
    name: ClassVar[str] = "IIS log files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\LogFiles\\W3SVC*\\")
    file_mask: ClassVar[str] = "*.log"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class IISLogFilesIISlogfiles1(KapeTarget):
    name: ClassVar[str] = "IIS log files"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\LogFiles\\W3SVC*\\"
    )
    file_mask: ClassVar[str] = "*.log"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class IISLogFilesIISlogfiles2(KapeTarget):
    name: ClassVar[str] = "IIS log files"
    base_path: ClassVar[Path] = Path("C:\\inetpub\\logs\\LogFiles\\")
    file_mask: ClassVar[str] = "*.log"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class IISLogFilesIISlogfiles3(KapeTarget):
    name: ClassVar[str] = "IIS log files"
    base_path: ClassVar[Path] = Path("C:\\inetpub\\logs\\LogFiles\\W3SVC*\\")
    file_mask: ClassVar[str] = "*.log"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class IISLogFilesIISlogfiles4(KapeTarget):
    name: ClassVar[str] = "IIS log files"
    base_path: ClassVar[Path] = Path(
        "C:\\Resources\\Directory\\*\\LogFiles\\Web\\W3SVC*\\"
    )
    file_mask: ClassVar[str] = "*.log"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class IISLogFiles(KapeTargetConfiguration):
    """
    Author: Troy Larson

    Version: 2.0

    ID: 701573f6-0ce1-454d-af41-612713e22af5

    IIS Log Files
    """

    name: ClassVar[str] = "IISLogFiles"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        IISLogFilesIISlogfiles0,
        IISLogFilesIISlogfiles1,
        IISLogFilesIISlogfiles2,
        IISLogFilesIISlogfiles3,
        IISLogFilesIISlogfiles4,
    ]


class ManageEngineLogsManageEngineDesktopCentralLogFiles0(KapeTarget):
    name: ClassVar[str] = "ManageEngine Desktop Central Log Files"
    base_path: ClassVar[Path] = Path("C:\\ManageEngine\\DesktopCentral_Server\\logs\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ManageEngineLogs(KapeTargetConfiguration):
    """
    Author: Whitney Champion

    Version: 1.0

    ID: c034ee17-a97f-48a1-b720-c73867ed66e6

    ManageEngine Desktop Central Log Files
    """

    name: ClassVar[str] = "ManageEngineLogs"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ManageEngineLogsManageEngineDesktopCentralLogFiles0
    ]


class NGINXLogsNGINXLogFiles0(KapeTarget):
    name: ClassVar[str] = "NGINX Log Files"
    base_path: ClassVar[Path] = Path("C:\\nginx\\logs\\")
    file_mask: ClassVar[str] = "*.log"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NGINXLogs(KapeTargetConfiguration):
    """
    Author: Eric Capuano

    Version: 1.0

    ID: d5c2cfd9-a8a5-400e-8be5-a8e9b5653a51

    NGINX Log Files
    """

    name: ClassVar[str] = "NGINXLogs"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [NGINXLogsNGINXLogFiles0]


class LogFilesLogFiles0(KapeTarget):
    name: ClassVar[str] = "LogFiles"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\LogFiles\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LogFilesLogFiles1(KapeTarget):
    name: ClassVar[str] = "LogFiles"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\LogFiles\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class LogFiles(KapeTargetConfiguration):
    """
    Author: Fabian Murer

    Version: 1.0

    ID: 67c9bb8d-342b-4380-a110-565317fce014

    LogFiles (includes SUM)
    """

    name: ClassVar[str] = "LogFiles"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [LogFilesLogFiles0, LogFilesLogFiles1]


class SUMSUMDatabasemdbfiles0(KapeTarget):
    """
    Grabs Current.mdb, SystemIdentity.mdb, and [GUID].mdb
    """

    name: ClassVar[str] = "SUM Database (.mdb files)"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\LogFiles\\SUM")
    file_mask: ClassVar[str] = "*.mdb"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUM(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 2f828ec7-75fc-4e46-a160-16d5d1b30118

    SUM Database
    """

    name: ClassVar[str] = "SUM"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [SUMSUMDatabasemdbfiles0]
