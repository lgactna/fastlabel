"""
Auto-generated classes from the YAML declarations in webservers.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class ApacheAccessLogs(GRRArtifactBase):
    """
    Location where Apache access logs are stored
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/log/apache/access_log*",
                    "/var/log/apache/access.log*",
                    "/var/log/apache2/access_log*",
                    "/var/log/apache2/access.log*",
                    "/var/log/apache2/other_vhosts_access_log*",
                    "/var/log/apache2/other_vhosts_access.log*",
                    "/var/log/httpd/access_log*",
                    "/var/log/httpd/access.log*",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_systemdrive%%\\**6\\logs\\access.log*"],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ApacheConfigurationFolder(GRRArtifactBase):
    """
    Location where Apache keeps configuration files
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/apache2/*.conf",
                    "/etc/httpd/*.conf",
                    "/etc/httpd/conf.d/*.conf",
                    "/etc/httpd/conf.modules.d/*.conf",
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


class ApacheDefaultSiteConfigurationFile(GRRArtifactBase):
    """
    Location where Apache keeps the default site configuration file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/apache2/sites-available/000-default.conf"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ApacheErrorLogs(GRRArtifactBase):
    """
    Location where Apache error logs are stored
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/log/apache/error*",
                    "/var/log/apache/error.log*",
                    "/var/log/apache2/error*",
                    "/var/log/apache2/error.log*",
                    "/var/log/httpd/error*",
                    "/var/log/httpd/error.log*",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_systemdrive%%\\**6\\logs\\error.log*"],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class NginxAccessLogs(GRRArtifactBase):
    """
    Location where nginx access logs are stored
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/var/log/nginx/access.log*"]},
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_systemdrive%%\\nginx\\logs\\*.log*"],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class NginxErrorLogs(GRRArtifactBase):
    """
    Location where nginx error logs are stored
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/nginx/error.log*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WordpressConfigFile(GRRArtifactBase):
    """
    WordPress configuration file
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/www/**/wp-config.php",
                    "/private/var/www/wp-config.php",
                    "/var/www/**/wp-config.php",
                    "/var/www/wp-config.php",
                    "/wp/wp-config.php",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.DARWIN,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MicrosoftIISLogs(GRRArtifactBase):
    """
    Internet Information Services (IIS) web server's log files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemdrive%%\\inetpub\\logs\\LogFiles\\*.log",
                    "%%environ_systemdrive%%\\inetpub\\logs\\LogFiles\\W3SVC*\\*.log",
                    "%%environ_systemdrive%%\\Resources\\Directory\\*\\LogFiles\\Web\\W3SVC*\\*.log",
                    "%%environ_systemroot%%\\System32\\LogFiles\\W3SVC*\\*.log",
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
