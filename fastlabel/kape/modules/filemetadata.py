"""
Auto-generated classes from the .mkape files for the Filemetadata category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class Bulkextractor(KapeModule):
    """
    Author: Pedro Sanchez Cordero (conexioninversa)

    Version: 1.0

    ID: 8340d9a0-0b1a-447e-bc4e-893c66a783ec

    is a high-performance digital forensics exploitation tool. It is a "get
    evidence" that rapidly scans any kind of input (disk images, files,
    directories of files, etc) and extracts structured information such as email
    addresses, credit card numbers, JPEGs and JSON snippets without parsing the
    file system or file system structures. The results are stored in text files
    that are easily inspected, searched, or used as inputs for other forensic
    processing.
    """

    name: ClassVar[str] = "Bulk_extractor"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.TXT]
