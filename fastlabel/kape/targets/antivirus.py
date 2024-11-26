"""
Auto-generated classes from the .tkape files for the Antivirus category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class AvastAvastAVLogsXP0(KapeTarget):
    name: ClassVar[str] = "Avast AV Logs (XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents And Settings\\All Users\\Application Data\\Avast Software\\Avast\\Log\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AvastAvastAVLogs1(KapeTarget):
    name: ClassVar[str] = "Avast AV Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Avast Software\\Avast\\Log\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AvastAvastAVUserLogs2(KapeTarget):
    name: ClassVar[str] = "Avast AV User Logs"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Avast Software\\Avast\\Log\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AvastAvastAVIndex3(KapeTarget):
    name: ClassVar[str] = "Avast AV Index"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Avast Software\\Avast\\Chest\\")
    regex: ClassVar[str] = r"(?s:index\.xml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AvastAvastPersistentDataLogs4(KapeTarget):
    name: ClassVar[str] = "Avast Persistent Data Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Avast Software\\Persistent Data\\Avast\\Logs"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AvastAvastIcarusLogs5(KapeTarget):
    name: ClassVar[str] = "Avast Icarus Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Avast Software\\Icarus\\Logs")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Avast(KapeTargetConfiguration):
    """
    Author: Drew Ervin and Dhiral Panjwani

    Version: 1.1

    ID: 8b625ea2-fafa-46be-8ba1-15efd1de2a53

    Avast Antivirus Data
    """

    name: ClassVar[str] = "Avast"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        AvastAvastAVLogsXP0,
        AvastAvastAVLogs1,
        AvastAvastAVUserLogs2,
        AvastAvastAVIndex3,
        AvastAvastPersistentDataLogs4,
        AvastAvastIcarusLogs5,
    ]


class AVGAVGAVLogsXP0(KapeTarget):
    name: ClassVar[str] = "AVG AV Logs (XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\All Users\\Application Data\\AVG\\Antivirus\\log"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AVGAVGAVReportLogsXP1(KapeTarget):
    name: ClassVar[str] = "AVG AV Report Logs (XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\All Users\\Application Data\\AVG\\Antivirus\\report"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AVGAVGAVLogs2(KapeTarget):
    name: ClassVar[str] = "AVG AV Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\AVG\\Antivirus\\log")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AVGAVGReportLogs3(KapeTarget):
    name: ClassVar[str] = "AVG Report Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\AVG\\Antivirus\\report")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AVGAVGPersistentLogs4(KapeTarget):
    name: ClassVar[str] = "AVG Persistent Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\AVG\\Persistent Data\\Antivirus\\Logs"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AVGAVGFileInfoDB5(KapeTarget):
    name: ClassVar[str] = "AVG FileInfo DB"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\AVG\\Antivirus")
    regex: ClassVar[str] = r"(?s:FileInfo2\.db)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AVGAVGlsdbj2JSON6(KapeTarget):
    name: ClassVar[str] = "AVG lsdbj2 JSON"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\AVG\\Antivirus")
    regex: ClassVar[str] = r"(?s:lsdb2\.json)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AVG(KapeTargetConfiguration):
    """
    Author: Kirtan Shah and Dhiral Panjwani

    Version: 1.1

    ID: b0a4112d-e7f6-4e47-a186-7459cf8b3ab4

    AVG Antivirus Data
    """

    name: ClassVar[str] = "AVG"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        AVGAVGAVLogsXP0,
        AVGAVGAVReportLogsXP1,
        AVGAVGAVLogs2,
        AVGAVGReportLogs3,
        AVGAVGPersistentLogs4,
        AVGAVGFileInfoDB5,
        AVGAVGlsdbj2JSON6,
    ]


class AviraAVLogsAviraActivityLogs0(KapeTarget):
    """
    Collects the scan logs of Avira Antivirus
    """

    name: ClassVar[str] = "Avira Activity Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Avira\\Antivirus\\LOGFILES\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AviraAVLogsAviraSecurityLogs1(KapeTarget):
    name: ClassVar[str] = "Avira Security Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Avira\\Security\\Logs")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AviraAVLogsAviraVPNLogs2(KapeTarget):
    """
    Collects the VPN logs
    """

    name: ClassVar[str] = "Avira VPN Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Avira\\VPN")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AviraAVLogs(KapeTargetConfiguration):
    """
    Author: Fabian Murer and Dhiral Panjwani

    Version: 1.1

    ID: f977c6c9-378b-4812-a5ca-1f6c5fe57b18

    Avira Logs
    """

    name: ClassVar[str] = "AviraAVLogs"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        AviraAVLogsAviraActivityLogs0,
        AviraAVLogsAviraSecurityLogs1,
        AviraAVLogsAviraVPNLogs2,
    ]


class BitdefenderBitdefenderEndpointSecurityLogs0(KapeTarget):
    name: ClassVar[str] = "Bitdefender Endpoint Security Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Bitdefender\\Endpoint Security\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BitdefenderBitdefenderInternetSecurityLogs1(KapeTarget):
    name: ClassVar[str] = "Bitdefender Internet Security Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Bitdefender\\Desktop\\Profiles\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BitdefenderBitdefenderSQLiteDBFiles2(KapeTarget):
    """
    Bitdefender SQLite databases
    """

    name: ClassVar[str] = "Bitdefender SQLite DB Files"
    base_path: ClassVar[Path] = Path("C:\\Program Files*\\Bitdefender*\\")
    regex: ClassVar[str] = r"(?s:regex:.*\.\+\\\.\(db\|db\-wal\|db\-shm\))\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Bitdefender(KapeTargetConfiguration):
    """
    Author: Drew Ervin, Ahmed Elshaer

    Version: 1.1

    ID: e48c32bf-4069-4f79-acac-4ed181fa84c9

    Bitdefender Antivirus Data
    """

    name: ClassVar[str] = "Bitdefender"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        BitdefenderBitdefenderEndpointSecurityLogs0,
        BitdefenderBitdefenderInternetSecurityLogs1,
        BitdefenderBitdefenderSQLiteDBFiles2,
    ]


class CombofixComboFix0(KapeTarget):
    name: ClassVar[str] = "ComboFix"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:ComboFix\.txt)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Combofix(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: 8fb8608e-65ab-4fd1-b7a4-13618caf5ad7

    ComboFix Antivirus Data
    """

    name: ClassVar[str] = "Combofix"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [CombofixComboFix0]


