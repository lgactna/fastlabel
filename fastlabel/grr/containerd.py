"""
Auto-generated classes from the YAML declarations in containerd.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class ContainerdConfig(GRRArtifactBase):
    """
    containerd configuration files
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/containerd/config.toml",
                    "/var/lib/containerd/io.containerd.metadata.v1.bolt/meta.db",
                    "/var/lib/containerd/io.containerd.snapshotter.v1.overlayfs/metadata.db",
                    "/var/run/containerd/io.containerd.runtime.v2.task/*/*/config.json",
                    "/var/run/containerd/io.containerd.runtime.v2.task/*/*/options.json",
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


class ContainerdLogs(GRRArtifactBase):
    """
    containerd related events in the log files
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/run/containerd/io.containerd.runtime.v2.task/*/*/log.json",
                    "/var/log/daemon.log",
                    "/var/log/daemon.log.*.gz",
                    "/var/log/syslog*",
                    "/var/log/message*",
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
