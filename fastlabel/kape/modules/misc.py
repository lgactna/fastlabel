"""
Auto-generated classes from the .mkape files for the Misc category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class HatTrickFreenetParser(KapeModule):
    """
    Author: Charlie Rubisoff

    Version: 1.0

    ID: 5c546be1-27f9-4739-86f6-e0391d1cc7db

    Hat-Trick: Freenet Parser
    """

    name: ClassVar[str] = "HatTrickFreenetParser"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]
