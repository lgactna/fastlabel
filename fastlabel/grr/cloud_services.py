"""
Auto-generated classes from the YAML declarations in cloud_services.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class DropboxClient(GRRArtifactBase):
    """
    Dropbox cloud storage client artifacts.

    Reference URLs: https://forensics.wiki/dropbox
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Dropbox\\*.db*",
                    "%%users.localappdata%%\\Dropbox\\*.db*",
                    "%%users.localappdata%%\\Dropbox\\instance*\\sync_history.db",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.dropbox/*.db*",
                    "%%users.homedir%%/.dropbox/instance*/sync_history.db",
                ]
            },
            "supported_os": ["Darwin", "Linux"],
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


class GoogleDriveClient(GRRArtifactBase):
    """
    Google Drive cloud storage client artifacts.

    Reference URLs: https://forensics.wiki/google_drive
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Google\\Drive\\snapshot.db",
                    "%%users.localappdata%%\\Google\\Drive\\sync_config.db",
                    "%%users.localappdata%%\\Google\\Drive\\sync_config.log*",
                    "%%users.localappdata%%\\Google\\Drive\\user_default\\snapshot.db",
                    "%%users.localappdata%%\\Google\\Drive\\user_default\\sync_config.db",
                    "%%users.localappdata%%\\Google\\Drive\\user_default\\sync_config.log*",
                    "%%users.localappdata%%\\Google\\Drive\\user_default\\sync_log.log*",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Google/Drive/snapshot.db",
                    "%%users.homedir%%/Library/Application Support/Google/Drive/sync_config.db",
                    "%%users.homedir%%/Library/Application Support/Google/Drive/sync_config.log*",
                    "%%users.homedir%%/Library/Application Support/Google/Drive/user_default/snapshot.db",
                    "%%users.homedir%%/Library/Application Support/Google/Drive/user_default/sync_config.db",
                    "%%users.homedir%%/Library/Application Support/Google/Drive/user_default/sync_config.log*",
                ]
            },
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SkyDriveClient(GRRArtifactBase):
    """
    Microsoft Sky Drive cloud storage client artifacts.

    Note that Sky Drive was renamed to One Drive.

    Reference URLs: https://forensics.wiki/one_drive#sky-drive-client
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Microsoft\\SkyDrive\\logs\\*.log",
                    "%%users.localappdata%%\\Microsoft\\SkyDrive\\setup\\logs\\*.log",
                    "%%users.localappdata%%\\Microsoft\\SkyDrive\\settings\\ApplicationSettings.xml",
                    "%%users.localappdata%%\\Microsoft\\SkyDrive\\settings\\*.dat",
                    "%%users.localappdata%%\\Microsoft\\SkyDrive\\settings\\*.ini",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class CloudStorageClients(GRRArtifactBase):
    """
    Multiple cloud storage client artifacts.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": ["DropboxClient", "GoogleDriveClient", "SkyDriveClient"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "DropboxClient": DropboxClient,
        "GoogleDriveClient": GoogleDriveClient,
        "SkyDriveClient": SkyDriveClient,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None
