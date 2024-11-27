"""
Auto-generated classes from the .mkape files for the Passwords category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class mimikatzNTLMHashes(KapeModule):
    """
    Author: Banaanhangwagen

    Version: 1.0

    ID: 899fd6c5-c957-42cf-a4f7-d62f4430b6b2

    Retrieve NTLM-hashes of all the user accounts
    """

    name: ClassVar[str] = "mimikatz_NTLMHashes"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]
