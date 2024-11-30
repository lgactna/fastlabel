"""
Auto-generated classes from the .tkape files for the File Downloads category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class FreenetFreenet0(KapeTarget):
    name: ClassVar[str] = "Freenet"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Freenet\\")
    file_mask: ClassVar[str] = "node*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreenetFreenet1(KapeTarget):
    name: ClassVar[str] = "Freenet"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Freenet\\")
    file_mask: ClassVar[str] = "*completed.list.downloads"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreenetFreenet2(KapeTarget):
    name: ClassVar[str] = "Freenet"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Freenet\\")
    file_mask: ClassVar[str] = "*completed.list.uploads"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreenetFreenet3(KapeTarget):
    name: ClassVar[str] = "Freenet"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Freenet\\")
    file_mask: ClassVar[str] = "*.bak"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreenetFreenet4(KapeTarget):
    name: ClassVar[str] = "Freenet"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Freenet\\downloads\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Freenet(KapeTargetConfiguration):
    """
    Author: Charlie Rubisoff

    Version: 1.0

    ID: dbf16082-0a99-4d3e-b24d-5fb20a1bd914

    Freenet
    """

    name: ClassVar[str] = "Freenet"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        FreenetFreenet0,
        FreenetFreenet1,
        FreenetFreenet2,
        FreenetFreenet3,
        FreenetFreenet4,
    ]
