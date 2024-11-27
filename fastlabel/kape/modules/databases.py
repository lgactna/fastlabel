"""
Auto-generated classes from the .mkape files for the Databases category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class LevelDBDumper(KapeModule):
    """
    Author: Matt Dawson

    Version: 1.1

    ID: 3a88b531-705b-487d-933c-75ce0921a656

    Dumps LevelDB Key/Value databases
    """

    name: ClassVar[str] = "LevelDBDumper"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]


class TeamsParser(KapeModule):
    """
    Author: Pedro Sanchez Cordero (conexioninversa)

    Version: 1.0

    ID: a099aa6f-fbd7-48a2-a4cb-da41100d2755

    Forensic open-source parser that allows extracting the messages, comments,
    posts, contacts, calendar entries and reactions from a Microsoft Teams
    IndexedDB LevelDB database.
    """

    name: ClassVar[str] = "TeamsParser"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]
