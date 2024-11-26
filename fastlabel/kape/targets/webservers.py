"""
Auto-generated classes from the .tkape files for the Webservers category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class ApacheAccessLogApacheAccessLog0(KapeTarget):
    name: ClassVar[str] = "Apache Access Log"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:access\.log)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ApacheAccessLog(KapeTargetConfiguration):
    """
    Author: Hadar Yudovich

    Version: 1.0

    ID: 6ad85ab3-701a-409c-98b8-ea4ef806cdf0

    Apache Access Log
    """

    name: ClassVar[str] = "ApacheAccessLog"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [ApacheAccessLogApacheAccessLog0]