class CybereasonCybereasonAntiRansomwareLogs0(KapeTarget):
    name: ClassVar[str] = "Cybereason Anti-Ransomware Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\crs1\\Logs")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CybereasonCybereasonSensorCommunicationsandAntiMalwareLogs1(KapeTarget):
    name: ClassVar[str] = "Cybereason Sensor Communications and Anti-Malware Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\apv2\\Logs")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CybereasonCybereasonApplicationControlandNGAVLogs2(KapeTarget):
    name: ClassVar[str] = "Cybereason Application Control and NGAV Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\crb1\\Logs")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Cybereason(KapeTargetConfiguration):
    """
    Author: piesecurity

    Version: 1.0

    ID: 73ddfac4-a50a-4fcf-9fa2-7eb360cfd896

    Cybereason Sensor/Detection Logs
    """

    name: ClassVar[str] = "Cybereason"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        CybereasonCybereasonAntiRansomwareLogs0,
        CybereasonCybereasonSensorCommunicationsandAntiMalwareLogs1,
        CybereasonCybereasonApplicationControlandNGAVLogs2,
    ]


class ESETESETNOD32AVLogsXP0(KapeTarget):
    name: ClassVar[str] = "ESET NOD32 AV Logs (XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\All Users\\Application Data\\ESET\\ESET NOD32 Antivirus\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ESETESETNOD32AVLogs1(KapeTarget):
    """
    Parser available at https://github.com/laciKE/EsetLogParser
    """

    name: ClassVar[str] = "ESET NOD32 AV Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\ESET\\ESET NOD32 Antivirus\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ESETESETNOD32AVLogs2(KapeTarget):
    name: ClassVar[str] = "ESET NOD32 AV Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\ESET\\ESET Security\\Logs")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ESETESETRemoteAdministratorLogs3(KapeTarget):
    """
    Remote Administrator logs include information on tasks executed on the
    target.
    """

    name: ClassVar[str] = "ESET Remote Administrator Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\ESET\\RemoteAdministrator\\Agent\\EraAgentApplicationData\\Logs"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ESET(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.2

    ID: 14ac7bff-2d77-4582-8558-73cf75805aaa

    ESET Antivirus Data
    """

    name: ClassVar[str] = "ESET"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ESETESETNOD32AVLogsXP0,
        ESETESETNOD32AVLogs1,
        ESETESETNOD32AVLogs2,
        ESETESETRemoteAdministratorLogs3,
    ]


class FSecureFSecureLogs0(KapeTarget):
    name: ClassVar[str] = "F-Secure Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\F-Secure\\Log\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FSecureFSecureUserLogs1(KapeTarget):
    name: ClassVar[str] = "F-Secure User Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\F-Secure\\Log\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FSecureFSecureScheduledScanReports2(KapeTarget):
    name: ClassVar[str] = "F-Secure Scheduled Scan Reports"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\F-Secure\\Antivirus\\ScheduledScanReports\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FSecure(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: 8bfd6f82-f867-4ce2-89ac-22802ff9a15f

    F-Secure Antivirus Data
    """

    name: ClassVar[str] = "FSecure"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        FSecureFSecureLogs0,
        FSecureFSecureUserLogs1,
        FSecureFSecureScheduledScanReports2,
    ]


