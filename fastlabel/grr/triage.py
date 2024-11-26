"""
Auto-generated classes from the YAML declarations in triage.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr import (
    antivirus,
    applications,
    cloud_services,
    config_files,
    database_servers,
    file_systems,
    hadoop,
    instant_messaging,
    java,
    legacy,
    linux,
    linux_proc,
    linux_services,
    shell,
    tomcat,
    unix_common,
    webbrowser,
    webservers,
    windows,
    wmi,
)
from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class TriageApplicationConfigsAndLogs(GRRArtifactBase):
    """
    Group of configuration files and logs of installed applications.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "ApacheAccessLogs",
                    "ApacheConfigurationFolder",
                    "ApacheDefaultSiteConfigurationFile",
                    "ApacheErrorLogs",
                    "ApacheKafkaLogFiles",
                    "ElasticsearchAccessLog",
                    "ElasticsearchAuditLog",
                    "ElasticsearchGCLog",
                    "ElasticsearchLogs",
                    "ElasticsearchServerLog",
                    "HadoopAppLogs",
                    "HadoopAppRoot",
                    "HadoopYarnLogs",
                    "HAProxyLogFiles",
                    "JenkinsLogFile",
                    "NginxAccessLogs",
                    "NginxErrorLogs",
                    "OsqueryLogFiles",
                    "TomcatLogFiles",
                    "TomcatPasswordFile",
                    "WordpressConfigFile",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "MicrosoftIISLogs",
                    "MicrosoftSqlServerErrorLogs",
                    "RedisConfigFile",
                    "TomcatFiles",
                    "TomcatPasswordFile",
                ]
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "MicrosoftSqlServerErrorLogs": applications.MicrosoftSqlServerErrorLogs,
        "NginxAccessLogs": webservers.NginxAccessLogs,
        "HadoopAppLogs": hadoop.HadoopAppLogs,
        "WordpressConfigFile": webservers.WordpressConfigFile,
        "HadoopYarnLogs": hadoop.HadoopYarnLogs,
        "OsqueryLogFiles": linux_services.OsqueryLogFiles,
        "ElasticsearchLogs": database_servers.ElasticsearchLogs,
        "JenkinsLogFile": linux_services.JenkinsLogFile,
        "ApacheDefaultSiteConfigurationFile": webservers.ApacheDefaultSiteConfigurationFile,
        "ApacheAccessLogs": webservers.ApacheAccessLogs,
        "MicrosoftIISLogs": webservers.MicrosoftIISLogs,
        "ElasticsearchGCLog": database_servers.ElasticsearchGCLog,
        "ElasticsearchServerLog": database_servers.ElasticsearchServerLog,
        "ElasticsearchAccessLog": database_servers.ElasticsearchAccessLog,
        "HAProxyLogFiles": linux_services.HAProxyLogFiles,
        "TomcatPasswordFile": tomcat.TomcatPasswordFile,
        "ApacheErrorLogs": webservers.ApacheErrorLogs,
        "TomcatFiles": tomcat.TomcatFiles,
        "ApacheKafkaLogFiles": linux_services.ApacheKafkaLogFiles,
        "ApacheConfigurationFolder": webservers.ApacheConfigurationFolder,
        "ElasticsearchAuditLog": database_servers.ElasticsearchAuditLog,
        "RedisConfigFile": config_files.RedisConfigFile,
        "TomcatLogFiles": tomcat.TomcatLogFiles,
        "HadoopAppRoot": hadoop.HadoopAppRoot,
        "NginxErrorLogs": webservers.NginxErrorLogs,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriageDatabaseConfigsAndLogs(GRRArtifactBase):
    """
    Group of configuration files and logs of installed databases.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "MongoDBConfigurationFile",
                    "MongoDBLogFiles",
                    "MySQLConfigurationFiles",
                    "MySQLLogFiles",
                    "OpenSearchLogFiles",
                    "PostgreSQLConfigurationFiles",
                    "PostgreSQLLogFiles",
                    "RedisConfigFile",
                    "RedisConfigurationFile",
                    "RedisLogFiles",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "MongoDBConfigurationFile": database_servers.MongoDBConfigurationFile,
        "PostgreSQLLogFiles": database_servers.PostgreSQLLogFiles,
        "MongoDBLogFiles": database_servers.MongoDBLogFiles,
        "OpenSearchLogFiles": database_servers.OpenSearchLogFiles,
        "RedisConfigurationFile": database_servers.RedisConfigurationFile,
        "RedisLogFiles": database_servers.RedisLogFiles,
        "RedisConfigFile": config_files.RedisConfigFile,
        "PostgreSQLConfigurationFiles": database_servers.PostgreSQLConfigurationFiles,
        "MySQLLogFiles": database_servers.MySQLLogFiles,
        "MySQLConfigurationFiles": database_servers.MySQLConfigurationFiles,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriageExecution(GRRArtifactBase):
    """
    Group of process/command execution related artifacts.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "JavaCacheFiles",
                    "WindowsAMCacheHveFile",
                    "WindowsCIMRepositoryFiles",
                    "WindowsCrashDumps",
                    "WindowsPrefetchFiles",
                    "WindowsRecentFileCacheBCF",
                    "WindowsStartupInfo",
                    "WindowsSuperFetchFiles",
                    "WindowsSystemResourceUsageMonitorDatabaseFile",
                    "WMICCMRUA",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "WindowsSuperFetchFiles": windows.WindowsSuperFetchFiles,
        "JavaCacheFiles": java.JavaCacheFiles,
        "WindowsCrashDumps": windows.WindowsCrashDumps,
        "WMICCMRUA": wmi.WMICCMRUA,
        "WindowsPrefetchFiles": windows.WindowsPrefetchFiles,
        "WindowsStartupInfo": windows.WindowsStartupInfo,
        "WindowsCIMRepositoryFiles": windows.WindowsCIMRepositoryFiles,
        "WindowsRecentFileCacheBCF": windows.WindowsRecentFileCacheBCF,
        "WindowsSystemResourceUsageMonitorDatabaseFile": windows.WindowsSystemResourceUsageMonitorDatabaseFile,
        "WindowsAMCacheHveFile": windows.WindowsAMCacheHveFile,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriageExternalMedia(GRRArtifactBase):
    """
    Group of external media data or events related artifacts.
    """

    SOURCES = [
        {"type": "ARTIFACT_GROUP", "attributes": {"names": ["WindowsSetupApiLogs"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "WindowsSetupApiLogs": windows.WindowsSetupApiLogs
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriageFileSystem(GRRArtifactBase):
    """
    Group of file system related artifacts.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {"names": ["NTFSLogFile", "NTFSMFTFiles"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "NTFSLogFile": file_systems.NTFSLogFile,
        "NTFSMFTFiles": file_systems.NTFSMFTFiles,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriageHistoryFiles(GRRArtifactBase):
    """
    Group of history files related artifacts.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "BashShellHistoryFile",
                    "BourneShellHistoryFile",
                    "FishShellHistoryFile",
                    "MySQLHistoryFile",
                    "PostgreSQLHistoryFile",
                    "PythonHistoryFile",
                    "RootUserShellHistory",
                    "SQLiteHistoryFile",
                    "ZShellHistoryFile",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "ShellConfigurationFile",
                    "ShellHistoryFile",
                    "WindowsPowerShellHistory",
                ]
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "MySQLHistoryFile": linux.MySQLHistoryFile,
        "BourneShellHistoryFile": shell.BourneShellHistoryFile,
        "SQLiteHistoryFile": linux.SQLiteHistoryFile,
        "WindowsPowerShellHistory": windows.WindowsPowerShellHistory,
        "ZShellHistoryFile": shell.ZShellHistoryFile,
        "BashShellHistoryFile": shell.BashShellHistoryFile,
        "ShellHistoryFile": shell.ShellHistoryFile,
        "PostgreSQLHistoryFile": linux.PostgreSQLHistoryFile,
        "FishShellHistoryFile": shell.FishShellHistoryFile,
        "ShellConfigurationFile": shell.ShellConfigurationFile,
        "PythonHistoryFile": linux.PythonHistoryFile,
        "RootUserShellHistory": shell.RootUserShellHistory,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriageInteractiveActivity(GRRArtifactBase):
    """
    Group of interactive user activity related artifacts.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "DropboxClient",
                    "FreeDesktopTrashInfoFiles",
                    "GnomeApplicationState",
                    "GnomeTracker",
                    "GTKRecentlyUsedDatabase",
                    "SignalDatabase",
                    "ThumbnailCacheFolder",
                    "Viminfo",
                    "WgetHSTSdatabase",
                    "XChatLogs",
                    "ZeitgeistDatabase",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "MicrosoftOfficeAutosave",
                    "MicrosoftOfficeMRU",
                    "WindowsActivitiesCacheDatabase",
                    "WindowsRDPClientBitmapCache",
                    "WindowsRecycleBinMetadata",
                    "WindowsSearchDatabaseFile",
                    "WindowsUserAutomaticDestinationsJumpLists",
                    "WindowsUserCustomDestinationsJumpLists",
                    "WindowsUserRecentFiles",
                ]
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "DropboxClient": cloud_services.DropboxClient,
        "GnomeTracker": linux.GnomeTracker,
        "WindowsRDPClientBitmapCache": windows.WindowsRDPClientBitmapCache,
        "GTKRecentlyUsedDatabase": linux.GTKRecentlyUsedDatabase,
        "GnomeApplicationState": linux.GnomeApplicationState,
        "WindowsUserRecentFiles": windows.WindowsUserRecentFiles,
        "WindowsActivitiesCacheDatabase": windows.WindowsActivitiesCacheDatabase,
        "MicrosoftOfficeMRU": applications.MicrosoftOfficeMRU,
        "WindowsUserAutomaticDestinationsJumpLists": windows.WindowsUserAutomaticDestinationsJumpLists,
        "WgetHSTSdatabase": linux.WgetHSTSdatabase,
        "SignalDatabase": instant_messaging.SignalDatabase,
        "ZeitgeistDatabase": linux.ZeitgeistDatabase,
        "WindowsRecycleBinMetadata": windows.WindowsRecycleBinMetadata,
        "MicrosoftOfficeAutosave": applications.MicrosoftOfficeAutosave,
        "WindowsUserCustomDestinationsJumpLists": windows.WindowsUserCustomDestinationsJumpLists,
        "WindowsSearchDatabaseFile": windows.WindowsSearchDatabaseFile,
        "XChatLogs": instant_messaging.XChatLogs,
        "Viminfo": linux.Viminfo,
        "ThumbnailCacheFolder": linux.ThumbnailCacheFolder,
        "FreeDesktopTrashInfoFiles": linux.FreeDesktopTrashInfoFiles,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriageNetwork(GRRArtifactBase):
    """
    Group of network related artifacts.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "DNSResolvConfFile",
                    "HostAccessPolicyConfiguration",
                    "LinuxHostnameFile",
                    "LinuxIgnoreICMPBroadcasts",
                    "LinuxNetworkIpForwardingState",
                    "LinuxNetworkPathFilteringSettings",
                    "LinuxNetworkRedirectState",
                    "LinuxProcArp",
                    "LinuxSyncookieState",
                    "UFWConfigFiles",
                    "UnixHostsFile",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {"names": ["WindowsFirewallLogFile", "WindowsHostsFiles"]},
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "LinuxNetworkRedirectState": linux_proc.LinuxNetworkRedirectState,
        "LinuxProcArp": linux_proc.LinuxProcArp,
        "HostAccessPolicyConfiguration": linux.HostAccessPolicyConfiguration,
        "LinuxNetworkIpForwardingState": linux_proc.LinuxNetworkIpForwardingState,
        "LinuxNetworkPathFilteringSettings": linux_proc.LinuxNetworkPathFilteringSettings,
        "UnixHostsFile": unix_common.UnixHostsFile,
        "UFWConfigFiles": linux.UFWConfigFiles,
        "LinuxSyncookieState": linux_proc.LinuxSyncookieState,
        "DNSResolvConfFile": linux.DNSResolvConfFile,
        "WindowsFirewallLogFile": windows.WindowsFirewallLogFile,
        "LinuxHostnameFile": linux.LinuxHostnameFile,
        "LinuxIgnoreICMPBroadcasts": linux_proc.LinuxIgnoreICMPBroadcasts,
        "WindowsHostsFiles": windows.WindowsHostsFiles,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriagePersistence(GRRArtifactBase):
    """
    Group of persistence mechanism related artifacts.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "AnacronFiles",
                    "LinuxAtJobs",
                    "LinuxCronTabs",
                    "LinuxSystemdServices",
                    "LinuxSystemdTimers",
                    "LinuxSysVInit",
                    "XDGAutostartEntries",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "WMIEnumerateASEC",
                    "WMIEnumerateCLEC",
                    "WindowsApplicationCompatibilityInstalledShimDatabases",
                    "WindowsAutoexecBat",
                    "WindowsAutorun",
                    "WindowsBITSQueueManagerDatabases",
                    "WindowsGroupPolicyScripts",
                    "WindowsPowerShellDefaultProfiles",
                    "WindowsScheduledTasks",
                    "WindowsStartupFolders",
                    "WindowsWinstart",
                ]
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "LinuxSysVInit": linux.LinuxSysVInit,
        "WindowsPowerShellDefaultProfiles": windows.WindowsPowerShellDefaultProfiles,
        "LinuxSystemdTimers": linux.LinuxSystemdTimers,
        "WindowsScheduledTasks": windows.WindowsScheduledTasks,
        "WindowsAutorun": windows.WindowsAutorun,
        "AnacronFiles": linux.AnacronFiles,
        "XDGAutostartEntries": linux.XDGAutostartEntries,
        "WindowsBITSQueueManagerDatabases": windows.WindowsBITSQueueManagerDatabases,
        "WindowsAutoexecBat": windows.WindowsAutoexecBat,
        "WindowsStartupFolders": windows.WindowsStartupFolders,
        "WindowsWinstart": windows.WindowsWinstart,
        "WMIEnumerateASEC": wmi.WMIEnumerateASEC,
        "LinuxAtJobs": linux.LinuxAtJobs,
        "WindowsGroupPolicyScripts": windows.WindowsGroupPolicyScripts,
        "WMIEnumerateCLEC": wmi.WMIEnumerateCLEC,
        "WindowsApplicationCompatibilityInstalledShimDatabases": windows.WindowsApplicationCompatibilityInstalledShimDatabases,
        "LinuxCronTabs": linux.LinuxCronTabs,
        "LinuxSystemdServices": linux.LinuxSystemdServices,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriageSecurityAgents(GRRArtifactBase):
    """
    Group of endpoint detection and response related artifacts.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "EsetAVQuarantine",
                    "MicrosoftAVLogs",
                    "MicrosoftAVQuarantine",
                    "SophosAVLogs",
                    "SophosAVQuarantine",
                    "SymantecAVLogs",
                    "SymantecAVQuarantine",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "SymantecAVLogs": antivirus.SymantecAVLogs,
        "SophosAVQuarantine": antivirus.SophosAVQuarantine,
        "MicrosoftAVQuarantine": antivirus.MicrosoftAVQuarantine,
        "SophosAVLogs": antivirus.SophosAVLogs,
        "EsetAVQuarantine": antivirus.EsetAVQuarantine,
        "SymantecAVQuarantine": antivirus.SymantecAVQuarantine,
        "MicrosoftAVLogs": antivirus.MicrosoftAVLogs,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriageSystemConfiguration(GRRArtifactBase):
    """
    Group of configuration files related artifacts.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "APTSources",
                    "APTTrustKeys",
                    "CronAtAllowDenyFiles",
                    "DebianPackagesStatus",
                    "DebianVersion",
                    "KernelModules",
                    "LinuxASLREnabled",
                    "LinuxCACertificates",
                    "LinuxDHCPConfigurationFile",
                    "LinuxDSDTTable",
                    "LinuxFstab",
                    "LinuxGrubConfiguration",
                    "LinuxInitrdFiles",
                    "LinuxIssueFile",
                    "LinuxKernelBootloader",
                    "LinuxKernelModuleRestrictions",
                    "LinuxKernelModuleTaintStatus",
                    "LinuxLoaderSystemPreloadFile",
                    "LinuxLocalTime",
                    "LinuxLSBInit",
                    "LinuxLSBRelease",
                    "LinuxNetworkManager",
                    "LinuxPamConfigs",
                    "LinuxPasswdFile",
                    "LinuxProcMounts",
                    "LinuxRelease",
                    "LinuxRestrictedDmesgReadPrivileges",
                    "LinuxRestrictedKernelPointerReadPrivileges",
                    "LinuxRsyslogConfigs",
                    "LinuxSecureFsLinks",
                    "LinuxSecureSuidCoreDumps",
                    "LinuxSSDTTables",
                    "LinuxSysctlConfigurationFiles",
                    "LinuxSyslogNgConfigs",
                    "LinuxSystemdJournalConfig",
                    "LinuxSystemdOSRelease",
                    "LinuxTimezoneFile",
                    "LinuxXinetd",
                    "LocateDatabase",
                    "LoginPolicyConfiguration",
                    "NetgroupConfiguration",
                    "NfsExportsFile",
                    "NtpConfFile",
                    "PCIDevicesInfoFiles",
                    "SambaConfigFile",
                    "SecretsServiceDatabaseFile",
                    "SshdConfigFile",
                    "SSHHostPubKeys",
                    "UnixGroupsFile",
                    "UnixLocalTimeConfigurationFile",
                    "UnixPasswdFile",
                    "UnixShadowFile",
                    "UnixSudoersConfigurationFile",
                    "YumSources",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "WindowsRegistryFilesAndTransactionLogs",
                    "WindowsSystemRegistryFilesAndTransactionLogsBackup",
                ]
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "DebianPackagesStatus": linux.DebianPackagesStatus,
        "LinuxInitrdFiles": linux.LinuxInitrdFiles,
        "LinuxPasswdFile": linux.LinuxPasswdFile,
        "NetgroupConfiguration": linux.NetgroupConfiguration,
        "LinuxLSBInit": linux.LinuxLSBInit,
        "APTTrustKeys": linux.APTTrustKeys,
        "LinuxNetworkManager": linux.LinuxNetworkManager,
        "LinuxXinetd": linux.LinuxXinetd,
        "LinuxFstab": linux.LinuxFstab,
        "UnixGroupsFile": unix_common.UnixGroupsFile,
        "DebianVersion": linux.DebianVersion,
        "LinuxDSDTTable": linux.LinuxDSDTTable,
        "LinuxRsyslogConfigs": linux.LinuxRsyslogConfigs,
        "LinuxLoaderSystemPreloadFile": linux.LinuxLoaderSystemPreloadFile,
        "LinuxASLREnabled": linux_proc.LinuxASLREnabled,
        "LinuxSecureSuidCoreDumps": linux_proc.LinuxSecureSuidCoreDumps,
        "KernelModules": linux.KernelModules,
        "LinuxSystemdJournalConfig": linux.LinuxSystemdJournalConfig,
        "SSHHostPubKeys": linux.SSHHostPubKeys,
        "LinuxSyslogNgConfigs": linux.LinuxSyslogNgConfigs,
        "CronAtAllowDenyFiles": linux.CronAtAllowDenyFiles,
        "LinuxPamConfigs": linux.LinuxPamConfigs,
        "LoginPolicyConfiguration": linux.LoginPolicyConfiguration,
        "LinuxCACertificates": linux.LinuxCACertificates,
        "LinuxRestrictedKernelPointerReadPrivileges": linux_proc.LinuxRestrictedKernelPointerReadPrivileges,
        "LinuxSecureFsLinks": linux_proc.LinuxSecureFsLinks,
        "LinuxLSBRelease": linux.LinuxLSBRelease,
        "LinuxKernelBootloader": linux_proc.LinuxKernelBootloader,
        "LinuxGrubConfiguration": linux.LinuxGrubConfiguration,
        "UnixSudoersConfigurationFile": unix_common.UnixSudoersConfigurationFile,
        "YumSources": linux.YumSources,
        "NtpConfFile": linux.NtpConfFile,
        "LinuxSSDTTables": linux.LinuxSSDTTables,
        "LinuxDHCPConfigurationFile": linux.LinuxDHCPConfigurationFile,
        "LocateDatabase": linux.LocateDatabase,
        "UnixLocalTimeConfigurationFile": unix_common.UnixLocalTimeConfigurationFile,
        "APTSources": linux.APTSources,
        "LinuxRestrictedDmesgReadPrivileges": linux_proc.LinuxRestrictedDmesgReadPrivileges,
        "LinuxKernelModuleRestrictions": linux_proc.LinuxKernelModuleRestrictions,
        "SshdConfigFile": config_files.SshdConfigFile,
        "SecretsServiceDatabaseFile": linux.SecretsServiceDatabaseFile,
        "NfsExportsFile": config_files.NfsExportsFile,
        "UnixPasswdFile": unix_common.UnixPasswdFile,
        "UnixShadowFile": unix_common.UnixShadowFile,
        "LinuxSysctlConfigurationFiles": linux.LinuxSysctlConfigurationFiles,
        "LinuxIssueFile": linux.LinuxIssueFile,
        "LinuxProcMounts": linux_proc.LinuxProcMounts,
        "LinuxTimezoneFile": linux.LinuxTimezoneFile,
        "LinuxLocalTime": linux.LinuxLocalTime,
        "PCIDevicesInfoFiles": linux.PCIDevicesInfoFiles,
        "WindowsSystemRegistryFilesAndTransactionLogsBackup": windows.WindowsSystemRegistryFilesAndTransactionLogsBackup,
        "SambaConfigFile": config_files.SambaConfigFile,
        "LinuxKernelModuleTaintStatus": linux_proc.LinuxKernelModuleTaintStatus,
        "LinuxRelease": legacy.LinuxRelease,
        "LinuxSystemdOSRelease": linux.LinuxSystemdOSRelease,
        "WindowsRegistryFilesAndTransactionLogs": windows.WindowsRegistryFilesAndTransactionLogs,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriageSystemLogs(GRRArtifactBase):
    """
    Group of system logs related artifacts.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "DebianPackagesLogFiles",
                    "LinuxAuditLogs",
                    "LinuxAuthLogs",
                    "LinuxCronLogs",
                    "LinuxDaemonLogFiles",
                    "LinuxKernelLogFiles",
                    "LinuxLastlogFile",
                    "LinuxMessagesLogFiles",
                    "LinuxSudoReplayLogs",
                    "LinuxSysLogFiles",
                    "LinuxSystemdJournalLogs",
                    "LinuxUtmpFiles",
                    "LinuxWtmp",
                    "SambaLogFiles",
                    "UFWLogFile",
                    "UnixUtmpFile",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {"names": ["WindowsUserAccessLogging", "WindowsEventLogs"]},
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "WindowsUserAccessLogging": windows.WindowsUserAccessLogging,
        "LinuxUtmpFiles": linux.LinuxUtmpFiles,
        "LinuxKernelLogFiles": linux.LinuxKernelLogFiles,
        "LinuxSysLogFiles": linux.LinuxSysLogFiles,
        "LinuxAuthLogs": linux.LinuxAuthLogs,
        "LinuxSudoReplayLogs": linux.LinuxSudoReplayLogs,
        "SambaLogFiles": linux.SambaLogFiles,
        "LinuxLastlogFile": linux.LinuxLastlogFile,
        "LinuxWtmp": linux.LinuxWtmp,
        "UFWLogFile": linux.UFWLogFile,
        "WindowsEventLogs": windows.WindowsEventLogs,
        "LinuxSystemdJournalLogs": linux.LinuxSystemdJournalLogs,
        "LinuxAuditLogs": linux.LinuxAuditLogs,
        "LinuxDaemonLogFiles": linux.LinuxDaemonLogFiles,
        "LinuxCronLogs": linux.LinuxCronLogs,
        "UnixUtmpFile": unix_common.UnixUtmpFile,
        "DebianPackagesLogFiles": linux.DebianPackagesLogFiles,
        "LinuxMessagesLogFiles": linux.LinuxMessagesLogFiles,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriageUserConfiguration(GRRArtifactBase):
    """
    Group of user configuration related artifacts.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "BashShellConfigurationFile",
                    "ChromePreferences",
                    "CShellConfigurationFile",
                    "FishShellConfigurationFile",
                    "JupyterConfigFile",
                    "KornShellConfigurationFile",
                    "RHostsFile",
                    "RootUserShellConfigs",
                    "ShellLogoutFile",
                    "ShellProfileFile",
                    "SignalApplicationContent",
                    "SSHAuthorizedKeysFiles",
                    "SSHKnownHostsFiles",
                    "SshUserConfigFile",
                    "TeeShellConfigurationFile",
                    "ZShellConfigurationFile",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "JupyterConfigFile": config_files.JupyterConfigFile,
        "KornShellConfigurationFile": shell.KornShellConfigurationFile,
        "BashShellConfigurationFile": shell.BashShellConfigurationFile,
        "SshUserConfigFile": config_files.SshUserConfigFile,
        "TeeShellConfigurationFile": shell.TeeShellConfigurationFile,
        "SSHAuthorizedKeysFiles": linux.SSHAuthorizedKeysFiles,
        "ShellLogoutFile": shell.ShellLogoutFile,
        "SSHKnownHostsFiles": linux.SSHKnownHostsFiles,
        "RootUserShellConfigs": shell.RootUserShellConfigs,
        "CShellConfigurationFile": shell.CShellConfigurationFile,
        "FishShellConfigurationFile": shell.FishShellConfigurationFile,
        "ZShellConfigurationFile": shell.ZShellConfigurationFile,
        "RHostsFile": linux.RHostsFile,
        "SignalApplicationContent": instant_messaging.SignalApplicationContent,
        "ShellProfileFile": shell.ShellProfileFile,
        "ChromePreferences": webbrowser.ChromePreferences,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriageWebBrowserExtensions(GRRArtifactBase):
    """
    Group of web browser extensions related artifacts.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "ChromiumBasedBrowsersExtensions",
                    "ChromiumBasedBrowsersExtensionActivitySQLiteDatabaseFile",
                    "ChromePreferences",
                    "FirefoxAddOns",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "ChromePreferences": webbrowser.ChromePreferences,
        "FirefoxAddOns": webbrowser.FirefoxAddOns,
        "ChromiumBasedBrowsersExtensionActivitySQLiteDatabaseFile": webbrowser.ChromiumBasedBrowsersExtensionActivitySQLiteDatabaseFile,
        "ChromiumBasedBrowsersExtensions": webbrowser.ChromiumBasedBrowsersExtensions,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class TriageWebBrowserHistory(GRRArtifactBase):
    """
    Group of web browser history related artifacts.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": ["BrowserHistory", "WindowsCryptnetUrlCacheMetadata"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "WindowsCryptnetUrlCacheMetadata": windows.WindowsCryptnetUrlCacheMetadata,
        "BrowserHistory": webbrowser.BrowserHistory,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None
