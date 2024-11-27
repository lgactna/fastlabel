"""
Auto-generated classes from the .mkape files for the SQLDatabases category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class SQLECmd(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: f9198051-4899-465d-aa5a-8291525d82b1

    SQLECmd: process SQLite databases
    """

    name: ClassVar[str] = "SQLECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]


class SQLECmdHunt(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 74343dd0-47bf-406d-9173-fb626e38cc50

    SQLECmd: process SQLite databases with Hunt mode
    """

    name: ClassVar[str] = "SQLECmd_Hunt"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]