class HitmanProHitmanProLogs0(KapeTarget):
    name: ClassVar[str] = "HitmanPro Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\HitmanPro\\Logs\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class HitmanProHitmanProAlertLogs1(KapeTarget):
    name: ClassVar[str] = "HitmanPro Alert Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\HitmanPro.Alert\\Logs\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class HitmanProHitmanProDatabase2(KapeTarget):
    """
    SQLite DB
    """

    name: ClassVar[str] = "HitmanPro Database"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\HitmanPro.Alert\\")
    regex: ClassVar[str] = r"(?s:excalibur\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class HitmanPro(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: db98e01b-bd07-4b40-a6ef-e75bdef39bb2

    HitmanPro Antivirus Data
    """

    name: ClassVar[str] = "HitmanPro"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        HitmanProHitmanProLogs0,
        HitmanProHitmanProAlertLogs1,
        HitmanProHitmanProDatabase2,
    ]


class MalwarebytesMalwareBytesAntiMalwareLogs0(KapeTarget):
    name: ClassVar[str] = "MalwareBytes Anti-Malware Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Malwarebytes\\Malwarebytes Anti-Malware\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:mbam\-log\-.*\.xml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MalwarebytesMalwareBytesAntiMalwareServiceLogs1(KapeTarget):
    name: ClassVar[str] = "MalwareBytes Anti-Malware Service Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Malwarebytes\\MBAMService\\logs\\"
    )
    regex: ClassVar[str] = r"(?s:mbamservice\.log.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MalwarebytesMalwareBytesAntiMalwareScanLogs2(KapeTarget):
    name: ClassVar[str] = "MalwareBytes Anti-Malware Scan Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Malwarebytes\\Malwarebytes Anti-Malware\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MalwarebytesMalwareBytesAntiMalwareScanResultsLogs3(KapeTarget):
    name: ClassVar[str] = "MalwareBytes Anti-Malware Scan Results Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Malwarebytes\\MBAMService\\ScanResults"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Malwarebytes(KapeTargetConfiguration):
    """
    Author: Drew Ervin & Kirtan Shah

    Version: 1.1

    ID: 3509c461-f6ef-499f-87e0-27bb30633259

    Malwarebytes Data
    """

    name: ClassVar[str] = "Malwarebytes"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        MalwarebytesMalwareBytesAntiMalwareLogs0,
        MalwarebytesMalwareBytesAntiMalwareServiceLogs1,
        MalwarebytesMalwareBytesAntiMalwareScanLogs2,
        MalwarebytesMalwareBytesAntiMalwareScanResultsLogs3,
    ]


class McAfeeMcAfeeDesktopProtectionLogsXP0(KapeTarget):
    name: ClassVar[str] = "McAfee Desktop Protection Logs XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\All Users\\Application Data\\McAfee\\DesktopProtection\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class McAfeeMcAfeeDesktopProtectionLogs1(KapeTarget):
    name: ClassVar[str] = "McAfee Desktop Protection Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\McAfee\\DesktopProtection\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class McAfeeMcAfeeEndpointSecurityLogs2(KapeTarget):
    name: ClassVar[str] = "McAfee Endpoint Security Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\McAfee\\Endpoint Security\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class McAfeeMcAfeeEndpointSecurityLogs3(KapeTarget):
    name: ClassVar[str] = "McAfee Endpoint Security Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\McAfee\\Endpoint Security\\Logs_Old\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class McAfeeMcAfeeVirusScanLogs4(KapeTarget):
    name: ClassVar[str] = "McAfee VirusScan Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Mcafee\\VirusScan\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class McAfee(KapeTargetConfiguration):
    """
    Author: Sam Smoker

    Version: 1.1

    ID: d2df019b-35d0-4f7b-8132-7500cbd39901

    McAfee Log Files
    """

    name: ClassVar[str] = "McAfee"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        McAfeeMcAfeeDesktopProtectionLogsXP0,
        McAfeeMcAfeeDesktopProtectionLogs1,
        McAfeeMcAfeeEndpointSecurityLogs2,
        McAfeeMcAfeeEndpointSecurityLogs3,
        McAfeeMcAfeeVirusScanLogs4,
    ]


class McAfeeePOMcAfeeePOLogs0(KapeTarget):
    name: ClassVar[str] = "McAfee ePO Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\McAfee\\Endpoint Security\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class McAfeeePO(KapeTargetConfiguration):
    """
    Author: Doug Metz

    Version: 1.0

    ID: 8e893785-6bf2-4990-a783-35b0f5e1b442

    McAfee ePO Log Files
    """

    name: ClassVar[str] = "McAfee_ePO"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [McAfeeePOMcAfeeePOLogs0]


class RogueKillerRogueKillerReports0(KapeTarget):
    name: ClassVar[str] = "RogueKiller Reports"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\RogueKiller\\logs\\")
    regex: ClassVar[str] = r"(?s:AdliceReport_.*\.json)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RogueKiller(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: 089b2afb-cc29-4565-9c2f-cbf0ba50f10d

    RogueKiller Anti-Malware (by Adlice Software)
    """

    name: ClassVar[str] = "RogueKiller"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [RogueKillerRogueKillerReports0]


