"""
Auto-generated classes from the .mkape files for the SOF-ELK category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class SOFELKParser(KapeModule):
    """
    Author: Tony Knutson and Andrew Rathbun

    Version: 1.2

    ID: ae3ce0ae-1531-4916-a448-2fa2039fb714

    Parsing for SOF-ELK Instance
    """

    name: ClassVar[str] = "SOFELK_Parser"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]


class SOFELKParserEvtxECmd(KapeModule):
    """
    Author: Tony Knutson and Andrew Rathbun

    Version: 1.0

    ID: 7e5e99c0-c97e-485a-baa9-3a284852bc69

    Parsing for SOF-ELK Instance
    """

    name: ClassVar[str] = "SOFELK_Parser_EvtxECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class SOFELKParserLEcmd(KapeModule):
    """
    Author: Tony Knutson and Andrew Rathbun

    Version: 1.0

    ID: 1544a0ef-63de-4229-8dab-d9b36b9f95fe

    Parsing for SOF-ELK Instance
    """

    name: ClassVar[str] = "SOFELK_Parser_LEcmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class SOFELKParserMFTECmdJ(KapeModule):
    """
    Author: Tony Knutson and Andrew Rathbun

    Version: 1.0

    ID: a3c8f694-b20e-43aa-96e5-3a5df2379321

    Parsing for SOF-ELK Instance
    """

    name: ClassVar[str] = "SOFELK_Parser_MFTECmd_J"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class SOFELKParserMFTECmdMFT(KapeModule):
    """
    Author: Tony Knutson and Andrew Rathbun

    Version: 1.1

    ID: bb160156-76b7-4790-83dc-519c06ba53df

    Parsing for SOF-ELK Instance
    """

    name: ClassVar[str] = "SOFELK_Parser_MFTECmd_MFT"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class SOFELKParserPECmd(KapeModule):
    """
    Author: Tony Knutson and Andrew Rathbun

    Version: 1.0

    ID: 5da0b20f-4dec-4f6e-8baf-0585f5b1f4d3

    Parsing for SOF-ELK Instance
    """

    name: ClassVar[str] = "SOFELK_Parser_PECmd"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]
