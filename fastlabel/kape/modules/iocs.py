"""
Auto-generated classes from the .mkape files for the IOCs category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class LokiScan(KapeModule):
    """
    Author: Georg Lauenstein and Andrew Rathbun

    Version: 1.0

    ID: 3c715b0c-fec3-4f41-a762-74233e240760

    Loki - Simple IOC and Incident Response Scanner - Mounted Image/Offline
    Files
    """

    name: ClassVar[str] = "Loki_Scan"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.LOG]


class ThorScan(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: d399005e-6acc-42d2-981e-d9d4b9cecbd0

    Thor, an IOC and YARA scanner written in Golang - Lab Scan
    """

    name: ClassVar[str] = "Thor_Scan"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.NONE]


class ThorUpgrade(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: aaff8e82-a5c1-42e0-b3f0-1c35c6932e12

    Thor, an IOC and YARA scanner written in Golang - Upgrade
    """

    name: ClassVar[str] = "Thor_Upgrade"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.NONE]


class ThorLiteLiveResponse(KapeModule):
    """
    Author: Jonas A. Wendorf (changes), Georg Lauenstein (changes), based on the
    original for Spark Core by Eric Capuano

    Version: 1.2

    ID: b75b558c-5ddb-45bc-bc1e-0db0635110ca

    Thor Lite, an IOC and YARA scanner written in Golang
    """

    name: ClassVar[str] = "Thor-Lite_LiveResponse"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class ThorLiteLiveResponseLookback30days(KapeModule):
    """
    Author: Georg Lauenstein

    Version: 1.0

    ID: 5dafe1af-eb44-4b08-a7fd-8e36d65d6a60

    Thor Lite, an IOC and YARA scanner written in Golang with 30 Days lookback
    option
    """

    name: ClassVar[str] = "Thor-Lite_LiveResponse_Lookback30days"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class ThorLiteScan(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: 60a5a5bd-2484-4f5d-8440-8dbce197b026

    Thor Lite, an IOC and YARA scanner written in Golang
    """

    name: ClassVar[str] = "Thor-Lite_Scan"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.CSV]


class ThorLiteUpgrade(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: e7ae5267-ccbc-49ae-8eaf-b6f031c750e5

    Thor Lite, an IOC and YARA scanner written in Golang
    """

    name: ClassVar[str] = "Thor-Lite_Upgrade"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.NONE]
