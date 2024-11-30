"""
Auto-generated classes from the .tkape files for the ApplicationCompatibility category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class AmcacheAmcache0(KapeTarget):
    name: ClassVar[str] = "Amcache"
    base_path: ClassVar[Path] = Path("C:\\Windows\\AppCompat\\Programs\\")
    file_mask: ClassVar[str] = "Amcache.hve"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AmcacheAmcache1(KapeTarget):
    name: ClassVar[str] = "Amcache"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\AppCompat\\Programs\\")
    file_mask: ClassVar[str] = "Amcache.hve"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AmcacheAmcachetransactionfiles2(KapeTarget):
    name: ClassVar[str] = "Amcache transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\AppCompat\\Programs\\")
    file_mask: ClassVar[str] = "Amcache.hve.LOG*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AmcacheAmcachetransactionfiles3(KapeTarget):
    name: ClassVar[str] = "Amcache transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\AppCompat\\Programs\\")
    file_mask: ClassVar[str] = "Amcache.hve.LOG*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Amcache(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 13ba1e33-4899-4843-adf1-c7e6b20d759a

    Amcache.hve
    """

    name: ClassVar[str] = "Amcache"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        AmcacheAmcache0,
        AmcacheAmcache1,
        AmcacheAmcachetransactionfiles2,
        AmcacheAmcachetransactionfiles3,
    ]
