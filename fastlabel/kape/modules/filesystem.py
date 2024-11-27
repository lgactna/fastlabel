"""
Auto-generated classes from the .mkape files for the FileSystem category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class EverythingParseEFU(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: aa99e399-bd8d-4881-81e1-3633724d6738

    Everything (VoidTools)
    """

    name: ClassVar[str] = "Everything_ParseEFU"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.EFU,
        KapeExportFormat.CSV,
    ]


class NTFSLogTrackerJ(KapeModule):
    """
    Author: Hyun Yi @hyuunnn

    Version: 1.0

    ID: adcf94a7-dde8-4eaf-855e-8072d7df1e14

    NTFS Log Tracker: process $J files
    """

    name: ClassVar[str] = "NTFSLogTracker_$J"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.SQLITE3,
        KapeExportFormat.CSV,
    ]


class NTFSLogTrackerLogFile(KapeModule):
    """
    Author: Hyun Yi @hyuunnn

    Version: 1.0

    ID: 03939a50-0325-49f0-8cad-1f35c083f44b

    NTFS Log Tracker: process $LogFile files
    """

    name: ClassVar[str] = "NTFSLogTracker_$LogFile"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.SQLITE3,
        KapeExportFormat.CSV,
    ]


class MFTECmd(KapeModule):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 7ef84a6b-5215-47bb-af2a-2139a3277e25

    MFTECmd: process all files handled by MFTECmd
    """

    name: ClassVar[str] = "MFTECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]


class NTFSLogTracker(KapeModule):
    """
    Author: Hyun Yi @hyuunnn

    Version: 1.0

    ID: 094e8964-ea15-4be1-869d-7b8fa1b55ada

    NTFS Log Tracker: process all files
    """

    name: ClassVar[str] = "NTFSLogTracker"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]


class INDXRipper(KapeModule):
    """
    Author: Harel Segev

    Version: 1.0

    ID: 7fc17392-ebd6-4b10-b8d4-55d67dc010a2

    INDXRipper: parse all $I30s from live system
    """

    name: ClassVar[str] = "INDXRipper"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class PowerShellMFTECmdJMFTParsing(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: ac0660c3-4eb2-4dee-ad90-5ef782b94750

    MFTECmd - Parse $J and $MFT together to produce CSV output with ParentPath
    populated in $J CSV
    """

    name: ClassVar[str] = "PowerShell_MFTECmd_J-MFTParsing"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class MFTECmdBoot(KapeModule):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 7ef84a6b-2215-47bb-af2a-3339a3227e25

    MFTECmd: process $Boot files
    """

    name: ClassVar[str] = "MFTECmd_$Boot"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]


class MFTECmdJ(KapeModule):
    """
    Author: Eric Zimmerman, Thomas DIOT

    Version: 1.1

    ID: 5ef67a6b-5895-46bb-af2a-3339a3227e25

    MFTECmd: process $J / $UsnJrnl$J files
    """

    name: ClassVar[str] = "MFTECmd_$J"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]


class MFTECmdMFT(KapeModule):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 7ef84a6b-5215-46bb-af2a-3339a3227e25

    MFTECmd: process $MFT files
    """

    name: ClassVar[str] = "MFTECmd_$MFT"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]


class MFTECmdMFTDumpResidentFiles(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 4b9ba0a9-1453-438f-94c7-8344bed6ad82

    MFTECmd: process $MFT files, then dump resident files within the $MFT
    """

    name: ClassVar[str] = "MFTECmd_$MFT_DumpResidentFiles"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class MFTECmdMFTFileListing(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 8bcb68fa-b62a-4347-b3cb-b00d72b2752d

    MFTECmd: process $MFT files, then output file listing
    """

    name: ClassVar[str] = "MFTECmd_$MFT_FileListing"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]


class MFTECmdMFTProcessMFTSlack(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 69553b37-e8d9-4ae9-b325-bc0dd2808a71

    MFTECmd: process $MFT files with FILE slack recovery
    """

    name: ClassVar[str] = "MFTECmd_$MFT_ProcessMFTSlack"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]


class MFTECmdSDS(KapeModule):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: 7ef84a6b-5215-46bb-af2a-3339a4247e41

    MFTECmd: process $SDS files
    """

    name: ClassVar[str] = "MFTECmd_$SDS"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.CSV,
        KapeExportFormat.JSON,
    ]
