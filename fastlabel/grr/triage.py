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
        "HadoopAppLogs": hadoop.HadoopAppLogs,
        "TomcatLogFiles": tomcat.TomcatLogFiles,
        "ApacheConfigurationFolder": webservers.ApacheConfigurationFolder,
        "ElasticsearchGCLog": database_servers.ElasticsearchGCLog,
        "NginxAccessLogs": webservers.NginxAccessLogs,
        "ElasticsearchLogs": database_servers.ElasticsearchLogs,
        "HadoopYarnLogs": hadoop.HadoopYarnLogs,
        "TomcatFiles": tomcat.TomcatFiles,
        "HadoopAppRoot": hadoop.HadoopAppRoot,
        "JenkinsLogFile": linux_services.JenkinsLogFile,
        "ApacheErrorLogs": webservers.ApacheErrorLogs,
        "WordpressConfigFile": webservers.WordpressConfigFile,
        "ApacheKafkaLogFiles": linux_services.ApacheKafkaLogFiles,
        "MicrosoftSqlServerErrorLogs": applications.MicrosoftSqlServerErrorLogs,
        "ApacheAccessLogs": webservers.ApacheAccessLogs,
        "TomcatPasswordFile": tomcat.TomcatPasswordFile,
        "OsqueryLogFiles": linux_services.OsqueryLogFiles,
        "ElasticsearchAccessLog": database_servers.ElasticsearchAccessLog,
        "HAProxyLogFiles": linux_services.HAProxyLogFiles,
        "ApacheDefaultSiteConfigurationFile": webservers.ApacheDefaultSiteConfigurationFile,
        "ElasticsearchServerLog": database_servers.ElasticsearchServerLog,
        "ElasticsearchAuditLog": database_servers.ElasticsearchAuditLog,
        "MicrosoftIISLogs": webservers.MicrosoftIISLogs,
        "NginxErrorLogs": webservers.NginxErrorLogs,
        "RedisConfigFile": config_files.RedisConfigFile,
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
        "OpenSearchLogFiles": database_servers.OpenSearchLogFiles,
        "PostgreSQLConfigurationFiles": database_servers.PostgreSQLConfigurationFiles,
        "PostgreSQLLogFiles": database_servers.PostgreSQLLogFiles,
        "MongoDBConfigurationFile": database_servers.MongoDBConfigurationFile,
        "MySQLConfigurationFiles": database_servers.MySQLConfigurationFiles,
        "RedisConfigurationFile": database_servers.RedisConfigurationFile,
        "MongoDBLogFiles": database_servers.MongoDBLogFiles,
        "MySQLLogFiles": database_servers.MySQLLogFiles,
        "RedisLogFiles": database_servers.RedisLogFiles,
        "RedisConfigFile": config_files.RedisConfigFile,
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
        "WindowsCIMRepositoryFiles": windows.WindowsCIMRepositoryFiles,
        "WindowsCrashDumps": windows.WindowsCrashDumps,
        "WindowsSuperFetchFiles": windows.WindowsSuperFetchFiles,
        "WindowsAMCacheHveFile": windows.WindowsAMCacheHveFile,
        "WindowsRecentFileCacheBCF": windows.WindowsRecentFileCacheBCF,
        "WMICCMRUA": wmi.WMICCMRUA,
        "WindowsSystemResourceUsageMonitorDatabaseFile": windows.WindowsSystemResourceUsageMonitorDatabaseFile,
        "JavaCacheFiles": java.JavaCacheFiles,
        "WindowsStartupInfo": windows.WindowsStartupInfo,
        "WindowsPrefetchFiles": windows.WindowsPrefetchFiles,
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
        "PostgreSQLHistoryFile": linux.PostgreSQLHistoryFile,
        "BourneShellHistoryFile": shell.BourneShellHistoryFile,
        "BashShellHistoryFile": shell.BashShellHistoryFile,
        "SQLiteHistoryFile": linux.SQLiteHistoryFile,
        "ShellConfigurationFile": shell.ShellConfigurationFile,
        "PythonHistoryFile": linux.PythonHistoryFile,
        "RootUserShellHistory": shell.RootUserShellHistory,
        "ZShellHistoryFile": shell.ZShellHistoryFile,
        "ShellHistoryFile": shell.ShellHistoryFile,
        "WindowsPowerShellHistory": windows.WindowsPowerShellHistory,
        "FishShellHistoryFile": shell.FishShellHistoryFile,
        "MySQLHistoryFile": linux.MySQLHistoryFile,
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
        "WindowsRecycleBinMetadata": windows.WindowsRecycleBinMetadata,
        "SignalDatabase": instant_messaging.SignalDatabase,
        "ThumbnailCacheFolder": linux.ThumbnailCacheFolder,
        "WindowsUserCustomDestinationsJumpLists": windows.WindowsUserCustomDestinationsJumpLists,
        "WindowsUserRecentFiles": windows.WindowsUserRecentFiles,
        "WindowsActivitiesCacheDatabase": windows.WindowsActivitiesCacheDatabase,
        "WindowsSearchDatabaseFile": windows.WindowsSearchDatabaseFile,
        "WgetHSTSdatabase": linux.WgetHSTSdatabase,
        "GnomeApplicationState": linux.GnomeApplicationState,
        "ZeitgeistDatabase": linux.ZeitgeistDatabase,
        "Viminfo": linux.Viminfo,
        "FreeDesktopTrashInfoFiles": linux.FreeDesktopTrashInfoFiles,
        "GTKRecentlyUsedDatabase": linux.GTKRecentlyUsedDatabase,
        "XChatLogs": instant_messaging.XChatLogs,
        "WindowsUserAutomaticDestinationsJumpLists": windows.WindowsUserAutomaticDestinationsJumpLists,
        "MicrosoftOfficeAutosave": applications.MicrosoftOfficeAutosave,
        "WindowsRDPClientBitmapCache": windows.WindowsRDPClientBitmapCache,
        "MicrosoftOfficeMRU": applications.MicrosoftOfficeMRU,
        "GnomeTracker": linux.GnomeTracker,
        "DropboxClient": cloud_services.DropboxClient,
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
        "LinuxNetworkIpForwardingState": linux_proc.LinuxNetworkIpForwardingState,
        "DNSResolvConfFile": linux.DNSResolvConfFile,
        "LinuxHostnameFile": linux.LinuxHostnameFile,
        "LinuxProcArp": linux_proc.LinuxProcArp,
        "LinuxSyncookieState": linux_proc.LinuxSyncookieState,
        "HostAccessPolicyConfiguration": linux.HostAccessPolicyConfiguration,
        "WindowsHostsFiles": windows.WindowsHostsFiles,
        "LinuxNetworkPathFilteringSettings": linux_proc.LinuxNetworkPathFilteringSettings,
        "UFWConfigFiles": linux.UFWConfigFiles,
        "LinuxNetworkRedirectState": linux_proc.LinuxNetworkRedirectState,
        "UnixHostsFile": unix_common.UnixHostsFile,
        "LinuxIgnoreICMPBroadcasts": linux_proc.LinuxIgnoreICMPBroadcasts,
        "WindowsFirewallLogFile": windows.WindowsFirewallLogFile,
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
        "WindowsGroupPolicyScripts": windows.WindowsGroupPolicyScripts,
        "LinuxSystemdTimers": linux.LinuxSystemdTimers,
        "WindowsBITSQueueManagerDatabases": windows.WindowsBITSQueueManagerDatabases,
        "WMIEnumerateASEC": wmi.WMIEnumerateASEC,
        "WindowsStartupFolders": windows.WindowsStartupFolders,
        "WindowsWinstart": windows.WindowsWinstart,
        "WindowsPowerShellDefaultProfiles": windows.WindowsPowerShellDefaultProfiles,
        "AnacronFiles": linux.AnacronFiles,
        "LinuxSystemdServices": linux.LinuxSystemdServices,
        "LinuxCronTabs": linux.LinuxCronTabs,
        "WindowsApplicationCompatibilityInstalledShimDatabases": windows.WindowsApplicationCompatibilityInstalledShimDatabases,
        "XDGAutostartEntries": linux.XDGAutostartEntries,
        "WindowsAutoexecBat": windows.WindowsAutoexecBat,
        "LinuxAtJobs": linux.LinuxAtJobs,
        "WindowsAutorun": windows.WindowsAutorun,
        "WMIEnumerateCLEC": wmi.WMIEnumerateCLEC,
        "WindowsScheduledTasks": windows.WindowsScheduledTasks,
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
        "SophosAVLogs": antivirus.SophosAVLogs,
        "EsetAVQuarantine": antivirus.EsetAVQuarantine,
        "SymantecAVQuarantine": antivirus.SymantecAVQuarantine,
        "SymantecAVLogs": antivirus.SymantecAVLogs,
        "SophosAVQuarantine": antivirus.SophosAVQuarantine,
        "MicrosoftAVLogs": antivirus.MicrosoftAVLogs,
        "MicrosoftAVQuarantine": antivirus.MicrosoftAVQuarantine,
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
        "LinuxSystemdJournalConfig": linux.LinuxSystemdJournalConfig,
        "LinuxASLREnabled": linux_proc.LinuxASLREnabled,
        "LinuxDHCPConfigurationFile": linux.LinuxDHCPConfigurationFile,
        "LinuxGrubConfiguration": linux.LinuxGrubConfiguration,
        "LinuxRelease": legacy.LinuxRelease,
        "LinuxSysctlConfigurationFiles": linux.LinuxSysctlConfigurationFiles,
        "KernelModules": linux.KernelModules,
        "LoginPolicyConfiguration": linux.LoginPolicyConfiguration,
        "LinuxFstab": linux.LinuxFstab,
        "APTTrustKeys": linux.APTTrustKeys,
        "LinuxNetworkManager": linux.LinuxNetworkManager,
        "LinuxKernelModuleTaintStatus": linux_proc.LinuxKernelModuleTaintStatus,
        "LinuxPamConfigs": linux.LinuxPamConfigs,
        "LinuxRestrictedKernelPointerReadPrivileges": linux_proc.LinuxRestrictedKernelPointerReadPrivileges,
        "UnixSudoersConfigurationFile": unix_common.UnixSudoersConfigurationFile,
        "LinuxSystemdOSRelease": linux.LinuxSystemdOSRelease,
        "LocateDatabase": linux.LocateDatabase,
        "UnixGroupsFile": unix_common.UnixGroupsFile,
        "LinuxRestrictedDmesgReadPrivileges": linux_proc.LinuxRestrictedDmesgReadPrivileges,
        "NfsExportsFile": config_files.NfsExportsFile,
        "WindowsRegistryFilesAndTransactionLogs": windows.WindowsRegistryFilesAndTransactionLogs,
        "LinuxKernelBootloader": linux_proc.LinuxKernelBootloader,
        "LinuxInitrdFiles": linux.LinuxInitrdFiles,
        "NtpConfFile": linux.NtpConfFile,
        "LinuxSecureFsLinks": linux_proc.LinuxSecureFsLinks,
        "UnixLocalTimeConfigurationFile": unix_common.UnixLocalTimeConfigurationFile,
        "LinuxIssueFile": linux.LinuxIssueFile,
        "LinuxXinetd": linux.LinuxXinetd,
        "SecretsServiceDatabaseFile": linux.SecretsServiceDatabaseFile,
        "DebianVersion": linux.DebianVersion,
        "SshdConfigFile": config_files.SshdConfigFile,
        "YumSources": linux.YumSources,
        "LinuxCACertificates": linux.LinuxCACertificates,
        "WindowsSystemRegistryFilesAndTransactionLogsBackup": windows.WindowsSystemRegistryFilesAndTransactionLogsBackup,
        "LinuxKernelModuleRestrictions": linux_proc.LinuxKernelModuleRestrictions,
        "PCIDevicesInfoFiles": linux.PCIDevicesInfoFiles,
        "NetgroupConfiguration": linux.NetgroupConfiguration,
        "LinuxLocalTime": linux.LinuxLocalTime,
        "LinuxLoaderSystemPreloadFile": linux.LinuxLoaderSystemPreloadFile,
        "LinuxSSDTTables": linux.LinuxSSDTTables,
        "APTSources": linux.APTSources,
        "LinuxLSBRelease": linux.LinuxLSBRelease,
        "LinuxTimezoneFile": linux.LinuxTimezoneFile,
        "LinuxPasswdFile": linux.LinuxPasswdFile,
        "LinuxRsyslogConfigs": linux.LinuxRsyslogConfigs,
        "SSHHostPubKeys": linux.SSHHostPubKeys,
        "LinuxSecureSuidCoreDumps": linux_proc.LinuxSecureSuidCoreDumps,
        "UnixPasswdFile": unix_common.UnixPasswdFile,
        "LinuxDSDTTable": linux.LinuxDSDTTable,
        "DebianPackagesStatus": linux.DebianPackagesStatus,
        "CronAtAllowDenyFiles": linux.CronAtAllowDenyFiles,
        "LinuxProcMounts": linux_proc.LinuxProcMounts,
        "UnixShadowFile": unix_common.UnixShadowFile,
        "LinuxLSBInit": linux.LinuxLSBInit,
        "LinuxSyslogNgConfigs": linux.LinuxSyslogNgConfigs,
        "SambaConfigFile": config_files.SambaConfigFile,
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
        "UnixUtmpFile": unix_common.UnixUtmpFile,
        "LinuxSysLogFiles": linux.LinuxSysLogFiles,
        "LinuxAuthLogs": linux.LinuxAuthLogs,
        "UFWLogFile": linux.UFWLogFile,
        "LinuxAuditLogs": linux.LinuxAuditLogs,
        "LinuxMessagesLogFiles": linux.LinuxMessagesLogFiles,
        "LinuxSudoReplayLogs": linux.LinuxSudoReplayLogs,
        "LinuxUtmpFiles": linux.LinuxUtmpFiles,
        "WindowsEventLogs": windows.WindowsEventLogs,
        "DebianPackagesLogFiles": linux.DebianPackagesLogFiles,
        "LinuxSystemdJournalLogs": linux.LinuxSystemdJournalLogs,
        "LinuxWtmp": linux.LinuxWtmp,
        "SambaLogFiles": linux.SambaLogFiles,
        "LinuxDaemonLogFiles": linux.LinuxDaemonLogFiles,
        "WindowsUserAccessLogging": windows.WindowsUserAccessLogging,
        "LinuxCronLogs": linux.LinuxCronLogs,
        "LinuxKernelLogFiles": linux.LinuxKernelLogFiles,
        "LinuxLastlogFile": linux.LinuxLastlogFile,
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
        "RHostsFile": linux.RHostsFile,
        "CShellConfigurationFile": shell.CShellConfigurationFile,
        "RootUserShellConfigs": shell.RootUserShellConfigs,
        "SSHAuthorizedKeysFiles": linux.SSHAuthorizedKeysFiles,
        "FishShellConfigurationFile": shell.FishShellConfigurationFile,
        "SshUserConfigFile": config_files.SshUserConfigFile,
        "SSHKnownHostsFiles": linux.SSHKnownHostsFiles,
        "ShellProfileFile": shell.ShellProfileFile,
        "SignalApplicationContent": instant_messaging.SignalApplicationContent,
        "BashShellConfigurationFile": shell.BashShellConfigurationFile,
        "TeeShellConfigurationFile": shell.TeeShellConfigurationFile,
        "KornShellConfigurationFile": shell.KornShellConfigurationFile,
        "ChromePreferences": webbrowser.ChromePreferences,
        "ZShellConfigurationFile": shell.ZShellConfigurationFile,
        "ShellLogoutFile": shell.ShellLogoutFile,
        "JupyterConfigFile": config_files.JupyterConfigFile,
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
        "ChromiumBasedBrowsersExtensionActivitySQLiteDatabaseFile": webbrowser.ChromiumBasedBrowsersExtensionActivitySQLiteDatabaseFile,
        "ChromePreferences": webbrowser.ChromePreferences,
        "FirefoxAddOns": webbrowser.FirefoxAddOns,
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
        "BrowserHistory": webbrowser.BrowserHistory,
        "WindowsCryptnetUrlCacheMetadata": windows.WindowsCryptnetUrlCacheMetadata,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None
