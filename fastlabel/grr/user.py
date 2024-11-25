"""
Auto-generated classes from the YAML declarations in user.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class UserDownloadsDirectory(GRRArtifactBase):
    """
    Contents of user Downloads directories.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#user-directories
    """

    SOURCES = [
        {
            "type": "PATH",
            "attributes": {"paths": ["%%users.homedir%%/Downloads/*"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "PATH",
            "attributes": {
                "paths": ["%%users.userprofile%%\\Downloads\\*"],
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
    aliases: ClassVar[Optional[list[str]]] = [
        "MacOSUserDownloadsDirectory",
        "UserDownloads",
        "WindowsUserDownloadsDirectory",
    ]


class UsersDirectory(GRRArtifactBase):
    """
    Contents of the Users directory.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#users
    """

    SOURCES = [{"type": "PATH", "attributes": {"paths": ["/Users/*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = [
        "MacOSUsers",
        "MacOSUsersDirectory",
        "OSXUsers",
        "UserHomeDirectory",
    ]