class SecureAgeSecureAgeAntvirusLogs0(KapeTarget):
    name: ClassVar[str] = "SecureAge Antvirus Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\SecureAge Technology\\SecureAge\\log\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SecureAge(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 3876be71-fd3d-4455-bb70-80541370f2a0

    SecureAge Antivirus Logs
    """

    name: ClassVar[str] = "SecureAge"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [SecureAgeSecureAgeAntvirusLogs0]


class SentinelOneSentinelOneEDRLog0(KapeTarget):
    """
    Logs are in Binary Format (.binlog)
    """

    name: ClassVar[str] = "SentinelOne EDR Log"
    base_path: ClassVar[Path] = Path("C:\\programdata\\sentinel\\logs\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SentinelOne(KapeTargetConfiguration):
    """
    Author: Kirtan Shah

    Version: 1.0

    ID: b658aca2-8a69-440d-83ac-b81666a6484d

    Sentinel One Logs
    """

    name: ClassVar[str] = "SentinelOne"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [SentinelOneSentinelOneEDRLog0]


class SophosSophosLogsXP0(KapeTarget):
    """
    Includes Anti-Virus, Client Firewall, Data Control, Device Control, Endpoint
    Defense, Network Threat Detection, Management Communications System, Patch
    Control, Tamper Protection
    """

    name: ClassVar[str] = "Sophos Logs (XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\All Users\\Application Data\\Sophos\\Sophos *\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SophosSophosLogs1(KapeTarget):
    """
    Includes Anti-Virus, Client Firewall, Data Control, Device Control, Endpoint
    Defense, Network Threat Detection, Management Communications System, Patch
    Control, Tamper Protection
    """

    name: ClassVar[str] = "Sophos Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Sophos\\Sophos *\\Logs\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SophosSophosApplicationEvents2(KapeTarget):
    """
    Event source: Sophos Anti-Virus
    """

    name: ClassVar[str] = "Sophos Application Events"
    base_path: ClassVar[Path] = Path("ApplicationEvents.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Sophos(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: a50e5204-878e-4b5d-82fb-e6148d976bf7

    Sophos Data
    """

    name: ClassVar[str] = "Sophos"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SophosSophosLogsXP0,
        SophosSophosLogs1,
        SophosSophosApplicationEvents2,
    ]


