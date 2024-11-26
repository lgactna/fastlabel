"""
Auto-generated classes from the YAML declarations in linux.yaml.

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


class AnacronFiles(GRRArtifactBase):
    """
    Anacron files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/anacrontab",
                    "/etc/cron.daily/*",
                    "/etc/cron.hourly/*",
                    "/etc/cron.monthly/*",
                    "/etc/cron.weekly/*",
                    "/var/spool/anacron/cron.daily",
                    "/var/spool/anacron/cron.hourly",
                    "/var/spool/anacron/cron.monthly",
                    "/var/spool/anacron/cron.weekly",
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


class AptitudeLogFiles(GRRArtifactBase):
    """
    Linux aptitude package manager log files.

    Reference URLs: https://www.debian.org/doc/manuals/aptitude/rn01re01.en.html
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/aptitude*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class APTSources(GRRArtifactBase):
    """
    APT package sources list

    Reference URLs:
    http://manpages.ubuntu.com/manpages/trusty/en/man5/sources.list.5.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/etc/apt/sources.list", "/etc/apt/sources.list.d/*.list"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class APTTrustKeys(GRRArtifactBase):
    """
    APT trusted keys

    Reference URLs: https://wiki.debian.org/SecureApt
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/apt/trusted.gpg",
                    "/etc/apt/trusted.gpg.d/*.gpg",
                    "/etc/apt/trustdb.gpg",
                    "/usr/share/keyrings/*.gpg",
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


class CronAtAllowDenyFiles(GRRArtifactBase):
    """
    Files containing users authorised to run cron or at jobs.

    Reference URLs:
    http://manpages.ubuntu.com/manpages/saucy/man5/at.allow.5.html
    http://manpages.ubuntu.com/manpages/precise/en/man1/crontab.1.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/cron.allow",
                    "/etc/cron.deny",
                    "/etc/at.allow",
                    "/etc/at.deny",
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


