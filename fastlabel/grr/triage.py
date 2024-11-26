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
        "MicrosoftIISLogs": webservers.MicrosoftIISLogs,
        "ApacheAccessLogs": webservers.ApacheAccessLogs,
        "HAProxyLogFiles": linux_services.HAProxyLogFiles,
        "ElasticsearchAccessLog": database_servers.ElasticsearchAccessLog,
        "JenkinsLogFile": linux_services.JenkinsLogFile,
        "HadoopYarnLogs": hadoop.HadoopYarnLogs,
        "ApacheConfigurationFolder": webservers.ApacheConfigurationFolder,
        "RedisConfigFile": config_files.RedisConfigFile,
        "ElasticsearchServerLog": database_servers.ElasticsearchServerLog,
        "ElasticsearchAuditLog": database_servers.ElasticsearchAuditLog,
        "OsqueryLogFiles": linux_services.OsqueryLogFiles,
        "ApacheDefaultSiteConfigurationFile": webservers.ApacheDefaultSiteConfigurationFile,
        "HadoopAppLogs": hadoop.HadoopAppLogs,
        "WordpressConfigFile": webservers.WordpressConfigFile,
        "TomcatLogFiles": tomcat.TomcatLogFiles,
        "ElasticsearchGCLog": database_servers.ElasticsearchGCLog,
        "NginxErrorLogs": webservers.NginxErrorLogs,
        "ElasticsearchLogs": database_servers.ElasticsearchLogs,
        "MicrosoftSqlServerErrorLogs": applications.MicrosoftSqlServerErrorLogs,
        "ApacheKafkaLogFiles": linux_services.ApacheKafkaLogFiles,
        "ApacheErrorLogs": webservers.ApacheErrorLogs,
        "TomcatFiles": tomcat.TomcatFiles,
        "TomcatPasswordFile": tomcat.TomcatPasswordFile,
        "HadoopAppRoot": hadoop.HadoopAppRoot,
        "NginxAccessLogs": webservers.NginxAccessLogs,
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
        "PostgreSQLConfigurationFiles": database_servers.PostgreSQLConfigurationFiles,
        "OpenSearchLogFiles": database_servers.OpenSearchLogFiles,
        "RedisConfigurationFile": database_servers.RedisConfigurationFile,
        "RedisConfigFile": config_files.RedisConfigFile,
        "RedisLogFiles": database_servers.RedisLogFiles,
        "MySQLLogFiles": database_servers.MySQLLogFiles,
        "PostgreSQLLogFiles": database_servers.PostgreSQLLogFiles,
        "MongoDBLogFiles": database_servers.MongoDBLogFiles,
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
        "WindowsCIMRepositoryFiles": windows.WindowsCIMRepositoryFiles,
        "WindowsStartupInfo": windows.WindowsStartupInfo,
        "WindowsRecentFileCacheBCF": windows.WindowsRecentFileCacheBCF,
        "WindowsSuperFetchFiles": windows.WindowsSuperFetchFiles,
        "WindowsAMCacheHveFile": windows.WindowsAMCacheHveFile,
        "WindowsSystemResourceUsageMonitorDatabaseFile": windows.WindowsSystemResourceUsageMonitorDatabaseFile,
        "WindowsPrefetchFiles": windows.WindowsPrefetchFiles,
        "JavaCacheFiles": java.JavaCacheFiles,
        "WindowsCrashDumps": windows.WindowsCrashDumps,
        "WMICCMRUA": wmi.WMICCMRUA,
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
        "RootUserShellHistory": shell.RootUserShellHistory,
        "ZShellHistoryFile": shell.ZShellHistoryFile,
        "FishShellHistoryFile": shell.FishShellHistoryFile,
        "WindowsPowerShellHistory": windows.WindowsPowerShellHistory,
        "BashShellHistoryFile": shell.BashShellHistoryFile,
        "PostgreSQLHistoryFile": linux.PostgreSQLHistoryFile,
        "ShellConfigurationFile": shell.ShellConfigurationFile,
        "ShellHistoryFile": shell.ShellHistoryFile,
        "SQLiteHistoryFile": linux.SQLiteHistoryFile,
        "BourneShellHistoryFile": shell.BourneShellHistoryFile,
        "PythonHistoryFile": linux.PythonHistoryFile,
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
        "WindowsSearchDatabaseFile": windows.WindowsSearchDatabaseFile,
        "WindowsUserCustomDestinationsJumpLists": windows.WindowsUserCustomDestinationsJumpLists,
        "FreeDesktopTrashInfoFiles": linux.FreeDesktopTrashInfoFiles,
        "WindowsActivitiesCacheDatabase": windows.WindowsActivitiesCacheDatabase,
        "ZeitgeistDatabase": linux.ZeitgeistDatabase,
        "DropboxClient": cloud_services.DropboxClient,
        "WgetHSTSdatabase": linux.WgetHSTSdatabase,
        "WindowsUserRecentFiles": windows.WindowsUserRecentFiles,
        "WindowsUserAutomaticDestinationsJumpLists": windows.WindowsUserAutomaticDestinationsJumpLists,
        "SignalDatabase": instant_messaging.SignalDatabase,
        "XChatLogs": instant_messaging.XChatLogs,
        "MicrosoftOfficeMRU": applications.MicrosoftOfficeMRU,
        "GnomeTracker": linux.GnomeTracker,
        "MicrosoftOfficeAutosave": applications.MicrosoftOfficeAutosave,
        "WindowsRecycleBinMetadata": windows.WindowsRecycleBinMetadata,
        "GnomeApplicationState": linux.GnomeApplicationState,
        "ThumbnailCacheFolder": linux.ThumbnailCacheFolder,
        "WindowsRDPClientBitmapCache": windows.WindowsRDPClientBitmapCache,
        "GTKRecentlyUsedDatabase": linux.GTKRecentlyUsedDatabase,
        "Viminfo": linux.Viminfo,
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
        "UFWConfigFiles": linux.UFWConfigFiles,
        "WindowsFirewallLogFile": windows.WindowsFirewallLogFile,
        "LinuxSyncookieState": linux_proc.LinuxSyncookieState,
        "WindowsHostsFiles": windows.WindowsHostsFiles,
        "LinuxNetworkIpForwardingState": linux_proc.LinuxNetworkIpForwardingState,
        "DNSResolvConfFile": linux.DNSResolvConfFile,
        "LinuxProcArp": linux_proc.LinuxProcArp,
        "UnixHostsFile": unix_common.UnixHostsFile,
        "LinuxNetworkPathFilteringSettings": linux_proc.LinuxNetworkPathFilteringSettings,
        "LinuxIgnoreICMPBroadcasts": linux_proc.LinuxIgnoreICMPBroadcasts,
        "LinuxHostnameFile": linux.LinuxHostnameFile,
        "LinuxNetworkRedirectState": linux_proc.LinuxNetworkRedirectState,
        "HostAccessPolicyConfiguration": linux.HostAccessPolicyConfiguration,
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
        "WindowsBITSQueueManagerDatabases": windows.WindowsBITSQueueManagerDatabases,
        "AnacronFiles": linux.AnacronFiles,
        "WindowsGroupPolicyScripts": windows.WindowsGroupPolicyScripts,
        "WindowsAutoexecBat": windows.WindowsAutoexecBat,
        "LinuxAtJobs": linux.LinuxAtJobs,
        "WMIEnumerateASEC": wmi.WMIEnumerateASEC,
        "LinuxSystemdTimers": linux.LinuxSystemdTimers,
        "WindowsScheduledTasks": windows.WindowsScheduledTasks,
        "WindowsWinstart": windows.WindowsWinstart,
        "LinuxSystemdServices": linux.LinuxSystemdServices,
        "XDGAutostartEntries": linux.XDGAutostartEntries,
        "WindowsStartupFolders": windows.WindowsStartupFolders,
        "WindowsAutorun": windows.WindowsAutorun,
        "WindowsPowerShellDefaultProfiles": windows.WindowsPowerShellDefaultProfiles,
        "LinuxCronTabs": linux.LinuxCronTabs,
        "LinuxSysVInit": linux.LinuxSysVInit,
        "WMIEnumerateCLEC": wmi.WMIEnumerateCLEC,
        "WindowsApplicationCompatibilityInstalledShimDatabases": windows.WindowsApplicationCompatibilityInstalledShimDatabases,
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
        "EsetAVQuarantine": antivirus.EsetAVQuarantine,
        "MicrosoftAVQuarantine": antivirus.MicrosoftAVQuarantine,
        "SophosAVLogs": antivirus.SophosAVLogs,
        "MicrosoftAVLogs": antivirus.MicrosoftAVLogs,
        "SymantecAVLogs": antivirus.SymantecAVLogs,
        "SophosAVQuarantine": antivirus.SophosAVQuarantine,
        "SymantecAVQuarantine": antivirus.SymantecAVQuarantine,
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
        "NtpConfFile": linux.NtpConfFile,
        "LinuxKernelBootloader": linux_proc.LinuxKernelBootloader,
        "KernelModules": linux.KernelModules,
        "LinuxASLREnabled": linux_proc.LinuxASLREnabled,
        "LinuxRestrictedDmesgReadPrivileges": linux_proc.LinuxRestrictedDmesgReadPrivileges,
        "LinuxIssueFile": linux.LinuxIssueFile,
        "CronAtAllowDenyFiles": linux.CronAtAllowDenyFiles,
        "APTSources": linux.APTSources,
        "LinuxSysctlConfigurationFiles": linux.LinuxSysctlConfigurationFiles,
        "SecretsServiceDatabaseFile": linux.SecretsServiceDatabaseFile,
        "LinuxSecureFsLinks": linux_proc.LinuxSecureFsLinks,
        "NetgroupConfiguration": linux.NetgroupConfiguration,
        "SSHHostPubKeys": linux.SSHHostPubKeys,
        "WindowsSystemRegistryFilesAndTransactionLogsBackup": windows.WindowsSystemRegistryFilesAndTransactionLogsBackup,
        "LinuxRestrictedKernelPointerReadPrivileges": linux_proc.LinuxRestrictedKernelPointerReadPrivileges,
        "LinuxXinetd": linux.LinuxXinetd,
        "LinuxProcMounts": linux_proc.LinuxProcMounts,
        "LinuxSystemdOSRelease": linux.LinuxSystemdOSRelease,
        "UnixGroupsFile": unix_common.UnixGroupsFile,
        "LinuxInitrdFiles": linux.LinuxInitrdFiles,
        "LinuxLSBRelease": linux.LinuxLSBRelease,
        "SambaConfigFile": config_files.SambaConfigFile,
        "LinuxGrubConfiguration": linux.LinuxGrubConfiguration,
        "LinuxRsyslogConfigs": linux.LinuxRsyslogConfigs,
        "PCIDevicesInfoFiles": linux.PCIDevicesInfoFiles,
        "UnixSudoersConfigurationFile": unix_common.UnixSudoersConfigurationFile,
        "LinuxSyslogNgConfigs": linux.LinuxSyslogNgConfigs,
        "LinuxDHCPConfigurationFile": linux.LinuxDHCPConfigurationFile,
        "LinuxPamConfigs": linux.LinuxPamConfigs,
        "APTTrustKeys": linux.APTTrustKeys,
        "LinuxLocalTime": linux.LinuxLocalTime,
        "LinuxRelease": legacy.LinuxRelease,
        "LoginPolicyConfiguration": linux.LoginPolicyConfiguration,
        "DebianPackagesStatus": linux.DebianPackagesStatus,
        "LinuxPasswdFile": linux.LinuxPasswdFile,
        "LinuxLoaderSystemPreloadFile": linux.LinuxLoaderSystemPreloadFile,
        "LinuxFstab": linux.LinuxFstab,
        "UnixLocalTimeConfigurationFile": unix_common.UnixLocalTimeConfigurationFile,
        "LinuxSecureSuidCoreDumps": linux_proc.LinuxSecureSuidCoreDumps,
        "SshdConfigFile": config_files.SshdConfigFile,
        "LinuxDSDTTable": linux.LinuxDSDTTable,
        "UnixShadowFile": unix_common.UnixShadowFile,
        "LinuxCACertificates": linux.LinuxCACertificates,
        "LinuxKernelModuleRestrictions": linux_proc.LinuxKernelModuleRestrictions,
        "LinuxTimezoneFile": linux.LinuxTimezoneFile,
        "LinuxSSDTTables": linux.LinuxSSDTTables,
        "LinuxLSBInit": linux.LinuxLSBInit,
        "WindowsRegistryFilesAndTransactionLogs": windows.WindowsRegistryFilesAndTransactionLogs,
        "UnixPasswdFile": unix_common.UnixPasswdFile,
        "DebianVersion": linux.DebianVersion,
        "LocateDatabase": linux.LocateDatabase,
        "LinuxNetworkManager": linux.LinuxNetworkManager,
        "NfsExportsFile": config_files.NfsExportsFile,
        "YumSources": linux.YumSources,
        "LinuxKernelModuleTaintStatus": linux_proc.LinuxKernelModuleTaintStatus,
        "LinuxSystemdJournalConfig": linux.LinuxSystemdJournalConfig,
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
        "LinuxDaemonLogFiles": linux.LinuxDaemonLogFiles,
        "LinuxSystemdJournalLogs": linux.LinuxSystemdJournalLogs,
        "LinuxWtmp": linux.LinuxWtmp,
        "DebianPackagesLogFiles": linux.DebianPackagesLogFiles,
        "LinuxSudoReplayLogs": linux.LinuxSudoReplayLogs,
        "UnixUtmpFile": unix_common.UnixUtmpFile,
        "LinuxAuthLogs": linux.LinuxAuthLogs,
        "WindowsUserAccessLogging": windows.WindowsUserAccessLogging,
        "LinuxUtmpFiles": linux.LinuxUtmpFiles,
        "WindowsEventLogs": windows.WindowsEventLogs,
        "LinuxAuditLogs": linux.LinuxAuditLogs,
        "LinuxCronLogs": linux.LinuxCronLogs,
        "LinuxKernelLogFiles": linux.LinuxKernelLogFiles,
        "LinuxLastlogFile": linux.LinuxLastlogFile,
        "LinuxMessagesLogFiles": linux.LinuxMessagesLogFiles,
        "SambaLogFiles": linux.SambaLogFiles,
        "LinuxSysLogFiles": linux.LinuxSysLogFiles,
        "UFWLogFile": linux.UFWLogFile,
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
        "BashShellConfigurationFile": shell.BashShellConfigurationFile,
        "ChromePreferences": webbrowser.ChromePreferences,
        "ShellProfileFile": shell.ShellProfileFile,
        "SshUserConfigFile": config_files.SshUserConfigFile,
        "CShellConfigurationFile": shell.CShellConfigurationFile,
        "SSHAuthorizedKeysFiles": linux.SSHAuthorizedKeysFiles,
        "JupyterConfigFile": config_files.JupyterConfigFile,
        "SignalApplicationContent": instant_messaging.SignalApplicationContent,
        "ZShellConfigurationFile": shell.ZShellConfigurationFile,
        "ShellLogoutFile": shell.ShellLogoutFile,
        "FishShellConfigurationFile": shell.FishShellConfigurationFile,
        "SSHKnownHostsFiles": linux.SSHKnownHostsFiles,
        "RootUserShellConfigs": shell.RootUserShellConfigs,
        "KornShellConfigurationFile": shell.KornShellConfigurationFile,
        "TeeShellConfigurationFile": shell.TeeShellConfigurationFile,
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
        "ChromiumBasedBrowsersExtensions": webbrowser.ChromiumBasedBrowsersExtensions,
        "ChromiumBasedBrowsersExtensionActivitySQLiteDatabaseFile": webbrowser.ChromiumBasedBrowsersExtensionActivitySQLiteDatabaseFile,
        "FirefoxAddOns": webbrowser.FirefoxAddOns,
        "ChromePreferences": webbrowser.ChromePreferences,
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
