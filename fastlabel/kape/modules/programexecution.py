"""
Auto-generated classes from the .mkape files for the ProgramExecution category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class AmcacheParser(KapeModule):
    """
    Author: Eric Zimmerman

    Version: 1.1

    ID: 4190c518-524f-4623-8038-a014784c018c

    AmcacheParser: extract program execution information
    """

    name: ClassVar[str] = "AmcacheParser"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class AppCompatCacheParser(KapeModule):
    """
    Author: Eric Zimmerman

    Version: 1.1

    ID: e5e0ffa8-fe3e-4196-ac5a-d21cbeb879c2

    AppCompatCacheParser: extract AppCompatCache (shimcache) information
    """

    name: ClassVar[str] = "AppCompatCacheParser"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class PECmd(KapeModule):
    """
    Author: Eric Zimmerman and Andrew Rathbun

    Version: 1.1

    ID: 7ef84a6b-5115-45bb-af2a-3249a3237e75

    PECmd: process prefetch files
    """

    name: ClassVar[str] = "PECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.HTML,
        KapeExportFormat.JSON,
    ]


class RecentFileCacheParser(KapeModule):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 32fa31cc-8be6-4a1d-917a-97fbdff552ef

    RecentFileCacheParser: extract file names from RecentFilecache.bcf
    """

    name: ClassVar[str] = "RecentFileCacheParser"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]


class CCMRUAFinderRecentlyUsedApps(KapeModule):
    """
    Author: Brian Maloney

    Version: 1.0

    ID: 591b2715-f4eb-47bd-9a6c-249b8c22aba1

    Extracts SCCM software metering RecentlyUsedApplication logs from
    OBJECTS.DATA files
    """

    name: ClassVar[str] = "CCMRUAFinder_RecentlyUsedApps"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TSV]