class DebianPackagesLogFiles(GRRArtifactBase):
    """
    Linux dpkg log files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/log/dpkg.log*",
                    "/var/log/apt/history.log*",
                    "/var/log/apt/term.log*",
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


class DebianPackagesStatus(GRRArtifactBase):
    """
    Linux dpkg status file.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/lib/dpkg/status"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class DebianVersion(GRRArtifactBase):
    """
    Debian version information.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/debian_version"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class DNSResolvConfFile(GRRArtifactBase):
    """
    DNS Resolver configuration file.

    Reference URLs: http://man7.org/linux/man-pages/man5/resolv.conf.5.html
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/resolv.conf"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class GnomeApplicationState(GRRArtifactBase):
    """
    Gnome application state for frequent application data.

    Reference URLs: https://forensics.wiki/gnome_desktop_environment
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.local/share/gnome-shell/application_state"
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


class FreeDesktopTrashInfoFiles(GRRArtifactBase):
    """
    FreeDesktop.org Trash Info Files.

    Reference URLs:
    https://specifications.freedesktop.org/trash-spec/trashspec-latest.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/.local/share/Trash/info/*.trashinfo"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class FreeDesktopTrashFiles(GRRArtifactBase):
    """
    FreeDesktop.org Trash Files.

    Reference URLs:
    https://specifications.freedesktop.org/trash-spec/trashspec-latest.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/.local/share/Trash/files/*"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class GnomeTracker(GRRArtifactBase):
    """
    Gnome Tracker database and backup files.

    Reference URLs:
    https://wiki.gnome.org/Projects/Tracker/Documentation/GettingStarted
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.cache/tracker/*",
                    "%%users.homedir%%/.local/share/tracker/data/*",
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


class GTKRecentlyUsedDatabase(GRRArtifactBase):
    """
    GTK Recent Manager database.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/.local/share/recently-used.xbel"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class HostAccessPolicyConfiguration(GRRArtifactBase):
    """
    Linux files related to host access policy configuration.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/hosts.allow", "/etc/hosts.deny"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class IPTablesRules(GRRArtifactBase):
    """
    List IPTables rules.
    """

    SOURCES = [
        {
            "type": "COMMAND",
            "attributes": {"args": ["-L", "-n", "-v"], "cmd": "/sbin/iptables"},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class KernelModules(GRRArtifactBase):
    """
    Kernel modules to be loaded on boot.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/modules.conf", "/etc/modprobe.d/*"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LessHistoryFile(GRRArtifactBase):
    """
    less history file which remembers search and shell commands

    Reference URLs: https://man7.org/linux/man-pages/man1/less.1.html
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["%%users.homedir%%/.lesshst"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxAtJobs(GRRArtifactBase):
    """
    Linux at jobs.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/spool/at/*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxAtJobsTemporaryOutputs(GRRArtifactBase):
    """
    Linux at jobs temporary outputs.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/var/spool/at/spool/*", "/var/spool/cron/atspool/*"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxAuditLogs(GRRArtifactBase):
    """
    Linux audit log files.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/audit/*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxAuthLogs(GRRArtifactBase):
    """
    Linux authentication log files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/var/log/auth*", "/var/log/secure*"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxCACertificatesConfiguration(GRRArtifactBase):
    """
    Linux CA Certificates configuration file.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/ca-certificates.conf"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = []
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxCACertificates(GRRArtifactBase):
    """
    Linux CA Certificates.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/ssl/certs/ca-certificates.crt",
                    "/usr/share/ca-certificates/*",
                    "/usr/local/share/ca-certificates/*",
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


class LinuxCronLogs(GRRArtifactBase):
    """
    Linux cron log files.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/cron.log*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxCronTabs(GRRArtifactBase):
    """
    Crontab files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/etc/crontab", "/etc/cron.d/*", "/var/spool/cron/**"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxDaemonLogFiles(GRRArtifactBase):
    """
    Linux daemon log files.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/daemon*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxDHCPConfigurationFile(GRRArtifactBase):
    """
    Linux DHCP Configuration File
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/dhcp/dhcp.conf"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxDistributionRelease(GRRArtifactBase):
    """
    Linux distribution release information of non-LSB compliant systems.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/centos-release",
                    "/etc/enterprise-release",
                    "/etc/oracle-release",
                    "/etc/redhat-release",
                    "/etc/rocky-release",
                    "/etc/SuSE-release",
                    "/etc/system-release",
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


class LinuxDSDTTable(GRRArtifactBase):
    """
    Linux file containing DSDT table.

    Reference URLs:
    https://www.kernel.org/doc/Documentation/acpi/initrd_table_override.txt
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/sys/firmware/acpi/tables/DSDT"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxFstab(GRRArtifactBase):
    """
    Linux fstab file.

    Reference URLs: http://en.wikipedia.org/wiki/Fstab
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/fstab"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxGrubConfiguration(GRRArtifactBase):
    """
    Linux grub configuration file.

    Reference URLs: https://en.wikipedia.org/wiki/GNU_GRUB
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/boot/grub/grub.cfg", "/boot/grub2/grub.cfg"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxHostnameFile(GRRArtifactBase):
    """
    Linux hostname file.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/hostname"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxIfUpDownScripts(GRRArtifactBase):
    """
    ifupdown scripts executed whenever a network interface goes up or down
    respectively.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/etc/network/if-up.d/*", "/etc/network/if-down.d/*"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxInitrdFiles(GRRArtifactBase):
    """
    Initrd (initramfs) files in /boot/ executed on startup.

    Reference URLs: http://en.wikipedia.org/wiki/Initrd
    https://www.kernel.org/doc/Documentation/initrd.txt
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/boot/initramfs*", "/boot/initrd*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxIssueFile(GRRArtifactBase):
    """
    Linux prelogin message and identification (issue) file.

    Reference URLs: https://linux.die.net/man/5/issue
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/etc/issue", "/etc/issue.net"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxKerberosConfiguration(GRRArtifactBase):
    """
    Linux Kerberos configuration information.

    Reference URLs:
    https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/krb5.conf"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxKernelLogFiles(GRRArtifactBase):
    """
    Linux kernel log files.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/kern*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxLastlogFile(GRRArtifactBase):
    """
    Linux lastlog file.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/lastlog"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxLoaderSystemPreloadFile(GRRArtifactBase):
    """
    Linux dynamic linker/loader system-wide preload file (ld.so.preload).

    Reference URLs: http://man7.org/linux/man-pages/man8/ld.so.8.html
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/ld.so.preload"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxLSBInit(GRRArtifactBase):
    """
    Linux LSB-style init scripts.

    Reference URLs: https://wiki.debian.org/LSBInitScripts
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/init.d/*",
                    "/etc/insserv.conf",
                    "/etc/insserv.conf.d/**",
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


class LinuxLocalTime(GRRArtifactBase):
    """
    Local time zone configuration
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/localtime"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxLSBRelease(GRRArtifactBase):
    """
    Linux Standard Base (LSB) release information

    Reference URLs: https://linux.die.net/man/1/lsb_release
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/lsb-release"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxMessagesLogFiles(GRRArtifactBase):
    """
    Linux messages log files.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/messages*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxMountCmd(GRRArtifactBase):
    """
    Linux output of mount
    """

    SOURCES = [{"type": "COMMAND", "attributes": {"args": [], "cmd": "/bin/mount"}}]
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


class LinuxNetworkManager(GRRArtifactBase):
    """
    Linux NetworkManager files.

    Reference URLs: https://linux.die.net/man/5/networkmanager.conf
    https://man.archlinux.org/man/NetworkManager.conf.5.en#FILE_FORMAT
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/NetworkManager/conf.d/name.conf",
                    "/etc/NetworkManager/NetworkManager.conf",
                    "/etc/NetworkManager/system-connections",
                    "/run/NetworkManager/conf.d/name.conf",
                    "/usr/lib/NetworkManager/conf.d/name.conf",
                    "/var/lib/NetworkManager/NetworkManager-intern.conf",
                    "/var/lib/NetworkManager/*",
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


class LinuxNssCachePasswdFile(GRRArtifactBase):
    """
    Local NSS database for remote directory services.

    Reference URLs: https://github.com/google/nsscache
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/passwd.cache"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxPamConfigs(GRRArtifactBase):
    """
    Configuration files for PAM.

    Reference URLs: http://www.linux-pam.org/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/pam.conf",
                    "/etc/pam.d",
                    "/etc/pam.d/common-password",
                    "/etc/pam.d/*",
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


class LinuxPasswdFile(GRRArtifactBase):
    """
    Linux passwd file.

    A passwd file consist of colon separated values in the format:
    username:password:uid:gid:full name:home directory:shell
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/passwd"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxSystemdOSRelease(GRRArtifactBase):
    """
    Linux systemd /etc/os-release file

    Reference URLs:
    https://www.freedesktop.org/software/systemd/man/os-release.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/os-release", "/usr/lib/os-release"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxRsyslogConfigs(GRRArtifactBase):
    """
    Linux rsyslog configurations.

    Reference URLs: http://www.rsyslog.com/doc/rsyslog_conf.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/etc/rsyslog.conf", "/etc/rsyslog.d", "/etc/rsyslog.d/*"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxSystemdServices(GRRArtifactBase):
    """
    Linux systemd service unit files

    Reference URLs:
    https://www.freedesktop.org/software/systemd/man/systemd.unit.html#System%20Unit%20Search%20Path
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/systemd/system.control/*.service",
                    "/etc/systemd/systemd.attached/*.service",
                    "/etc/systemd/system/*.service",
                    "/etc/systemd/user/*.service",
                    "/lib/systemd/system/*.service",
                    "/lib/systemd/user/*.service",
                    "/run/systemd/generator.early/*.service",
                    "/run/systemd/generator.late/*.service",
                    "/run/systemd/generator/*.service",
                    "/run/systemd/system.control/*.service",
                    "/run/systemd/systemd.attached/*.service",
                    "/run/systemd/system/*.service",
                    "/run/systemd/transient/*.service",
                    "/run/systemd/user/*.service",
                    "/run/user/*/systemd/generator.early/*.service",
                    "/run/user/*/systemd/generator.late/*.service",
                    "/run/user/*/systemd/generator/*.service",
                    "/run/user/*/systemd/transient/*.service",
                    "/run/user/*/systemd/user.control/*.service",
                    "/run/user/*/systemd/user/*.service",
                    "/usr/lib/systemd/system/*.service",
                    "/usr/lib/systemd/user/*.service",
                    "%%users.homedir%%/.config/systemd/user.control/*.service",
                    "%%users.homedir%%/.config/systemd/user/*.service",
                    "%%users.homedir%%/.local/share/systemd/user/*.service",
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


class LinuxSysVInit(GRRArtifactBase):
    """
    Services started by sysv-style init scripts.

    Reference URLs: http://savannah.nongnu.org/projects/sysvinit
    http://docs.oracle.com/cd/E37670_01/E41138/html/ol_svcscripts.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/rc.local",
                    "/etc/rc*.d",
                    "/etc/rc*.d/*",
                    "/etc/rc.d/rc*.d/*",
                    "/etc/rc.d/init.d/*",
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


class LinuxXinetd(GRRArtifactBase):
    """
    Linux xinetd configurations.

    Reference URLs: http://en.wikipedia.org/wiki/Xinetd
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/xinetd.conf", "/etc/xinetd.d/**"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxSSDTTables(GRRArtifactBase):
    """
    Linux files containing SSDT table.

    Reference URLs:
    https://www.kernel.org/doc/Documentation/acpi/initrd_table_override.txt
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/sys/firmware/acpi/tables/SSDT*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxSudoReplayLogs(GRRArtifactBase):
    """
    Linux sudoreplay log files.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/sudo-io/**"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxSysctlConfigurationFiles(GRRArtifactBase):
    """
    Linux sysctl preload/configuration files.

    Reference URLs: https://man7.org/linux/man-pages/man5/sysctl.conf.5.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/sysctl.d/*.conf",
                    "/run/sysctl.d/*.conf",
                    "/usr/local/lib/sysctl.d/*.conf",
                    "/usr/lib/sysctl.d/*.conf",
                    "/lib/sysctl.d/*.conf",
                    "/etc/sysctl.con",
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


class LinuxSysLogFiles(GRRArtifactBase):
    """
    Linux syslog log files.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/syslog*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxSyslogNgConfigs(GRRArtifactBase):
    """
    Linux syslog-ng configurations.

    Reference URLs: http://linux.die.net/man/5/syslog-ng.conf
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/syslog-ng/syslog-ng.conf",
                    "/etc/syslog-ng/conf-d/*.conf",
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


class LinuxSystemdJournalConfig(GRRArtifactBase):
    """
    Linux systemd journal config file

    Reference URLs: https://wiki.archlinux.org/title/Systemd/Journal
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/etc/systemd/journald.conf"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxSystemdJournalLogs(GRRArtifactBase):
    """
    Linux systemd journal log files

    Reference URLs: https://wiki.archlinux.org/title/Systemd/Journal
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/log/journal/*/*.journal",
                    "/var/log/journal/*/*.journal~",
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


