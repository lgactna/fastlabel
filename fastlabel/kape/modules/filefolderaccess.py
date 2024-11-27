"""
Auto-generated classes from the .mkape files for the FileFolderAccess category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class JLECmd(KapeModule):
    """
    Author: Eric Zimmerman

    Version: 1.1

    ID: 81fe4336-eb10-4733-a770-cb57ec9bd108

    JLECmd: process jumplist files
    """

    name: ClassVar[str] = "JLECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.HTML,
        KapeExportFormat.JSON,
    ]


class LECmd(KapeModule):
    """
    Author: Eric Zimmerman

    Version: 1.1

    ID: 1b66f0e2-2ccf-449c-ae02-a1b3dc59df08

    LECmd: process .lnk files
    """

    name: ClassVar[str] = "LECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.HTML,
        KapeExportFormat.JSON,
    ]


class SBECmd(KapeModule):
    """
    Author: Barrie Hill

    Version: 1.0

    ID: fe12cf94-dad8-4f1a-b09d-3e64614fe2de

    SBECmd: process shellbags
    """

    name: ClassVar[str] = "SBECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class WxTCmd(KapeModule):
    """
    Author: Mike Cary

    Version: 1.0

    ID: 47b717ab-9a2f-4eb6-a79f-9f56b2c076c4

    WxTCmd.exe: process Windows Timeline/Activities Cache files
    """

    name: ClassVar[str] = "WxTCmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
