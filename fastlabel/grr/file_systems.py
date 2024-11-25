"""
Auto-generated classes from the YAML declarations in file_systems.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class NTFSLogFile(GRRArtifactBase):
    """
    The NTFS $LogFile file system metadata file.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/file_systems/NTFS.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_systemdrive%%\\$LogFile"],
                "separator": "\\",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class NTFSMFTFiles(GRRArtifactBase):
    """
    The NTFS $MFT and $MFTMirr file system metadata files.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/file_systems/NTFS.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemdrive%%\\$MFT",
                    "%%environ_systemdrive%%\\$MFTMirr",
                ],
                "separator": "\\",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class NTFSUSNJournal(GRRArtifactBase):
    """
    The NTFS $UsnJnrl file system metadata file.

    Note that this currently does not include the $J alternate data stream name.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/file_systems/NTFS.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_systemdrive%%\\$Extend\\$UsnJrnl"],
                "separator": "\\",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None
