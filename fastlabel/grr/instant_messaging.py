"""
Auto-generated classes from the YAML declarations in instant_messaging.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class SignalApplicationContent(GRRArtifactBase):
    """
    Signal Application Content and Configuration
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.var/app/org.signal.Signal/*/attachments.noindex/*",
                    "%%users.homedir%%/.var/app/org.signal.Signal/*/Cache/*",
                    "%%users.homedir%%/.var/app/org.signal.Signal/*/logs/*",
                    "%%users.homedir%%/.var/app/org.signal.Signal/config.json",
                ]
            },
            "supported_os": ["Linux"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SignalDatabase(GRRArtifactBase):
    """
    Signal Database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/.var/app/org.signal.Signal/db.sqlite"]
            },
            "supported_os": ["Linux"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SkypeChatSync(GRRArtifactBase):
    """
    Chat Sync Directory

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#skype
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Skype/*/chatsync/*"
                ]
            },
            "supported_os": ["Darwin"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SkypeDb(GRRArtifactBase):
    """
    Main Skype database

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#skype
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Skype/*/Main.db"
                ]
            },
            "supported_os": ["Darwin"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SkypeMainDirectory(GRRArtifactBase):
    """
    Skype Directory
    """

    SOURCES = [
        {
            "type": "PATH",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Application Support/Skype/*"]
            },
            "supported_os": ["Darwin"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SkypePreferences(GRRArtifactBase):
    """
    Skype Preferences and Recent Searches

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#skype
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Preferences/com.skype.skype.plist"]
            },
            "supported_os": ["Darwin"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SkypeUserProfile(GRRArtifactBase):
    """
    Skype User profile

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#skype
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Application Support/Skype/*/*"]
            },
            "supported_os": ["Darwin"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class XChatLogs(GRRArtifactBase):
    """
    XChat Log Files

    Reference URLs: http://xchat.org/faq/#q222
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.xchat2/xchatlogs/*.log",
                    "%%users.homedir%%/.xchat2/xchatlogs/*/*.log",
                ]
            },
            "supported_os": ["Linux"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None
