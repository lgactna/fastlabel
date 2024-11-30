"""
Auto-generated classes from the .tkape files for the FileMetadata category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class SignatureCatalogSignatureCatalog0(KapeTarget):
    name: ClassVar[str] = "SignatureCatalog"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\CatRoot\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SignatureCatalogSignatureCatalog1(KapeTarget):
    name: ClassVar[str] = "SignatureCatalog"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\CatRoot\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SignatureCatalog(KapeTargetConfiguration):
    """
    Author: Mike Pilkington

    Version: 1.0

    ID: 953b16e8-69ea-4967-9f9b-bcfa4f4fbe7b

    Obtain detached signature catalog files
    """

    name: ClassVar[str] = "SignatureCatalog"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SignatureCatalogSignatureCatalog0,
        SignatureCatalogSignatureCatalog1,
    ]
