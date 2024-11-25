"""
Auto-generated classes from the YAML declarations in hadoop.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class HadoopAppLogs(GRRArtifactBase):
    """
    Location where Hadoop application logs are stored
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/hadoop/logs/*",
                    "/hadoop/logs/userlogs/application_*/container_*/*",
                    "/**2/hadoop/logs/*",
                    "/**2/hadoop/logs/userlogs/application_*/container_*/*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class HadoopAppRoot(GRRArtifactBase):
    """
    Location where Hadoop application files are stored
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/hadoop/*/yarn/system/rmstore/FSRMStateRoot/RMAppRoot/application_*/application_*",
                    "/hadoop/yarn/system/rmstore/FSRMStateRoot/RMAppRoot/application_*/application_*",
                    "/**2/hadoop/*/yarn/system/rmstore/FSRMStateRoot/RMAppRoot/application_*/application_*",
                    "/**2/hadoop/yarn/system/rmstore/FSRMStateRoot/RMAppRoot/application_*/application_*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class HadoopYarnLogs(GRRArtifactBase):
    """
    Location where Hadoop Yarn LevelDB/Timeline files are stored
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/hadoop/yarn/timeline/leveldb-timeline-store.ldb/*",
                    "/hadoop/*/yarn/timeline/leveldb-timeline-store.ldb/*",
                    "/**2/hadoop/yarn/timeline/leveldb-timeline-store.ldb/*",
                    "/**2/hadoop/*/yarn/timeline/leveldb-timeline-store.ldb/*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None
