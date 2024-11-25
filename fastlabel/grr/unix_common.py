"""
Auto-generated classes from the YAML declarations in unix_common.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr import unix_common
from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class CupsJobCacheFile(GRRArtifactBase):
    """
    Common UNIX Printing System (CUPS) job cache file.

    Reference URLs: https://www.cups.org/doc/man-cups-files.conf.html
    https://www.cups.org/doc/spec-design.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/var/spool/cups/cache/job.cache"]},
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/private/var/spool/cups/cache/job.cache"]},
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/var/cache/cups/job.cache"]},
            "supported_os": ["Linux"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSCupsJobCacheFile"]


class UnixGroupsFile(GRRArtifactBase):
    """
    Unix groups file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/group"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/private/etc/group"]},
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
    ]
    aliases: ClassVar[Optional[list[str]]] = ["UnixGroups"]


class UnixHostsFile(GRRArtifactBase):
    """
    Unix hosts file
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/hosts"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/private/etc/hosts"]},
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSHostsFile"]


class UnixLocalTimeConfigurationFile(GRRArtifactBase):
    """
    Unix local time zone configuration file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/localtime"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/private/etc/localtime"]},
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSLocalTime"]


class UnixPasswdFile(GRRArtifactBase):
    """
    Unix passwd file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/passwd"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/private/etc/passwd"]},
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
    ]
    aliases: ClassVar[Optional[list[str]]] = ["UnixPasswd"]


class UnixShadowFile(GRRArtifactBase):
    """
    Unix shadow file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/shadow"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/private/etc/shadow"]},
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class UnixShadowBackupFile(GRRArtifactBase):
    """
    Unix shadow backup file.

    Reference URLs: https://man7.org/linux/man-pages/man5/shadow.5.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/shadow-"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/private/etc/shadow-"]},
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class UnixSudoersConfigurationFile(GRRArtifactBase):
    """
    Unix sudoers configuration file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/sudoers"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/private/etc/sudoers"]},
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
    ]
    aliases: ClassVar[Optional[list[str]]] = ["UnixSudoersConfiguration"]


class UnixUsersGroups(GRRArtifactBase):
    """
    Unix users and groups files.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": ["UnixGroupsFile", "UnixPasswdFile", "UnixShadowFile"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "UnixGroupsFile": unix_common.UnixGroupsFile,
        "UnixPasswdFile": unix_common.UnixPasswdFile,
        "UnixShadowFile": unix_common.UnixShadowFile,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class UnixUtmpFile(GRRArtifactBase):
    """
    Utmp login record files.

    Reference URLs:
    https://github.com/libyal/dtformats/blob/main/documentation/Utmp%20login%20records%20format.asciidoc
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/var/log/btmp", "/var/log/wtmp", "/var/run/utmp"]
            },
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/log/btmp",
                    "/private/var/log/wtmp",
                    "/private/var/run/utmp",
                ]
            },
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSUtmpFile"]
