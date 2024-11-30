"""
Auto-generated classes from the .tkape files for the Prefetch category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


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


class PrefetchPrefetch0(KapeTarget):
    name: ClassVar[str] = "Prefetch"
    base_path: ClassVar[Path] = Path("C:\\Windows\\prefetch\\")
    file_mask: ClassVar[str] = "*.pf"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class PrefetchPrefetch1(KapeTarget):
    name: ClassVar[str] = "Prefetch"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\prefetch\\")
    file_mask: ClassVar[str] = "*.pf"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


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
