"""
Auto-generated classes from the YAML declarations in kaspersky_careto.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class KasperskyCaretoDarwinFile(GRRArtifactBase):
    """
    Kaspersky Careto Darwin file system indicators of compromise (IOCs).

    Reference URLs:
    https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/20133638/unveilingthemask_v1.0.pdf
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Applications/.DS_Store.app/**10",
                    "/Library/LaunchAgents/com.apple.launchport.plist",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["KasperskyCaretoDarwinFiles"]


class KasperskyCaretoWindowsRegistryValue(GRRArtifactBase):
    """
    Kaspersky Careto Windows Registry indicators of compromise (IOCs).

    Reference URLs:
    https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/20133638/unveilingthemask_v1.0.pdf
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\WindowsUpdate",
                        "value": "CISCNF4654",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\WindowsUpdate",
                        "value": "CISCNF0654",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\WindowsUpdate",
                        "value": "CISCNF4654",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\WindowsUpdate",
                        "value": "CISCNF0654",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\\\CLSID\\{ECD4FC4D-521C-11D0-B792-00A0C90312E1}",
                        "value": "InprocServer32",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\CLSID\\{E6BB64BE-0618-4353-9193-0AFE606D6F0C}",
                        "value": "InprocServer32",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = ["KasperskyCaretoWindowsRegKeys"]


class KasperskyCaretoWindowsFile(GRRArtifactBase):
    """
    Kaspersky Careto Windows file system indicators of compromise (IOCs).

    Reference URLs:
    https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/20133638/unveilingthemask_v1.0.pdf
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\awcodc32.dll",
                    "%%environ_systemroot%%\\System32\\awview32.dll",
                    "%%environ_systemroot%%\\System32\\c_50225.nls",
                    "%%environ_systemroot%%\\System32\\c_50227.nls",
                    "%%environ_systemroot%%\\System32\\c_50229.nls",
                    "%%environ_systemroot%%\\System32\\c_51932.nls",
                    "%%environ_systemroot%%\\System32\\c_51936.nls",
                    "%%environ_systemroot%%\\System32\\c_51949.nls",
                    "%%environ_systemroot%%\\System32\\c_51950.nls",
                    "%%environ_systemroot%%\\System32\\c_57002.nls",
                    "%%environ_systemroot%%\\System32\\c_57006.nls",
                    "%%environ_systemroot%%\\System32\\c_57008.nls",
                    "%%environ_systemroot%%\\System32\\c_57010.nls",
                    "%%environ_systemroot%%\\System32\\cdgext32.dll",
                    "%%environ_systemroot%%\\System32\\cdllait32.dll",
                    "%%environ_systemroot%%\\System32\\cdllait64.dll",
                    "%%environ_systemroot%%\\System32\\cdlluninstallsgh32.dll",
                    "%%environ_systemroot%%\\System32\\cdlluninstallsgh64.dll",
                    "%%environ_systemroot%%\\System32\\cdlluninstallws32.dll",
                    "%%environ_systemroot%%\\System32\\cdlluninstallws64.dll",
                    "%%environ_systemroot%%\\System32\\cfgbkmgrs.dll",
                    "%%environ_systemroot%%\\System32\\cfgmgr64.dll",
                    "%%environ_systemroot%%\\System32\\comsvrpcs.dll",
                    "%%environ_systemroot%%\\System32\\d3dx8_20.dll",
                    "%%environ_systemroot%%\\System32\\dllcomm.dll",
                    "%%environ_systemroot%%\\System32\\drivers\\wmimgr.sys",
                    "%%environ_systemroot%%\\System32\\drvinfo.bin",
                    "%%environ_systemroot%%\\System32\\FCache.bin",
                    "%%environ_systemroot%%\\System32\\FFExtendedCommand.dll",
                    "%%environ_systemroot%%\\System32\\gpktcsp32.dll",
                    "%%environ_systemroot%%\\System32\\HPQueue.bin",
                    "%%environ_systemroot%%\\System32\\LPQueue.bin",
                    "%%environ_systemroot%%\\System32\\mdwmnsp.dll",
                    "%%environ_systemroot%%\\System32\\mfcn30.dll",
                    "%%environ_systemroot%%\\System32\\nmwcdlog.dll",
                    "%%environ_systemroot%%\\System32\\objframe.dll",
                    "%%environ_systemroot%%\\System32\\rpcdist.dll",
                    "%%environ_systemroot%%\\System32\\scsvrft.dll",
                    "%%environ_systemroot%%\\System32\\sdptbw.dll",
                    "%%environ_systemroot%%\\System32\\shlink32.dll",
                    "%%environ_systemroot%%\\System32\\shlink64.dll",
                    "%%environ_systemroot%%\\System32\\siiw9x.dll",
                    "%%environ_systemroot%%\\System32\\skypeie6plugin.dll",
                    "%%environ_systemroot%%\\System32\\slbkbw.dll",
                    "%%environ_systemroot%%\\System32\\WifiScan.dll",
                    "%%environ_systemroot%%\\System32\\wmspdmgr.dll",
                    "%%users.appdata%%\\microsoft\\c_27803.nls",
                    "%%users.appdata%%\\microsoft\\objframe.dll",
                    "%%users.appdata%%\\microsoft\\shmgr.dll",
                    "%%users.temp%%\\~DF01AC74D8BE15EE01.tmp",
                    "%%users.temp%%\\~DF23BF45A473C42B56.tmp",
                    "%%users.temp%%\\~DF8471938479DA49221.tmp",
                    "%%users.temp%%\\~DFA0528CD81300F372.tmp",
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
    aliases: ClassVar[Optional[list[str]]] = ["KasperskyCaretoWindowsFiles"]


class KasperskyCaretoIndicators(GRRArtifactBase):
    """
    Kaspersky Careto indicators of compromise (IOCs).

    Reference URLs:
    https://media.kasperskycontenthub.com/wp-content/uploads/sites/43/2018/03/20133638/unveilingthemask_v1.0.pdf
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "KasperskyCaretoDarwinFile",
                    "KasperskyCaretoWindowsFile",
                    "KasperskyCaretoWindowsRegistryValue",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "KasperskyCaretoWindowsRegistryValue": KasperskyCaretoWindowsRegistryValue,
        "KasperskyCaretoWindowsFile": KasperskyCaretoWindowsFile,
        "KasperskyCaretoDarwinFile": KasperskyCaretoDarwinFile,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS,
        ArtifactSupportedOS.DARWIN,
    ]
    aliases: ClassVar[Optional[list[str]]] = None
