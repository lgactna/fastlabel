"""
Auto-generated classes from the .tkape files for the Event Trace Logs category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class EventTraceLogsWDITraceLogs10(KapeTarget):
    name: ClassVar[str] = "WDI Trace Logs 1"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\WDI\\LogFiles\\")
    file_mask: ClassVar[str] = "*.etl*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventTraceLogsWDITraceLogs11(KapeTarget):
    name: ClassVar[str] = "WDI Trace Logs 1"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\WDI\\LogFiles\\"
    )
    file_mask: ClassVar[str] = "*.etl*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventTraceLogsWDITraceLogs22(KapeTarget):
    name: ClassVar[str] = "WDI Trace Logs 2"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\WDI\\{*\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventTraceLogsWDITraceLogs23(KapeTarget):
    name: ClassVar[str] = "WDI Trace Logs 2"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\WDI\\{*\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventTraceLogsWMITraceLogs4(KapeTarget):
    name: ClassVar[str] = "WMI Trace Logs"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\LogFiles\\WMI\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventTraceLogsWMITraceLogs5(KapeTarget):
    name: ClassVar[str] = "WMI Trace Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\LogFiles\\WMI\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventTraceLogsSleepStudyTraceLogs6(KapeTarget):
    name: ClassVar[str] = "SleepStudy Trace Logs"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\SleepStudy\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventTraceLogsSleepStudyTraceLogs7(KapeTarget):
    name: ClassVar[str] = "SleepStudy Trace Logs"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\SleepStudy\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventTraceLogsEnergyNTKLTraceLogs8(KapeTarget):
    name: ClassVar[str] = "Energy-NTKL Trace Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Microsoft\\Windows\\PowerEfficiency Diagnostics\\"
    )
    file_mask: ClassVar[str] = "energy-ntkl.etl"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventTraceLogsDeliveryOptimizationTraceLogs9(KapeTarget):
    name: ClassVar[str] = "Delivery Optimization Trace Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows\\ServiceProfiles\\NetworkService\\AppData\\Local\\Microsoft\\Windows\\DeliveryOptimization\\Logs\\"
    )
    file_mask: ClassVar[str] = "*.etl*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventTraceLogs(KapeTargetConfiguration):
    """
    Author: Mark Hallman

    Version: 1.1

    ID: af494526-9e44-4548-9d29-f088eafa6f3d

    Event Trace Logs
    """

    name: ClassVar[str] = "EventTraceLogs"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        EventTraceLogsWDITraceLogs10,
        EventTraceLogsWDITraceLogs11,
        EventTraceLogsWDITraceLogs22,
        EventTraceLogsWDITraceLogs23,
        EventTraceLogsWMITraceLogs4,
        EventTraceLogsWMITraceLogs5,
        EventTraceLogsSleepStudyTraceLogs6,
        EventTraceLogsSleepStudyTraceLogs7,
        EventTraceLogsEnergyNTKLTraceLogs8,
        EventTraceLogsDeliveryOptimizationTraceLogs9,
    ]
