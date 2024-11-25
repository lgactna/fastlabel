"""
Auto-generated classes from the YAML declarations in linux_services.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class ApacheKafkaLogFiles(GRRArtifactBase):
    """
    Apache Kafka Log files
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/opt/kafka/logs/*",
                    "/opt/kafka/logs/controller.log*",
                    "/opt/kafka/logs/kafka-*.log*",
                    "/opt/kafka/logs/server.log*",
                    "/opt/kafka/logs/state-change.log*",
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


class HAProxyLogFiles(GRRArtifactBase):
    """
    HAProxy Log files

    Reference URLs:
    https://cbonte.github.io/haproxy-dconv/1.8/configuration.html#8
    https://www.haproxy.com/blog/introduction-to-haproxy-logging/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/log/haproxy/*",
                    "/var/log/haproxy.log",
                    "/var/log/haproxy-traffic.log",
                    "/var/log/haproxy-admin.log",
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


class JenkinsLogFile(GRRArtifactBase):
    """
    Jenkins log file

    Reference URLs: https://wiki.jenkins.io/display/JENKINS/Logging.html
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/var/log/jenkins/jenkins.log"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class OsqueryLogFiles(GRRArtifactBase):
    """
    Osquery daemon log files

    Reference URLs: https://osquery.readthedocs.io/en/stable/deployment/logging/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/log/osquery/osqueryd.results.log",
                    "/var/log/osquery/osqueryd.snapshots.log",
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
