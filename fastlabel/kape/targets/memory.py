"""
Auto-generated classes from the .tkape files for the Memory category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class VirtualBoxMemoryVirtualBox0(KapeTarget):
    """
    Captures all partial memory images from VirtualBox.
    """

    name: ClassVar[str] = "VirtualBox"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.sav)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualBoxMemory(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 4af61e3f-7fa7-4c59-a6d7-a495582fbb56

    VirtualBox - Memory
    """

    name: ClassVar[str] = "VirtualBoxMemory"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [VirtualBoxMemoryVirtualBox0]


class VMwareMemoryVMwareFusionWorkstationServerPlayer0(KapeTarget):
    """
    Captures all raw memory from VMware virtual machines.
    """

    name: ClassVar[str] = "VMware (Fusion/Workstation/Server/Player)"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.vmem)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VMwareMemoryVMwareFusionWorkstationServerPlayer1(KapeTarget):
    """
    Captures all memory images from VMware virtual machines.
    """

    name: ClassVar[str] = "VMware (Fusion/Workstation/Server/Player)"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.vmss)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VMwareMemoryVMwareFusionWorkstationServerPlayer2(KapeTarget):
    """
    Captures all memory images from VMware virtual machines.
    """

    name: ClassVar[str] = "VMware (Fusion/Workstation/Server/Player)"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.vmsn)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VMwareMemory(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 45945262-2e36-47c7-a36f-3cf4124dbe63

    VMware - Virtual Machine Memory
    """

    name: ClassVar[str] = "VMwareMemory"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        VMwareMemoryVMwareFusionWorkstationServerPlayer0,
        VMwareMemoryVMwareFusionWorkstationServerPlayer1,
        VMwareMemoryVMwareFusionWorkstationServerPlayer2,
    ]


class MemoryFileshiberfilsys0(KapeTarget):
    name: ClassVar[str] = "hiberfil.sys"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:hiberfil\.sys)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MemoryFilespagefilesys1(KapeTarget):
    name: ClassVar[str] = "pagefile.sys"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:pagefile\.sys)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MemoryFilesswapfilesys2(KapeTarget):
    name: ClassVar[str] = "swapfile.sys"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:swapfile\.sys)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MemoryFilesSmallMemoryDumpdirectory3(KapeTarget):
    """

    https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/small-memory-dump
    """

    name: ClassVar[str] = "Small Memory Dump directory"
    base_path: ClassVar[Path] = Path("C:\\Windows\\Minidump\\")
    regex: ClassVar[str] = r"(?s:.*\.dmp)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MemoryFilesSmallMemoryDumpdirectory4(KapeTarget):
    """

    https://docs.microsoft.com/en-us/windows-hardware/drivers/debugger/small-memory-dump
    """

    name: ClassVar[str] = "Small Memory Dump directory"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\Minidump\\")
    regex: ClassVar[str] = r"(?s:.*\.dmp)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MemoryFiles(KapeTargetConfiguration):
    """
    Author: Ahmed Elshaer, Teo Kia Meng

    Version: 1.0

    ID: d9e7fc93-7b63-4286-aa05-27ce3437c9c0

    Memory Files
    """

    name: ClassVar[str] = "MemoryFiles"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        MemoryFileshiberfilsys0,
        MemoryFilespagefilesys1,
        MemoryFilesswapfilesys2,
        MemoryFilesSmallMemoryDumpdirectory3,
        MemoryFilesSmallMemoryDumpdirectory4,
    ]