class SUPERAntiSpywareSUPERAntiSpywareLogs0(KapeTarget):
    name: ClassVar[str] = "SUPERAntiSpyware Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\SUPERAntiSpyware\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUPERAntiSpyware(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: 0b2c9e30-8d85-43ea-aa26-b20503b8e1da

    SUPERAntiSpyware Data
    """

    name: ClassVar[str] = "SUPERAntiSpyware"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [SUPERAntiSpywareSUPERAntiSpywareLogs0]


class SymantecAVLogsSymantecEndpointProtectionLogsXP0(KapeTarget):
    name: ClassVar[str] = "Symantec Endpoint Protection Logs (XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\All Users\\Application Data\\Symantec\\Symantec Endpoint Protection\\Logs\\AV\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SymantecAVLogsSymantecEndpointProtectionLogs1(KapeTarget):
    name: ClassVar[str] = "Symantec Endpoint Protection Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Symantec\\Symantec Endpoint Protection\\*\\Data\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SymantecAVLogsSymantecEndpointProtectionUserLogs2(KapeTarget):
    name: ClassVar[str] = "Symantec Endpoint Protection User Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Symantec\\Symantec Endpoint Protection\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SymantecAVLogsSymantecEventLogWin73(KapeTarget):
    """
    Symantec specific Windows event log
    """

    name: ClassVar[str] = "Symantec Event Log Win7+"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\winevt\\logs\\")
    regex: ClassVar[str] = r"(?s:Symantec\ Endpoint\ Protection\ Client\.evtx)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SymantecAVLogsSymantecEventLogWin74(KapeTarget):
    """
    Symantec specific Windows event log
    """

    name: ClassVar[str] = "Symantec Event Log Win7+"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\winevt\\logs\\"
    )
    regex: ClassVar[str] = r"(?s:Symantec\ Endpoint\ Protection\ Client\.evtx)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SymantecAVLogsSymantecEndpointProtectionManagerSEPMApplicationEvents5(KapeTarget):
    """
    Contains SEPM entries, documented here:
    https://support.symantec.com/us/en/article.tech196455.html
    """

    name: ClassVar[str] = (
        "Symantec Endpoint Protection Manager (SEPM) Application Events"
    )
    base_path: ClassVar[Path] = Path("ApplicationEvents.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SymantecAVLogsSymantecEndpointProtectionQuarantineXP6(KapeTarget):
    name: ClassVar[str] = "Symantec Endpoint Protection Quarantine (XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\All Users\\Application Data\\Symantec\\Symantec Endpoint Protection\\Quarantine\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SymantecAVLogsSymantecEndpointProtectionQuarantine7(KapeTarget):
    name: ClassVar[str] = "Symantec Endpoint Protection Quarantine"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Symantec\\Symantec Endpoint Protection\\*\\Data\\Quarantine\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SymantecAVLogsccSubSDKDatabase8(KapeTarget):
    name: ClassVar[str] = "ccSubSDK Database"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Symantec\\Symantec Endpoint Protection\\*\\Data\\CmnClnt\\ccSubSDK\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SymantecAVLogsregistrationInfoxml9(KapeTarget):
    name: ClassVar[str] = "registrationInfo.xml"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Symantec\\Symantec Endpoint Protection\\*\\Data\\"
    )
    regex: ClassVar[str] = r"(?s:registrationInfo\.xml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SymantecAVLogs(KapeTargetConfiguration):
    """
    Author: Brian Maloney

    Version: 1.3

    ID: 5e750ea2-f6dc-4981-88d1-636ce042aa0d

    Symantec AV Logs
    """

    name: ClassVar[str] = "Symantec_AV_Logs"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SymantecAVLogsSymantecEndpointProtectionLogsXP0,
        SymantecAVLogsSymantecEndpointProtectionLogs1,
        SymantecAVLogsSymantecEndpointProtectionUserLogs2,
        SymantecAVLogsSymantecEventLogWin73,
        SymantecAVLogsSymantecEventLogWin74,
        SymantecAVLogsSymantecEndpointProtectionManagerSEPMApplicationEvents5,
        SymantecAVLogsSymantecEndpointProtectionQuarantineXP6,
        SymantecAVLogsSymantecEndpointProtectionQuarantine7,
        SymantecAVLogsccSubSDKDatabase8,
        SymantecAVLogsregistrationInfoxml9,
    ]


class TotalAVTotalAVLogs0(KapeTarget):
    name: ClassVar[str] = "TotalAV Logs"
    base_path: ClassVar[Path] = Path("C:\\Program Files*\\TotalAV\\logs")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TotalAVTotalAVLogs1(KapeTarget):
    name: ClassVar[str] = "TotalAV Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\TotalAV\\logs")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TotalAV(KapeTargetConfiguration):
    """
    Author: Kirtan Shah

    Version: 1.0

    ID: 8e5ca015-26e8-4993-8008-19421d15f35a

    TotalAV Antivirus Data
    """

    name: ClassVar[str] = "TotalAV"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        TotalAVTotalAVLogs0,
        TotalAVTotalAVLogs1,
    ]


class TrendMicroTrendMicroLogs0(KapeTarget):
    name: ClassVar[str] = "Trend Micro Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Trend Micro\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TrendMicroTrendMicroSecurityAgentReportLogs1(KapeTarget):
    name: ClassVar[str] = "Trend Micro Security Agent Report Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Program Files*\\Trend Micro\\Security Agent\\Report\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TrendMicroTrendMicroSecurityAgentConnectionLogs2(KapeTarget):
    name: ClassVar[str] = "Trend Micro Security Agent Connection Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Program Files*\\Trend Micro\\Security Agent\\ConnLog\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TrendMicro(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: 73f8ccea-61cf-4993-aa26-e5cad4f8cc8f

    Trend Micro Data
    """

    name: ClassVar[str] = "TrendMicro"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        TrendMicroTrendMicroLogs0,
        TrendMicroTrendMicroSecurityAgentReportLogs1,
        TrendMicroTrendMicroSecurityAgentConnectionLogs2,
    ]


