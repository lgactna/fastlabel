"""
Auto-generated classes from the .tkape files for the FileFolderAccess category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class WindowsTimelineActivitiesCachedb0(KapeTarget):
    name: ClassVar[str] = "ActivitiesCache.db"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\ConnectedDevicesPlatform\\*\\"
    )
    regex: ClassVar[str] = r"(?s:ActivitiesCache\.db.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsTimeline(KapeTargetConfiguration):
    """
    Author: Lee Whitfield

    Version: 1.0

    ID: 8315040f-c9a4-455a-b02c-96372583f436

    ActivitiesCache.db collector
    """

    name: ClassVar[str] = "WindowsTimeline"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [WindowsTimelineActivitiesCachedb0]
