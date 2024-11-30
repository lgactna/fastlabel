"""
Auto-generated classes from the .tkape files for the ApplicationCompatability category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class RecentFileCacheRecentFileCache0(KapeTarget):
    name: ClassVar[str] = "RecentFileCache"
    base_path: ClassVar[Path] = Path("C:\\Windows\\AppCompat\\Programs\\")
    file_mask: ClassVar[str] = "RecentFileCache.bcf"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RecentFileCacheRecentFileCache1(KapeTarget):
    name: ClassVar[str] = "RecentFileCache"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\AppCompat\\Programs\\")
    file_mask: ClassVar[str] = "RecentFileCache.bcf"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RecentFileCache(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 0d93d3fc-1b09-4894-b21f-dddc7f269934

    RecentFileCache
    """

    name: ClassVar[str] = "RecentFileCache"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RecentFileCacheRecentFileCache0,
        RecentFileCacheRecentFileCache1,
    ]
