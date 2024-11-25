"""
Auto-generated classes from the YAML declarations in linux_proc.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr import linux_proc
from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class LinuxASLREnabled(GRRArtifactBase):
    """
    Kernel ASLR state.

    Reference URLs: https://www.kernel.org/doc/Documentation/sysctl/kernel.txt
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/proc/sys/kernel/randomize_va_space"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxIgnoreICMPBroadcasts(GRRArtifactBase):
    """
    Whether the system ignores ICMP pings.

    Reference URLs:
    https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/proc/sys/net/ipv4/icmp_echo_ignore_broadcasts"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxKernelBootloader(GRRArtifactBase):
    """
    Bootloader state acquired from the kernel.

    Reference URLs: https://www.kernel.org/doc/Documentation/sysctl/kernel.txt
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/proc/sys/kernel/bootloader_type",
                    "/proc/sys/kernel/bootloader_version",
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


class LinuxKernelModuleRestrictions(GRRArtifactBase):
    """
    Module loading controls.

    Reference URLs: https://www.kernel.org/doc/Documentation/sysctl/kernel.txt
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/proc/sys/kernel/kexec_load_disabled",
                    "/proc/sys/kernel/modules_disabled",
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


class LinuxKernelModuleTaintStatus(GRRArtifactBase):
    """
    Taint state of loaded modules (binary blobs, unsigned modules etc).

    Reference URLs: https://www.kernel.org/doc/Documentation/sysctl/kernel.txt
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/proc/sys/kernel/tainted"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxNetworkIpForwardingState(GRRArtifactBase):
    """
    IP forwarding states.

    Reference URLs:
    https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/proc/sys/net/ipv*/conf/*/forwarding",
                    "/proc/sys/net/ipv4/conf/*/mc_forwarding",
                    "/proc/sys/net/ipv4/ip_forward",
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


class LinuxNetworkPathFilteringSettings(GRRArtifactBase):
    """
    States that determine how the system responds to route manipulation.

    Reference URLs:
    https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/proc/sys/net/ipv*/conf/*/accept_source_route",
                    "/proc/sys/net/ipv4/conf/*/rp_filter",
                    "/proc/sys/net/ipv4/conf/*/log_martians",
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


class LinuxNetworkRedirectState(GRRArtifactBase):
    """
    Redirect send/receive states.

    Reference URLs:
    https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/proc/sys/net/ipv*/conf/*/accept_redirects",
                    "/proc/sys/net/ipv4/conf/*/secure_redirects",
                    "/proc/sys/net/ipv4/conf/*/send_redirects",
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


class LinuxProcArp(GRRArtifactBase):
    """
    ARP table via /proc/net/arp.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/proc/net/arp"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxProcMounts(GRRArtifactBase):
    """
    Current mounted filesystems.

    Reference URLs:
    https://www.kernel.org/doc/Documentation/filesystems/proc.txt
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/proc/mounts"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxProcSysHardeningSettings(GRRArtifactBase):
    """
    Linux sysctl settings obtained from /proc/sys.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "LinuxASLREnabled",
                    "LinuxIgnoreICMPBroadcasts",
                    "LinuxKernelBootloader",
                    "LinuxKernelModuleTaintStatus",
                    "LinuxKernelModuleRestrictions",
                    "LinuxNetworkIpForwardingState",
                    "LinuxNetworkPathFilteringSettings",
                    "LinuxNetworkRedirectState",
                    "LinuxRestrictedDmesgReadPrivileges",
                    "LinuxRestrictedKernelPointerReadPrivileges",
                    "LinuxSecureSuidCoreDumps",
                    "LinuxSecureFsLinks",
                    "LinuxSyncookieState",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "LinuxASLREnabled": linux_proc.LinuxASLREnabled,
        "LinuxRestrictedDmesgReadPrivileges": linux_proc.LinuxRestrictedDmesgReadPrivileges,
        "LinuxNetworkIpForwardingState": linux_proc.LinuxNetworkIpForwardingState,
        "LinuxSyncookieState": linux_proc.LinuxSyncookieState,
        "LinuxKernelBootloader": linux_proc.LinuxKernelBootloader,
        "LinuxNetworkPathFilteringSettings": linux_proc.LinuxNetworkPathFilteringSettings,
        "LinuxSecureFsLinks": linux_proc.LinuxSecureFsLinks,
        "LinuxKernelModuleRestrictions": linux_proc.LinuxKernelModuleRestrictions,
        "LinuxNetworkRedirectState": linux_proc.LinuxNetworkRedirectState,
        "LinuxKernelModuleTaintStatus": linux_proc.LinuxKernelModuleTaintStatus,
        "LinuxRestrictedKernelPointerReadPrivileges": linux_proc.LinuxRestrictedKernelPointerReadPrivileges,
        "LinuxSecureSuidCoreDumps": linux_proc.LinuxSecureSuidCoreDumps,
        "LinuxIgnoreICMPBroadcasts": linux_proc.LinuxIgnoreICMPBroadcasts,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxRestrictedDmesgReadPrivileges(GRRArtifactBase):
    """
    Restrict whether non-privileged users can read dmesg.

    Reference URLs: https://www.kernel.org/doc/Documentation/sysctl/kernel.txt
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/proc/sys/kernel/dmesg_restrict"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxRestrictedKernelPointerReadPrivileges(GRRArtifactBase):
    """
    Memory address obfuscation settings.

    Reference URLs: https://www.kernel.org/doc/Documentation/sysctl/kernel.txt
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/proc/sys/kernel/kptr_restrict"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxSecureFsLinks(GRRArtifactBase):
    """
    Security controls to restrict operations on links in world writable
    directories.

    Reference URLs: https://www.kernel.org/doc/Documentation/sysctl/fs.txt
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/proc/sys/fs/protected_hardlinks",
                    "/proc/sys/fs/protected_symlinks",
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


class LinuxSecureSuidCoreDumps(GRRArtifactBase):
    """
    Security controls for suid core dumps.

    Reference URLs: https://www.kernel.org/doc/Documentation/sysctl/fs.txt
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/proc/sys/fs/suid_dumpable"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxSyncookieState(GRRArtifactBase):
    """
    Whether the system uses syncookies.

    Reference URLs:
    https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/proc/sys/net/ipv4/tcp_syncookies"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxSysctlCmd(GRRArtifactBase):
    """
    Linux output of systctl -a.

    Reference URLs: https://www.kernel.org/doc/Documentation/sysctl
    """

    SOURCES = [
        {"type": "COMMAND", "attributes": {"args": ["-a"], "cmd": "/sbin/sysctl"}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None
