"""
Auto-generated classes from the YAML declarations in esxi.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class ESXApiForwarder(GRRArtifactBase):
    """
    Records activities related to the vSphere Trust Authority API forwarder.
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/var/run/log/esxapiadapter.log"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ESXiAttestationService(GRRArtifactBase):
    """
    Records activities related to the vSphere Trust Authority Attestation
    Service.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/run/log/attestd.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ESXiAuthenticationLog(GRRArtifactBase):
    """
    Contains all events related to authentication for the local system.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/auth.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ESXiHostAgentLog(GRRArtifactBase):
    """
    Contains information about the agent that manages and configures the ESXi
    host and its virtual machines.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/hostd.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ESXiKeyProviderService(GRRArtifactBase):
    """
    Records activities related to the vSphere Trust Authority Key Provider
    Service.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/run/log/kmxd.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ESXiQuickBootLog(GRRArtifactBase):
    """
    Contains all events related to restarting an ESXi host through Quick Boot.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/loadESX.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ESXiShellLog(GRRArtifactBase):
    """
    Contains a record of all commands typed into the ESXi Shell and shell events
    (for example, when the shell was enabled)
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/shell.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ESXiSystemLogsDirectory(GRRArtifactBase):
    """
    ESXi System Logs Directory

    Reference URLs:
    https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.monitoring.doc/GUID-DACC9E0E-E857-4AE1-A469-3FDAE2B391A0.html
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/run/log/*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ESXiSystemMessageslog(GRRArtifactBase):
    """
    Contains all general log messages and can be used for troubleshooting. This
    information was formerly located in the messages log file.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/syslog.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ESXTokenService(GRRArtifactBase):
    """
    Records activities related to the vSphere Trust Authority ESX Token Service.
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/var/run/log/esxtokend.log"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ESXiTrustedInfrastructureAgentLog(GRRArtifactBase):
    """
    Records activities related to the Client Service on the ESXi Trusted Host.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/run/log/kmxa.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ESXiVMKernelLog(GRRArtifactBase):
    """
    Records activities related to virtual machines and ESXi.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/vmkernel.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ESXiVMKernelSummaryLog(GRRArtifactBase):
    """
    Used to determine uptime and availability statistics for ESXi (comma
    separated).
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/var/log/vmksummarylog.log"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ESXiVMKernelWarningsLog(GRRArtifactBase):
    """
    Records activities related to virtual machines.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/vmkwarning.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class vCenterServerAgentLog(GRRArtifactBase):
    """
    Contains information about the agent that communicates with vCenter Server
    (if the host is managed by vCenter Server).
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/vxpa.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class vSphereClientLogsDirectory(GRRArtifactBase):
    """
    vSphere Client Logs Directory

    Reference URLs:
    https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.monitoring.doc/GUID-7E10C58F-16EA-44AB-8AA0-8D4A66399879.html
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/var/log/vmware/vsphere-ui/logs/*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.ESXI
    ]
    aliases: ClassVar[Optional[list[str]]] = None
