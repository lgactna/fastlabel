"""
Auto-generated classes from the .mkape files for the Modules category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class EZParser(KapeModule):
    """
    Author: Phill Moore

    Version: 1.4

    ID: f531e7cc-c9f3-4d04-881b-dbc89d1e7f38

    Eric Zimmerman Parsers
    """

    name: ClassVar[str] = "!EZParser"
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
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]


class bstrings(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 5a564195-2de6-422b-904e-312cf2303d2f

    Run all bstrings Modules
    """

    name: ClassVar[str] = "bstrings"
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
    ]


class bstringsCryptoWallets(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 47eb13e8-3bed-49fe-9192-fb0c14eb937d

    Run all bstrings Crypto Wallet-related Modules
    """

    name: ClassVar[str] = "bstrings_CryptoWallets"
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
    ]


class LogParser(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 60643e70-1f3d-4aa6-a08a-c907f69faaa5

    LogParser Compound Module
    """

    name: ClassVar[str] = "LogParser"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]
