"""
Auto-generated classes from the .mkape files for the IISLogs category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class iisGeoLocate(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: beec158e-bd05-4b9f-b8dc-a99b2881b051

    iisGeoLocate - Geolocate IP addresses found in IIS logs, extracts unique
    IPs, records bad data from logs
    """

    name: ClassVar[str] = "iisGeoLocate"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]
