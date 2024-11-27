"""
Auto-generated classes from the .mkape files for the ChainsawSync category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class PowerShellGetChainsawSigmaRules(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: b3fc53a5-4f10-431d-903a-65700bf16e2f

    Get-ChainsawSigmaRules.ps1 - Update Sigma Rules that Chainsaw relies on
    """

    name: ClassVar[str] = "PowerShell_Get-ChainsawSigmaRules"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]
