"""
Auto-generated classes from the .mkape files for the KAPESync category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class SyncEvtxECmd(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: 43ed0fa4-9d29-44a5-9cfa-3db06e5b5a46

    EvtxECmd: Sync for new Maps
    """

    name: ClassVar[str] = "Sync_EvtxECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.NONE]


class SyncKAPE(KapeModule):
    """
    Author: Andrew Rathbun, Sean Straw, and Isaiah Jensen

    Version: 1.3

    ID: 371e0944-8025-4690-9c79-15faafa561a9

    KAPE: Sync for new Targets/Modules
    """

    name: ClassVar[str] = "Sync_KAPE"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.NONE]


class SyncRECmd(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: 3651465e-7165-4705-b7de-ae3006c05db0

    RECmd: Sync for new Maps
    """

    name: ClassVar[str] = "Sync_RECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.NONE]


class SyncSQLECmd(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: 6da27d9b-b3e2-4a21-9762-ce7058f5aac2

    SQLECmd: Sync for new Maps
    """

    name: ClassVar[str] = "Sync_SQLECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.NONE]
