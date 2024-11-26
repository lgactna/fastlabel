"""
Auto-generated classes from the .tkape files for the Disk Images category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class VirtualDisksVHD0(KapeTarget):
    name: ClassVar[str] = "VHD"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.VHD)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualDisksVHDX1(KapeTarget):
    name: ClassVar[str] = "VHDX"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.VHDX)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualDisksVDI2(KapeTarget):
    name: ClassVar[str] = "VDI"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.VDI)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualDisksVMDK3(KapeTarget):
    name: ClassVar[str] = "VMDK"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.VMDK)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualDisks(KapeTargetConfiguration):
    """
    Author: Phill Moore

    Version: 1.0

    ID: 283fd2b7-b914-4683-85b4-40dd3fefecbb

    Virtual Disks
    """

    name: ClassVar[str] = "VirtualDisks"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        VirtualDisksVHD0,
        VirtualDisksVHDX1,
        VirtualDisksVDI2,
        VirtualDisksVMDK3,
    ]
