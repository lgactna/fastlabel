"""
Auto-generated classes from the .tkape files for the FileDeletion category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class RecycleBinRecycleBinInfoFiles0(KapeTarget):
    name: ClassVar[str] = "RecycleBin_InfoFiles"
    base_path: ClassVar[Path] = Path("RecycleBin_InfoFiles.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RecycleBinRecycleBinDataFiles1(KapeTarget):
    name: ClassVar[str] = "RecycleBin_DataFiles"
    base_path: ClassVar[Path] = Path("RecycleBin_DataFiles.tkape")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RecycleBin(KapeTargetConfiguration):
    """
    Author: Mark Hallman / Joshua Hickman

    Version: 2.0

    ID: afac78f5-a5bc-475d-9c67-649456dc4dc2

    Recycle Bin DataAndInfo
    """

    name: ClassVar[str] = "RecycleBin"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RecycleBinRecycleBinInfoFiles0,
        RecycleBinRecycleBinDataFiles1,
    ]


class RecycleBinDataFilesRecycleBinWindowsVista0(KapeTarget):
    name: ClassVar[str] = "Recycle Bin - Windows Vista+"
    base_path: ClassVar[Path] = Path("C:\\$Recycle.Bin\\")
    file_mask: ClassVar[str] = "$R*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RecycleBinDataFilesRecycleBinWindowsVista1(KapeTarget):
    name: ClassVar[str] = "Recycle Bin - Windows Vista+"
    base_path: ClassVar[Path] = Path("C:\\$Recycle.Bin\\*\\$R*\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RecycleBinDataFilesRECYCLERWinXP2(KapeTarget):
    name: ClassVar[str] = "RECYCLER - WinXP"
    base_path: ClassVar[Path] = Path("C:\\RECYCLE*\\")
    file_mask: ClassVar[str] = "D*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RecycleBinDataFiles(KapeTargetConfiguration):
    """
    Author: Joshua Hickman, Andreas Hunkeler (@Karneades), Brian Maloney

    Version: 1.2

    ID: bb5785ec-0e6e-42f9-97ca-94ef12720827

    Recycle Bin Data Files
    """

    name: ClassVar[str] = "RecycleBin_DataFiles"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RecycleBinDataFilesRecycleBinWindowsVista0,
        RecycleBinDataFilesRecycleBinWindowsVista1,
        RecycleBinDataFilesRECYCLERWinXP2,
    ]


class RecycleBinInfoFilesRecycleBinWindowsVista0(KapeTarget):
    name: ClassVar[str] = "Recycle Bin - Windows Vista+"
    base_path: ClassVar[Path] = Path("C:\\$Recycle.Bin\\")
    file_mask: ClassVar[str] = "$I*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RecycleBinInfoFilesRECYCLERWinXP1(KapeTarget):
    name: ClassVar[str] = "RECYCLER - WinXP"
    base_path: ClassVar[Path] = Path("C:\\RECYCLE*\\")
    file_mask: ClassVar[str] = "INFO2"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RecycleBinInfoFiles(KapeTargetConfiguration):
    """
    Author: Joshua Hickman, Andreas Hunkeler (@Karneades)

    Version: 1.0

    ID: 6205454f-fcaa-4ace-a7b5-33c4e40b156a

    Recycle Bin Info Files
    """

    name: ClassVar[str] = "RecycleBin_InfoFiles"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RecycleBinInfoFilesRecycleBinWindowsVista0,
        RecycleBinInfoFilesRECYCLERWinXP1,
    ]
