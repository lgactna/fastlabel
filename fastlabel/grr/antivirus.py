"""
Auto-generated classes from the YAML declarations in antivirus.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class Bit9LocalCache(GRRArtifactBase):
    """
    Bit9 local cache database.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_allusersappdata%%\\Bit9\\Parity Agent\\cache.*"],
                "separator": "\\",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class CrowdstrikeQuarantine(GRRArtifactBase):
    """
    Crowdstrike stores quarantined files encoded on disk.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Library/CS/Quarantine/*",
                    "/Library/Application Support/Crowdstrike/Falcon/Quarantine/*",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\drivers\\CrowdStrike\\Quarantine\\*"
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class CrowdstrikeAgentID(GRRArtifactBase):
    """
    Identifier of a CrowdStrike agent.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/Library/CS/registry.base"]},
            "supported_os": ["Darwin"],
        },
        {
            "type": "COMMAND",
            "attributes": {
                "args": ["-g", "--cid", "--aid"],
                "cmd": "/opt/CrowdStrike/falconctl",
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\CSAgent\\Sim",
                        "value": "AG",
                    }
                ]
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class EsetAVQuarantine(GRRArtifactBase):
    """
    Eset Anti-Virus Quarantine (Infected) files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/Library/Application Support/ESET/esets/cache/quarantine/*"]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersappdata%%\\ESET\\ESET NOD32 Antivirus\\Logs\\**"
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MicrosoftAVQuarantine(GRRArtifactBase):
    """
    Microsoft Anti-Virus Quarantine (Infected) files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersappdata%%\\Microsoft\\Microsoft Antimalware\\Quarantine\\**",
                    "%%environ_allusersappdata%%\\Microsoft\\Windows Defender\\Quarantine\\**",
                ],
                "separator": "\\",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MicrosoftAVLogs(GRRArtifactBase):
    """
    Microsoft Anti-Virus log files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersappdata%%\\Microsoft\\Windows AntiMalware\\Support\\MPDetection-*.log",
                    "%%environ_allusersappdata%%\\Microsoft\\Windows AntiMalware\\Support\\MPLog-*.log",
                    "%%environ_allusersappdata%%\\Microsoft\\Windows Defender\\Scans\\History\\Service\\DetectionHistory\\**",
                    "%%environ_allusersappdata%%\\Microsoft\\Windows Defender\\Support\\MPDetection-*.log",
                    "%%environ_allusersappdata%%\\Microsoft\\Windows Defender\\Support\\MPLog-*.log",
                    "%%environ_systemroot%%\\ServiceProfiles\\LocalService\\AppData\\Local\\Temp\\MpCmdRun.log",
                    "%%environ_systemroot%%\\Temp\\MpCmdRun.log",
                    "%%users.temp%%\\MpCmdRun.log",
                ],
                "separator": "\\",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsDefenderScanDetectionHistoryFiles(GRRArtifactBase):
    """
    Microsoft Windows Defender scan detection history files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersappdata%%\\Microsoft\\Windows Defender\\Scans\\History\\Service\\DetectionHistory\\*\\*-*-*-*"
                ],
                "separator": "\\",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsDefenderExclusions(GRRArtifactBase):
    """
    Directories, processes and extensions configured not to be scanned by
    Windows Defender. The can be set locally or through group policy objects
    (GPO).

    Certain malware families (for example, Tofsee) are known to add directories
    to the Paths list in order to avoid being detected by Windows Defender.
    Other malware (for example, REvil) use the existing exclusions to be ignored
    by Anti-Virus products.

    Reference URLs:
    https://blog.malwarebytes.com/detections/pum-optional-msexclusion/
    https://answers.microsoft.com/en-us/protect/forum/all/windows-defender-how-to-remove-exclusions/2a0cc465-97b2-46ea-ae77-b87075ed124e
    https://blog.talosintelligence.com/2019/05/threat-roundup-0503-0510.html
    https://news.sophos.com/en-us/2021/07/04/independence-day-revil-uses-supply-chain-exploit-to-attack-hundreds-of-businesses/
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows Defender\\Exclusions\\Paths\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows Defender\\Exclusions\\Processes\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows Defender\\Exclusions\\Extensions\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows Defender\\Exclusions\\TemporaryPaths\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows Defender\\Exclusions\\Paths\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows Defender\\Exclusions\\Processes\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows Defender\\Exclusions\\Extensions\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows Defender\\Exclusions\\TemporaryPaths\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SantaLogs(GRRArtifactBase):
    """
    Local Santa logs.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/var/db/santa/*", "/private/var/db/santa/*"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SophosAVLogs(GRRArtifactBase):
    """
    Sophos Anti-Virus log files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/Library/Logs/Sophos*.log"]},
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersappdata%%\\Sophos\\Sophos Anti-Virus\\Logs\\*"
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SophosAVQuarantine(GRRArtifactBase):
    """
    Sophos Anti-Virus Quarantine (Infected) files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/Users/Shared/Infected/*"]},
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersappdata%%\\Sophos\\Sophos Anti-Virus\\INFECTED\\*"
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SymantecAVLogs(GRRArtifactBase):
    """
    Symantec Anti-Virus Log Files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersappdata%%\\Symantec\\Symantec Endpoint Protection\\*\\Data\\Logs\\*.log",
                    "%%environ_allusersappdata%%\\Symantec\\Symantec Endpoint Protection\\*\\Data\\Logs\\AV\\*.log",
                    "%%environ_allusersappdata%%\\Symantec\\Symantec Endpoint Protection\\Logs\\AV\\*.log",
                    "%%users.localappdata%%\\Symantec\\Symantec Endpoint Protection\\Logs\\*.log",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SymantecAVQuarantine(GRRArtifactBase):
    """
    Symantec Anti-Virus quarantine (infected) and cloud submission files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersappdata%%\\Symantec\\Symantec Endpoint Protection\\**5\\*.vbn",
                    "%%environ_allusersappdata%%\\Symantec\\Symantec Endpoint Protection\\Quarantine\\**",
                    "%%environ_allusersappdata%%\\Symantec\\Symantec Endpoint Protection\\*\\Data\\Quarantine\\**",
                    "%%environ_allusersappdata%%\\Symantec\\Symantec Endpoint Protection\\*\\Data\\CmnClnt\\ccSubSDK\\**",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None
