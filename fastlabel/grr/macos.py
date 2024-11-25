"""
Auto-generated classes from the YAML declarations in macos.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class MacOSAddressBookImagesSQLiteDatabaseFile(GRRArtifactBase):
    """
    Address book images SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Applications/Xcode.app/Contents/Developer/Platforms/*.platform/Developer/Library/CoreSimulator/Profiles/Runtimes/*.simruntime/Contents/Resources/SampleContent/Library/AddressBook/AddressBookImages.sqlitedb",
                    "%%users.homedir%%/Library/Developer/CoreSimulator/Devices/*/data/Library/AddressBook/AddressBookImages.sqlitedb",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSAirportPreferencesPlistFile(GRRArtifactBase):
    """
    Airport (wireless networking) preferences property list (plist) file.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/macos/NetworkSettings.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Library/Preferences/SystemConfiguration/com.apple.airport.preferences.plist"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSWirelessNetworks"]


class MacOSApplePushServiceSQLiteDatabaseFile(GRRArtifactBase):
    """
    Apple push service SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/Library/Application Support/ApplePushService/aps.db"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSAppleSetupDoneFile(GRRArtifactBase):
    """
    Mac OS .AppleSetupDone file that hints to the system installation date and
    time.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-settings-and-informations
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/private/var/db/.AppleSetupDone", "/var/db/.AppleSetupDone"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSSystemInstallationTime"]


class MacOSAppleSystemLogFile(GRRArtifactBase):
    """
    Apple system log (ASL) files.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-logs
    https://support.apple.com/guide/console/reports-cnsl664be99a/mac
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/log/asl/*.asl",
                    "/private/var/log/DiagnosticMessages/*.asl",
                    "/var/log/asl/*.asl",
                    "/var/log/DiagnosticMessages/*.asl",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSAppleSystemLogFiles"]


class MacOSApplicationBundleCacheSQLiteDatabaseFile(GRRArtifactBase):
    """
    Application bundle cache SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/Library/Caches/*/Cache.db"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSApplicationResourcesStringsPlistFile(GRRArtifactBase):
    """
    Application resources strings plist file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Applications/*.app/Contents/Resources/*.lproj/*.strings",
                    "/Applications/*/*.app/Contents/Resources/*.lproj/*.strings",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSAssetCacheInfoSQLiteDatabaseFile(GRRArtifactBase):
    """
    Asset cache information SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/Library/Caches/com.apple.AssetCache/AssetInfo.db"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSAuthorizationRulesSQLiteDatabaseFile(GRRArtifactBase):
    """
    Authorization rules SQLite database file.

    Superscedes /etc/authorization seen Mac OS X 10.8 Mountain Lion and earlier
    versions.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/private/var/db/auth.db", "/var/db/auth.db"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSCalendarCacheSQLiteDatabaseFile(GRRArtifactBase):
    """
    Calendar cache SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Calendars/Calendar Cache"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSCallHistoryCacheSQLiteDatabaseFile(GRRArtifactBase):
    """
    Call history cache SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/CallHistoryDB/CallHistory.storedata"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSApplicationsDirectory(GRRArtifactBase):
    """
    Contents of the Applications directory.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#user-directories
    """

    SOURCES = [{"type": "PATH", "attributes": {"paths": ["/Applications/*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSApplications"]


class MacOSApplicationsRecentItems(GRRArtifactBase):
    """
    Recent Items application specific

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#recent-items
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Preferences/*.LSSharedFileList.plist"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSAtJobs(GRRArtifactBase):
    """
    MacOS at jobs

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-info-misc
    https://developer.apple.com/library/mac/documentation/Darwin/Reference/ManPages/man1/at.1.html#//apple_ref/doc/man/1/at
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/usr/lib/cron/jobs/*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSAuditLogFile(GRRArtifactBase):
    """
    Audit log files.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-logs
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/audit/[0-9]*.[0-9]*",
                    "/var/audit/[0-9]*.[0-9]*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSAuditLogFiles"]


class MacOSBluetoothPlistFile(GRRArtifactBase):
    """
    Bluetooth preferences and paired device information property list (plist)
    file

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-preferences
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/Library/Preferences/com.apple.Bluetooth.plist"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSCodeSignatureCodeResourcesPlistFile(GRRArtifactBase):
    """
    Code signature CodeResources plist file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Applications/Utilities/*.app/Contents/_CodeSignature/CodeResources",
                    "/System/Library/CoreServices/*.app/Contents/_CodeSignature/CodeResources",
                    "/System/Library/Extensions/*.kext/Contents/_CodeSignature/CodeResources",
                    "/System/Library/Extensions/*.kext/Contents/PlugIns/*.kext/Contents/_CodeSignature/CodeResources",
                    "/System/Library/Extensions/*.kext/Contents/PlugIns/*.kext/Contents/PlugIns/*.plugin/Contents/_CodeSignature/CodeResources",
                    "/System/Library/Extensions/*.kext/Contents/PlugIns/*.kext/Contents/Resources/*.bundle/Contents/_CodeSignature/CodeResources",
                    "/System/Library/Extensions/*.kext/Contents/Resources/*.bundle/Contents/_CodeSignature/CodeResources",
                    "/System/Library/Filesystems/*/*.kext/Contents/_CodeSignature/CodeResources",
                    "/System/Library/Filesystems/*/Encodings/*.kext/Contents/_CodeSignature/CodeResources",
                    "/System/Library/PrivateFrameworks/*.framework/Versions/A/Resources/*.kext/Contents/_CodeSignature/CodeResources",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSContentsInfoPlistFile(GRRArtifactBase):
    """
    Contents Info.plist file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Applications/*/*.app/Contents/Info.plist",
                    "/Applications/*/*.app/Contents/Resources/*.help/Contents/Info.plist",
                    "/System/Library/CoreServices/*.app/Contents/Info.plist",
                    "/System/Library/Extensions/*.kext/Contents/Info.plist",
                    "/System/Library/Extensions/*.kext/Contents/PlugIns/*.kext/Contents/Info.plist",
                    "/System/Library/Extensions/*.kext/Contents/PlugIns/*.kext/Contents/PlugIns/*.plugin/Contents/Info.plist",
                    "/System/Library/Extensions/*.kext/Contents/PlugIns/*.kext/Contents/Resources/*.bundle/Contents/Info.plist",
                    "/System/Library/Extensions/*.kext/Contents/Resources/*.bundle/Contents/Info.plist",
                    "/System/Library/Extensions/*.kext/PlugIns/*.kext/Info.plist",
                    "/System/Library/Filesystems/*/*.kext/Contents/Info.plist",
                    "/System/Library/Filesystems/*/Encodings/*.kext/Contents/Info.plist",
                    "/System/Library/Frameworks/*.framework/Versions/A/Resources/Info.plist",
                    "/System/Library/PrivateFrameworks/*.framework/Versions/A/Resources/*.kext/Contents/Info.plist",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSContentsVersionPlistFile(GRRArtifactBase):
    """
    Contents version.plist file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Applications/*/*.app/Contents/version.plist",
                    "/Applications/*/*.app/Contents/Resources/*.help/Contents/version.plist",
                    "/System/Library/CoreServices/*.app/Contents/version.plist",
                    "/System/Library/Extensions/*.kext/Contents/PlugIns/*.kext/Contents/version.plist",
                    "/System/Library/Extensions/*.kext/Contents/PlugIns/*.kext/Contents/PlugIns/*.plugin/Contents/version.plist",
                    "/System/Library/Extensions/*.kext/Contents/PlugIns/*.kext/Contents/Resources/*.bundle/Contents/version.plist",
                    "/System/Library/Extensions/*.kext/Contents/Resources/*.bundle/Contents/version.plist",
                    "/System/Library/Extensions/*.kext/Contents/version.plist",
                    "/System/Library/Extensions/*.kext/PlugIns/*.kext/version.plist",
                    "/System/Library/Filesystems/*/*.kext/Contents/version.plist",
                    "/System/Library/Filesystems/*/Encodings/*.kext/Contents/version.plist",
                    "/System/Library/Frameworks/*.framework/Versions/A/Resources/version.plist",
                    "/System/Library/PrivateFrameworks/*.framework/Versions/A/Resources/*.kext/Contents/version.plist",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSCoreAnalyticsFile(GRRArtifactBase):
    """
    CoreAnalytics log files.

    Reference URLs: https://forensics.wiki/mac_os_x#diagnostic-reports
    https://www.crowdstrike.com/blog/i-know-what-you-did-last-month-a-new-artifact-of-execution-on-macos-10-13/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Library/Logs/DiagnosticReports/*.core_analytics",
                    "/private/var/db/analyticsd/aggregates/*",
                    "/var/db/analyticsd/aggregates/*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSCoreAnalyticsFiles"]


class MacOSCronTabs(GRRArtifactBase):
    """
    Cron tabs

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-info-misc
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/crontab",
                    "/private/etc/crontab",
                    "/usr/lib/cron/tabs/*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSDockConfigurationPlistFile(GRRArtifactBase):
    """
    Dock configuration property list (plist) file.

    This property list contains information about the configuration of a user's
    Dock.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#preferences
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Preferences/com.apple.Dock.plist"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSDock"]


class MacOSDirectoryServicesLocalNodesSQLiteDatabaseFile(GRRArtifactBase):
    """
    Directory services local nodes database.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/db/dslocal/nodes/Default/sqlindex",
                    "/var/db/dslocal/nodes/Default/sqlindex",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSDuetActivitySchedulerSQLiteDatabaseFile(GRRArtifactBase):
    """
    Duet activity scheduler database.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/db/DuetActivityScheduler/DuetActivitySchedulerClassC.db",
                    "/var/db/DuetActivityScheduler/DuetActivitySchedulerClassC.db",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSDuetinteractionCSQLiteDatabaseFile(GRRArtifactBase):
    """
    Duet interactionC database.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/db/CoreDuet/People/interactionC.db",
                    "/var/db/CoreDuet/People/interactionC.db",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSDuetKnowledgeCSQLiteDatabaseFile(GRRArtifactBase):
    """
    Duet knowledgeC User and Application usage database.

    Reference URLs:
    https://www.mac4n6.com/blog/2018/8/5/knowledge-is-power-using-the-knowledgecdb-database-on-macos-and-ios-to-determine-precise-user-and-application-usage
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Knowledge/knowledgeC.db",
                    "/private/var/db/CoreDuet/Knowledge/knowledgeC.db",
                    "/var/db/CoreDuet/Knowledge/knowledgeC.db",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSDuetKnowledgeBase"]


class MacOSDuetSQLiteDatabaseFile(GRRArtifactBase):
    """
    Duet database.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/db/CoreDuet/coreduetd.db",
                    "/var/db/CoreDuet/coreduetd.db",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSDuetSystemEventsSQLiteDatabaseFile(GRRArtifactBase):
    """
    Duet system events database.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/db/CoreDuet/coreduetd.db",
                    "/var/db/CoreDuet/coreduetd.db",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSFSEventsFile(GRRArtifactBase):
    """
    File system events disk log stream (fsevents) files.

    Reference URLs:
    https://github.com/libyal/dtformats/blob/main/documentation/MacOS%20File%20System%20Events%20Disk%20Log%20Stream%20format.asciidoc
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/.fseventsd/*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSFSEvents"]


class MacOSGatekeeperOpaqueConfigurationSQLiteDatabaseFile(GRRArtifactBase):
    """
    Gatekeeper opaque configuration database.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/db/gkopaque.bundle/Contents/Resources/gkopaque.db",
                    "/var/db/gkopaque.bundle/Contents/Resources/gkopaque.db",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSGlobalPreferencesPlistFile(GRRArtifactBase):
    """
    Global preferences property list (plist) file.

    This property list contains information about the system's locale and time
    zone.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-preferences
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/Library/Preferences/.GlobalPreferences.plist"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSiCloudAccounts(GRRArtifactBase):
    """
    iCloud Accounts
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/iCloud/Accounts/*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSiCloudPreferences(GRRArtifactBase):
    """
    iCloud user preferences

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#preferences
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Preferences/MobileMeAccounts.plist"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSIdentityServicesSQLiteDatabaseFile(GRRArtifactBase):
    """
    Identity services SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/IdentityServices/ids.db"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSiDevices(GRRArtifactBase):
    """
    Attached iDevices

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#preferences
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Preferences/com.apple.iPod.plist"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSInstallationHistoryPlistFile(GRRArtifactBase):
    """
    Software installation history property list (plist) file.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#software-installation
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/Library/Receipts/InstallHistory.plist"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSInstallationHistory"]


class MacOSInstallationLogFile(GRRArtifactBase):
    """
    Software installation log file

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-logs
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/private/var/log/install.log", "/var/log/install.log"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSiTunesInterfaceBuilderDocumentPlistFile(GRRArtifactBase):
    """
    iTunes Interface Builder document (*.itxib) plist file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/Applications/iTunes.app/Contents/Resources/*.lproj/*.itxib"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSiOSBackupInfo(GRRArtifactBase):
    """
    iOS device backup information

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#idevice-backup
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/MobileSync/Backup/*/info.plist"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSiOSBackupManifest(GRRArtifactBase):
    """
    iOS device backup apps information

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#idevice-backup
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/MobileSync/Backup/*/Manifest.plist"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSiOSBackupMbdb(GRRArtifactBase):
    """
    iOS device backup files information

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#idevice-backup
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/MobileSync/Backup/*/Manifest.mdbd"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSiOSBackupsMainDirectory(GRRArtifactBase):
    """
    iOS device backups directory

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#idevice-backup
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/MobileSync/Backup/*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSiOSBackupStatus(GRRArtifactBase):
    """
    iOS device backup status information.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#idevice-backup
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/MobileSync/Backup/*/Status.plist"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSKernelExtensionFile(GRRArtifactBase):
    """
    Kernel extension (.kext) files.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#kernel-extension
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/Library/Extensions/*", "/System/Library/Extensions/*"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSKextFiles"]


class MacOSKeyboardLayoutPlistFile(GRRArtifactBase):
    """
    Keyboard layout property list (plist) file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/Library/Preferences/com.apple.HIToolbox.plist"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSLastlogFile(GRRArtifactBase):
    """
    Lastlog file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/private/var/log/lastlog", "/var/log/lastlog"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSLaunchAgentsPlistFile(GRRArtifactBase):
    """
    Launch Agents property list (plist) files.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#autorun-locations
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Library/LaunchAgents/*.plist",
                    "/System/Library/LaunchAgents/*.plist",
                    "%%users.homedir%%/Library/LaunchAgents/*.plist",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSLaunchAgentsPlistFiles"]


class MacOSLaunchDaemonsPlistFile(GRRArtifactBase):
    """
    Launch Daemons property list (plist) files.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#autorun-locations
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Library/LaunchDaemons/*.plist",
                    "/System/Library/LaunchDaemons/*.plist",
                    "%%users.homedir%%/Library/LaunchDaemons/*.plist",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSLaunchDaemonsPlistFiles"]


class MacOSLoadedKexts(GRRArtifactBase):
    """
    MacOS Loaded Kernel Extensions.
    """

    SOURCES = [
        {"type": "COMMAND", "attributes": {"args": [], "cmd": "/usr/sbin/kextstat"}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSLogFile(GRRArtifactBase):
    """
    Miscellaneous system log files.

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#logs
    """

    SOURCES = [{"type": "FILE", "attributes": {"paths": ["/Library/Logs/*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSMiscLogs"]


class MacOSLoginWindowPlistFile(GRRArtifactBase):
    """
    Log-in window information property list (plist) file

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-preferences
    https://taomm.org/PDFs/vol1/CH%200x02%20Persistence.pdf
    https://developer.apple.com/documentation/devicemanagement/loginwindowscripts
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Library/Preferences/com.apple.loginwindow.plist",
                    "%%users.homedir%%/Library/Preferences/loginwindow.plist",
                    "%%users.homedir%%/Library/Preferences/ByHost/com.apple.loginwindow.plist",
                    "%%users.homedir%%/Library/Preferences/ByHost/com.apple.loginwindow.*.plist",
                    "/var/root/Library/Preferences/com.apple.loginwindow.plist",
                    "/private/var/root/Library/Preferences/com.apple.loginwindow.plist",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMailAccounts(GRRArtifactBase):
    """
    Mail Accounts. Until now only V2, V3 and V5 have been observed.

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#mail
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Mail/V[0-9]/MailData/Accounts.plist"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMailBackupTOC(GRRArtifactBase):
    """
    Mail Backup Table of Content. Until now only V2, V3 and V5 have been
    observed.

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#mail
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Mail/V[0-9]/MailData/BackupTOC.plist"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMailboxes(GRRArtifactBase):
    """
    Mail Mailbox Directory. Until now only V2, V3 and V5 have been observed.

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#mail
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Mail/V[0-9]/Mailboxes/*"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMailDownloadAttachments(GRRArtifactBase):
    """
    Mail Downloads Directory

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#mail
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Containers/com.apple.mail/Data/Library/Mail Downloads/*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMailEnvelopIndex(GRRArtifactBase):
    """
    Mail Envelope Index. Until now only V2, V3 and V5 have been observed.

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#mail
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Mail/V[0-9]/MailData/Envelope Index"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMailIMAP(GRRArtifactBase):
    """
    Mail IMAP Synched Mailboxes. Until now only V2, V3 and V5 have been
    observed.

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#mail
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/Library/Mail/V[0-9]/IMAP-*/*"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMailMainDirectory(GRRArtifactBase):
    """
    Mail Main Folder. Until now only V2, V3 and V5 have been observed.

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#mail
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/Library/Mail/V[0-9]/*"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMailOpenedAttachments(GRRArtifactBase):
    """
    Mail Opened Attachments

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#mail
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Mail/V[0-9]/MailData/OpenedAttachmentsV2.plist"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMailPOP(GRRArtifactBase):
    """
    Mail POP Synched Mailboxes. Until now only V2, V3 and V5 have been observed.

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#mail
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/Library/Mail/V[0-9]/POP-*/*"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMailPreferences(GRRArtifactBase):
    """
    Mail Preferences

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#mail
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Preferences/com.apple.Mail.plist"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMailRecentContacts(GRRArtifactBase):
    """
    Mail Recent Contacts

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#mail
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/AddressBook/MailRecents-v4.abcdmr"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMailSignatures(GRRArtifactBase):
    """
    Mail Signatures by Account. Until now only V2, V3 and V5 have been observed.

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#mail
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Mail/V[0-9]/MailData/Signatures/*"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMessageChatSQLiteDatabaseFile(GRRArtifactBase):
    """
    iMessage chat SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/Library/Messages/chat.db"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSMountedDMGs(GRRArtifactBase):
    """
    MacOS Mounted DMG files.
    """

    SOURCES = [
        {"type": "COMMAND", "attributes": {"args": ["info"], "cmd": "/usr/bin/hdiutil"}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSNetworkUsageSQLiteDatabaseFile(GRRArtifactBase):
    """
    Network usage SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/networkd/netusage.sqlite",
                    "/var/networkd/netusage.sqlite",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSNotesSQLiteDatabaseFile(GRRArtifactBase):
    """
    Notes SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Containers/com.apple.Notes/Data/Library/Notes/NotesV*.storedata"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSNotificationCenterSQLiteDatabaseFile(GRRArtifactBase):
    """
    MacOS NotificationCenter SQLite database files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/NotificationCenter/*.db",
                    "/private/var/folders/[a-z][0-9]/*/0/com.apple.notificationcenter/db/db",
                    "/private/var/folders/[a-z][0-9]/*/0/com.apple.notificationcenter/db2/db",
                    "/var/folders/[a-z][0-9]/*/0/com.apple.notificationcenter/db/db",
                    "/var/folders/[a-z][0-9]/*/0/com.apple.notificationcenter/db2/db",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSNotificationCenter"]


