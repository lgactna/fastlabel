"""
Auto-generated classes from the .mkape files for the FileKnowledge category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class SQLite3TeraCopyHistory(KapeModule):
    """
    Author: Kevin Pagano

    Version: 1.0

    ID: d77856a2-b657-4be7-88a8-5dffc32e8983

    Parses the history file databases for TeraCopy history
    """

    name: ClassVar[str] = "SQLite3_TeraCopy_History"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class SQLite3TeraCopyMain(KapeModule):
    """
    Author: Kevin Pagano

    Version: 1.0

    ID: 1ae7d97b-cb8e-4e29-8aec-3514f30e6919

    Parses the main.db for TeraCopy history
    """

    name: ClassVar[str] = "SQLite3_TeraCopy_Main"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class OneDriveExplorer(KapeModule):
    """
    Author: Brian Maloney

    Version: 1.1

    ID: 6a2d7872-9eeb-4614-9090-b61a9ada2bba

    OneDriveExplorer: process OneDrive .dat and .previous.dat files
    """

    name: ClassVar[str] = "OneDriveExplorer"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.HTML,
        KapeExportFormat.JSON,
    ]


class ThumbCacheViewer(KapeModule):
    """
    Author: Dennis Reneau

    Version: 1.0

    ID: 8896483c-563a-4a28-ad8a-07ba74a54a63

    thumbcache_viewer_cmd.exe: process Windows Thumbcache files
    """

    name: ClassVar[str] = "ThumbCacheViewer"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.HTML]


class VLSeeRecentVLCRecentFiles(KapeModule):
    """
    Author: Charlie Rubisoff

    Version: 1.0

    ID: 43632314-7e65-4730-91ac-b46e45487468

    VLC Recent Files Parser
    """

    name: ClassVar[str] = "VLSeeRecent_VLCRecentFiles"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]