class LinuxSystemdTimers(GRRArtifactBase):
    """
    Linux systemd Timer files

    Reference URLs:
    https://www.freedesktop.org/software/systemd/man/systemd.timer.html#
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/systemd/system.control/*.timer",
                    "/etc/systemd/systemd.attached/*.timer",
                    "/etc/systemd/system/*.timer",
                    "/etc/systemd/user/*.timer",
                    "/lib/systemd/system/*.timer",
                    "/lib/systemd/user/*.timer",
                    "/run/systemd/generator.early/*.timer",
                    "/run/systemd/generator.late/*.timer",
                    "/run/systemd/generator/*.timer",
                    "/run/systemd/system.control/*.timer",
                    "/run/systemd/systemd.attached/*.timer",
                    "/run/systemd/system/*.timer",
                    "/run/systemd/transient/*.timer",
                    "/run/systemd/user/*.timer",
                    "/run/user/*/systemd/generator.early/*.timer",
                    "/run/user/*/systemd/generator.late/*.timer",
                    "/run/user/*/systemd/generator/*.timer",
                    "/run/user/*/systemd/transient/*.timer",
                    "/run/user/*/systemd/user.control/*.timer",
                    "/run/user/*/systemd/user/*.timer",
                    "/usr/lib/systemd/system/*.timer",
                    "/usr/lib/systemd/user/*.timer",
                    "%%users.homedir%%/.config/systemd/user.control/*.timer",
                    "%%users.homedir%%/.config/systemd/user/*.timer",
                    "%%users.homedir%%/.local/share/systemd/user/*.timer",
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


class LinuxTimezoneFile(GRRArtifactBase):
    """
    Linux timezone file.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/timezone"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxUdevRules(GRRArtifactBase):
    """
    Linux udev rules for the events received by the udev's daemon from the Linux
    kernel.

    Reference URLs: https://wiki.archlinux.org/title/Udev
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/usr/lib/udev/rules.d/*", "/etc/udev/rules.d/*"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxUtmpFiles(GRRArtifactBase):
    """
    Linux btmp, utmp and wtmp login record files.

    Reference URLs:
    https://github.com/libyal/dtformats/blob/main/documentation/Utmp%20login%20records%20format.asciidoc
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/var/log/btmp*", "/var/log/wtmp*", "/var/run/utmp*"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxWtmp(GRRArtifactBase):
    """
    Linux wtmp login record file

    Reference URLs:
    https://github.com/libyal/dtformats/blob/main/documentation/Utmp%20login%20records%20format.asciidoc
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/wtmp*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ListProcessesPsCommand(GRRArtifactBase):
    """
    Full process listing via the 'ps' command.

    Reference URLs: https://gitlab.com/procps-ng/procps
    """

    SOURCES = [{"type": "COMMAND", "attributes": {"args": ["-ef"], "cmd": "/bin/ps"}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LoadedKernelModules(GRRArtifactBase):
    """
    Linux output of lsmod.
    """

    SOURCES = [{"type": "COMMAND", "attributes": {"args": [], "cmd": "/sbin/lsmod"}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LocateDatabase(GRRArtifactBase):
    """
    locate/mlocate database and updatedb configuration.

    Reference URLs: https://linux.die.net/man/1/locate
    https://linux.die.net/man/8/updatedb
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/var/lib/mlocate/mlocate.db", "/etc/updatedb.conf"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LoginPolicyConfiguration(GRRArtifactBase):
    """
    Linux files related to login policy configuration.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/netgroup",
                    "/etc/nsswitch.conf",
                    "/etc/passwd",
                    "/etc/shadow",
                    "/etc/security/access.conf",
                    "/root/.k5login",
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


class MySQLHistoryFile(GRRArtifactBase):
    """
    MySQL History file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/.mysql_history",
                    "/root/.mysql_history",
                    "%%users.homedir%%/.mysql_history",
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