class VIPREVIPREBusinessAgentLogs0(KapeTarget):
    name: ClassVar[str] = "VIPRE Business Agent Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\VIPRE Business Agent\\Logs\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VIPREVIPREBusinessUserLogsv71(KapeTarget):
    name: ClassVar[str] = "VIPRE Business User Logs (v7+)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\VIPRE Business\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VIPREVIPREBusinessUserLogsv5v62(KapeTarget):
    name: ClassVar[str] = "VIPRE Business User Logs (v5-v6)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\GFI Software\\AntiMalware\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VIPREVIPREBusinessUserLogsuptov43(KapeTarget):
    name: ClassVar[str] = "VIPRE Business User Logs (up to v4)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Sunbelt Software\\AntiMalware\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VIPRE(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: 8af4ffd8-264e-4c7d-aa28-8cc4f543b01d

    VIPRE Data
    """

    name: ClassVar[str] = "VIPRE"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        VIPREVIPREBusinessAgentLogs0,
        VIPREVIPREBusinessUserLogsv71,
        VIPREVIPREBusinessUserLogsv5v62,
        VIPREVIPREBusinessUserLogsuptov43,
    ]


class WebrootWebrootProgramData0(KapeTarget):
    name: ClassVar[str] = "Webroot Program Data"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\WRData\\")
    regex: ClassVar[str] = r"(?s:WRLog\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Webroot(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: c53c2b4e-075b-4162-b93e-aaf8c968e0b0

    Webroot Antivirus
    """

    name: ClassVar[str] = "Webroot"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [WebrootWebrootProgramData0]


class WinDefendDetectionHistDetectionHistory0(KapeTarget):
    name: ClassVar[str] = "DetectionHistory"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Microsoft\\Windows Defender\\Scans\\History\\Service\\DetectionHistory\\*\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WinDefendDetectionHist(KapeTargetConfiguration):
    """
    Author: Jordan Klepser

    Version: 1.1

    ID: a780af32-cb91-4e32-b946-0546cc123930

    Windows Defender Threat DetectionHistory files
    """

    name: ClassVar[str] = "WinDefendDetectionHist"
    recreate_directories: ClassVar[bool] = False
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WinDefendDetectionHistDetectionHistory0
    ]


class WindowsDefenderWindowsDefenderLogs0(KapeTarget):
    name: ClassVar[str] = "Windows Defender Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Microsoft\\Microsoft AntiMalware\\Support\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsDefenderWindowsDefenderEventLogs1(KapeTarget):
    name: ClassVar[str] = "Windows Defender Event Logs"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\winevt\\Logs\\")
    regex: ClassVar[str] = r"(?s:Microsoft\-Windows\-Windows\ Defender.*\.evtx)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsDefenderWindowsDefenderEventLogs2(KapeTarget):
    name: ClassVar[str] = "Windows Defender Event Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\winevt\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:Microsoft\-Windows\-Windows\ Defender.*\.evtx)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsDefenderWindowsDefenderLogs3(KapeTarget):
    name: ClassVar[str] = "Windows Defender Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Microsoft\\Windows Defender\\Support\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsDefenderWindowsDefenderLogs4(KapeTarget):
    name: ClassVar[str] = "Windows Defender Logs"
    base_path: ClassVar[Path] = Path("C:\\Windows\\Temp\\")
    regex: ClassVar[str] = r"(?s:MpCmdRun\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsDefenderWindowsDefenderLogs5(KapeTarget):
    name: ClassVar[str] = "Windows Defender Logs"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\Temp\\")
    regex: ClassVar[str] = r"(?s:MpCmdRun\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsDefender(KapeTargetConfiguration):
    """
    Author: Drew Ervin

    Version: 1.0

    ID: 061aa929-292b-4d7f-a4af-a3fe2673a3e5

    Windows Defender Data
    """

    name: ClassVar[str] = "WindowsDefender"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WindowsDefenderWindowsDefenderLogs0,
        WindowsDefenderWindowsDefenderEventLogs1,
        WindowsDefenderWindowsDefenderEventLogs2,
        WindowsDefenderWindowsDefenderLogs3,
        WindowsDefenderWindowsDefenderLogs4,
        WindowsDefenderWindowsDefenderLogs5,
    ]


