"""
Auto-generated classes from the YAML declarations in tomcat.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr import tomcat
from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class TomcatFiles(GRRArtifactBase):
    """
    Tomcat files.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {"names": ["TomcatLogFiles", "TomcatPasswordFile"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "TomcatPasswordFile": tomcat.TomcatPasswordFile,
        "TomcatLogFiles": tomcat.TomcatLogFiles,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TomcatLogFiles(GRRArtifactBase):
    """
    Tomcat log files.

    Reference URLs:
    https://tomcat.apache.org/tomcat-8.0-doc/config/valve.html#Access_Logging
    https://tomcat.apache.org/tomcat-8.0-doc/logging.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersappdata%%\\Apache Software Foundation\\Tomcat*\\logs\\**\\access_log*",
                    "%%environ_allusersappdata%%\\Apache Software Foundation\\Tomcat*\\logs\\access_log*",
                    "%%environ_allusersappdata%%\\Apache Software Foundation\\Tomcat*\\logs\\**\\catalina.out",
                    "%%environ_allusersappdata%%\\Apache Software Foundation\\Tomcat*\\logs\\catalina.out",
                    "%%environ_programfiles%%\\Apache Software Foundation\\Tomcat*\\logs\\**\\access_log*",
                    "%%environ_programfiles%%\\Apache Software Foundation\\Tomcat*\\logs\\access_log*",
                    "%%environ_programfiles%%\\Apache Software Foundation\\Tomcat*\\logs\\**\\catalina.out",
                    "%%environ_programfiles%%\\Apache Software Foundation\\Tomcat*\\logs\\catalina.out",
                    "%%environ_programfilesx86%%\\Apache Software Foundation\\Tomcat*\\logs\\**\\access_log*",
                    "%%environ_programfilesx86%%\\Apache Software Foundation\\Tomcat*\\logs\\access_log*",
                    "%%environ_programfilesx86%%\\Apache Software Foundation\\Tomcat*\\logs\\**\\catalina.out",
                    "%%environ_programfilesx86%%\\Apache Software Foundation\\Tomcat*\\logs\\catalina.out",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/opt/tomcat*/logs/**/access_log*",
                    "/opt/tomcat*/logs/access_log*",
                    "/opt/tomcat*/logs/**/catalina.out",
                    "/opt/tomcat*/logs/catalina.out",
                    "/usr/local/tomcat*/logs/**/access_log*",
                    "/usr/local/tomcat*/logs/access_log*",
                    "/usr/local/tomcat*/logs/**/catalina.out",
                    "/usr/local/tomcat*/logs/catalina.out",
                    "/usr/share/tomcat*/logs/**/access_log*",
                    "/usr/share/tomcat*/logs/access_log*",
                    "/usr/share/tomcat*/logs/**/catalina.out",
                    "/usr/share/tomcat*/logs/catalina.out",
                    "/var/lib/tomcat*/logs/**/access_log*",
                    "/var/lib/tomcat*/logs/access_log*",
                    "/var/lib/tomcat*/logs/**/catalina.out",
                    "/var/lib/tomcat*/logs/catalina.out",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Library/Tomcat/logs/**/access_log*",
                    "/Library/Tomcat/logs/access_log*",
                    "/Library/Tomcat/logs/**/catalina.out",
                    "/Library/Tomcat/logs/catalina.out",
                    "/usr/local/apache-tomcat*/logs/**/access_log*",
                    "/usr/local/apache-tomcat*/logs/access_log*",
                    "/usr/local/apache-tomcat*/logs/**/catalina.out",
                    "/usr/local/apache-tomcat*/logs/catalina.out",
                    "/usr/local/Cellar/tomcat*/logs/**/access_log*",
                    "/usr/local/Cellar/tomcat*/logs/access_log*",
                    "/usr/local/Cellar/tomcat*/logs/**/catalina.out",
                    "/usr/local/Cellar/tomcat*/logs/catalina.out",
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
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TomcatPasswordFile(GRRArtifactBase):
    """
    Tomcat password file.

    Reference URLs:
    https://tomcat.apache.org/tomcat-8.0-doc/manager-howto.html#Configuring_Manager_Application_Access
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersappdata%%\\Apache Software Foundation\\Tomcat*\\conf\\tomcat-users.xml",
                    "%%environ_programfiles%%\\Apache Software Foundation\\Tomcat*\\conf\\tomcat-users.xml",
                    "%%environ_programfilesx86%%\\Apache Software Foundation\\Tomcat*\\conf\\tomcat-users.xml",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/opt/tomcat*/conf/tomcat-users.xml",
                    "/private/var/lib/tomcat*/conf/tomcat-users.xml",
                    "/usr/local/tomcat*/conf/tomcat-users.xml",
                    "/usr/share/tomcat*/conf/tomcat-users.xml",
                    "/var/lib/tomcat*/conf/tomcat-users.xml",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Library/Tomcat/conf/tomcat-users.xml",
                    "/usr/local/apache-tomcat-*/conf/tomcat-users.xml",
                    "/usr/local/Cellar/tomcat/*/conf/tomcat-users.xml",
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
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None
