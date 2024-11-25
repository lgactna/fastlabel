"""
Auto-generated classes from the YAML declarations in ics.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class WindowsSiemensWinCCLogFile(GRRArtifactBase):
    """
    Siemens WinCC software logs.

    Reference URLs:
    https://cache.industry.siemens.com/dl/files/865/109757865/att_963121/v5/109757865_WinCC_Diagnostics_en.pdf
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_programfiles%%\\Siemens\\WinCC\\Diagnose\\*",
                    "%%environ_programfiles%%\\Common Files\\Siemens\\ace\\bin\\Diagnosis\\*",
                    "%%environ_programfilesx86%%\\Siemens\\WinCC\\Diagnose\\*",
                    "%%environ_programfilesx86%%\\Common Files\\Siemens\\ace\\bin\\Diagnosis\\*",
                    "%%environ_windir%%\\security\\SecurityController\\*",
                    "%%environ_allusersappdata%%\\Siemens\\Automation\\Logfiles\\*",
                    "%%environ_allusersappdata%%\\Siemens\\Automation\\Logfiles\\Setup\\*",
                    "%%environ_allusersappdata%%\\Siemens\\Logs\\*",
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