class NanoHistoryFile(GRRArtifactBase):
    """
    nano history file that logs search and replace strings.

    Reference URLs: https://www.nano-editor.org/dist/v2.2/nano.html
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["%%users.homedir%%/.nano_history"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class NetgroupConfiguration(GRRArtifactBase):
    """
    Linux netgroup configuration.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/netgroup"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class NtpConfFile(GRRArtifactBase):
    """
    The configuration file for ntpd. e.g. ntp.conf.

    Reference URLs: https://www.freebsd.org/cgi/man.cgi?query=ntp.conf&sektion=5
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/etc/ntp.conf"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class PCIDevicesInfoFiles(GRRArtifactBase):
    """
    Info and config files for PCI devices located on the system.

    Reference URLs:
    https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-bus-pci
    https://www.kernel.org/doc/Documentation/filesystems/sysfs-pci.txt
    https://wiki.debian.org/HowToIdentifyADevice/PCI
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/sys/bus/pci/devices/*/vendor",
                    "/sys/bus/pci/devices/*/device",
                    "/sys/bus/pci/devices/*/class",
                    "/sys/bus/pci/devices/*/config",
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


class PostgreSQLHistoryFile(GRRArtifactBase):
    """
    PostgreSQL History file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/.psql_history",
                    "/root/.psql_history",
                    "/var/lib/postgresql/.psql_history",
                    "/var/lib/pgsql/.psql_history",
                    "%%users.homedir%%/.psql_history",
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


class PythonHistoryFile(GRRArtifactBase):
    """
    Python REPL history file.
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["%%users.homedir%%/.python_history"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class RHostsFile(GRRArtifactBase):
    """
    RHosts file.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["%%users.homedir%%/.rhosts"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SambaLogFiles(GRRArtifactBase):
    """
    Samba log files.

    Reference URLs:
    https://wiki.samba.org/index.php/Configuring_Logging_on_a_Samba_Server
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/samba/*.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SecretsServiceDatabaseFile(GRRArtifactBase):
    """
    The System Security Services Daemon (SSSD) database file.

    Reference URLs:
    https://docs.pagure.org/SSSD.sssd/design_pages/secrets_service.html
    https://www.fireeye.com/blog/threat-research/2020/04/kerberos-tickets-on-linux-red-teams.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/var/lib/sss/secrets/secrets.ldb",
                    "/var/lib/sss/secrets/.secrets.mkey",
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


class SQLiteHistoryFile(GRRArtifactBase):
    """
    SQLite History file.
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["%%users.homedir%%/.sqlite_history"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SSHAuthorizedKeysFiles(GRRArtifactBase):
    """
    SSH authorized keys files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.ssh/authorized_keys",
                    "%%users.homedir%%/.ssh/authorized_keys2",
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


class SSHHostPubKeys(GRRArtifactBase):
    """
    SSH host public keys
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/etc/ssh/ssh_host_*_key.pub"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SSHKnownHostsFiles(GRRArtifactBase):
    """
    SSH known_hosts files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/.ssh/known_hosts", "/etc/ssh/known_hosts"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ThumbnailCacheFolder(GRRArtifactBase):
    """
    Thumbnail cache folder.
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["%%users.homedir%%/.thumbnails/**3"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class UFWConfigFiles(GRRArtifactBase):
    """
    UFW Configuration files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/default/ufw",
                    "/etc/ufw/sysctl.conf",
                    "/etc/ufw/*.rules",
                    "/etc/ufw/applications.d/*",
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


class UFWLogFile(GRRArtifactBase):
    """
    UFW Log file.
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/var/log/ufw.log"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class Viminfo(GRRArtifactBase):
    """
    Viminfo file.
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["%%users.homedir%%/.viminfo"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WgetHSTSdatabase(GRRArtifactBase):
    """
    Default wget HTTP Strict Transport Security (HSTS) database

    Reference URLs:
    https://www.gnu.org/software/wget/manual/html_node/HTTPS-_0028SSL_002fTLS_0029-Options.html
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["%%users.homedir%%/.wget-hsts"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class XDGAutostartEntries(GRRArtifactBase):
    """
    XDG Autostart Entries

    Reference URLs:
    https://specifications.freedesktop.org/autostart-spec/autostart-spec-latest.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/xdg/autostart/*.desktop",
                    "%%users.homedir%%/.config/autostart/*.desktop",
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


class YumSources(GRRArtifactBase):
    """
    Yum package sources list

    Reference URLs:
    https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/System_Administrators_Guide/sec-Configuring_Yum_and_Yum_Repositories.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/etc/yum.conf", "/etc/yum.repos.d/*.repo"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ZeitgeistDatabase(GRRArtifactBase):
    """
    Zeitgeist user activity database.

    Reference URLs: https://forensics.wiki/zeitgeist
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.local/share/zeitgeist/activity.sqlite",
                    "%%users.homedir%%/.local/share/zeitgeist/activity.sqlite-wal",
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


class LinuxScheduleFiles(GRRArtifactBase):
    """
    All Linux job scheduling files.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {"names": ["AnacronFiles", "LinuxCronTabs", "LinuxAtJobs"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "LinuxAtJobs": LinuxAtJobs,
        "LinuxCronTabs": LinuxCronTabs,
        "AnacronFiles": AnacronFiles,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxMountInfo(GRRArtifactBase):
    """
    Linux mount options.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {"names": ["LinuxFstab", "LinuxProcMounts"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "LinuxProcMounts": linux_proc.LinuxProcMounts,
        "LinuxFstab": LinuxFstab,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxReleaseInfo(GRRArtifactBase):
    """
    Release information for Linux platforms.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "LinuxDistributionRelease",
                    "LinuxLSBRelease",
                    "LinuxSystemdOSRelease",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "LinuxDistributionRelease": LinuxDistributionRelease,
        "LinuxSystemdOSRelease": LinuxSystemdOSRelease,
        "LinuxLSBRelease": LinuxLSBRelease,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class LinuxServices(GRRArtifactBase):
    """
    Services running on a Linux system.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "LinuxXinetd",
                    "LinuxLSBInit",
                    "LinuxSysVInit",
                    "LinuxSystemdServices",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "LinuxLSBInit": LinuxLSBInit,
        "LinuxSystemdServices": LinuxSystemdServices,
        "LinuxSysVInit": LinuxSysVInit,
        "LinuxXinetd": LinuxXinetd,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None