class SANSTriageAntivirus0(KapeTarget):
    name: ClassVar[str] = "Antivirus"
    base_path: ClassVar[Path] = Path("Antivirus.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageCloudStorageMetadata1(KapeTarget):
    name: ClassVar[str] = "CloudStorage_Metadata"
    base_path: ClassVar[Path] = Path("CloudStorage_Metadata.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageCombinedLogs2(KapeTarget):
    name: ClassVar[str] = "CombinedLogs"
    base_path: ClassVar[Path] = Path("CombinedLogs.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageEvidenceOfExecution3(KapeTarget):
    name: ClassVar[str] = "EvidenceOfExecution"
    base_path: ClassVar[Path] = Path("EvidenceOfExecution.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageFileSystem4(KapeTarget):
    name: ClassVar[str] = "FileSystem"
    base_path: ClassVar[Path] = Path("FileSystem.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageLNKFilesAndJumpLists5(KapeTarget):
    name: ClassVar[str] = "LNKFilesAndJumpLists"
    base_path: ClassVar[Path] = Path("LNKFilesAndJumpLists.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageMessagingClients6(KapeTarget):
    name: ClassVar[str] = "MessagingClients"
    base_path: ClassVar[Path] = Path("MessagingClients.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageRecycleBinInfoFiles7(KapeTarget):
    name: ClassVar[str] = "RecycleBin_InfoFiles"
    base_path: ClassVar[Path] = Path("RecycleBin_InfoFiles.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageRegistryHives8(KapeTarget):
    name: ClassVar[str] = "RegistryHives"
    base_path: ClassVar[Path] = Path("RegistryHives.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageRemoteAccess9(KapeTarget):
    name: ClassVar[str] = "RemoteAccess"
    base_path: ClassVar[Path] = Path("RemoteAdmin.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageScheduledTasks10(KapeTarget):
    name: ClassVar[str] = "ScheduledTasks"
    base_path: ClassVar[Path] = Path("ScheduledTasks.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageSRUM11(KapeTarget):
    name: ClassVar[str] = "SRUM"
    base_path: ClassVar[Path] = Path("SRUM.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageSUM12(KapeTarget):
    name: ClassVar[str] = "SUM"
    base_path: ClassVar[Path] = Path("SUM.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageThumbCache13(KapeTarget):
    name: ClassVar[str] = "ThumbCache"
    base_path: ClassVar[Path] = Path("Thumbcache.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageWBEM14(KapeTarget):
    name: ClassVar[str] = "WBEM"
    base_path: ClassVar[Path] = Path("WBEM.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageWebBrowsers15(KapeTarget):
    name: ClassVar[str] = "WebBrowsers"
    base_path: ClassVar[Path] = Path("WebBrowsers.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageWindowsIndexSearch16(KapeTarget):
    name: ClassVar[str] = "WindowsIndexSearch"
    base_path: ClassVar[Path] = Path("WindowsIndexSearch.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriageWindowsTimeline17(KapeTarget):
    name: ClassVar[str] = "WindowsTimeline"
    base_path: ClassVar[Path] = Path("WindowsTimeline.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SANSTriage(KapeTargetConfiguration):
    """
    Author: Mark Hallman

    Version: 1.3

    ID: 1bfbd59d-6c58-4eeb-9da7-1d9612b79964

    SANS Triage Collection
    """

    name: ClassVar[str] = "!SANS_Triage"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SANSTriageAntivirus0,
        SANSTriageCloudStorageMetadata1,
        SANSTriageCombinedLogs2,
        SANSTriageEvidenceOfExecution3,
        SANSTriageFileSystem4,
        SANSTriageLNKFilesAndJumpLists5,
        SANSTriageMessagingClients6,
        SANSTriageRecycleBinInfoFiles7,
        SANSTriageRegistryHives8,
        SANSTriageRemoteAccess9,
        SANSTriageScheduledTasks10,
        SANSTriageSRUM11,
        SANSTriageSUM12,
        SANSTriageThumbCache13,
        SANSTriageWBEM14,
        SANSTriageWebBrowsers15,
        SANSTriageWindowsIndexSearch16,
        SANSTriageWindowsTimeline17,
    ]


class AntivirusAvast0(KapeTarget):
    name: ClassVar[str] = "Avast"
    base_path: ClassVar[Path] = Path("Avast.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusAVG1(KapeTarget):
    name: ClassVar[str] = "AVG"
    base_path: ClassVar[Path] = Path("AVG.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusAvira2(KapeTarget):
    name: ClassVar[str] = "Avira"
    base_path: ClassVar[Path] = Path("AviraAVLogs.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusBitdefender3(KapeTarget):
    name: ClassVar[str] = "Bitdefender"
    base_path: ClassVar[Path] = Path("Bitdefender.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusComboFix4(KapeTarget):
    name: ClassVar[str] = "ComboFix"
    base_path: ClassVar[Path] = Path("ComboFix.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusCybereason5(KapeTarget):
    name: ClassVar[str] = "Cybereason"
    base_path: ClassVar[Path] = Path("Cybereason.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusEmsisoft6(KapeTarget):
    name: ClassVar[str] = "Emsisoft"
    base_path: ClassVar[Path] = Path("Emsisoft.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusESET7(KapeTarget):
    name: ClassVar[str] = "ESET"
    base_path: ClassVar[Path] = Path("ESET.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusFSecure8(KapeTarget):
    name: ClassVar[str] = "FSecure"
    base_path: ClassVar[Path] = Path("FSecure.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusHitmanPro9(KapeTarget):
    name: ClassVar[str] = "HitmanPro"
    base_path: ClassVar[Path] = Path("HitmanPro.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusMalwarebytes10(KapeTarget):
    name: ClassVar[str] = "Malwarebytes"
    base_path: ClassVar[Path] = Path("Malwarebytes.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusMcAfee11(KapeTarget):
    name: ClassVar[str] = "McAfee"
    base_path: ClassVar[Path] = Path("McAfee.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusMcAfeeePO12(KapeTarget):
    name: ClassVar[str] = "McAfee ePO"
    base_path: ClassVar[Path] = Path("McAfee_ePO.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusRogueKiller13(KapeTarget):
    name: ClassVar[str] = "RogueKiller"
    base_path: ClassVar[Path] = Path("RogueKiller.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusSecureAge14(KapeTarget):
    name: ClassVar[str] = "SecureAge"
    base_path: ClassVar[Path] = Path("SecureAge.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusSentinelOne15(KapeTarget):
    name: ClassVar[str] = "SentinelOne"
    base_path: ClassVar[Path] = Path("SentinelOne.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusSophos16(KapeTarget):
    name: ClassVar[str] = "Sophos"
    base_path: ClassVar[Path] = Path("Sophos.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusSUPERAntiSpyware17(KapeTarget):
    name: ClassVar[str] = "SUPERAntiSpyware"
    base_path: ClassVar[Path] = Path("SUPERAntiSpyware.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusSymantec18(KapeTarget):
    name: ClassVar[str] = "Symantec"
    base_path: ClassVar[Path] = Path("Symantec_AV_Logs.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusTotalAV19(KapeTarget):
    name: ClassVar[str] = "TotalAV"
    base_path: ClassVar[Path] = Path("TotalAV.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusTrendMicro20(KapeTarget):
    name: ClassVar[str] = "TrendMicro"
    base_path: ClassVar[Path] = Path("TrendMicro.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusVIPRE21(KapeTarget):
    name: ClassVar[str] = "VIPRE"
    base_path: ClassVar[Path] = Path("VIPRE.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusWebroot22(KapeTarget):
    name: ClassVar[str] = "Webroot"
    base_path: ClassVar[Path] = Path("Webroot.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AntivirusWindowsDefender23(KapeTarget):
    name: ClassVar[str] = "Windows Defender"
    base_path: ClassVar[Path] = Path("WindowsDefender.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Antivirus(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.2

    ID: 280c6a63-f6ab-438a-b40b-ca42fa78315f

    Antivirus
    """

    name: ClassVar[str] = "Antivirus"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        AntivirusAvast0,
        AntivirusAVG1,
        AntivirusAvira2,
        AntivirusBitdefender3,
        AntivirusComboFix4,
        AntivirusCybereason5,
        AntivirusEmsisoft6,
        AntivirusESET7,
        AntivirusFSecure8,
        AntivirusHitmanPro9,
        AntivirusMalwarebytes10,
        AntivirusMcAfee11,
        AntivirusMcAfeeePO12,
        AntivirusRogueKiller13,
        AntivirusSecureAge14,
        AntivirusSentinelOne15,
        AntivirusSophos16,
        AntivirusSUPERAntiSpyware17,
        AntivirusSymantec18,
        AntivirusTotalAV19,
        AntivirusTrendMicro20,
        AntivirusVIPRE21,
        AntivirusWebroot22,
        AntivirusWindowsDefender23,
    ]
