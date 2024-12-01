"""
Auto-generated classes from the .mkape files for the ProgramExecution category.

This file was generated using the `generate_kape.py` script.
"""

import csv
from pathlib import Path
from typing import ClassVar, Optional

from pydantic import AwareDatetime, BaseModel

from fastlabel.kape.core import KapeExportFormat, KapeModule
from fastlabel.kape.util import ez_to_aware_datetime


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


class PrefetchTimelineEntry(BaseModel):
    """
    A single entry from the PECmd_Output_Timeline.csv file.
    """

    run_time: AwareDatetime
    executable_name: str

    @classmethod
    def from_csv_line(cls, line: list[str]) -> "PrefetchTimelineEntry":
        """
        Parse a single line from the PECmd_Output_Timeline.csv file.
        """
        return cls(run_time=ez_to_aware_datetime(line[0]), executable_name=line[1])

    @classmethod
    def from_csv_file(cls, path: Path) -> list["PrefetchTimelineEntry"]:
        """
        Parse a PECmd_Output_Timeline.csv file.
        """
        csv.field_size_limit(2147483647)
        with open(path, "r") as f:
            reader = csv.reader(f)
            # Skip the header
            next(reader)
            # Read the rest of the lines
            return [cls.from_csv_line(line) for line in reader]


class PrefetchOutputEntry(BaseModel):
    """
    A single entry from the PECmd_Output_Prefetch.csv file.
    """

    note: Optional[str] = None
    source_file: Path
    source_create_time: AwareDatetime
    source_modify_time: AwareDatetime
    source_access_time: AwareDatetime
    executable_name: str
    hash: str
    size: int
    version: str
    run_count: int
    run_times: list[AwareDatetime]
    vol_0_name: str
    vol_0_serial: str
    vol_0_created: AwareDatetime
    vol_1_name: Optional[str] = None
    vol_1_serial: Optional[str] = None
    vol_1_created: Optional[AwareDatetime] = None
    directories: list[Path]
    files_loaded: list[Path]
    parsing_error: bool

    @classmethod
    def from_csv_line(cls, line: list[str]) -> "PrefetchOutputEntry":
        """
        Parse a single line from the PECmd_Output_Prefetch.csv file.
        """
        return cls(
            note=line[0],
            source_file=Path(line[1]),
            source_create_time=ez_to_aware_datetime(line[2]),
            source_modify_time=ez_to_aware_datetime(line[3]),
            source_access_time=ez_to_aware_datetime(line[4]),
            executable_name=line[5],
            hash=line[6],
            size=int(line[7]),
            version=line[8],
            run_count=int(line[9]),
            run_times=[ez_to_aware_datetime(x) for x in line[10:18] if x],
            vol_0_name=line[18],
            vol_0_serial=line[19],
            vol_0_created=ez_to_aware_datetime(line[20]),
            vol_1_name=line[21] if line[21] else None,
            vol_1_serial=line[22] if line[22] else None,
            vol_1_created=ez_to_aware_datetime(line[23]) if line[23] else None,
            directories=[Path(x.strip()) for x in line[24].split(",")],
            files_loaded=[Path(x.strip()) for x in line[25].split(",")],
            parsing_error=line[26] == "True",
        )

    @classmethod
    def from_csv_file(cls, path: Path) -> list["PrefetchOutputEntry"]:
        """
        Parse a PECmd_Output_Prefetch.csv file.
        """
        csv.field_size_limit(2147483647)
        with open(path, "r") as f:
            reader = csv.reader(f)
            # Skip the header
            next(reader)
            # Read the rest of the lines
            return [cls.from_csv_line(line) for line in reader]


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

    timeline_entries: list[PrefetchTimelineEntry] = []
    output_entries: list[PrefetchOutputEntry] = []

    @classmethod
    def scan_module_destination(cls, module_destination: Path) -> "PECmd":
        # PECmd normally places its output in the ProgramExecution folder relative
        # to the module destination, but I don't know if that assumption is airtight
        obj = cls()

        try:
            timeline_path = next(
                module_destination.rglob("*_PECmd_Output_Timeline.csv")
            )
            obj.timeline_entries = PrefetchTimelineEntry.from_csv_file(timeline_path)
        except StopIteration:
            pass

        try:
            output_path = next(module_destination.rglob("*_PECmd_Output.csv"))
            obj.output_entries = PrefetchOutputEntry.from_csv_file(output_path)
        except StopIteration:
            pass

        return obj


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
