"""
Auto-generated classes from the YAML declarations in docker.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class DockerContainerConfig(GRRArtifactBase):
    """
    Docker container configuration files
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/lib/docker/containers/*/config.v2.json",
                    "/var/lib/docker/containers/*/config.json",
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


class GKEDockerContainerLogs(GRRArtifactBase):
    """
    Location where stdout and stderr from containers is logged in a Google
    Kubernetes Engine (GKE) environment.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/var/lib/docker/containers/*/*-json.log*"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None