class MacOSPeriodicSystemFunctionConfigurationFile(GRRArtifactBase):
    """
    Configuration files of system function scripts that should run periodically.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-info-misc
    https://www.freebsd.org/cgi/man.cgi?periodic
    https://www.freebsd.org/cgi/man.cgi?periodic.conf
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/daily.local/*",
                    "/etc/defaults/periodic.conf",
                    "/etc/monthly.local/*",
                    "/etc/periodic/**2",
                    "/etc/periodic.conf",
                    "/etc/periodic.conf.local",
                    "/etc/periodic/daily/*",
                    "/etc/periodic/monthly/*",
                    "/etc/periodic/weekly/*",
                    "/etc/weekly.local/*",
                    "/private/etc/daily.local/*",
                    "/private/etc/defaults/periodic.conf",
                    "/private/etc/monthly.local/*",
                    "/private/etc/periodic/**2",
                    "/private/etc/periodic.conf",
                    "/private/etc/periodic.conf.local",
                    "/private/etc/periodic/daily/*",
                    "/private/etc/periodic/monthly/*",
                    "/private/etc/periodic/weekly/*",
                    "/private/etc/weekly.local/*",
                    "/usr/local/etc/periodic/**2",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSPeriodicSystemFunctions"]


class MacOSQuarantineEventsSQLiteDatabaseFile(GRRArtifactBase):
    """
    Quarantine events SQLite database file.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#preferences
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Preferences/com.apple.LaunchServices.QuarantineEvents",
                    "%%users.homedir%%/Library/Preferences/com.apple.LaunchServices.QuarantineEventsV2",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSQuarantineEvents"]


