"""
Auto-generated classes from the .tkape files for the Prefetch category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration
from fastlabel.kape.modules import programexecution
from fastlabel.uco import observable
from fastlabel.uco.core import UcoObject


class EvidenceOfExecutionPrefetch0(KapeTarget):
    name: ClassVar[str] = "Prefetch"
    base_path: ClassVar[Path] = Path("Prefetch.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EvidenceOfExecutionRecentFileCache1(KapeTarget):
    name: ClassVar[str] = "RecentFileCache"
    base_path: ClassVar[Path] = Path("RecentFileCache.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EvidenceOfExecutionAmcache2(KapeTarget):
    name: ClassVar[str] = "Amcache"
    base_path: ClassVar[Path] = Path("Amcache.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EvidenceOfExecutionSyscache3(KapeTarget):
    name: ClassVar[str] = "Syscache"
    base_path: ClassVar[Path] = Path("Syscache.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EvidenceOfExecution(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 13ba1e33-4899-4843-adf0-c7e6a20d758a

    Evidence of execution related files
    """

    name: ClassVar[str] = "EvidenceOfExecution"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        EvidenceOfExecutionPrefetch0,
        EvidenceOfExecutionRecentFileCache1,
        EvidenceOfExecutionAmcache2,
        EvidenceOfExecutionSyscache3,
    ]


def prefetch_output_entries_to_case(
    output_entries: list[programexecution.PrefetchOutputEntry],
) -> list[UcoObject]:
    # This is the same between PrefetchPrefetch0 and PrefetchPrefetch1
    observables: list[UcoObject] = []

    for prefetch_entry in output_entries:
        root = observable.WindowsPrefetch()

        file_facet = observable.FileFacet(
            isDirectory=False,
            accessedTime=prefetch_entry.source_access_time,
            observableCreatedTime=prefetch_entry.source_create_time,
            modifiedTime=prefetch_entry.source_modify_time,
            fileName=prefetch_entry.source_file.name,
            filePath=str(prefetch_entry.source_file.parent),
            extension=prefetch_entry.source_file.suffix.lstrip("."),
        )

        directory_objs: list[observable.ObservableObject] = []
        for directory in prefetch_entry.directories:
            directory_objs.append(
                observable.File(
                    hasFacet=[
                        observable.FileFacet(isDirectory=True, fileName=str(directory))
                    ]
                )
            )
        file_objs: list[observable.ObservableObject] = []
        for file in prefetch_entry.files_loaded:
            file_objs.append(
                observable.File(
                    hasFacet=[
                        observable.FileFacet(isDirectory=False, fileName=str(file))
                    ]
                )
            )

        # TODO: volume not supported because I'm not sure what that looks like
        prefetch_facet = observable.WindowsPrefetchFacet(
            accessedDirectory=directory_objs,
            accessedFile=file_objs,
            firstRun=sorted(prefetch_entry.run_times)[0],
            lastRun=sorted(prefetch_entry.run_times)[-1],
            timesExecuted=prefetch_entry.run_count,
            applicationFileName=prefetch_entry.executable_name,
            prefetchHash=prefetch_entry.hash,
        )

        root.hasFacet = [file_facet, prefetch_facet]
        observables.append(root)

    return observables


class PrefetchPrefetch0(KapeTarget):
    name: ClassVar[str] = "Prefetch"
    base_path: ClassVar[Path] = Path("C:\\Windows\\prefetch\\")
    file_mask: ClassVar[str] = "*.pf"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = [programexecution.PECmd]

    # Add any instance variables specific to this target as Pydantic fields here.
    timeline_entries: list[programexecution.PrefetchTimelineEntry] = []
    output_entries: list[programexecution.PrefetchOutputEntry] = []

    @classmethod
    def run_modules_on_module_dest(
        cls, module_destination: Path
    ) -> "PrefetchPrefetch0":
        data = programexecution.PECmd.scan_module_destination(module_destination)
        return cls(
            timeline_entries=data.timeline_entries,
            output_entries=data.output_entries,
        )

    def to_case_objects(self) -> list[UcoObject]:
        return prefetch_output_entries_to_case(self.output_entries)


class PrefetchPrefetch1(KapeTarget):
    name: ClassVar[str] = "Prefetch"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\prefetch\\")
    file_mask: ClassVar[str] = "*.pf"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = [programexecution.PECmd]

    # Add any instance variables specific to this target as Pydantic fields here.
    timeline_entries: list[programexecution.PrefetchTimelineEntry] = []
    output_entries: list[programexecution.PrefetchOutputEntry] = []

    @classmethod
    def run_modules_on_module_dest(
        cls, module_destination: Path
    ) -> "PrefetchPrefetch1":
        data = programexecution.PECmd.scan_module_destination(module_destination)
        return cls(
            timeline_entries=data.timeline_entries,
            output_entries=data.output_entries,
        )

    def to_case_objects(self) -> list[UcoObject]:
        return prefetch_output_entries_to_case(self.output_entries)


class Prefetch(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: f6715d3f-b8ca-4cc2-9e5e-4ed18e88abbe

    Prefetch files
    """

    name: ClassVar[str] = "Prefetch"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [PrefetchPrefetch0, PrefetchPrefetch1]
