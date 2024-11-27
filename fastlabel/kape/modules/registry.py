"""
Auto-generated classes from the .mkape files for the Registry category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class RECmdAllBatchFiles(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: f2c9c95d-375e-4fb7-b069-7e9b95ea6db5

    RECmd: All RECmd Batch Output
    """

    name: ClassVar[str] = "RECmd_AllBatchFiles"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]


class Reghunter(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: 2701714e-4de8-435b-9d7c-dfe81c3ea22e

    Execute all Reghunter modules
    """

    name: ClassVar[str] = "Reghunter"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]


class RegRipper(KapeModule):
    """
    Author: ZeArioch <https://{github,twitter}.com/ZeArioch>, Phill Moore,
    Andreas Hunkeler (@Karneades)

    Version: 1.1

    ID: 76037ee9-0346-459a-a44a-1b67edc711c8

    RegRipper: parse all supported hives
    """

    name: ClassVar[str] = "RegRipper"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]


class TZWorksCAFAERegistrySystem(KapeModule):
    """
    Author: Scott Downie

    Version: 1.0

    ID: 5405e8ff-e40f-407c-9c73-224b09ef57ba

    CAFAE: extract registry information
    """

    name: ClassVar[str] = "TZWorks_CAFAE_Registry_System"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class RegRipperNTUserVariable(KapeModule):
    """
    Author: Andreas Hunkeler (@Karneades)

    Version: 1.0

    ID: b1c7a758-664a-459d-82d5-3165772f21fc

    RegRipper: parse NTUSER hives using provided plugin name
    """

    name: ClassVar[str] = "RegRipper_NTUser-Variable"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class RegRipperNTUser(KapeModule):
    """
    Author: ZeArioch <https://{github,twitter}.com/ZeArioch>, Phill Moore

    Version: 1.1

    ID: ce3bf979-0d4d-4a31-8240-6be6f95610b7

    RegRipper: parse NTUSER hives
    """

    name: ClassVar[str] = "RegRipper_NTUser"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class RegRipperSAM(KapeModule):
    """
    Author: ZeArioch <https://{github,twitter}.com/ZeArioch>, Phill Moore

    Version: 1.1

    ID: 4b1babd2-c7e1-4f1f-a34f-1968d3672752

    RegRipper: parse SAM hive
    """

    name: ClassVar[str] = "RegRipper_SAM"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class RegRipperSECURITYVariable(KapeModule):
    """
    Author: Andreas Hunkeler (@Karneades)

    Version: 1.0

    ID: 8743b688-bebf-4ae5-8700-aed6681fc4eb

    RegRipper: parse SECURITY hive using provided plugin name
    """

    name: ClassVar[str] = "RegRipper_SECURITY-Variable"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class RegRipperSECURITY(KapeModule):
    """
    Author: ZeArioch <https://{github,twitter}.com/ZeArioch>, Phill Moore

    Version: 1.1

    ID: a0011605-10ac-4e7b-b422-8d1afeebfd5c

    RegRipper: parse SECURITY hive
    """

    name: ClassVar[str] = "RegRipper_SECURITY"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class RegRipperSOFTWAREVariable(KapeModule):
    """
    Author: Andreas Hunkeler (@Karneades)

    Version: 1.0

    ID: c2e63e6f-4207-4bf4-b6af-d4a465009418

    RegRipper: parse SOFTWARE hive using provided plugin name
    """

    name: ClassVar[str] = "RegRipper_SOFTWARE-Variable"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class RegRipperSOFTWARE(KapeModule):
    """
    Author: ZeArioch <https://{github,twitter}.com/ZeArioch>, Phill Moore

    Version: 1.1

    ID: 8fa920ff-03ce-4f88-af2a-0558187f708c

    RegRipper: parse SOFTWARE hive
    """

    name: ClassVar[str] = "RegRipper_SOFTWARE"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class RegRipperSYSTEMVariable(KapeModule):
    """
    Author: Andreas Hunkeler (@Karneades)

    Version: 1.0

    ID: 2eda739f-6af9-4b53-8d63-2c1154701a7c

    RegRipper: parse SYSTEM hive using provided plugin name
    """

    name: ClassVar[str] = "RegRipper_SYSTEM-Variable"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class RegRipperSYSTEM(KapeModule):
    """
    Author: ZeArioch <https://{github,twitter}.com/ZeArioch>, Phill Moore

    Version: 1.1

    ID: ef988f41-7d77-436d-bc1a-1789f062506b

    RegRipper: parse SYSTEM hive
    """

    name: ClassVar[str] = "RegRipper_SYSTEM"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class RegRipperUsrClassVariable(KapeModule):
    """
    Author: Andreas Hunkeler (@Karneades)

    Version: 1.0

    ID: 26a1534a-c11d-4434-96c5-864699513aee

    RegRipper: parse UsrClass hives using provided plugin name
    """

    name: ClassVar[str] = "RegRipper_UsrClass-Variable"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class RegRipperUsrClass(KapeModule):
    """
    Author: Andreas Hunkeler (@Karneades)

    Version: 1.0

    ID: 253acccb-86c0-49dd-9b6d-b9c228a49a55

    RegRipper: parse UsrClass hives
    """

    name: ClassVar[str] = "RegRipper_UsrClass"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]


class reghunterbinary(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: 6a4235ed-7288-43b3-8750-f404aa85ed6a

    Execute Reghunter Binary module to find possible MZ headers in REG_BINARY
    values
    """

    name: ClassVar[str] = "reg_hunter_binary"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class reghunteremail(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: 446d56d0-e799-482b-bfb8-14feca77b257

    Execute Reghunter Email module
    """

    name: ClassVar[str] = "reg_hunter_email"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class reghunterencoding(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: d7654551-8f22-4062-87b6-6630789b22ce

    Execute Reghunter Encoding module
    """

    name: ClassVar[str] = "reg_hunter_encoding"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class reghunterip(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: 52d50dcf-eae7-4b9b-9828-2f4caec860bf

    Execute Reghunter IP module to search for IP adresses
    """

    name: ClassVar[str] = "reg_hunter_ip"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class reghunterlink(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: 736f9493-2b95-4002-8fb1-7d6eb8834b0d

    Execute Reghunter Link module for hunting symbolic links
    """

    name: ClassVar[str] = "reg_hunter_link"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class reghunterobfuscation(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: 576ca9cd-30bf-4db2-98a6-7bdd36a9bb13

    Execute Reghunter Obfuscation module to find obfuscated values
    """

    name: ClassVar[str] = "reg_hunter_obfuscation"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class reghunterscript(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: 44485205-d803-4fb3-b4b5-8fe050bb0cda

    Execute Reghunter Script module to find script files
    """

    name: ClassVar[str] = "reg_hunter_script"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class reghuntershell(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: de0ced67-fa0d-4bf0-9022-27b2a2457917

    Execute Reghunter Shell module to find command shells (cmd.exe,
    powershell.exe, ...)
    """

    name: ClassVar[str] = "reg_hunter_shell"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class reghuntershellcode(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: 67925c73-a5ed-4e4d-97c4-6d6b757f3037

    Execute Reghunter Shellcode to find possible shellcode
    """

    name: ClassVar[str] = "reg_hunter_shellcode"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class reghuntersuspicious(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: 92bbd283-8446-46db-b0d2-eb8068c627fd

    Execute Reghunter Suspicious module to find various suspicious substrings
    (e.g. iex, invoke-expression, etc.)
    """

    name: ClassVar[str] = "reg_hunter_suspicious"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class reghunterunc(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: 78bb9543-80df-45fc-aef5-1f560702529e

    Execute Reghunter UNC module to find UNC paths
    """

    name: ClassVar[str] = "reg_hunter_unc"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class reghunterurl(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: 36786dd5-da30-4acc-a055-c22f79e744e2

    Execute Reghunter URL module to find URLs
    """

    name: ClassVar[str] = "reg_hunter_url"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class RECmdAllRegExecutablesFoundOrRun(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 23cfcb78-60bb-4b2a-a7a4-b256f42fb83b

    RECmd: AllRegExecutablesFoundOrRun
    """

    name: ClassVar[str] = "RECmd_AllRegExecutablesFoundOrRun"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class RECmdBasicSystemInfo(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: e6da3300-447a-4912-9689-7d0679cae71b

    RECmd: BasicSystemInfo
    """

    name: ClassVar[str] = "RECmd_BasicSystemInfo"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class RECmdBCDBootVolume(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 4de3e322-491d-44a2-a870-edf0387b41b4

    RECmd: BCDBootVolume
    """

    name: ClassVar[str] = "RECmd_BCDBootVolume"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class RECmdInstalledSoftware(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 82d89b1d-19c1-439b-a30d-2f8659adf691

    RECmd: InstalledSoftware
    """

    name: ClassVar[str] = "RECmd_InstalledSoftware"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class RECmdKroll(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 26e4a8f6-d745-4195-8b8e-563cf32a4952

    RECmd: Kroll
    """

    name: ClassVar[str] = "RECmd_Kroll"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class RECmdRECmdBatchMC(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 8690f004-a406-40c9-b566-2fdf5f106209

    RECmd: RECmd_Batch_MC
    """

    name: ClassVar[str] = "RECmd_RECmd_Batch_MC"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class RECmdRegistryASEPs(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 176dd6af-4077-42ee-af03-1020768149ff

    RECmd: RegistryASEPs
    """

    name: ClassVar[str] = "RECmd_RegistryASEPs"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class RECmdSoftwareASEPs(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 193817d5-85a1-4dbb-b8e0-61693d2deebc

    RECmd: SoftwareASEPs
    """

    name: ClassVar[str] = "RECmd_SoftwareASEPs"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class RECmdSoftwareClassesASEPs(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 0e38b045-6512-41c2-962f-49a9da37b02f

    RECmd: SoftwareClassesASEPs
    """

    name: ClassVar[str] = "RECmd_SoftwareClassesASEPs"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class RECmdSoftwareWoW6432ASEPs(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 63e39ae3-63c3-44c8-86ac-fb7ac4365d7b

    RECmd: SoftwareWoW6432ASEPs
    """

    name: ClassVar[str] = "RECmd_SoftwareWoW6432ASEPs"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class RECmdSystemASEPs(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 3ef19b6e-3489-44ee-a5fa-0245fd54ecd1

    RECmd: SystemASEPs
    """

    name: ClassVar[str] = "RECmd_SystemASEPs"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class RECmdUserActivity(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 05db97da-327b-46d0-942c-a468c087c09c

    RECmd: UserActivity
    """

    name: ClassVar[str] = "RECmd_UserActivity"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class RECmdUserClassesASEPs(KapeModule):
    """
    Author: Andreas Hunkeler (@Karneades)

    Version: 1.0

    ID: df3d2d54-dda9-49fb-a427-c9d8348b375d

    RECmd: UserClassesASEPs
    """

    name: ClassVar[str] = "RECmd_UserClassesASEPs"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