class MacOSRecentItemsPlistFile(GRRArtifactBase):
    """
    Recent items property list (plist) file.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#recent-items
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Preferences/com.apple.recentitems.plist"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSRecentItems"]


class MacOSRemoteDesktopAdministratorSystem(GRRArtifactBase):
    """
    Apple Remote Desktop (ARD) was first released in 2002 and is Apple’s desktop
    management system for software distribution, asset management, and remote
    assistance.

    Reference URLs: https://help.apple.com/remotedesktop/mac/3.9/
    https://www.fireeye.com/blog/threat-research/2019/10/leveraging-apple-remote-desktop-for-good-and-evil.html
    https://github.com/fireeye/ARDvark#ard-artifacts-to-parse
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/db/RemoteManagement/ClientCaches/*",
                    "/private/var/db/RemoteManagement/RMDB/rmdb.sqlite3",
                    "/var/db/RemoteManagement/ClientCaches/*",
                    "/var/db/RemoteManagement/RMDB/rmdb.sqlite3",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSRemoteDesktopClientSystem(GRRArtifactBase):
    """
    Apple Remote Desktop (ARD) was first released in 2002 and is Apple’s desktop
    management system for software distribution, asset management, and remote
    assistance.

    Reference URLs: https://help.apple.com/remotedesktop/mac/3.9/
    https://www.fireeye.com/blog/threat-research/2019/10/leveraging-apple-remote-desktop-for-good-and-evil.html
    https://github.com/fireeye/ARDvark#ard-artifacts-to-parse
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/db/RemoteManagement/caches/AppUsage.plist",
                    "/var/db/RemoteManagement/caches/AppUsage.plist",
                    "/private/var/db/RemoteManagement/caches/UserAcct.tmp",
                    "/var/db/RemoteManagement/caches/UserAcct.tmp",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSResourcesInfoStringsPlistFile(GRRArtifactBase):
    """
    Resources InfoPlist.strings plist file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Applications/*.app/Contents/Resources/*.help/Contents/Resources/*.lproj/InfoPlist.strings",
                    "/Applications/*/*.app/Contents/Resources/*.help/Contents/Resources/*.lproj/InfoPlist.strings",
                    "/System/Library/CoreServices/*.app/Contents/Resources/*.lproj/InfoPlist.strings",
                    "/System/Library/Extensions/*.kext/Contents/PlugIns/*.bundle/Contents/Resources/*.lproj/InfoPlist.strings",
                    "/System/Library/Extensions/*.kext/Contents/PlugIns/*.kext/Contents/Resources/*.bundle/Contents/Resources/*.lproj/InfoPlist.strings",
                    "/System/Library/Extensions/*.kext/Contents/Resources/InfoPlist.strings",
                    "/System/Library/Extensions/*.kext/Contents/Resources/*.lproj/InfoPlist.strings",
                    "/System/Library/Filesystems/*/*.kext/Contents/Resources/*.lproj/InfoPlist.strings",
                    "/System/Library/Filesystems/*/Encodings/*.kext/Contents/Resources/*.lproj/InfoPlist.strings",
                    "/System/Library/PrivateFrameworks/*.framework/Versions/A/Resources/*.kext/Contents/Resources/*.lproj/InfoPlist.strings",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSResourcesLocalizableStringsPlistFile(GRRArtifactBase):
    """
    Resources Localizable.strings plist file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/System/Library/CoreServices/*.app/Contents/Resources/*.lproj/Localizable.strings",
                    "/System/Library/Extensions/*.kext/Contents/Resources/*.lproj/Localizable.strings",
                    "/System/Library/Extensions/*.kext/Contents/PlugIns/*.kext/Contents/Resources/*.lproj/Localizable.strings",
                    "/System/Library/Frameworks/*.framework/Versions/A/Frameworks/*.framework/Versions/A/Resources/*.lproj/Localizable.strings",
                    "/System/Library/PreferencePanes/*.prefPane/Contents/Resources/*.lproj/Localizable.strings",
                    "/System/Library/PrivateFrameworks/*.framework/Versions/A/Plugins/*.bundle/Contents/Resources/*.lproj/Localizable.strings",
                    "/System/Library/PrivateFrameworks/*.framework/Versions/A/Resources/*.lproj/Localizable.strings",
                    "/System/Library/SystemProfiler/*/Contents/Resources/*.lproj/Localizable.strings",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSSidebarListsPlistFile(GRRArtifactBase):
    """
    Sidebar lists preferences property list (plist) file.

    This property list contains the names of volumes mounted on the desktop that
    have appeared in the sidebar list.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#preferences
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Preferences/com.apple.sidebarlists.plist",
                    "%%users.homedir%%/Preferences/com.apple.sidebarlists.plist",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSSidebarLists"]


class MacOSSiriAnalyticsSQLiteDatabaseFile(GRRArtifactBase):
    """
    Siri analytics SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Assistant/SiriAnalytics.db"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSSiriSuggestionsEntitiesSQLiteDatabaseFile(GRRArtifactBase):
    """
    Siri suggestions entities SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Suggestions/entities.db",
                    "%%users.homedir%%/Library/Suggestions/entities.db-wal",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSSiriSuggestionsPendingQueueSQLiteDatabaseFile(GRRArtifactBase):
    """
    Siri suggestions pending queue SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Suggestions/pending/queue.db",
                    "%%users.homedir%%/Library/Suggestions/pending/queue.db-wal",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSSiriSuggestionsSnippetsSQLiteDatabaseFile(GRRArtifactBase):
    """
    Siri suggestions snippets SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Suggestions/snippets.db",
                    "%%users.homedir%%/Library/Suggestions/snippets.db-wal",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSSleepimageFile(GRRArtifactBase):
    """
    Sleepimage file which contains the content of memory before going to sleep

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#sleep.2fhibernate-and-swap-image-file
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/private/var/vm/sleepimage", "/var/vm/sleepimage"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSSoftwareUpdatePreferencesPlistFile(GRRArtifactBase):
    """
    Software update preferences property list (plist) files.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#software-installation
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/Library/Preferences/com.apple.SoftwareUpdate.plist"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSUpdate"]


class MacOSSpotlightStoreVolumeConfigurationPlistFile(GRRArtifactBase):
    """
    Spotlight store volume configuration plist file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/.Spotlight-V100/Store-V1/VolumeConfig.plist"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSSpotlightVolumeConfigurationPlistFile(GRRArtifactBase):
    """
    Spotlight volume configuration plist file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/.Spotlight-V100/VolumeConfiguration.plist"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSStartupItemsPlistFile(GRRArtifactBase):
    """
    Startup Items property list (plist) files.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#autorun-locations
    https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/StartupItems.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Library/StartupItems/**/*.plist",
                    "/System/Library/StartupItems/**/*.plist",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSStartupItemsPlistFiles"]


