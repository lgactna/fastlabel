"""
Auto-generated classes from the YAML declarations in applications.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class GnomeEvolution(GRRArtifactBase):
    """
    Gnome Evolution files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.cache/evolution/**",
                    "%%users.homedir%%/.config/evolution/**",
                    "%%users.homedir%%/.local/share/evolution/**",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MicrosoftOfficeAutosave(GRRArtifactBase):
    """
    Automatically created Microsoft Office recovery files.

    Reference URLs: https://forensics.wiki/windows#microsoft-office-autosave
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Microsoft\\Word\\**",
                    "%%users.appdata%%\\Microsoft\\Excel\\**",
                    "%%users.appdata%%\\Microsoft\\Powerpoint\\**",
                    "%%users.appdata%%\\Microsoft\\Publisher\\**",
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
    aliases: ClassVar[Optional[list[str]]] = ["WindowsMsOfficeAutosave"]


class MicrosoftOfficeMRU(GRRArtifactBase):
    """
    Microsoft Office Most Recently Used

    Reference URLs: https://github.com/mac4n6/macMRU-Parser
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Preferences/com.microsoft.office.plist",
                    "%%users.homedir%%/Library/Containers/com.microsoft.*/Data/Library/Preferences/com.microsoft.*.securebookmarks.plist",
                ],
                "separator": "/",
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Office\\*\\*\\File MRU",
                        "value": "Item *",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Office\\*\\*\\Place MRU",
                        "value": "Item *",
                    },
                ]
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


class MicrosoftOutlookPABFiles(GRRArtifactBase):
    """
    Microsoft Outlook PAB Files

    Reference URLs: https://forensics.wiki/personal_folder_file_(pab,_pst,_ost)
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Microsoft\\Outlook\\*.pab",
                    "%%users.userprofile%%\\Documents\\Outlook Files\\*.pab",
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


class MicrosoftOutlookPSTFiles(GRRArtifactBase):
    """
    Microsoft Outlook PST Files

    Reference URLs: https://forensics.wiki/personal_folder_file_(pab,_pst,_ost)
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Microsoft\\Outlook\\*.pst",
                    "%%users.userprofile%%\\Documents\\Outlook Files\\*.pst",
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


class MicrosoftOutlookOSTFiles(GRRArtifactBase):
    """
    Microsoft Outlook OST Files

    Reference URLs: https://forensics.wiki/personal_folder_file_(pab,_pst,_ost)
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Microsoft\\Outlook\\*.ost",
                    "%%users.userprofile%%\\Documents\\Outlook Files\\*.ost",
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


class NodeJSPackageManagerCacheFiles(GRRArtifactBase):
    """
    Node JS package manager (NPM) cache files

    Reference URLs: https://docs.npmjs.com/cli/cache
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/.npm/*"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.appdata%%\\npm-cache\\*"],
                "separator": "\\",
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


class WinRARExternalViewer(GRRArtifactBase):
    """
    Executable run when a file is opened by WinRAR inside an archive.

    Reference URLs:
    http://www.hexacorn.com/blog/2012/09/16/beyond-good-ol-run-key-part-2/
    http://acritum.com/software/manuals/winrar/html/helpinterfaceviewing.htm
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\WinRAR\\Viewer\\",
                        "value": "ExternalViewer",
                    }
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


class WinRARAVScan(GRRArtifactBase):
    """
    Executable run to scan a file when it is opened by WinRAR.

    Reference URLs:
    http://www.hexacorn.com/blog/2012/09/16/beyond-good-ol-run-key-part-2/
    http://acritum.com/software/manuals/winrar/html/helpcommandsvirusscan.htm
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\WinRAR\\VirusScan\\",
                        "value": "Name",
                    }
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


class MicrosoftSqlServerErrorLogs(GRRArtifactBase):
    """
    Microsoft SQL Server's error log files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_programfiles%%\\Microsoft SQL Server\\*\\MSSQL\\LOG\\ERRORLOG*",
                    "%%environ_programfilesx86%%\\Microsoft SQL Server\\*\\MSSQL\\LOG\\ERRORLOG*",
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


class MozillaThunderbird(GRRArtifactBase):
    """
    Mozilla Thunderbird files.
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["%%users.homedir%%/.thunderbird/**"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None
