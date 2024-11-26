"""
Auto-generated classes from the YAML declarations in config_files.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class JupyterConfigFile(GRRArtifactBase):
    """
    Jupyter notebook configuration file
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.jupyter/jupyter_notebook_config.py",
                    "/etc/jupyter/jupyter_notebook_config.py",
                    "/private/etc/jupyter/jupyter_notebook_config.py",
                    "/user/local/etc/jupyter/jupyter_notebook_config.py",
                ]
            },
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_programdata%%\\jupyter\\jupyter_notebook_config.py"
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class NfsExportsFile(GRRArtifactBase):
    """
    NFS Exports configuration
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/exports", "/private/etc/exports"]},
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/exports"]},
            "supported_os": ["Linux"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.DARWIN,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class RedisConfigFile(GRRArtifactBase):
    """
    Redis configuration file
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_programfiles%%\\Redis\\conf\\redis.windows.conf",
                    "%%environ_programfiles%%\\Redis\\conf\\redis.conf",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/redis/redis.conf"]},
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/etc/redis/redis.conf", "/private/etc/redis/redis.conf"]
            },
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SambaConfigFile(GRRArtifactBase):
    """
    Samba configuration file
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/samba/smb.conf"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SshUserConfigFile(GRRArtifactBase):
    """
    User ssh configuration file
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["%%users.homedir%%/.ssh/config"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.DARWIN,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SshdConfigFile(GRRArtifactBase):
    """
    Sshd configuration
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/etc/ssh/sshd_config", "/private/etc/ssh/sshd_config"]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/ssh/sshd_config"]},
            "supported_os": ["Linux"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.DARWIN,
    ]
    aliases: ClassVar[Optional[list[str]]] = None
