"""
Auto-generated classes from the .tkape files for the SystemEvents category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class EventTranscriptDBEventTranscriptdb0(KapeTarget):
    name: ClassVar[str] = "EventTranscript.db"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Microsoft\\Diagnosis\\EventTranscript"
    )
    regex: ClassVar[str] = r"(?s:EventTranscript\.db.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventTranscriptDBEventTranscriptdb1(KapeTarget):
    name: ClassVar[str] = "EventTranscript.db"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\ProgramData\\Microsoft\\Diagnosis\\EventTranscript"
    )
    regex: ClassVar[str] = r"(?s:EventTranscript\.db.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventTranscriptDBMicrosoftOfficeDiagnosticLogs2(KapeTarget):
    name: ClassVar[str] = "Microsoft Office Diagnostic Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%User%\\AppData\\Local\\Temp\\Diagnostics"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EventTranscriptDB(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun and Josh Mitchell

    Version: 1.2

    ID: 4a5c1487-8894-4b7a-8fba-71a1824bb9ab

    EventTranscript.db (and other files related to Telemetry and Diagnostic
    Data)
    """

    name: ClassVar[str] = "EventTranscriptDB"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        EventTranscriptDBEventTranscriptdb0,
        EventTranscriptDBEventTranscriptdb1,
        EventTranscriptDBMicrosoftOfficeDiagnosticLogs2,
    ]


class WindowsTelemetryDiagnosticsLegacyLegacyrbsfilesrelatingtoWindowsTelemetryandDiagnostics0(
    KapeTarget
):
    name: ClassVar[str] = (
        "Legacy .rbs files relating to Windows Telemetry and Diagnostics"
    )
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Microsoft\\Diagnosis\\")
    regex: ClassVar[str] = r"(?s:events.*\.rbs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsTelemetryDiagnosticsLegacyLegacyrbsfilesrelatingtoWindowsTelemetryandDiagnostics1(
    KapeTarget
):
    name: ClassVar[str] = (
        "Legacy .rbs files relating to Windows Telemetry and Diagnostics"
    )
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\ProgramData\\Microsoft\\Diagnosis\\"
    )
    regex: ClassVar[str] = r"(?s:events.*\.rbs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsTelemetryDiagnosticsLegacy(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun and Josh Mitchell

    Version: 1.0

    ID: 4bc4b0bc-9334-4ad8-a331-78c4751ea07d

    Legacy Windows Telemetry and Diagnostics files (*.rbs)
    """

    name: ClassVar[str] = "WindowsTelemetryDiagnosticsLegacy"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WindowsTelemetryDiagnosticsLegacyLegacyrbsfilesrelatingtoWindowsTelemetryandDiagnostics0,
        WindowsTelemetryDiagnosticsLegacyLegacyrbsfilesrelatingtoWindowsTelemetryandDiagnostics1,
    ]