class MacOSSwapFile(GRRArtifactBase):
    """
    Swap file

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#sleep.2fhibernate-and-swap-image-file
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/private/var/vm/swapfile[0-9]", "/var/vm/swapfile[0-9]"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSSwapFiles"]


class MacOSSystemConfigurationPreferencesPlistFile(GRRArtifactBase):
    """
    System configuration preferences property list (plist) file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/Library/Preferences/SystemConfiguration/preferences.plist"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSSystemLogFile(GRRArtifactBase):
    """
    System log file.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-logs
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/private/var/log/*", "/var/log/*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSSystemLogFiles"]


class MacOSSystemPolicySQLiteDatabaseFile(GRRArtifactBase):
    """
    System policy database.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/private/var/db/SystemPolicy", "/var/db/SystemPolicy"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSSystemPreferencesPlistFile(GRRArtifactBase):
    """
    System Preferences property list (plist) files

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-preferences
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["/Library/Preferences/**/*.plist"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSSystemPreferencesPlistFiles"]


class MacOSSystemVersionPlistFile(GRRArtifactBase):
    """
    Operating system name and version property list (plist) file

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-settings-and-informations
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/System/Library/CoreServices/SystemVersion.plist"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSTCCSQLiteDatabaseFile(GRRArtifactBase):
    """
    Transparency, Consent, Control (TCC) framework SQLite database files.

    Reference URLs: https://forensics.wiki/tcc_database
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/Library/Application Support/com.apple.TCC/TCC.db",
                    "%%users.homedir%%/Library/Application Support/com.apple.TCC/TCC.db",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSTCC"]


class MacOSTextReplacementsSQLiteDatabaseFile(GRRArtifactBase):
    """
    Text replacements SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/KeyboardServices/TextReplacements.db"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSTimeMachinePlistFile(GRRArtifactBase):
    """
    Time Machine information property list (plist) file

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-preferences
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/Library/Preferences/com.apple.TimeMachine.plist"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSUnifiedLogging(GRRArtifactBase):
    """
    Apple Unified Logging and Activity Tracing

    Reference URLs:
    https://github.com/mac4n6/Presentations/blob/master/Logs%20Unite!%20-%20Forensic%20Analysis%20of%20Apple%20Unified%20Logs/LogsUnite.pdf
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/db/diagnostics/*.tracev3",
                    "/private/var/db/diagnostics/*/*.tracev3",
                    "/private/var/db/uuidtext/*/*",
                    "/var/db/diagnostics/*.tracev3",
                    "/var/db/diagnostics/*/*.tracev3",
                    "/var/db/uuidtext/*/*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSUserApplicationLogFile(GRRArtifactBase):
    """
    User applications log files.

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#logs
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/Library/Logs/*.log"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSUserApplicationLogs"]


class MacOSUserApplicationSupportDirectory(GRRArtifactBase):
    """
    Contents of the user Application Support directories.

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#misc
    """

    SOURCES = [
        {
            "type": "PATH",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Application Support/*"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSApplicationSupport"]


class MacOSUserDesktopDirectory(GRRArtifactBase):
    """
    Contents of the user Desktop directories.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#user-directories
    """

    SOURCES = [
        {"type": "PATH", "attributes": {"paths": ["%%users.homedir%%/Desktop/*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSUserDockDesktopPictureSQLiteDatabaseFile(GRRArtifactBase):
    """
    Dock user desktop picture SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Dock/desktoppicture.db"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSUserDocumentsDirectory(GRRArtifactBase):
    """
    Contents of the user Documents directories.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#user-directories
    """

    SOURCES = [
        {"type": "PATH", "attributes": {"paths": ["%%users.homedir%%/Documents/*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSUserGlobalPreferencesPlistFile(GRRArtifactBase):
    """
    User global preferences property list (plist) file.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#preferences
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Preferences/.GlobalPreferences.plist"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSUserGlobalPreferences"]


class MacOSUserKeychainFile(GRRArtifactBase):
    """
    User keychain files.

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#misc
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/Library/Keychains/*.keychain"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSKeychains"]


class MacOSUserKeychainOCSPCacheSQLiteDatabaseFile(GRRArtifactBase):
    """
    User keychain CRL and OCSP cache SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Keychains/*/ocspcache.sqlite3"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSUserLibraryDirectory(GRRArtifactBase):
    """
    Contents of the user Library directories.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#user-directories
    """

    SOURCES = [
        {"type": "PATH", "attributes": {"paths": ["%%users.homedir%%/Library/*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSUserLocalItemsKeychainKeybagSQLiteDatabaseFile(GRRArtifactBase):
    """
    User (iCloud) local items keychain keybag SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/Library/Keychains/*/user.db"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSUserLocalItemsKeychainRecordsSQLiteDatabaseFile(GRRArtifactBase):
    """
    User (iCloud) local items keychain encrypted records SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Keychains/*/keychain-2.db"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSUserLoginItemsPlistFile(GRRArtifactBase):
    """
    User login items property list (plist) file.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#autorun-locations-2
    https://objective-see.org/blog/blog_0x31.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Preferences/com.apple.loginitems.plist",
                    "%%users.homedir%%/Library/Application Support/com.apple.backgroundtaskmanagementagent/backgrounditems.btm",
                    "/private/var/db/com.apple.backgroundtaskmanagement/BackgroundItems-v*.btm",
                    "/var/db/com.apple.backgroundtaskmanagement/BackgroundItems-v*.btm",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSUserLoginItems"]


class MacOSUserMoviesDirectory(GRRArtifactBase):
    """
    Contents of the user Movies directories.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#user-directories
    """

    SOURCES = [
        {"type": "PATH", "attributes": {"paths": ["%%users.homedir%%/Movies/*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSUserMusicDirectory(GRRArtifactBase):
    """
    Contents of the user Music directories.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#user-directories
    """

    SOURCES = [{"type": "PATH", "attributes": {"paths": ["%%users.homedir%%/Music/*"]}}]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSUserPasswordHashesPlistFile(GRRArtifactBase):
    """
    User password hashes property list (plist) files.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#system-settings-and-informations
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/db/dslocal/nodes/Default/users/*.plist",
                    "/var/db/dslocal/nodes/Default/users/*.plist",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSUserPasswordHashesPlistFiles"]


class MacOSUserPicturesDirectory(GRRArtifactBase):
    """
    Contents of the user Pictures directories.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#user-directories
    """

    SOURCES = [
        {"type": "PATH", "attributes": {"paths": ["%%users.homedir%%/Pictures/*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSUserPreferencesDirectory(GRRArtifactBase):
    """
    Contents of the user Preferences directories.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#preferences
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/Library/Preferences/*"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSUserPreferences"]


class MacOSUserPublicDirectory(GRRArtifactBase):
    """
    Contents of the user Public directories.

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#user-directories
    """

    SOURCES = [
        {"type": "PATH", "attributes": {"paths": ["%%users.homedir%%/Public/*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSUserAccountsSQLiteDatabaseFile(GRRArtifactBase):
    """
    User Accounts SQLite database files.

    Seen Accounts3.sqlite and Accounts4.sqlite

    Reference URLs:
    https://forensics.wiki/mac_os_x_10.9_artifacts_location#user.27s-accounts
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Accounts/Accounts*.sqlite",
                    "%%users.homedir%%/Library/Accounts/Accounts*.sqlite-wal",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSUserSocialAccounts"]


class MacOSUserTrashDirectory(GRRArtifactBase):
    """
    Contents of the user Trash directories.

    Reference URLs: https://forensics.wiki/mac_os_x_10.9_artifacts_location#misc
    """

    SOURCES = [
        {"type": "FILE", "attributes": {"paths": ["%%users.homedir%%/.Trash/*"]}}
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSUserTrash"]


class MacOSUtmpxFile(GRRArtifactBase):
    """
    Utmpx login record file.

    Reference URLs:
    https://github.com/libyal/dtformats/blob/main/documentation/Utmp%20login%20records%20format.asciidoc
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["/private/var/run/utmpx", "/var/run/utmpx"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSWalletSQLiteDatabaseFile(GRRArtifactBase):
    """
    Apple Wallet SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Passes/passes23.sqlite"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSWirelessDiagnosticDataPersistentSQLiteDatabaseFile(GRRArtifactBase):
    """
    Apple Wireless Diagnostic Data (AWDD) persistent SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/var/db/awdd/persistent.db",
                    "/var/db/awdd/persistent.db",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class MacOSXcodeiOSDeviceLogsSQLiteDatabaseFile(GRRArtifactBase):
    """
    Xcode iOS Device Logs SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Developer/Xcode/iOS Device Logs/iOS Device Logs *.db"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None
