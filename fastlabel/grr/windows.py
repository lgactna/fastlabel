"""
Auto-generated classes from the YAML declarations in windows.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr import webbrowser
from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class WindowsActionCenterSettings(GRRArtifactBase):
    """
    Windows Action Center Settings

    Malware can modify these keys to disable notifications that occur when
    various security features are disabled. One malware family known to modify
    these keys is Kovter, a well-known trojan.

    Reference URLs:
    https://winaero.com/blog/registry-tweak-to-disable-action-center-notifications-in-windows-7/
    https://blog.talosintelligence.com/2019/05/threat-roundup-0517-0524.html
    https://blogs.technet.microsoft.com/platforms_lync_cloud/2017/05/05/disabling-windows-10-action-center-notifications/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Action Center\\Checks\\{e8433b72-5842-4d43-8645-bc2c35960837}.check.*",
                        "value": "CheckSetting",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Action Center\\Checks\\{e8433b72-5842-4d43-8645-bc2c35960837}.check.*",
                        "value": "CheckSetting",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings\\Windows.SystemToast.SecurityAndMaintenance",
                        "value": "Enabled",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Notifications\\Settings\\Windows.SystemToast.SecurityAndMaintenance",
                        "value": "Enabled",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsActiveDesktop(GRRArtifactBase):
    """
    Windows Active Desktop settings and components.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/ActiveDesktop.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer\\Desktop\\Components\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer\\Desktop\\General",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsActiveDirectoryDatabaseFile(GRRArtifactBase):
    """
    Windows Active Directory database file (ntds.dit).

    Reference URLs:
    https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc772829(v=ws.10)
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\ntds\\ntds.dit",
                    "%%environ_systemroot%%\\ServicePackFiles\\*\\ntds.dit*",
                    "%%environ_systemroot%%\\SoftwareDistribution\\Download\\*\\*\\ntds.dit*",
                    "%%environ_systemroot%%\\System32\\ntds.dit",
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
    aliases: ClassVar[Optional[list[str]]] = ["WindowsActiveDirectoryDatabase"]


class WindowsActiveSyncAutoStart(GRRArtifactBase):
    """
    Windows ActiveSync AutoStart entries

    Reference URLs:
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows CE Services\\AutoStartOnConnect\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows CE Services\\AutoStartOnDisconnect\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows CE Services\\AutoStartOnConnect\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows CE Services\\AutoStartOnDisconnect\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsActivitiesCacheDatabase(GRRArtifactBase):
    """
    SQLite database containing the Windows activities cache.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/ActivitiesCacheDatabase.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\ConnectedDevicesPlatform\\L.%%users.username%%\\ActivitiesCache.db"
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


class WindowsAlternateShell(GRRArtifactBase):
    """
    Alternate Shell to be run via Userinit.

    Reference URLs: https://www.microsoftpressstore.com/articles/article.aspx
    https://technet.microsoft.com/en-us/library/cc976124.aspx
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\SafeBoot",
                        "value": "AlternateShell",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\SafeBoot\\Option",
                        "value": "UseAlternateShell",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsAMCacheHveFile(GRRArtifactBase):
    """
    The AMCache file, stored in the Windows NT Registry file format.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/AMCache.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\AppCompat\\Programs\\Amcache.hve",
                    "%%environ_systemroot%%\\AppCompat\\Programs\\Amcache.hve.LOG1",
                    "%%environ_systemroot%%\\AppCompat\\Programs\\Amcache.hve.LOG2",
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


class WindowsAppCertDLLs(GRRArtifactBase):
    """
    Windows AppCertDLLs persistence.

    Reference URLs:
    http://blogs.technet.com/b/mmpc/archive/2011/03/19/how-to-defang-the-fake-defragmenter.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\AppCertDLLs"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsAppCompatCache(GRRArtifactBase):
    """
    Windows Application Compatibility Cache

    Reference URLs:
    https://github.com/libyal/winreg-kb/blob/main/documentation/Application%20Compatibility%20Cache%20key.asciidoc
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\AppCompatibility",
                        "value": "AppCompatCache",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\AppCompatCache",
                        "value": "AppCompatCache",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsAppInitDLLs(GRRArtifactBase):
    """
    Windows Application Initial (AppInit) DLLs persistence.

    AppInit DLLs is a mechanism that allows an arbitrary list of DLLs to be
    loaded into each user mode process on the system.

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/dd744762(v=vs.85).aspx
    https://support.microsoft.com/en-us/kb/197571
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows",
                        "value": "AppInit_DLLs",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Windows",
                        "value": "AppInit_DLLs",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows",
                        "value": "AppInit_DLLs",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Windows",
                        "value": "AppInit_DLLs",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsApplicationRegistration(GRRArtifactBase):
    """
    Windows Application Registration (AppPath) Registry keys.

    Reference URLs:
    https://github.com/keydet89/RegRipper2.8/blob/master/plugins/apppaths.pl
    http://www.hexacorn.com/blog/2013/01/19/beyond-good-ol-run-key-part-3/
    https://msdn.microsoft.com/en-us/library/windows/desktop/ee872121(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\App Paths\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\App Paths\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsApplicationCompatibilityInstalledShimDatabases(GRRArtifactBase):
    """
    Windows Application Compatibility Installed Shim Databases.

    drvmain.sdb, frxmain.sdb, msimain.sdb, pcamain.sdb, and sysmain.sdb are shim
    database files (SDB files) that are provided by Windows, and contain many
    predefined shims that address known application compatibility issues. Note
    that these database files are not signed.

    Windows also supports custom shim database. These are typically installed by
    the sdbinst.exe utility. Note, that shim database files can also exist
    elsewhere in the file system.

    Windows application shims provide a way for the operating system to apply
    patches to executables before they are run, ultimately providing a
    lightweight mechanism for applying hot fixes and making modifications to
    ensure compatibility across the various versions of Windows. This
    functionality can also be leveraged maliciously to change how certain
    programs operate, or to provide capabilities to malware, such as the ability
    to bypass UAC, gain persistence by injecting loading into legitimate
    processes, or avoid detection by disabling anti-virus software.

    Reference URLs: https://attack.mitre.org/techniques/T1138/
    https://countercept.com/blog/hunting-for-application-shim-databases/
    http://files.brucon.org/2015/Tomczak_and_Ballenthin_Shims_for_the_Win.pdf
    https://www.blackhat.com/docs/eu-15/materials/eu-15-Pierce-Defending-Against-Malicious-Application-Compatibility-Shims-wp.pdf
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_windir%%\\AppPatch\\drvmain.sdb",
                    "%%environ_windir%%\\AppPatch\\frxmain.sdb",
                    "%%environ_windir%%\\AppPatch\\msimain.sdb",
                    "%%environ_windir%%\\AppPatch\\pcamain.sdb",
                    "%%environ_windir%%\\AppPatch\\sysmain.sdb",
                    "%%environ_windir%%\\AppPatch\\AppPatch64\\Custom\\*",
                    "%%environ_windir%%\\AppPatch\\Custom\\*",
                    "%%environ_windir%%\\AppPatch\\Custom\\Custom64\\*",
                    "%%environ_windir%%\\AppPatch\\CustomSDB\\*",
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


class WindowsApplicationCompatibilityShimDatabaseMappings(GRRArtifactBase):
    """
    Windows Application Compatibility Shim Database Mappings.

    Mappings between the Windows Application Compatibility shim database files
    and the programs that they apply to.

    Windows allows for custom application shims to be installed via the
    sdbinst.exe application. For example a mapping for 'notepad.exe':

    Key: HKEY_LOCAL_MACHINE/Software/Microsoft/Windows
    NT/CurrentVersion/AppCompatFlags/Custom/notepad.exe Value:
    {00000000-1111-2222-3333-444444444444}.sdb = 0

    Key: AppCompatFlags/InstalledSDB/{00000000-1111-2222-3333-444444444444}
    Value: DatabasePath =
    "C:/Windows/AppPatch/Custom/{00000000-1111-2222-3333-444444444444}.sdb"

    Windows application shims provide a way for the operating system to apply
    patches to executables before they are run, ultimately providing a
    lightweight mechanism for applying hot fixes and making modifications to
    ensure compatibility across the various versions of Windows. This
    functionality can also be leveraged maliciously to change how certain
    programs operate, or to provide capabilities to malware, such as the ability
    to bypass UAC, gain persistence by injecting loading into legitimate
    processes, or avoid detection by disabling anti-virus software.

    Reference URLs: https://attack.mitre.org/techniques/T1138/
    https://countercept.com/blog/hunting-for-application-shim-databases/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\InstalledSDB\\*",
                        "value": "DatabaseDescription",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\InstalledSDB\\*",
                        "value": "DatabasePath",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\AppCompatFlags\\Custom\\*",
                        "value": "*",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsAppXRT(GRRArtifactBase):
    """
    WinAppXRT DLL loaded by .Net applications when the APPX_PROCESS environment
    variable is set.

    Reference URLs:
    http://www.hexacorn.com/blog/2014/08/31/beyond-good-ol-run-key-part-17/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\system32\\WinAppXRT.dll",
                    "%%environ_systemroot%%\\WinAppXRT.dll",
                    "%%environ_systemroot%%\\System32\\Wbem\\WinAppXRT.dll",
                    "%%environ_systemroot%%\\System32\\WindowsPowerShell\\v1.0\\WinAppXRT.dll",
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
    aliases: ClassVar[Optional[list[str]]] = ["WinAppXRT"]


class WindowsAutoexecBat(GRRArtifactBase):
    """
    Windows autoexec.bat file
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemdrive%%\\autoexec.bat",
                    "%%environ_windir%%\\autoexec.nt",
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


class WindowsAutomaticDebugging(GRRArtifactBase):
    """
    Windows automatic debugging (Aedebug)

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/bb204634(v=vs.85).aspx
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\AeDebug",
                        "value": "Debugger",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsAutomaticDebuggingExclusionList(GRRArtifactBase):
    """
    Windows automatic debugging (Aedebug) exclusion list

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/bb204634(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\AutoExclusionList\\*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsAutorun(GRRArtifactBase):
    """
    Filebased Tests.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_systemdrive%%\\autorun.inf"],
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


class WindowsAvailableTimeZones(GRRArtifactBase):
    """
    Timezones available on a Windows system.

    Reference URLs:
    https://github.com/libyal/winreg-kb/blob/main/documentation/Time%20zone%20keys.asciidoc
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Time Zones\\*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsBackgroundActivityModeratorKeys(GRRArtifactBase):
    """
    Windows Background Activity Moderator (BAM) and Desktop Activity Moderator
    (DAM) registry keys.

    Reference URLs: https://dfir.ru/2020/04/08/bam-internals/
    https://notes.qazeer.io/dfir/windows/_artefacts_overview
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\bam\\UserSettings\\*",
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\bam\\State\\UserSettings\\*",
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\dam\\UserSettings\\*",
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\dam\\State\\UserSettings\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsBITSQueueManagerDatabases(GRRArtifactBase):
    """
    Databases that contain the Windows BITS jobs definition and state.

    Reference URLs:
    http://dfrws.org/2015/proceedings/presentations/DFRWS2015-pres3.pdf
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersprofile%%\\Microsoft\\Network\\Downloader\\qmgr*.dat",
                    "%%environ_allusersprofile%%\\Microsoft\\Network\\Downloader\\qmgr.db",
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


class WindowsBootConfigurationDataRegistryFiles(GRRArtifactBase):
    """
    Boot Configuration Data (BCD) Windows Registry files.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/RegistryFiles.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "\\Boot\\BCD",
                    "\\Boot\\BCD.LOG",
                    "\\Boot\\BCD.LOG1",
                    "\\Boot\\BCD.LOG2",
                    "\\EFI\\Microsoft\\Boot\\BCD",
                    "\\EFI\\Microsoft\\Boot\\BCD.LOG",
                    "\\EFI\\Microsoft\\Boot\\BCD.LOG1",
                    "\\EFI\\Microsoft\\Boot\\BCD.LOG2",
                    "\\EFI\\Microsoft\\Recovery\\BCD",
                    "\\EFI\\Microsoft\\Recovery\\BCD.LOG",
                    "\\EFI\\Microsoft\\Recovery\\BCD.LOG1",
                    "\\EFI\\Microsoft\\Recovery\\BCD.LOG2",
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


class WindowsBootVerificationProgram(GRRArtifactBase):
    """
    Path to custom startup verification program.

    Reference URLs:
    https://technet.microsoft.com/en-us/library/cc786702(WS.10).aspx
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\BootVerificationProgram",
                        "value": "ImagePath",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsBootConfigurationSettings(GRRArtifactBase):
    """
    Windows Boot Configuration Settings

    Reference URLs: https://forensics.wiki/windows_boot_configuration_data
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\BCD00000000\\Objects\\*\\Elements\\16000009",
                        "value": "Element",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\BCD00000000\\Objects\\*\\Elements\\250000e0",
                        "value": "Element",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsCIMRepositoryFiles(GRRArtifactBase):
    """
    Windows Common Information Model (CIM) repository.

    Persistent database that holds the schema, also called the object repository
    or class store, that models the managed environment and defines every piece
    of data exposed by WMI.

    This definition does not specify the copies of the CIM repository that are
    stored in system restore points.

    Reference URLs:
    https://github.com/libyal/dtformats/blob/main/documentation/WMI%20repository%20file%20format.asciidoc
    https://forensics.wiki/wmi
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_windir%%\\System\\Wbem\\Repository\\cim.rep",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\CIM.REC",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\CIM.REP",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\INDEX.BTR",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\INDEX.MAP",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\MAPPING.VER",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\MAPPING[1-3].MAP",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\OBJECTS.DATA",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\OBJECTS.MAP",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\FS\\INDEX.BTR",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\FS\\INDEX.MAP",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\FS\\MAPPING.VER",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\FS\\MAPPING[1-2].MAP",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\FS\\OBJECTS.DATA",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository\\FS\\OBJECTS.MAP",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository.00[1-9]\\INDEX.BTR",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository.00[1-9]\\INDEX.MAP",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository.00[1-9]\\MAPPING.VER",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository.00[1-9]\\MAPPING[1-3].MAP",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository.00[1-9]\\OBJECTS.DATA",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository.00[1-9]\\OBJECTS.MAP",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository.00[1-9]\\FS\\INDEX.BTR",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository.00[1-9]\\FS\\INDEX.MAP",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository.00[1-9]\\FS\\MAPPING.VER",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository.00[1-9]\\FS\\MAPPING[1-2].MAP",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository.00[1-9]\\FS\\OBJECTS.DATA",
                    "%%environ_systemroot%%\\System32\\wbem\\Repository.00[1-9]\\FS\\OBJECTS.MAP",
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


class WindowsCodePage(GRRArtifactBase):
    """
    The system code page.

    Reference URLs:
    https://winreg-kb.readthedocs.io/en/latest/sources/system-keys/Codepage.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Nls\\CodePage",
                        "value": "ACP",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = ["WinCodePage"]


class WindowsComputerName(GRRArtifactBase):
    """
    The name of the system.
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\ComputerName\\ComputerName",
                        "value": "ComputerName",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsCommandProcessorAutoRun(GRRArtifactBase):
    """
    Commands that are run each time the Command Processor (Cmd.exe) is started.

    Reference URLs:
    https://technet.microsoft.com/en-us/library/cc779439(v=ws.10).aspx
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    http://blogs.msdn.com/b/oldnewthing/archive/2007/11/21/6447771.aspx
    https://technet.microsoft.com/en-us/library/cc756720(v=ws.10).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Command Processor",
                        "value": "AutoRun",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Command Processor",
                        "value": "AutoRun",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Command Processor",
                        "value": "AutoRun",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Command Processor",
                        "value": "AutoRun",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsCOMInprocHandlers(GRRArtifactBase):
    """
    Windows COM in-process handlers

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms694515(v=vs.85).aspx
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms691354(v=vs.85).aspx
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms693485(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\CLSID\\*",
                        "value": "InprocHandler",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\CLSID\\*",
                        "value": "InprocHandler32",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\CLSID\\*",
                        "value": "InprocHandler",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\CLSID\\*",
                        "value": "InprocHandler32",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\CLSID\\*",
                        "value": "InprocHandler",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\CLSID\\*",
                        "value": "InprocHandler32",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\CLSID\\*",
                        "value": "InprocHandler",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\CLSID\\*",
                        "value": "InprocHandler32",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsCOMInprocServers(GRRArtifactBase):
    """
    Windows COM in-process servers

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms694515(v=vs.85).aspx
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms682390(v=vs.85).aspx
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms694328(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\CLSID\\*\\InprocServer",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\CLSID\\*\\InprocServer32",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\CLSID\\*\\InprocServer",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\CLSID\\*\\InprocServer32",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\CLSID\\*\\InprocServer",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\CLSID\\*\\InprocServer32",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\CLSID\\*\\InprocServer",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\CLSID\\*\\InprocServer32",
                        "value": "",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsCOMLocalServers(GRRArtifactBase):
    """
    Windows COM local servers

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms694515(v=vs.85).aspx
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms686595(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\CLSID\\*",
                        "value": "LocalServer",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\CLSID\\*\\LocalServer32",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\CLSID\\*\\LocalServer32",
                        "value": "ServerExecutable",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\CLSID\\*",
                        "value": "LocalServer",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\CLSID\\*\\LocalServer32",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\CLSID\\*\\LocalServer32",
                        "value": "ServerExecutable",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\CLSID\\*",
                        "value": "LocalServer",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\CLSID\\*\\LocalServer32",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\CLSID\\*\\LocalServer32",
                        "value": "ServerExecutable",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\CLSID\\*",
                        "value": "LocalServer",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\CLSID\\*\\LocalServer32",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\CLSID\\*\\LocalServer32",
                        "value": "ServerExecutable",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsCommonFilePlacementAttacks(GRRArtifactBase):
    """
    Common files associated with search order hijacking and other file placement
    attacks.

    Reference URLs:
    http://web.cs.ucdavis.edu/~su/publications/issta10-loading.pdf
    https://www.mandiant.com/blog/fxsst/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_programfiles%%\\Internet Explorer\\sxs.dll",
                    "%%environ_programfilesx86%%\\Internet Explorer\\sxs.dll",
                    "%%environ_systemdrive%%\\explorer.exe",
                    "%%environ_systemdrive%%\\program.exe",
                    "%%environ_systemroot%%\\linkinfo.dll",
                    "%%environ_systemroot%%\\ntshrui.dll",
                    "%%environ_systemroot%%\\System32\\oci.dll",
                    "%%environ_systemroot%%\\System32\\sysprep\\cryptbase.dll",
                    "%%environ_systemroot%%\\SysWOW64\\oci.dll",
                    "%%environ_systemroot%%\\SysWOW64\\sysprep\\cryptbase.dll",
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


class WindowsCOMProperties(GRRArtifactBase):
    """
    Various properties of Windows COM Objects.

    These artifacts are meant to highlight properties of COM objects that,
    although legitimate, are known to be associated with persistence techniques
    or other capabilities that malware can leverage.

    ShellFolder/HideOnDesktop, ShellFolder/Attributes (specifically with value
    0xf090013d), and InprocServer/LoadWithoutCOM are associated with a technique
    to cause iexplore or explorer to load a malicious DLL by registering a COM
    object and invoking it through the use of Junction Folders.

    Reference URLs:
    https://ired.team/offensive-security/code-execution/forcing-iexplore.exe-to-load-a-malicious-dll-via-com-abuse
    https://labs.nettitude.com/blog/com-and-the-powerthief/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\CLSID\\*\\ShellFolder",
                        "value": "Attributes",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\CLSID\\*\\ShellFolder",
                        "value": "Attributes",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\CLSID\\*\\ShellFolder",
                        "value": "Attributes",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\CLSID\\*\\ShellFolder",
                        "value": "Attributes",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\CLSID\\*\\ShellFolder",
                        "value": "HideOnDesktop",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\CLSID\\*\\ShellFolder",
                        "value": "HideOnDesktop",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\CLSID\\*\\ShellFolder",
                        "value": "HideOnDesktop",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\CLSID\\*\\ShellFolder",
                        "value": "HideOnDesktop",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\CLSID\\*\\InprocServer32",
                        "value": "LoadWithoutCOM",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\CLSID\\*\\InprocServer32",
                        "value": "LoadWithoutCOM",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\CLSID\\*\\InprocServer32",
                        "value": "LoadWithoutCOM",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\CLSID\\*\\InprocServer32",
                        "value": "LoadWithoutCOM",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsCOMRegisteredTypeLibraries(GRRArtifactBase):
    """
    Windows COM registered type libraries

    Reference URLs:
    https://github.com/libyal/winreg-kb/blob/main/documentation/Component%20Object%20Model%20keys.asciidoc#type-libraries-key
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Typelib\\*\\*\\*\\*",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\Typelib\\*\\*\\*\\*",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Typelib\\*\\*\\*\\*",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\Typelib\\*\\*\\*\\*",
                        "value": "",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsConfigSys(GRRArtifactBase):
    """
    Windows config.sys file
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemdrive%%\\config.sys",
                    "%%environ_windir%%\\config.nt",
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


class WindowsControlPanelFilePaths(GRRArtifactBase):
    """
    DLLs listed here will be run when the user opens the Windows Control Panel.

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/hh127454(v=vs.85).aspx
    http://www.geoffchappell.com/studies/windows/shell/shell32/classes/controlpanel.htm
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms683844(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Control Panel\\CPLs",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Control Panel\\CPLs",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Control Panel\\CPLs",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Control Panel\\CPLs",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsCortanaDatabase(GRRArtifactBase):
    """
    Windows Cortana database

    Reference URLs: https://forensics.wiki/cortana
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Packages\\Microsoft.Windows.Cortana_*\\AppData\\Indexed DB\\IndexedDB.edb",
                    "%%users.localappdata%%\\Packages\\Microsoft.Windows.Cortana_*\\LocalState\\ESEDatabase_CortanaCoreInstance\\CortanaCoreDb.dat",
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


class WindowsCrashDumps(GRRArtifactBase):
    """
    Windows Error Reporting (WER) files and crash dumps.

    The files include information about the crashed processes and potentially
    process dumps, whether auto-generated upon a crash or by a user. It's
    helpful to analyze them to identify unexpected process executions or
    exploitation attempts.

    Reference URLs: https://forensics.wiki/windows#crash-and-minidumps
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersprofile%%\\Microsoft\\Windows\\WER\\**",
                    "%%environ_systemroot%%\\*.dmp",
                    "%%environ_systemroot%%\\Minidump\\*.dmp",
                    "%%environ_systemroot%%\\ServiceProfiles\\AppData\\Local\\CrashDumps\\**",
                    "%%environ_systemroot%%\\ServiceProfiles\\AppData\\Local\\Temp\\*.dmp",
                    "%%environ_systemroot%%\\System32\\config\\systemprofile\\AppData\\Local\\CrashDumps\\**",
                    "%%environ_systemroot%%\\System32\\config\\systemprofile\\AppData\\Local\\Temp\\*.dmp",
                    "%%environ_systemroot%%\\Temp\\*.dmp",
                    "%%users.localappdata%%\\CrashDumps\\**",
                    "%%users.localappdata%%\\Microsoft\\Windows\\WER\\**",
                    "%%users.localappdata%%\\Temp\\*.dmp",
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


class WindowsCredentialProviderFilters(GRRArtifactBase):
    """
    Windows Credential Provider Filters

    Reference URLs:
    http://blog.leetsys.com/2012/01/02/capturing-windows-7-credentials-at-logon-using-custom-credential-provider/
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Authentication\\Credential Provider Filters\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Authentication\\Credential Provider Filters\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsCredentialProviders(GRRArtifactBase):
    """
    CLSIDs of applications to use as Credential Providers

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    http://blogs.technet.com/b/ad/archive/2009/05/26/thoughts-on-single-sign-on-and-credential-providers.aspx
    http://blog.leetsys.com/2012/01/02/capturing-windows-7-credentials-at-logon-using-custom-credential-provider/
    https://www.sophos.com/en-us/support/knowledgebase/114190.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Authentication\\Credential Providers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Authentication\\Credential Providers\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsCryptnetUrlCacheMetadata(GRRArtifactBase):
    """
    Metadata of a Windows cache of files downloaded from the internet.

    Helpful when investigating the use of "Living of the Land" tools that allow
    attackers to download arbitrary files from the internet, such as
    "certutil.exe".

    Reference URLs: https://forensics.wiki/windows#cryptnet-url-cache
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\config\\systemprofile\\AppData\\LocalLow\\Microsoft\\CryptnetUrlCache\\MetaData\\*",
                    "%%environ_systemroot%%\\SysWOW64\\config\\systemprofile\\AppData\\LocalLow\\Microsoft\\CryptnetUrlCache\\MetaData\\*",
                    "%%users.userprofile%%\\AppData\\LocalLow\\Microsoft\\CryptnetUrlCache\\MetaData\\*",
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


class WindowsCryptnetUrlCacheContent(GRRArtifactBase):
    """
    Content of a Windows cache of files downloaded from the internet.

    Helpful when investigating the use of "Living of the Land" tools that allow
    attackers to download arbitrary files from the internet, such as
    "certutil.exe".

    Reference URLs: https://forensics.wiki/windows#cryptnet-url-cache
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\config\\systemprofile\\AppData\\LocalLow\\Microsoft\\CryptnetUrlCache\\Content\\*",
                    "%%environ_systemroot%%\\SysWOW64\\config\\systemprofile\\AppData\\LocalLow\\Microsoft\\CryptnetUrlCache\\Content\\*",
                    "%%users.userprofile%%\\AppData\\LocalLow\\Microsoft\\CryptnetUrlCache\\Content\\*",
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


class WindowsCurrentVersion(GRRArtifactBase):
    """
    The Windows current version

    Reference URLs:
    https://github.com/libyal/winreg-kb/blob/main/documentation/System%20keys.asciidoc
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion",
                        "value": "CurrentVersion",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsDebugger(GRRArtifactBase):
    """
    Windows Debugger peristence or AV disable.

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/a329t4ed%28VS.71%29.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\*",
                        "value": "Debugger",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\*",
                        "value": "Debugger",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\*",
                        "value": "Debugger",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\*",
                        "value": "Debugger",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsDNSSettings(GRRArtifactBase):
    """
    Windows Registry Keys that contain DNS and DHCP settings.

    Reference URLs:
    https://technet.microsoft.com/en-us/library/dd197418(v=ws.10).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\Tcpip\\Parameters",
                        "value": "NameServer",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\Interfaces\\*",
                        "value": "NameServer",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Dnscache\\Parameters",
                        "value": "NameServer",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\services\\Tcpip\\Parameters\\Interfaces\\*",
                        "value": "DhcpNameServer",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\services\\Tcpip\\Parameters\\Interfaces\\*",
                        "value": "DhcpServer",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsDomainCachedCredentials(GRRArtifactBase):
    """
    Windows domain cached credentials

    Reference URLs: http://juggernaut.wikidot.com/cached-credentials
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {"key": "HKEY_LOCAL_MACHINE\\Security\\Cache", "value": "NL$*"}
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsDomainName(GRRArtifactBase):
    """
    The domain the system is connected to.
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\Tcpip\\Parameters",
                        "value": "Domain",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsDisallowedSystemCertificates(GRRArtifactBase):
    """
    Windows Disallowed System Certificates

    Malware can add code-signing certificates associated with antivirus programs
    to the disallowed list to prevent the AV programs from running.

    Reference URLs:
    https://blog.malwarebytes.com/detections/pum-optional-misplacedcertificate/
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\SystemCertificates\\Disallowed\\Certificates\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Policies\\Microsoft\\SystemCertificates\\Disallowed\\Certificates\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Policies\\Microsoft\\SystemCertificates\\Disallowed\\Certificates\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Policies\\Microsoft\\SystemCertificates\\Disallowed\\Certificates\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsEnvironmentUserLoginScripts(GRRArtifactBase):
    """
    User login scripts configured via Windows environment variables.

    Reference URLs:
    http://www.hexacorn.com/blog/2014/11/14/beyond-good-ol-run-key-part-18/
    https://social.msdn.microsoft.com/Forums/windowsdesktop/en-US/cb6f1d6f-60a6-4369-803e-ec03d902e638/gina-how-to-run-domain-scripts-after-logon
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Environment",
                        "value": "UserInitLogonServer",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Environment",
                        "value": "UserInitLogonScript",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Environment",
                        "value": "UserInitMprLogonScript",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsEnvironmentVariableAllUsersProfile(GRRArtifactBase):
    """
    The system-wide %AllUsersProfile% environment variable contains the path of
    the of the "All Users" or "Common" profile directory.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList",
                        "value": "AllUsersProfile",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsEnvironmentVariableAppxProcess(GRRArtifactBase):
    """
    The user-specific %APPX_PROCESS% environment variable is used for .NET
    applications.

    If set, a .NET applications will attempt to load WinAppXRT.dll from %PATH%,
    which can be used as a persistence mechanism by malware.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Environment",
                        "value": "APPX_PROCESS",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsEnvironmentVariableCommonProgramFiles(GRRArtifactBase):
    """
    The %COMMONPROGRAMFILES% environment variable contains the path of the
    common program files folder.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion",
                        "value": "CommonFilesDir",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsEnvironmentVariableCommonProgramFilesX86(GRRArtifactBase):
    """
    The %COMMONPROGRAMFILES(X86)% environment variable contains the path of the
    32-bit common program files folder on a 64-bit Windows installation.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion",
                        "value": "CommonFilesDir (x86)",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsEnvironmentVariableComSpec(GRRArtifactBase):
    """
    The %ComSpec% environment variable contains the path of the command
    processor, typically "cmd.exe".

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment",
                        "value": "ComSpec",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsEnvironmentVariableDriverData(GRRArtifactBase):
    """
    The %DriverData% environment variable contains the path of the directory
    used for temporary state files of user-mode drivers.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Environment",
                        "value": "DriverData",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsEnvironmentVariablePath(GRRArtifactBase):
    """
    The %PATH% environment variable contains an ordered list of paths of
    directories that will be searched on execution request without a specific
    path.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\Environment",
                        "value": "Path",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = ["WinPathEnvironmentVariable"]


class WindowsEnvironmentVariableProfilesDirectory(GRRArtifactBase):
    """
    The %ProfilesDirectory% environment variable contain a path of a directory
    that contains the users' profile directories, typically
    "%SystemDrive%/Users".

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList",
                        "value": "ProfilesDirectory",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsEnvironmentVariableProgramData(GRRArtifactBase):
    """
    The %ProgramData% environment variable contains a path of the "Program Data"
    directory.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList",
                        "value": "ProgramData",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsEnvironmentVariableProgramFiles(GRRArtifactBase):
    """
    The %ProgramFiles% environment variable contains a path of the "Program
    Files" directory.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "PATH",
            "attributes": {"paths": ["\\Program Files"], "separator": "\\"},
        },
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion",
                        "value": "ProgramFilesDir",
                    }
                ]
            },
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = ["ProgramFiles"]


class WindowsEnvironmentVariableProgramFilesX86(GRRArtifactBase):
    """
    The %ProgramFiles(x86)% environment variable contains a path of the 32-bit
    "Program Files" directory on a 64-bit Windows installation.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "PATH",
            "attributes": {"paths": ["\\Program Files (x86)"], "separator": "\\"},
        },
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion",
                        "value": "ProgramFilesDir (x86)",
                    }
                ]
            },
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = ["ProgramFilesx86"]


class WindowsEnvironmentVariableSystemRoot(GRRArtifactBase):
    """
    The %SystemRoot%, environment variable contains the path of the system
    directory, typically "C:/Windows".

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "PATH",
            "attributes": {
                "paths": ["\\Windows", "\\WinNT", "\\WINNT35", "\\WTSRV"],
                "separator": "\\",
            },
        },
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion",
                        "value": "SystemRoot",
                    }
                ]
            },
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = ["SystemRoot"]


class WindowsEnvironmentVariableTemp(GRRArtifactBase):
    """
    The %TEMP% environment variable.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\Environment",
                        "value": "TEMP",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = ["TempEnvironmentVariable"]


class WindowsEnvironmentVariableWinDir(GRRArtifactBase):
    """
    The %WinDir%, environment variable contains the path of the Windows
    directory, typically "C:/Windows".

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "PATH",
            "attributes": {
                "paths": ["\\Windows", "\\WinNT", "\\WINNT35", "\\WTSRV"],
                "separator": "\\",
            },
        },
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\Environment",
                        "value": "windir",
                    }
                ]
            },
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = ["WinDirEnvironmentVariable"]


class WindowsEventLogApplication(GRRArtifactBase):
    """
    Application Windows Event Log.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EventLog.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_systemroot%%\\System32\\config\\AppEvent.evt"],
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


class WindowsEventLogPublishers(GRRArtifactBase):
    """
    Windows EventLog publishers (or providers) Registry keys.

    Reference URLs:
    https://winreg-kb.readthedocs.io/en/latest/sources/EventLog-keys.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\WINEVT\\Publishers\\*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsEventLogs(GRRArtifactBase):
    """
    Windows Event logs.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EventLog.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\config\\*.evt",
                    "%%environ_systemroot%%\\System32\\winevt\\Logs\\*.evtx",
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


class WindowsEventLogSecurity(GRRArtifactBase):
    """
    Security Windows Event Log.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EventLog.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_systemroot%%\\System32\\config\\SecEvent.evt"],
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


class WindowsEventLogSources(GRRArtifactBase):
    """
    Windows EventLog sources Registry keys.

    Reference URLs:
    https://winreg-kb.readthedocs.io/en/latest/sources/EventLog-keys.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\EventLog\\*\\*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = ["WindowsEventLogProviders"]


class WindowsEventLogSystem(GRRArtifactBase):
    """
    System Windows Event Log.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EventLog.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_systemroot%%\\System32\\config\\SysEvent.evt"],
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


class WindowsEventTracingLogFiles(GRRArtifactBase):
    """
    Event Tracing for Windows (ETW) log files.

    Reference URLs: https://forensics.wiki/event_tracing_for_windows_(etw)
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersappdata%%\\Microsoft\\Diagnosis\\ETLLogs\\ShutdownLogger\\*.etl",
                    "%%environ_allusersappdata%%\\Microsoft\\DiagnosticLogCSP\\Collectors\\*.etl",
                    "%%environ_allusersappdata%%\\Microsoft\\Windows\\wfp\\*.etl",
                    "%%environ_allusersappdata%%\\Microsoft\\Windows Security Health\\Logs\\*.etl",
                    "%%environ_allusersappdata%%\\USOShared\\Logs\\System\\*.etl",
                    "%%users.localappdata%%\\Microsoft\\OneDrive\\logs\\Personal\\*.etl",
                    "%%users.localappdata%%\\Microsoft\\Windows\\Explorer\\*.etl",
                    "%%users.localappdata%%\\Packages\\Microsoft.Windows.Photos_*\\LocalState\\*.etl",
                    "%%environ_systemroot%%\\Logs\\*\\*.etl",
                    "%%environ_systemroot%%\\Panther\\*.etl",
                    "%%environ_systemroot%%\\Security\\Logs\\*.etl",
                    "%%environ_systemroot%%\\ServiceProfiles\\NetworkService\\AppData\\Local\\Microsoft\\Windows\\DeliveryOptimization\\Logs\\*.etl",
                    "%%environ_systemroot%%\\System32\\LogFiles\\WMI\\*.etl",
                    "%%environ_systemroot%%\\System32\\LogFiles\\WMI\\*.etl.0*",
                    "%%environ_systemroot%%\\System32\\LogFiles\\WMI\\RtBackup\\*.etl",
                    "%%environ_systemroot%%\\System32\\SleepStudy\\*.etl",
                    "%%environ_systemroot%%\\System32\\SleepStudy\\ScreenOn\\*.etl",
                    "%%environ_systemroot%%\\System32\\WDI\\LogFiles\\*.etl",
                    "%%environ_systemroot%%\\System32\\WDI\\LogFiles\\*.etl.0*",
                    "%%environ_systemroot%%\\System32\\WDI\\{86432a0b-3c7d-4ddf-a89c-172faa90485d}\\*\\*.etl",
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


class WindowsExcludeFromKnownDLLs(GRRArtifactBase):
    """
    ExcludeFromKnownDLLs can be used to bypass search order hijacking
    protection.

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms682586%28v=vs.85%29.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager",
                        "value": "ExcludeFromKnownDLLs",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsExplorerAppKey(GRRArtifactBase):
    """
    Handlers for special keys on some keyboards (file path or CLSID).

    Reference URLs:
    http://answers.microsoft.com/en-us/windows/forum/windows_vista-hardware/assigning-the-special-keys-at-the-top-of-the/d1ab2e13-5297-457d-a8e8-bc2c883d8b58?db=5
    http://h30434.www3.hp.com/t5/Notebook-Hardware/How-do-I-customize-the-Action-Keys/td-p/379207
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\AppKey\\*",
                        "value": "ShellExecute",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsExplorerAutoplayHandlers(GRRArtifactBase):
    """
    Handlers for autoplay events in Windows Explorer.

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    https://msdn.microsoft.com/en-us/library/windows/desktop/aa468474.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\AutoplayHandlers\\Handlers\\*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsExplorerContextMenuHandlers(GRRArtifactBase):
    """
    Handlers for subcommands on context menu

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/hh127467(v=vs.85).aspx
    https://msdn.microsoft.com/en-us/library/windows/desktop/cc144171(v=vs.85).aspx
    http://www.windowrdb.com/w.php?w=hklm-software-microsoft-windows-currentversion-explorer-commandstore-shell-windows-closewindow
    http://www.checkfilename.com/view-details/Windows-7-Ultimate/RespageIndex/4/sTab/2/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommandStore\\shell\\*",
                        "value": "CommandStateHandler",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommandStore\\shell\\*",
                        "value": "ExplorerCommandHandler",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommandStore\\shell\\*",
                        "value": "command",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommandStore\\shell\\*\\command",
                        "value": "DelegateExecute",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsExplorerNamespaceCommonPlaces(GRRArtifactBase):
    """
    CLSIDs listed here are used to populate the Common Places items.

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/hh127450(v=vs.85).aspx
    http://www.geoffchappell.com/studies/windows/shell/shell32/classes/commonplacesfolder.htm
    http://www.windowrdb.com/w.php?w=hklm-software-microsoft-windows-currentversion-explorer-commonplaces
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommonPlaces\\NameSpace",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommonPlaces\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommonPlaces\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommonPlaces\\NameSpace",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommonPlaces\\NameSpace\\DelegateFolders",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommonPlaces\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommonPlaces\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\CommonPlaces\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\CommonPlaces\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\CommonPlaces\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\CommonPlaces\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\CommonPlaces\\NameSpace\\DelegateFolders",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsExplorerNamespaceControlPanel(GRRArtifactBase):
    """
    CLSIDs listed here are used to populate the Control Panel items.

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/hh127450(v=vs.85).aspx
    http://www.geoffchappell.com/studies/windows/shell/shell32/classes/controlpanel.htm
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ControlPanel\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ControlPanel\\NameSpace",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ControlPanel\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ControlPanel\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\ControlPanel\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\ControlPanel\\NameSpace\\DelegateFolders",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ControlPanelWOW64\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ControlPanelWOW64\\NameSpace",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ControlPanel\\NameSpaceWOW64\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ControlPanelWOW64\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\ControlPanelWOW64\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\ControlPanelWOW64\\NameSpace\\DelegateFolders",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ControlPanel\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ControlPanel\\NameSpace",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ControlPanel\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ControlPanel\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\ControlPanel\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\ControlPanel\\NameSpace\\DelegateFolders",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ControlPanelWOW64\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Wow6432Node\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\ControlPanelWOW64\\NameSpace\\DelegateFolders",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsExplorerNamespaceDesktop(GRRArtifactBase):
    """
    CLSIDs listed here are used to populate the Desktop items.

    Reference URLs:
    https://social.technet.microsoft.com/Forums/windowsserver/en-US/2760309c-89d1-414c-a04c-ce4178e90787/hide-libraries-icon-from-desktop
    http://www.geoffchappell.com/studies/windows/shell/shell32/classes/regfolder.htm
    http://www.geoffchappell.com/notes/windows/shell/controlpanel/desktopicons.htm
    https://support.microsoft.com/en-us/kb/321777
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Desktop\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Desktop\\NameSpace",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Desktop\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Desktop\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\Desktop\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\Desktop\\NameSpace\\DelegateFolders",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Desktop\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Desktop\\NameSpace",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Wow6432Node\\Windows\\CurrentVersion\\Explorer\\Desktop\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Desktop\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\Desktop\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\Desktop\\NameSpace\\DelegateFolders",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsExplorerNamespaceMyComputer(GRRArtifactBase):
    """
    CLSIDs listed here are used to populate the MyComputer items.

    Reference URLs:
    http://www.geoffchappell.com/studies/windows/shell/shell32/classes/mycomputer.htm
    http://www.howtogeek.com/168081/how-to-remove-the-folders-from-my-computer-in-windows-8.1/
    http://answers.microsoft.com/en-us/windows/forum/windows8_1-files/how-to-remove-these-folders-from-windows-81/777c4ba3-7853-453e-bfa0-9a0f4245b9e1?db=5
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\MyComputer\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\MyComputer\\NameSpace\\DelegateFolders",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Wow6432Node\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\MyComputer\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\MyComputer\\NameSpace\\DelegateFolders",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsExplorerNamespaceNetworkNeighborhood(GRRArtifactBase):
    """
    CLSIDs listed here are used to populate the Network Neighborhood items.

    Reference URLs:
    http://www.geoffchappell.com/studies/windows/shell/shell32/classes/regfolder.htm
    http://www.lavasoft.com/mylavasoft/rogues/secretservice
    http://www.wikihow.com/Manually-Remove-Macatte-Malware
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\NetworkNeighborhood\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\NetworkNeighborhood\\NameSpace",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\NetworkNeighborhood\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\NetworkNeighborhood\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\NetworkNeighborhood\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\NetworkNeighborhood\\NameSpace\\DelegateFolders",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\NetworkNeighborhood\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\NetworkNeighborhood\\NameSpace",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\NetworkNeighborhood\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\NetworkNeighborhood\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\NetworkNeighborhood\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\NetworkNeighborhood\\NameSpace\\DelegateFolders",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsExplorerNamespacePrintersAndFaxes(GRRArtifactBase):
    """
    CLSIDs listed here are used to populate the Printer and Fax items.

    Reference URLs:
    http://www.geoffchappell.com/studies/windows/shell/shell32/classes/printers.htm
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\PrintersAndFaxes\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\PrintersAndFaxes\\NameSpace",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\PrintersAndFaxes\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\PrintersAndFaxes\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\PrintersAndFaxes\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\PrintersAndFaxes\\NameSpace\\DelegateFolders",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\PrintersAndFaxes\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\PrintersAndFaxes\\NameSpace",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\PrintersAndFaxes\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\PrintersAndFaxes\\NameSpace\\DelegateFolders",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\PrintersAndFaxes\\NameSpace",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SessionInfo\\*\\PrintersAndFaxes\\NameSpace\\DelegateFolders",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsExplorerSettings(GRRArtifactBase):
    """
    Windows Explorer Settings

    Malware can modify these keys to make it more difficult for the user to
    detect and remove malicious software.

    Reference URLs:
    https://www.sdkhere.com/2016/02/analysis-of-malware-using-wmi-query.html
    https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/troj_mandrom.e
    https://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/troj_deleter.ah
    https://blog.malwarebytes.com/detections/pum-optional-disabledrightclick/
    https://blog.malwarebytes.com/detections/pum-optional-disableshowcontrolpanel/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "Hidden",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "Hidden",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "Hidden",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "Hidden",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "HideFileExt",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "HideFileExt",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "HideFileExt",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "HideFileExt",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "ShowSuperHidden",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "ShowSuperHidden",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "ShowSuperHidden",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "ShowSuperHidden",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "HideSCAHealth",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "HideSCAHealth",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "HideSCAHealth",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "HideSCAHealth",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoControlPanel",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoControlPanel",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoControlPanel",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoControlPanel",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoFolderOptions",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoFolderOptions",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoFolderOptions",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoFolderOptions",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoRun",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoRun",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoRun",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoRun",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoViewContextMenu",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoViewContextMenu",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoViewContextMenu",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "NoViewContextMenu",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "ShowControlPanel",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "ShowControlPanel",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "ShowControlPanel",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced",
                        "value": "ShowControlPanel",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "TaskbarNoNotification",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "TaskbarNoNotification",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "TaskbarNoNotification",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer",
                        "value": "TaskbarNoNotification",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsFileTypeAutorunAssociations(GRRArtifactBase):
    """
    Registry value for what application class identifier (CLSID) to launch for a
    file extension.

    Extension subkeys start with a dot. The '(Default)' value will be a ProgID,
    which points to another entry in HKCR specifying the command to run to open
    a file of the given type. The WindowsShellOpenCommand artifact is associated
    with these ProgID command invocations.

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms678415(v=vs.85).aspx
    https://docs.microsoft.com/en-us/windows/desktop/shell/fa-file-types
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {"key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\.*", "value": ""},
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\.*",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\.*",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\.*",
                        "value": "",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsFirewallLogFile(GRRArtifactBase):
    """
    Windows Firewall default logfile

    Reference URLs:
    https://docs.microsoft.com/en-us/windows/access-protection/windows-firewall/configure-the-windows-firewall-log
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\logfiles\\firewall\\pfirewall.log"
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


class WindowsFirewallEnabledRules(GRRArtifactBase):
    """
    Command to list the enabled Windows Firewall rules.
    """

    SOURCES = [
        {
            "type": "COMMAND",
            "attributes": {
                "args": [
                    "advfirewall",
                    "monitor",
                    "show",
                    "firewall",
                    "rule",
                    "name=all",
                ],
                "cmd": "netsh.exe",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsFirewallRules(GRRArtifactBase):
    """
    Command to list the configured Windows Firewall rules.
    """

    SOURCES = [
        {
            "type": "COMMAND",
            "attributes": {
                "args": ["advfirewall", "firewall", "show", "rule", "name=all"],
                "cmd": "netsh.exe",
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsGroupPolicyScripts(GRRArtifactBase):
    """
    Windows group policy scripts
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\GroupPolicy\\User\\Scripts\\psscripts.ini",
                    "%%environ_systemroot%%\\System32\\GroupPolicy\\User\\Scripts\\scripts.ini",
                    "%%environ_systemroot%%\\System32\\GroupPolicy\\User\\Scripts\\Logoff\\*",
                    "%%environ_systemroot%%\\System32\\GroupPolicy\\User\\Scripts\\Logon\\*",
                    "%%environ_systemroot%%\\System32\\GroupPolicy\\Machine\\Scripts\\psscripts.ini",
                    "%%environ_systemroot%%\\System32\\GroupPolicy\\Machine\\Scripts\\scripts.ini",
                    "%%environ_systemroot%%\\System32\\GroupPolicy\\Machine\\Scripts\\Shutdown\\*",
                    "%%environ_systemroot%%\\System32\\GroupPolicy\\Machine\\Scripts\\Startup\\*",
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


class WindowsFirewallAuthorizedApplications(GRRArtifactBase):
    """
    Windows Firewall Authorized Applications

    Malware can add paths to this list to more easily communicate over the
    network on an infected machine. For instance, Emotet modifies some these
    settings after gaining execution.

    Reference URLs:
    https://threatvector.cylance.com/en_us/home/threat-spotlight-eyepyramid-malware.html
    https://blog.talosintelligence.com/2019/05/threat-roundup-0524-0531.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\WindowsFirewall\\DomainProfile\\AuthorizedApplications\\List\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\WindowsFirewall\\StandardProfile\\AuthorizedApplications\\List\\*",
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\DomainProfile\\AuthorizedApplications\\List\\*",
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\PublicProfile\\AuthorizedApplications\\List\\*",
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile\\AuthorizedApplications\\List\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsFirewallGloballyOpenPorts(GRRArtifactBase):
    """
    Windows Firewall Globally Open Ports

    Malware can add to the list of open ports to avoid having to create Windows
    Firewall exceptions tied to specific applications.

    Reference URLs:
    https://qaforce.wordpress.com/2009/10/06/windows-firewall-registry-keys/
    https://github.com/steeve85/Malwares/wiki/Registry
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\WindowsFirewall\\DomainProfile\\GloballyOpenPorts\\List\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\WindowsFirewall\\StandardProfile\\GloballyOpenPorts\\List\\*",
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\DomainProfile\\GloballyOpenPorts\\List\\*",
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\PublicProfile\\GloballyOpenPorts\\List\\*",
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile\\GloballyOpenPorts\\List\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsFirewallPolicySettings(GRRArtifactBase):
    """
    Windows Firewall Policy Settings

    Malware can modify these settings to more easily communicate over the
    network on an infected machine. For instance, Emotet modifies some these
    settings after gaining execution.

    Reference URLs:
    https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/networking-mpssvc-svc-privateprofile-enablefirewall
    https://docs.microsoft.com/en-us/windows-hardware/customize/desktop/unattend/networking-mpssvc-svc-privateprofile-disablenotifications
    https://blog.talosintelligence.com/2019/05/threat-roundup-0503-0510.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\DomainProfile",
                        "value": "EnableFirewall",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\DomainProfile",
                        "value": "DisableNotifications",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\DomainProfile",
                        "value": "DoNotAllowExceptions",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\DomainProfile",
                        "value": "DefaultInboundAction",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\DomainProfile",
                        "value": "DefaultOutboundAction",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\PublicProfile",
                        "value": "EnableFirewall",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\PublicProfile",
                        "value": "DisableNotifications",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\PublicProfile",
                        "value": "DoNotAllowExceptions",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\PublicProfile",
                        "value": "DefaultInboundAction",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\PublicProfile",
                        "value": "DefaultOutboundAction",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile",
                        "value": "EnableFirewall",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile",
                        "value": "DisableNotifications",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile",
                        "value": "DoNotAllowExceptions",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile",
                        "value": "DefaultInboundAction",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\StandardProfile",
                        "value": "DefaultOutboundAction",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsFontDrivers(GRRArtifactBase):
    """
    Windows font drivers from the Registry.

    Reference URLs:
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Font Drivers\\*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsHelpCenterDatabaseFile(GRRArtifactBase):
    """
    Windows Help Center database file (HCdata.edb).
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\PCHEALTH\\HELPCTR\\Database\\HCdata.edb"
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


class WindowsHostsFiles(GRRArtifactBase):
    """
    The Windows hosts and lmhosts file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\Drivers\\etc\\Lmhosts",
                    "%%environ_systemroot%%\\System32\\Drivers\\etc\\hosts",
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


class WindowsHotkeyReplacement(GRRArtifactBase):
    """
    Hotkey executable replacement.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\magnifier.exe",
                    "%%environ_systemroot%%\\System32\\sethc.exe",
                    "%%environ_systemroot%%\\System32\\utilman.exe",
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


class WindowsInstallationDateTime(GRRArtifactBase):
    """
    Windows installation date and time
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion",
                        "value": "InstallDate",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsLanguage(GRRArtifactBase):
    """
    The system language.

    Reference URLs:
    https://winreg-kb.readthedocs.io/en/latest/sources/system-keys/Language.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Nls\\Language",
                        "value": "Default",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsLogoffScript(GRRArtifactBase):
    """
    Windows policy logoff script

    Reference URLs: https://technet.microsoft.com/en-us/library/ff404236.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Policies\\Microsoft\\Windows\\System\\Scripts",
                        "value": "Logoff",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\System\\Scripts",
                        "value": "Logoff",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsLogonScript(GRRArtifactBase):
    """
    Windows policy logon script

    Reference URLs: https://technet.microsoft.com/en-us/library/ff404236.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Policies\\Microsoft\\Windows\\System\\Scripts",
                        "value": "Logon",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\System\\Scripts",
                        "value": "Logon",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsLSAAuthenticationPackages(GRRArtifactBase):
    """
    Authentication Packages can be injected into LSASS.

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    https://technet.microsoft.com/en-us/library/cc963218.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Lsa",
                        "value": "Authentication Packages",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\OSConfig",
                        "value": "Authentication Packages",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsLSANotificationPackages(GRRArtifactBase):
    """
    Notification Packages can be injected into LSASS.

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    https://technet.microsoft.com/en-us/library/cc963221.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Lsa",
                        "value": "Notification Packages",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\OSConfig",
                        "value": "Notification Packages",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsLSASecurityPackages(GRRArtifactBase):
    """
    Security Packages can be injected into LSASS.

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/aa379392(v=vs.85).aspx
    https://dl.mandiant.com/EE/library/MIRcon2014/MIRcon_2014_IR_Track_Analysis_of_Malicious_SSP.pdf
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Lsa",
                        "value": "Security Packages",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Lsa\\OSConfig",
                        "value": "Security Packages",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsMapNetworkDriveMRU(GRRArtifactBase):
    """
    Recently mapped network shares.
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Map Network Drive MRU"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsMetroApplicationCache(GRRArtifactBase):
    """
    Windows Metro application cache.

    Reference URLs:
    http://www.forensicmag.com/article/2012/09/microsoft-windows-8-forensic-first-look
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.localappdata%%\\Packages\\*\\AC\\INetCache"],
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


class WindowsMetroApplicationCookies(GRRArtifactBase):
    """
    Windows Metro application cookies.

    Reference URLs:
    http://www.forensicmag.com/article/2012/09/microsoft-windows-8-forensic-first-look
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.localappdata%%\\Packages\\*\\AC\\INetCookies"],
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


class WindowsMetroApplicationHistory(GRRArtifactBase):
    """
    Windows Metro application history.

    Reference URLs:
    http://www.forensicmag.com/article/2012/09/microsoft-windows-8-forensic-first-look
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.localappdata%%\\Packages\\*\\AC\\INetHistory"],
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


class WindowsMetroUserPinnedFavoriteTiles(GRRArtifactBase):
    """
    Windows Metro user-pinned favorite tiles.

    Reference URLs:
    http://www.forensicmag.com/article/2012/09/microsoft-windows-8-forensic-first-look
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.localappdata%%\\Microsoft\\Windows\\RoamingTiles"],
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


class WindowsMostRecentApplication(GRRArtifactBase):
    """
    Windows Most Recent Application name key

    Reference URLs:
    http://www.trendmicro.com/vinfo/us/threat-encyclopedia/malware/troj_ransom.smc7
    https://www.symantec.com/security_response/writeup.jsp?docid=2014-092314-3644-99&tabid=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\*\\MostRecentApplication",
                        "value": "Name",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\*\\MostRecentApplication",
                        "value": "Name",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsMountedDevices(GRRArtifactBase):
    """
    Windows mounted devices

    Reference URLs:
    https://winreg-kb.readthedocs.io/en/latest/sources/system-keys/Mounted-devices.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {"keys": ["HKEY_LOCAL_MACHINE\\System\\MountedDevices"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsMSDTCDLLs(GRRArtifactBase):
    """
    Windows MSDTC attempts to load these DLLs on start

    Reference URLs:
    https://www.mandiant.com/blog/hikit-rootkit-advanced-persistent-attack-techniques-part-1-2/
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\MSDTC\\MTxOCI\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\MSDTC\\MTxOCI\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsMultiMediaDrivers(GRRArtifactBase):
    """
    Configured drivers for different multimedia filetypes.

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    https://support.microsoft.com/en-us/kb/126054
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\*",
                    "HKEY_USERS\\%%users.sid%%\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\*",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\*",
                    "HKEY_USERS\\%%users.sid%%\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Drivers32\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsNetworkShellHelpers(GRRArtifactBase):
    """
    Windows Network Shell (netsh) helpers are loaded on boot

    Reference URLs: https://support.microsoft.com/en-us/kb/242468
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Netsh",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Netsh",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsOpenSaveMRU(GRRArtifactBase):
    """
    Information about files opened or saved in a Windows shell dialog.

    Reference URLs: https://forensics.wiki/opensavemru
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ComDIg32\\OpenSaveMRU\\*\\*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsOpenSavePidlMRU(GRRArtifactBase):
    """
    Information about files opened or saved in a Windows shell dialog.

    Reference URLs: https://forensics.wiki/opensavepidlmru
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ComDlg32\\OpenSavePidlMRU\\*\\*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsPendingFileRenames(GRRArtifactBase):
    """
    Windows Pending file renames on reboot

    Reference URLs: https://technet.microsoft.com/en-us/library/cc960241.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager",
                        "value": "PendingFileRenameOperations",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsPendingGPOs(GRRArtifactBase):
    """
    Windows Pending GPOs registry settings.

    This is a persistence mechanism known to be used by the Gootkit malware
    family.

    Reference URLs: https://www.certego.net/en/news/malware-tales-gootkit/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\IEAK\\GroupPolicy\\PendingGPOs",
                        "value": "Path1",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\IEAK\\GroupPolicy\\PendingGPOs",
                        "value": "Path1",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsServices(GRRArtifactBase):
    """
    Windows service and driver configurations.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/ServicesAndDrivers.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": ["HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\*"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsPowerShellDefaultProfiles(GRRArtifactBase):
    """
    Default PowerShell Profile files. These files are executed by default when
    PowerShell starts up.

    Reference URLs:
    https://technet.microsoft.com/en-us/magazine/2008.10.windowspowershell.aspx#id0190010
    http://www.hexacorn.com/blog/2014/08/27/beyond-good-ol-run-key-part-16/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\system32\\WindowsPowerShell\\v1.0\\profile.ps1",
                    "%%environ_systemroot%%\\system32\\WindowsPowerShell\\v1.0\\Microsoft.PowerShell_profile.ps1",
                    "%%users.userprofile%%\\Documents\\WindowsPowerShell\\profile.ps1",
                    "%%users.userprofile%%\\Documents\\WindowsPowerShell\\Microsoft.PowerShell_profile.ps1",
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


class WindowsPLAPProviders(GRRArtifactBase):
    """
    Windows Pre-Logon Access Provider (PLAP) Providers

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/bb530584(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Authentication\\PLAP Providers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Authentication\\PLAP Providers\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsPrintMonitors(GRRArtifactBase):
    """
    Windows Print Monitor DLL config.

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    https://support.microsoft.com/en-us/kb/102966
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Print\\Monitors\\*",
                        "value": "Driver",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsShellExecuteHooks(GRRArtifactBase):
    """
    Shell execution hooks are called when ShellExecuteEx() is called.

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    http://regenerus.com/malware-common-loadpoints/
    https://code.google.com/p/regripper/wiki/ASEPs
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellExecuteHooks\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellExecuteHooks\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSessionManagerBootExecute(GRRArtifactBase):
    """
    Windows Session Manager BootExecute persistence.

    Reference URLs: https://technet.microsoft.com/en-us/library/cc963230.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager",
                        "value": "BootExecute",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsTerminalServerRunKeys(GRRArtifactBase):
    """
    Windows Terminal Server Run keys

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Runonce\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\RunonceEx\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Runonce\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\RunonceEx\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Runonce\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\RunonceEx\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Runonce\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\RunonceEx\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Terminal Server\\Install\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsWinlogonAppSetup(GRRArtifactBase):
    """
    Windows Winlogon Appsetup

    Reference URLs: https://technet.microsoft.com/en-us/library/cc939701.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "AppSetup",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSessionManagerSubSystems(GRRArtifactBase):
    """
    Windows Session Manager SubSystems persistence

    Reference URLs: https://technet.microsoft.com/en-us/library/cc976130.aspx
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\SubSystems",
                        "value": "Windows",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsRunKeys(GRRArtifactBase):
    """
    Windows Run and RunOnce keys.

    Note users.sid will currently only expand to SIDs with profiles on the
    system, not all SIDs.

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/aa376977%28v=vs.85%29.aspx
    https://support.microsoft.com/en-us/kb/137367
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    https://technet.microsoft.com/en-us/magazine/ee851671.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\Setup\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\Setup\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Run\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\Setup\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\Run\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnce\\Setup\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunOnceEx\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WinSock2NamespaceProviders(GRRArtifactBase):
    """
    Used to provide name-resolution services through WinSock2

    Reference URLs:
    https://www.symantec.com/security_response/writeup.jsp?docid=2012-020609-4221-99&tabid=2
    http://www.nirsoft.net/utils/winsock_service_providers.html
    https://msdn.microsoft.com/en-us/library/windows/desktop/ms739923(v=vs.85).aspx
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\WinSock2\\Parameters\\NameSpace_Catalog5\\Catalog_Entries\\*",
                        "value": "LibraryPath",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\WinSock2\\Parameters\\NameSpace_Catalog5\\Catalog_Entries64\\*",
                        "value": "LibraryPath",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsWinlogonNotify(GRRArtifactBase):
    """
    Windows Winlogon Notify DLL names.

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/aa379402(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Notify\\*",
                        "value": "DLLName",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\Notify\\*",
                        "value": "DLLName",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsStubPaths(GRRArtifactBase):
    """
    Windows StubPath persistence.

    Each time a user logs in, the Active Setup Installed Components in HKLM are
    compared ot the ones in HKCU, and if any are missing, or if the associated
    version is less, the program is executed.

    Reference URLs:
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    http://bonemanblog.blogspot.com/2004/12/active-setup-registry-keys-and-their.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Active Setup\\Installed Components\\*",
                        "value": "StubPath",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Active Setup\\Installed Components\\*",
                        "value": "Version",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Active Setup\\Installed Components\\*",
                        "value": "StubPath",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Active Setup\\Installed Components\\*",
                        "value": "Version",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Active Setup\\Installed Components\\*",
                        "value": "StubPath",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Active Setup\\Installed Components\\*",
                        "value": "Version",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Active Setup\\Installed Components\\*",
                        "value": "StubPath",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Active Setup\\Installed Components\\*",
                        "value": "Version",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsShellRunasCommand(GRRArtifactBase):
    """
    Executed every time an executable or script file type is run as
    administrator.

    For most file types, the value should be '"%1" %*' or something similar.
    Example file type subkeys include 'exefile', 'batfile', and 'cmdfile'. These
    keys can be modified by malware as a way to be periodically executed or to
    bypass UAC.

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    https://enigma0x3.net/2017/03/17/fileless-uac-bypass-using-sdclt-exe/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\*\\shell\\runas\\command",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\*\\shell\\runas\\command",
                        "value": "IsolatedCommand",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\*\\shell\\runas\\command",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\*\\shell\\runas\\command",
                        "value": "IsolatedCommand",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\*\\shell\\runas\\command",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\*\\shell\\runas\\command",
                        "value": "IsolatedCommand",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\*\\shell\\runas\\command",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\*\\shell\\runas\\command",
                        "value": "IsolatedCommand",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsWinlogonSystem(GRRArtifactBase):
    """
    Applications launched by Winlogon in the system context during the system
    initialisation.

    Reference URLs: https://code.google.com/p/regripper/wiki/ASEPs
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    http://regenerus.com/malware-common-loadpoints/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "System",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "System",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSearchFilterHandlers(GRRArtifactBase):
    """
    Windows Search filter handlers configured for file types and applications.

    Windows Search loads DLLs that implement the IFilter interface in order to
    scan files for text and extract certain types of information. Malware can
    replace the filter handler for a given file type or CLSID with itself to
    gain execution when a search operation is performed on that file. Search
    operations can be performed indirectly in a number of cases; for instance,
    the .txt, .html, and .rtf filter handlers are invoked when indexing email
    message bodies.

    The filter handler to use is specified indirectly via a persistent handler.
    The persistent handler GUID is indicated via the PersistentHandler subkey
    for a file type or application GUID. The filter handler CLSID is indicated
    via the PersistentAddinsRegistered/{89BCB740-6119-101A-BCB7-00DD010655AF}
    subkey under the persistent handler GUID key path. This artifact inspects
    both of these paths.

    NOTE: Only the HKEY_LOCAL_MACHINE root key needs be checked, because these
    are the only keys used. SearchFilterHost.exe runs under the SYSTEM account,
    which does not have access to HKEY_CURRENT_USER.

    Reference URLs:
    https://docs.microsoft.com/en-us/windows/desktop/search/-search-ifilter-about
    https://docs.microsoft.com/en-us/windows/desktop/search/-search-ifilter-implementations
    https://docs.microsoft.com/en-us/windows/desktop/search/-search-ifilter-registering-filters
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\*\\PersistentHandler",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\*\\PersistentHandler",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\CLSID\\*\\PersistentHandler",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\CLSID\\*\\PersistentHandler",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\CLSID\\*\\PersistentAddinsRegistered\\{89BCB740-6119-101A-BCB7-00DD010655AF}",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\CLSID\\*\\PersistentAddinsRegistered\\{89BCB740-6119-101A-BCB7-00DD010655AF}",
                        "value": "",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsRunServices(GRRArtifactBase):
    """
    Windows Run Services.

    Reference URLs: https://support.microsoft.com/en-us/kb/179365
    https://threatvector.cylance.com/en_us/home/windows-registry-persistence-part-2-the-run-keys-and-search-order.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\RunServicesOnce\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\RunServices\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunServicesOnce\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunServices\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\RunServicesOnce\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\RunServices\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunServicesOnce\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\RunServices\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsServiceControlManagerExtension(GRRArtifactBase):
    """
    Windows service control manager extension

    Reference URLs:
    http://forum.sysinternals.com/autoruns-and-windows-7_topic19770.html
    https://support.microsoft.com/en-us/kb/102985
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    http://www.silentrunners.org/Silent%20Runners.vbs
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control",
                        "value": "ServiceControlManagerExtension",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsWinlogonGPExtensions(GRRArtifactBase):
    """
    Windows Winlogon Group Policy Extensions

    These keys specify DLLs that should be loaded when the group policy engine
    loads, and can act as a persistence mechanism for malware.

    Reference URLs:
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\GPExtensions\\*",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\GPExtensions\\*",
                        "value": "DllName",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\GPExtensions\\*",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\GPExtensions\\*",
                        "value": "DllName",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSessionManagerSetupExecute(GRRArtifactBase):
    """
    Windows Session Manager SetupExecute persistence

    This entry shouldn't be populated after Windows has been installed

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/dd392286%28v=vs.85%29.aspx
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager",
                        "value": "SetupExecute",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsShellServiceObjects(GRRArtifactBase):
    """
    Windows Shell (explorer.exe) service objects delayed load.

    Reference URLs:
    http://www.microsoft.com/security/portal/threat/encyclopedia/Entry.aspx?Name=TrojanClicker:Win32/Zirit.X#tab=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\ShellServiceObjectDelayLoad",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\ShellServiceObjectDelayLoad",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsIconServiceLib(GRRArtifactBase):
    """
    Windows Icon Service Library Name

    The value should default to 'IconCodecService.dll'

    Reference URLs:
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows",
                        "value": "IconServiceLib",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsShellExtensions(GRRArtifactBase):
    """
    Approved extensions to the Windows Shell (explorer.exe).

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/cc144110(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Shell Extensions\\Approved",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Shell Extensions\\Approved",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Shell Extensions\\Approved",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Shell Extensions\\Approved",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsWinlogonAvailableShells(GRRArtifactBase):
    """
    Windows Server Winlogon Available Shells

    Used to specify an alternate shell application to be launched when logging
    into Windows Server 2012 and later. Legitimate keys under AvailableShells
    should just cause cmd.exe or explorer.exe to be executed, whereas malicious
    programs may create keys that cause malware to be run when a user logs in.

    Reference URLs:
    https://andymorgan.wordpress.com/2012/03/30/changing-the-default-shell-of-windows-server-8-core/
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon\\AlternateShells\\AvailableShells\\*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class InternetExplorerBrowserHelperObjects(GRRArtifactBase):
    """
    Loaded on Internet Explorer startup

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    http://regenerus.com/malware-common-loadpoints/
    https://code.google.com/p/regripper/wiki/ASEPs
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Browser Helper Objects\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Browser Helper Objects\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSystemPolicyShell(GRRArtifactBase):
    """
    Windows System policy replacement shell (custom user interface).

    Reference URLs:
    https://technet.microsoft.com/en-us/library/cc728472(v=ws.10).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "Shell",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "Shell",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WinSock2LayeredServiceProviders(GRRArtifactBase):
    """
    Used to filter TCP/IP traffic through WinSock2.

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    https://en.wikipedia.org/wiki/Layered_Service_Provider
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\WinSock2\\Parameters\\Protocol_Catalog9\\Catalog_Entries\\*",
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\WinSock2\\Parameters\\Protocol_Catalog9\\Catalog_Entries64\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsWinlogonShell(GRRArtifactBase):
    """
    Windows shell replacement.

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/ms838576%28v=winembedded.5%29.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "Shell",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "Shell",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsWinlogonUserinit(GRRArtifactBase):
    """
    Windows Winlogon Userinit replacement.

    Reference URLs: https://technet.microsoft.com/en-us/library/cc939862.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "Userinit",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "Userinit",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSetupCommandLine(GRRArtifactBase):
    """
    Command line invocation used for custom setup and deployment tasks

    Reference URLs:
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {"key": "HKEY_LOCAL_MACHINE\\System\\Setup", "value": "CmdLine"}
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsWinlogonVMApplet(GRRArtifactBase):
    """
    Windows VMApplet replacement.

    Reference URLs: https://technet.microsoft.com/en-us/library/cc939701.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "VMApplet",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "VMApplet",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSecurityProviders(GRRArtifactBase):
    """
    Security Providers DLLs

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    https://github.com/wmark/security-configuration/blob/master/Windows/disable-weak-ciphers-and-enable-TLS1.x.reg
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\SecurityProviders\\*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSessionManagerExecute(GRRArtifactBase):
    """
    Windows Session Manager Execute persistence

    This entry shouldn't be populated after Windows has been installed

    Reference URLs: https://technet.microsoft.com/en-us/library/cc976130.aspx
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager",
                        "value": "Execute",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsScreenSaverExecutable(GRRArtifactBase):
    """
    ScreenSaver Executable

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    https://technet.microsoft.com/en-us/library/cc737855(v=ws.10).aspx
    https://technet.microsoft.com/en-us/library/cc957840.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Policies\\Microsoft\\Windows\\Control Panel\\Desktop",
                        "value": "scrnsave.exe",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Control Panel\\Desktop",
                        "value": "scrnsave.exe",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSharedTaskScheduler(GRRArtifactBase):
    """
    Runs on windows boot.

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    http://www.bleepingcomputer.com/tutorials/windows-program-automatic-startup-locations/
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SharedTaskScheduler\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\SharedTaskScheduler\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsShellOpenCommand(GRRArtifactBase):
    """
    Executed every time this file type is opened. For most file types, the value
    should be '"%1" %*'.

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    https://pentestlab.blog/2017/06/09/uac-bypass-sdclt/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\*\\shell\\open\\command",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\*\\shell\\open\\command",
                        "value": "IsolatedCommand",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\*\\shell\\open\\command",
                        "value": "",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\*\\shell\\open\\command",
                        "value": "IsolatedCommand",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\*\\shell\\open\\command",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\*\\shell\\open\\command",
                        "value": "IsolatedCommand",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\*\\shell\\open\\command",
                        "value": "",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\*\\shell\\open\\command",
                        "value": "IsolatedCommand",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsToolPaths(GRRArtifactBase):
    """
    Paths to windows tools such as defrag, chkdsk.

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    http://www.liutilities.com/products/registrybooster/tweaklibrary/tweaks/11118/
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\BackupPath",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\ChkDskPath",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\cleanuppath",
                    "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\MyComputer\\DefragPath",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSessionManagerS0InitialCommand(GRRArtifactBase):
    """
    Windows Session Manager S0InitialCommand persistence

    This entry shouldn't be populated after Windows has been installed

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/windows/desktop/dd392286%28v=vs.85%29.aspx
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager",
                        "value": "S0InitialCommand",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsWinlogonGinaDLL(GRRArtifactBase):
    """
    Windows Gina DLL replacement.

    Reference URLs: https://technet.microsoft.com/en-us/library/cc939701.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "GinaDLL",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "GinaDLL",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsTerminalServerStartupPrograms(GRRArtifactBase):
    """
    Windows Terminal Server Startup Programs

    Reference URLs: http://forum.sysinternals.com/rdpclip_topic4729.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Terminal Server\\Wds\\rdpwd",
                        "value": "StartupPrograms",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsShellLoadAndRun(GRRArtifactBase):
    """
    Windows Shell Load and Run values

    Reference URLs: https://support.microsoft.com/en-us/kb/103865
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows",
                        "value": "Load",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Windows",
                        "value": "Run",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Windows",
                        "value": "Load",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\Windows",
                        "value": "Run",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsRunGrpConv(GRRArtifactBase):
    """
    The Windows RunGrpConv Registry value.

    When this Registry value is non-zero userinit.exe will launch grpconv.exe at
    user login.

    Reference URLs:
    http://www.hexacorn.com/blog/2014/06/18/beyond-good-ol-run-key-part-13/
    http://www.exploit-id.com/local-exploits/windows-xp-sp2-grpconv-exe
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "RunGrpConv",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsWinlogonUiHost(GRRArtifactBase):
    """
    Windows Winlogon UI screen application

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    http://www.bleepingcomputer.com/forums/t/14028/change-the-loginwelcome-screen/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "UiHost",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "UiHost",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsShellIconOverlayIdentifiers(GRRArtifactBase):
    """
    Called to display custom icons.

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    https://msdn.microsoft.com/en-us/library/windows/desktop/hh127455(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellIconOverlayIdentifiers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellIconOverlayIdentifiers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellIconOverlayIdentifiers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\ShellIconOverlayIdentifiers\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsTerminalServerInitialProgram(GRRArtifactBase):
    """
    Windows Terminal Server Initial Program

    Reference URLs:
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Terminal Server\\WinStations\\RDP-Tcp",
                        "value": "InitialProgram",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows NT\\Terminal Services",
                        "value": "InitialProgram",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Policies\\Microsoft\\Windows NT\\Terminal Services",
                        "value": "InitialProgram",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Policies\\Microsoft\\Windows NT\\Terminal Services",
                        "value": "InitialProgram",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Policies\\Microsoft\\Windows NT\\Terminal Services",
                        "value": "InitialProgram",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsWinlogonTaskman(GRRArtifactBase):
    """
    Windows Winlogon Taskman replacement.

    Reference URLs: https://technet.microsoft.com/en-us/library/cc939701.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "Taskman",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon",
                        "value": "Taskman",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSessionManagerWOWCommandLine(GRRArtifactBase):
    """
    Windows Session Manager Windows-on-Windows (WOW) command line

    Reference URLs: https://support.microsoft.com/en-us/kb/102986
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\WOW",
                        "value": "cmdline",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\Session Manager\\WOW",
                        "value": "wowcmdline",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsPolicyDisallowRun(GRRArtifactBase):
    """
    Restrict users from running specific applications, typically used by malware
    to block AV.

    Reference URLs: https://support.microsoft.com/en-us/kb/323525
    https://blog.malwarebytes.com/detections/pum-optional-disallowrun/
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\DisallowRun\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\DisallowRun\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsPortProxyConfiguration(GRRArtifactBase):
    """
    Windows PortProxy registry keys (set by netsh portproxy command or
    manually).

    Reference URLs:
    https://www.fireeye.com/blog/threat-research/2019/01/bypassing-network-restrictions-through-rdp-tunneling.html
    https://adepts.of0x.cc/netsh-portproxy-code/
    https://www.dfirnotes.net/portproxy_detection/
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\PortProxy\\*\\*\\*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsPowerShellEnableScripts(GRRArtifactBase):
    """
    Registry keys that control whether PowerShell scripts can execute directly.

    Reference URLs: https://technet.microsoft.com/library/hh847748.aspx
    http://www.hexacorn.com/blog/2014/08/27/beyond-good-ol-run-key-part-16/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Policies\\Microsoft\\Windows\\PowerShell",
                        "value": "EnableScripts",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\PowerShell",
                        "value": "EnableScripts",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsPowerShellExecutionPolicies(GRRArtifactBase):
    """
    PowerShell Script Execution Policies for all users, and the system.

    Reference URLs: https://technet.microsoft.com/library/hh847748.aspx
    http://www.hexacorn.com/blog/2014/08/27/beyond-good-ol-run-key-part-16/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Policies\\Microsoft\\Windows\\PowerShell",
                        "value": "ExecutionPolicy",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\PowerShell",
                        "value": "ExecutionPolicy",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsPowerShellHistory(GRRArtifactBase):
    """
    History of commands executed in an interactive PowerShell session.

    Reference URLs:
    https://0xdf.gitlab.io/2018/11/08/powershell-history-file.html
    https://docs.microsoft.com/en-us/powershell/module/psreadline/get-psreadlineoption?view=powershell-7.1
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Microsoft\\Windows\\PowerShell\\PSReadLine\\ConsoleHost_history.txt"
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


class WindowsPrefetchFiles(GRRArtifactBase):
    """
    Windows Prefetch files.

    Reference URLs: https://forensics.wiki/prefetch
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_systemroot%%\\Prefetch\\*.pf"],
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


class WindowsProductName(GRRArtifactBase):
    """
    The Windows product name

    Reference URLs:
    https://github.com/libyal/winreg-kb/blob/main/documentation/System%20keys.asciidoc
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion",
                        "value": "ProductName",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsProgramsCache(GRRArtifactBase):
    """
    Windows Programs Cache

    Reference URLs:
    https://github.com/libyal/winreg-kb/blob/main/documentation/Programs%20Cache%20values.asciidoc
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\StartPage",
                        "value": "ProgramsCache",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\StartPage2",
                        "value": "ProgramsCache",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsProgramsCacheJumpLists(GRRArtifactBase):
    """
    Windows Programs Cache Jump Lists

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/JumpLists.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\StartPage2",
                        "value": "ProgramsCacheSMP",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\StartPage2",
                        "value": "ProgramsCacheTBP",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsProxyPACAutoConfigURL(GRRArtifactBase):
    """
    Windows Proxy PAC AutoConfigURL.

    Reference URLs:
    https://blogs.msdn.microsoft.com/askie/2015/07/17/how-can-i-configure-proxy-autoconfigurl-setting-using-group-policy-preference-gpp/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                        "value": "AutoConfigURL",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsProxyServerSettings(GRRArtifactBase):
    """
    Windows Proxy Server Settings.

    Malware can modify these settings to redirect traffic through a malicious
    program running on the machine (for instance, by specifying 127.0.0.1 as the
    IP address of the proxy server to use) or to a malicious host on the local
    network or internet.

    Reference URLs:
    https://blog.malwarebytes.com/detections/pum-optional-proxyhijacker/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                        "value": "ProxyServer",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                        "value": "ProxyServer",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                        "value": "ProxyServer",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Internet Settings",
                        "value": "ProxyServer",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\NlaSvc\\Parameters\\Internet\\ManualProxies",
                        "value": "ProxyServer",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\System\\CurrentControlSet\\Services\\NlaSvc\\Parameters\\Internet\\ManualProxies",
                        "value": "ProxyServer",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsPushNotificationDatabaseFile(GRRArtifactBase):
    """
    The Windows Push Notification (WPN) database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Microsoft\\Windows\\Notifications\\wpndatabase.db",
                    "%%environ_systemroot%%\\System32\\config\\systemprofile\\AppData\\Local\\Microsoft\\Windows\\Notifications\\wpndatabase.db",
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


class WindowsRDPClientBitmapCache(GRRArtifactBase):
    """
    Artifacts of RDP connection contents

    Reference URLs: https://forensics.wiki/windows#rdp-bitmap-cache
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Microsoft\\Terminal Server Client\\Cache\\*.*"
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


class WindowsRecentFileCacheBCF(GRRArtifactBase):
    """
    The RecentFileCache.bcf file.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/RecentFileCache.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\AppCompat\\Programs\\RecentFileCache.bcf"
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


class WindowsRecycleBin(GRRArtifactBase):
    """
    Windows Recycle Bin (Recyler, $Recycle.Bin) files.

    Reference URLs: https://forensics.wiki/windows#recycle-bin
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["\\$Recycle.Bin\\**", "\\Recycler\\**"],
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


class WindowsRecycleBinMetadata(GRRArtifactBase):
    """
    Windows Recycle Bin (Recyler, $Recycle.Bin) metadata files only.

    Reference URLs: https://forensics.wiki/windows#recycle-bin
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["\\$Recycle.Bin\\*\\$I*", "\\Recycler\\*\\INFO2"],
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


class WindowsRegistryCurrentControlSet(GRRArtifactBase):
    """
    The current control set of the Windows Registry.

    Reference URLs:
    https://github.com/libyal/winreg-kb/blob/main/documentation/System%20keys.asciidoc
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {"key": "HKEY_LOCAL_MACHINE\\System\\Select", "value": "Current"}
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = ["CurrentControlSet"]


class WindowsUserRegistryFiles(GRRArtifactBase):
    """
    Windows user specific Registry files.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/RegistryFiles.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.userprofile%%\\NTUSER.DAT",
                    "%%users.userprofile%%\\NTUSER.MAN",
                    "%%users.localappdata%%\\Microsoft\\Windows\\UsrClass.dat",
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


class WindowsSystemRegistryTransactionLogFiles(GRRArtifactBase):
    """
    Windows system Registry transaction log files.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/RegistryFiles.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\config\\SAM.LOG",
                    "%%environ_systemroot%%\\System32\\config\\SAM.LOG1",
                    "%%environ_systemroot%%\\System32\\config\\SAM.LOG2",
                    "%%environ_systemroot%%\\System32\\config\\SECURITY.LOG",
                    "%%environ_systemroot%%\\System32\\config\\SECURITY.LOG1",
                    "%%environ_systemroot%%\\System32\\config\\SECURITY.LOG2",
                    "%%environ_systemroot%%\\System32\\config\\SOFTWARE.LOG",
                    "%%environ_systemroot%%\\System32\\config\\SOFTWARE.LOG1",
                    "%%environ_systemroot%%\\System32\\config\\SOFTWARE.LOG2",
                    "%%environ_systemroot%%\\System32\\config\\SYSTEM.LOG",
                    "%%environ_systemroot%%\\System32\\config\\SYSTEM.LOG1",
                    "%%environ_systemroot%%\\System32\\config\\SYSTEM.LOG2",
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


class WindowsSystemRegistryFiles(GRRArtifactBase):
    """
    Windows system Registry files.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/RegistryFiles.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemdrive%%\\System Volume Information\\Syscache.hve",
                    "%%environ_systemroot%%\\System32\\config\\SAM",
                    "%%environ_systemroot%%\\System32\\config\\SECURITY",
                    "%%environ_systemroot%%\\System32\\config\\SOFTWARE",
                    "%%environ_systemroot%%\\System32\\config\\SYSTEM",
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


class WindowsUserRegistryTransactionLogFiles(GRRArtifactBase):
    """
    Windows user Registry transaction log files.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/RegistryFiles.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.userprofile%%\\NTUSER.DAT.LOG",
                    "%%users.userprofile%%\\NTUSER.DAT.LOG1",
                    "%%users.userprofile%%\\NTUSER.DAT.LOG2",
                    "%%users.localappdata%%\\Microsoft\\Windows\\UsrClass.dat.LOG",
                    "%%users.localappdata%%\\Microsoft\\Windows\\UsrClass.dat.LOG1",
                    "%%users.localappdata%%\\Microsoft\\Windows\\UsrClass.dat.LOG2",
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


class WindowsRegistryProfiles(GRRArtifactBase):
    """
    Get SIDs for all users on the system with profiles present in the Registry.

    This looks in the Windows Registry where the profiles are stored and
    retrieves the paths for each profile.

    Reference URLs:
    http://msdn.microsoft.com/en-us/library/windows/desktop/bb776892(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList\\*",
                        "value": "ProfileImagePath",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsReleaseIdentifier(GRRArtifactBase):
    """
    The Windows 10 release identifier (or version number).

    This Windows Registry value contains the semi-annual Windows 10 version
    number.

    Reference URLs:
    https://www.microsoft.com/en-us/itpro/windows-10/release-information
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion",
                        "value": "ReleaseID",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsRoverAutostartDLL(GRRArtifactBase):
    """
    Windows Rover autostart DLL.

    The DLL loaded via the Windows Rover autostart mechanism. If this file
    exists, and the Rover autostart Registry key is set, userinit.exe will load
    this file and call its RunMonitor export.

    Reference URLs:
    http://www.hexacorn.com/blog/2014/05/21/beyond-good-ol-run-key-part-12/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_systemroot%%\\System32\\rover.dll"],
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


class WindowsRoverAutostartKey(GRRArtifactBase):
    """
    Windows Rover autostart Registry key.

    When set userinit.exe will load the DLL at %SystemRoot%/System32/rover.dll
    and call its RunMonitor export.

    Reference URLs:
    http://www.hexacorn.com/blog/2014/05/21/beyond-good-ol-run-key-part-12/
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_CLASSES_ROOT\\CLSID\\{16d12736-7a9e-4765-bec6-f301d679caaa}"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsScheduledTasks(GRRArtifactBase):
    """
    Windows Scheduled Tasks.

    Reference URLs: https://forensics.wiki/windows#scheduled-tasks
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\Tasks\\**10",
                    "%%environ_systemroot%%\\System32\\Tasks\\**10",
                    "%%environ_systemroot%%\\SysWow64\\Tasks\\**10",
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


class WindowsSearchDatabaseFile(GRRArtifactBase):
    """
    Windows Search database (Windows.edb).

    Reference URLs: https://forensics.wiki/windows_desktop_search
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersappdata%%\\Microsoft\\Search\\Data\\Applications\\Windows\\Windows.edb"
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
    aliases: ClassVar[Optional[list[str]]] = ["WindowsSearchDatabase"]


class WindowsSecurityCenterSettings(GRRArtifactBase):
    """
    Windows Security Center Settings

    Malware can modify these settings to avoid detection on an infected machine.
    For instance, Emotet modifies some of these settings after gaining
    execution.

    Reference URLs:
    https://blog.talosintelligence.com/2019/05/threat-roundup-0503-0510.html
    https://blog.appriver.com/phorphiex/trik-botnet-campaign-leads-to-multiple-infections-ransomware-banking-trojan-cryptojacking
    https://ccm.net/faq/1446-disabling-security-alerts-under-vista
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Security Center",
                        "value": "AntiSpyWareDisableNotify",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Security Center",
                        "value": "AntiSpyWareDisableNotify",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Security Center",
                        "value": "AntiVirusDisableNotify",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Security Center",
                        "value": "AntiVirusDisableNotify",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Security Center",
                        "value": "AntiVirusOverride",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Security Center",
                        "value": "AntiVirusOverride",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Security Center",
                        "value": "AutoUpdateDisableNotify",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Security Center",
                        "value": "AutoUpdateDisableNotify",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Security Center",
                        "value": "FirewallDisableNotify",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Security Center",
                        "value": "FirewallDisableNotify",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Security Center",
                        "value": "FirewallOverride",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Security Center",
                        "value": "FirewallOverride",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Security Center",
                        "value": "UpdatesDisableNotify",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Security Center",
                        "value": "UpdatesDisableNotify",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Security Center",
                        "value": "UpdatesOverride",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Security Center",
                        "value": "UpdatesOverride",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Security Center",
                        "value": "UacDisableNotify",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Security Center",
                        "value": "UacDisableNotify",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSecuritySettingsDatabases(GRRArtifactBase):
    """
    Windows security settings databases (secedit.sdb and spsecupd.sdb)
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\security\\Database\\secedit.sdb",
                    "%%environ_systemroot%%\\security\\templates\\spsecupd.sdb",
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


class WindowsShellHandlersRegistryKeys(GRRArtifactBase):
    """
    Windows registry values for shell handler artifacts.

    ContextMenuHandlers are added to right-click menus. CopyHookHandlers,
    DragDropHandlers, and ColumnHandlers are similar contextual settings to
    trigger on these actions.

    Reference URLs:
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    http://www.codeguru.com/cpp/com-tech/shell/article.php/c4515/Logging-the-Shell-Activity.htm
    http://www.trendmicro.com/vinfo/us/threat-encyclopedia/archive/malware/troj_qoolaid.r
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\*\\ShellEx\\ColumnHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\*\\ShellEx\\ContextMenuHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\*\\ShellEx\\CopyHookHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\*\\ShellEx\\DragDropHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\*\\ShellEx\\PropertySheetHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\Directory\\Background\\ShellEx\\ContextMenuHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\Directory\\Background\\ShellEx\\CopyHookHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\Directory\\Background\\ShellEx\\DragDropHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\Directory\\Background\\ShellEx\\PropertySheetHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\*\\ShellEx\\ColumnHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\*\\ShellEx\\ContextMenuHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\*\\ShellEx\\CopyHookHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\*\\ShellEx\\DragDropHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\*\\ShellEx\\PropertySheetHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\Directory\\Background\\ShellEx\\ContextMenuHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\Directory\\Background\\ShellEx\\CopyHookHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\Directory\\Background\\ShellEx\\DragDropHandlers\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\Classes\\Wow6432Node\\Directory\\Background\\ShellEx\\PropertySheetHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\*\\ShellEx\\ColumnHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\*\\ShellEx\\ContextMenuHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\*\\ShellEx\\CopyHookHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\*\\ShellEx\\DragDropHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\*\\ShellEx\\PropertySheetHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Directory\\Background\\ShellEx\\ContextMenuHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Directory\\Background\\ShellEx\\CopyHookHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Directory\\Background\\ShellEx\\DragDropHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Directory\\Background\\ShellEx\\PropertySheetHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\*\\ShellEx\\ColumnHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\*\\ShellEx\\ContextMenuHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\*\\ShellEx\\CopyHookHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\*\\ShellEx\\DragDropHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\*\\ShellEx\\PropertySheetHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\Directory\\Background\\ShellEx\\ContextMenuHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\Directory\\Background\\ShellEx\\CopyHookHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\Directory\\Background\\ShellEx\\DragDropHandlers\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Classes\\Wow6432Node\\Directory\\Background\\ShellEx\\PropertySheetHandlers\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSmsRouterInterceptStoreDatabaseFile(GRRArtifactBase):
    """
    Windows SmsRouter intercept store database file (SmsInterceptStore.db)
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_programdata%%\\Microsoft\\SmsRouter\\MessageStore\\SmsInterceptStore.db"
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


class WindowsSetupApiLogs(GRRArtifactBase):
    """
    Windows setup API logs.

    Reference URLs: https://forensics.wiki/setup_api_logs
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\setupapi.log",
                    "%%environ_systemroot%%\\inf\\setupapi.app.log",
                    "%%environ_systemroot%%\\inf\\setupapi.dev.log",
                    "%%environ_systemroot%%\\inf\\setupapi.offline.log",
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


class WindowsShutdownScript(GRRArtifactBase):
    """
    Windows policy shutdown script

    Reference URLs: https://technet.microsoft.com/en-us/library/ff404236.aspx
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\System\\Scripts",
                        "value": "Shutdown",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Group Policy\\Scripts\\Shutdown\\*\\*",
                        "value": "Script",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Group Policy\\Scripts\\Shutdown\\*\\*",
                        "value": "Parameters",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Group Policy\\State\\Machine\\Scripts\\Shutdown\\*\\*",
                        "value": "Script",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Group Policy\\State\\Machine\\Scripts\\Shutdown\\*\\*",
                        "value": "Parameters",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsStateRepositoryDeploymentDatabaseFile(GRRArtifactBase):
    """
    The State Reposistory deployment database file
    (StateRepository-Deployment.srd).
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_programdata%%\\Microsoft\\Windows\\AppRepository\\StateRepository-Deployment.srd"
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


class WindowsStateRepositoryMachineDatabaseFile(GRRArtifactBase):
    """
    The State Reposistory machine database file (StateRepository-Machine.srd).
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_programdata%%\\Microsoft\\Windows\\AppRepository\\StateRepository-Machine.srd"
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


class WindowsStartupFolderModification(GRRArtifactBase):
    """
    Windows startup folder Registry values.
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders",
                        "value": "Common Startup",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders",
                        "value": "Startup",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders",
                        "value": "Common Startup",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders",
                        "value": "Startup",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders",
                        "value": "Common Startup",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders",
                        "value": "Startup",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders",
                        "value": "Common Startup",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders",
                        "value": "Startup",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders",
                        "value": "Common Startup",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders",
                        "value": "Startup",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders",
                        "value": "Common Startup",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders",
                        "value": "Startup",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders",
                        "value": "Common Startup",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders",
                        "value": "Startup",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders",
                        "value": "Common Startup",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Explorer\\User Shell Folders",
                        "value": "Startup",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsStartupFolders(GRRArtifactBase):
    """
    Windows startup folder persistence.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_allusersprofile%%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\*",
                    "%%environ_allusersprofile%%\\Start Menu\\Programs\\Startup\\*",
                    "%%users.appdata%%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\*",
                    "%%users.userprofile%%\\Start Menu\\Programs\\Startup\\*",
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


class WindowsStartupScript(GRRArtifactBase):
    """
    Windows policy startup script

    Reference URLs: https://technet.microsoft.com/en-us/library/ff404236.aspx
    https://www.microsoftpressstore.com/articles/article.aspx?p=2762082&seqNum=2
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\System\\Scripts",
                        "value": "Startup",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Group Policy\\Scripts\\Startup\\*\\*",
                        "value": "Script",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Group Policy\\Scripts\\Startup\\*\\*",
                        "value": "Parameters",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Group Policy\\State\\Machine\\Scripts\\Startup\\*\\*",
                        "value": "Script",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Group Policy\\State\\Machine\\Scripts\\Startup\\*\\*",
                        "value": "Parameters",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSuperFetchFiles(GRRArtifactBase):
    """
    Windows SuperFetch files.

    Reference URLs: https://forensics.wiki/superfetch
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\Prefetch\\Ag*.db",
                    "%%environ_systemroot%%\\Prefetch\\Ag*.db.trx",
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


class WindowsSystemRestoreSettings(GRRArtifactBase):
    """
    Windows System Restore Settings

    Some malware, especially ransomware, will disable system restore to make
    system recovery more difficult.

    Reference URLs:
    https://blog.talosintelligence.com/2019/05/threat-roundup-0503-0510.html
    https://www.windows-commandline.com/enable-disable-system-restore-service/
    https://docs.microsoft.com/en-us/windows/desktop/msi/limitsystemrestorecheckpointing
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows NT\\SystemRestore",
                        "value": "DisableConfig",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\SystemRestore",
                        "value": "DisableConfig",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Policies\\Microsoft\\Windows NT\\SystemRestore",
                        "value": "DisableConfig",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\SystemRestore",
                        "value": "DisableConfig",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows NT\\SystemRestore",
                        "value": "DisableSR",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\SystemRestore",
                        "value": "DisableSR",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Policies\\Microsoft\\Windows NT\\SystemRestore",
                        "value": "DisableSR",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows NT\\CurrentVersion\\SystemRestore",
                        "value": "DisableSR",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\Installer",
                        "value": "LimitSystemRestoreCheckpointing",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Policies\\Microsoft\\Windows\\Installer",
                        "value": "LimitSystemRestoreCheckpointing",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSystemSettings(GRRArtifactBase):
    """
    Windows System Settings

    Malware can modify these keys to make it more difficult for the user to
    detect and remove malicious software.

    Reference URLs:
    https://www.sdkhere.com/2016/02/analysis-of-malware-using-wmi-query.html
    https://www.thewindowsclub.com/enable-disable-command-prompt-windows
    https://blog.malwarebytes.com/detections/pum-optional-disableregistrytools/
    https://blog.malwarebytes.com/detections/pum-optional-disabletaskmgr/
    https://www.stigviewer.com/stig/windows_7/2014-04-02/finding/V-1154
    https://blog.malwarebytes.com/detections/pum-optional-nodispcpl/
    https://blog.malwarebytes.com/detections/pum-optional-disablecmdprompt/
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "DisableCAD",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "DisableCAD",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "DisableCAD",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "DisableCAD",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "DisableRegistryTools",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "DisableRegistryTools",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "DisableRegistryTools",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "DisableRegistryTools",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "DisableTaskMgr",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "DisableTaskMgr",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "DisableTaskMgr",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "DisableTaskMgr",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "NoDispCPL",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "NoDispCPL",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "NoDispCPL",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "NoDispCPL",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\System",
                        "value": "DisableCMD",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Policies\\Microsoft\\Windows\\System",
                        "value": "DisableCMD",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Policies\\Microsoft\\Windows\\System",
                        "value": "DisableCMD",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Wow6432Node\\Policies\\Microsoft\\Windows\\System",
                        "value": "DisableCMD",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSystemIniFiles(GRRArtifactBase):
    """
    Windows system ini files
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemdrive%%\\system.ini",
                    "%%environ_windir%%\\win.ini",
                    "%%environ_windir%%\\wininit.ini",
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


class WindowsSystemRegistryFilesBackup(GRRArtifactBase):
    """
    Backup of Windows system Registry files.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/RegistryFiles.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SAM",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SECURITY",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SOFTWARE",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SYSTEM",
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


class WindowsSystemRegistryTransactionLogFilesBackup(GRRArtifactBase):
    """
    Backup of Windows system Registry transaction log files.

    These files have been observed to be typically 0 byte in size.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/RegistryFiles.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SAM.LOG",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SAM.LOG1",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SAM.LOG2",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SECURITY.LOG",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SECURITY.LOG1",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SECURITY.LOG2",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SOFTWARE.LOG",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SOFTWARE.LOG1",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SOFTWARE.LOG2",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SYSTEM.LOG",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SYSTEM.LOG1",
                    "%%environ_systemroot%%\\System32\\config\\RegBack\\SYSTEM.LOG2",
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


class WindowsSystemResourceUsageMonitorDatabaseFile(GRRArtifactBase):
    """
    Windows System Resource Usage Monitor (SRUM) database file.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/SystemResourceUsageMonitor.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_systemroot%%\\System32\\sru\\SRUDB.dat"],
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


class WindowsStartupInfo(GRRArtifactBase):
    """
    StartupInfo XML files.

    The files include the user account's Security Identifier (SID) in the name
    and there could be up to 5 per user account. They contain a list of
    processes that were executed within the first 90 seconds from the time the
    user logged in. The info includes start time, the full command line and the
    parent process info, among other things.

    Reference URLs: https://forensics.wiki/windows#startup-info
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\WDI\\LogFiles\\StartupInfo\\*.xml"
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


class WindowsTempDirectories(GRRArtifactBase):
    """
    Contents of the Windows temporary directories
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemdrive%%\\Temp\\*",
                    "%%environ_systemroot%%\\Temp\\*",
                    "%%users.localappdata%%\\Temp\\*",
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


class WindowsThumbcacheDatabaseFiles(GRRArtifactBase):
    """
    Windows thumbcache_*.db files.

    Reference URLs: https://forensics.wiki/vista_thumbcache/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Microsoft\\Windows\\Explorer\\thumbcache_*.db"
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


class WindowsTimezone(GRRArtifactBase):
    """
    The time zone of the system as a Windows time zone name or in MUI form.

    Reference URLs:
    https://winreg-kb.readthedocs.io/en/latest/sources/system-keys/Time-zones.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\TimeZoneInformation",
                        "value": "StandardName",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Control\\TimeZoneInformation",
                        "value": "TimeZoneKeyName",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = ["WinTimeZone"]


class WindowsTileDataLayerDatabase(GRRArtifactBase):
    """
    Windows tile data layer database (vedatamodel.edb)

    The tile data layer database is used to store information about Start Tiles.

    Reference URLs:
    https://forensics.wiki/extensible_storage_engine_(ese)_database_file_(edb)_format#tile-data-layer-database
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\TileDataLayer\\Database\\vedatamodel.edb"
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


class WindowsUninstallKeys(GRRArtifactBase):
    """
    Uninstall Registry keys

    Reference URLs:
    https://msdn.microsoft.com/en-us/library/aa372105(v=vs.85).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\*\\*",
                    "HKEY_LOCAL_MACHINE\\Software\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\*\\*",
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\*\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsUpdateBuildRevision(GRRArtifactBase):
    """
    Windows kernel update build revision (UBR).

    This Windows Registry value contains the monthly rollup patch version.

    Reference URLs:
    https://social.technet.microsoft.com/Forums/en-US/cadee4de-24d0-403e-9f3e-75868abf8f34
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion",
                        "value": "UBR",
                    }
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsUpdateCatalogDatabaseFile(GRRArtifactBase):
    """
    Windows Update catalog package signatures database file (catdb).

    Reference URLs:
    https://learn.microsoft.com/en-us/windows-hardware/drivers/install/catalog-files
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\catroot2\\{*-*-*-*-*}\\catdb"
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


class WindowsUpdateDataStoreDatabaseFile(GRRArtifactBase):
    """
    Windows Update data store database file (DataStore.edb).
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_windir%%\\SoftwareDistribution\\DataStore\\DataStore.edb"
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


class WindowsUpdateLogFile(GRRArtifactBase):
    """
    Windows Update log files.

    Reference URLs:
    https://learn.microsoft.com/en-us/windows/deployment/update/windows-update-logs
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_programdata%%\\USOShared\\Logs\\System\\*.etl",
                    "%%environ_systemroot%%\\Logs\\CBS\\CBS*.log",
                    "%%environ_systemroot%%\\Logs\\WindowsUpdate\\WindowsUpdate*.etl",
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


class WindowsUpdateSettings(GRRArtifactBase):
    """
    Windows Update Settings

    Reference URLs:
    https://docs.microsoft.com/en-us/windows/deployment/update/waas-wu-settings
    https://blog.talosintelligence.com/2019/06/threat-roundup-0531-0607.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU",
                        "value": "NoAutoUpdate",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU",
                        "value": "NoAutoUpdate",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsUpdateStatus(GRRArtifactBase):
    """
    Windows auto update status.

    Reference URLs: https://forensics.wiki/windows_update
    http://blogs.msdn.com/b/aruns_blog/archive/2011/06/20/active-setup-registry-key-what-it-is-and-how-to-create-in-the-package-using-admin-studio-install-shield.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Detect",
                        "value": "LastError",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Detect",
                        "value": "LastSuccessTime",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Download",
                        "value": "LastError",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Download",
                        "value": "LastSuccessTime",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Install",
                        "value": "LastError",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\WindowsUpdate\\Auto Update\\Results\\Install",
                        "value": "LastSuccessTime",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsUpdateStoreDatabaseFile(GRRArtifactBase):
    """
    The Update Service Orchestrator (USO) private update store database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_programdata%%\\USOPrivate\\UpdateStore\\store.db"],
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


class WindowsUpgradeSettings(GRRArtifactBase):
    """
    Windows Upgrade Settings

    Malware sometimes disables a machine ability to upgrade from previous
    versions of Windows to Windows 10. One malware family known to modify these
    keys is Kovter, a well-known trojan.

    Reference URLs:
    https://www.ghacks.net/2016/01/08/disableosupgrade-prevents-the-upgrade-to-windows-10/
    https://blog.talosintelligence.com/2019/05/threat-roundup-0517-0524.html
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\WindowsUpdate",
                        "value": "DisableOSUpgrade",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Policies\\Microsoft\\Windows\\WindowsUpdate",
                        "value": "DisableOSUpgrade",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Policies\\Microsoft\\Windows\\WindowsUpdate\\OSUpgrade",
                        "value": "ReservationsAllowed",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Policies\\Microsoft\\Windows\\WindowsUpdate\\OSUpgrade",
                        "value": "ReservationsAllowed",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsUserAccessLogging(GRRArtifactBase):
    """
    User Access Logging (UAL) databases.

    UAL is a local data aggregation feature (enabled by default) on Windows
    Servers 2012 and above, recording client usage by role and product on each
    system providing the resource. It's typically between 2 and 4 extensible
    storage engine (ESE) databases ("Current.mdb", "SystemIdentity.mdb, and
    "<GUID>.mdb").

    Reference URLs: https://forensics.wiki/windows#user-access-logging-ual
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%environ_systemroot%%\\System32\\LogFiles\\SUM\\*.mdb"],
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


class WindowsUserAccountControlSettings(GRRArtifactBase):
    """
    Windows User Account Control Settings

    Malware sometimes disables UAC to make it easier to perform actions on an
    infected machine.

    Reference URLs:
    https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-gpsb/958053ae-5397-4f96-977f-b7700ee461ec
    https://blog.talosintelligence.com/2019/05/threat-roundup-0503-0510.html
    https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-gpsb/341747f5-6b5d-4d30-85fc-fa1cc04038d4
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "EnableLUA",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "EnableLUA",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "ConsentPromptBehaviorAdmin",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Policies\\System",
                        "value": "ConsentPromptBehaviorAdmin",
                    },
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsUserAutomaticDestinationsJumpLists(GRRArtifactBase):
    """
    Windows user AutomaticDestinations Jump Lists.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/JumpLists.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Microsoft\\Windows\\Recent\\AutomaticDestinations\\*.automaticDestinations-ms"
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


class WindowsUserCustomDestinationsJumpLists(GRRArtifactBase):
    """
    Windows user CustomDestinations Jump Lists.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/JumpLists.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Microsoft\\Windows\\Recent\\CustomDestinations\\*.customDestinations-ms"
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


class WindowsUserRecentFiles(GRRArtifactBase):
    """
    Windows user specific recent files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Microsoft\\Office\\Recent\\*",
                    "%%users.appdata%%\\Microsoft\\Windows\\Recent\\*",
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


class WindowsUserShellFolders(GRRArtifactBase):
    """
    The Shell Folders information for Windows users.
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders\\*",
                    "HKEY_USERS\\%%users.sid%%\\Environment\\*",
                    "HKEY_USERS\\%%users.sid%%\\Volatile Environment\\*",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsWebCacheStorageQuotaDatabaseFile(GRRArtifactBase):
    """
    Windows WebCache storage quota database file (CacheStorage.edb)
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Packages\\*\\AppData\\CacheStorage\\CacheStorage.edb"
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


class WindowsWinstart(GRRArtifactBase):
    """
    Windows winstart.bat file
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_windir%%\\winstart.bat",
                    "%%environ_windir%%\\dosstart.bat",
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


class WindowsWordWheelQueryRegistryKey(GRRArtifactBase):
    """
    Keywords searched in from the Windows start menu, potentially resulting in
    files or folders access or program executions.
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\WordWheelQuery\\*"
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsXMLEventLogApplication(GRRArtifactBase):
    """
    Application Windows XML Event Log.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EventLog.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\winevt\\Logs\\Application.evtx"
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


class WindowsXMLEventLogPowerShell(GRRArtifactBase):
    """
    PowerShell Windows XML Event Logs.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EventLog.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\winevt\\Logs\\Microsoft-Windows-PowerShell%4Admin.evtx",
                    "%%environ_systemroot%%\\System32\\winevt\\Logs\\Microsoft-Windows-PowerShell%4Operational.evtx",
                    "%%environ_systemroot%%\\System32\\winevt\\Logs\\PowerShellCore Operational.evtx",
                    "%%environ_systemroot%%\\System32\\winevt\\Logs\\Windows PowerShell.evtx",
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


class WindowsXMLEventLogSecurity(GRRArtifactBase):
    """
    Security Windows XML Event Log.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EventLog.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\winevt\\Logs\\Security.evtx"
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


class WindowsXMLEventLogSysmon(GRRArtifactBase):
    """
    Sysmon Windows XML Event Log.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EventLog.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\winevt\\Logs\\Microsoft-Windows-Sysmon%4Operational.evtx"
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


class WindowsXMLEventLogSystem(GRRArtifactBase):
    """
    System Windows XML Event Log.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EventLog.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\winevt\\Logs\\System.evtx"
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


class WindowsXMLEventLogTerminalServices(GRRArtifactBase):
    """
    TerminalServices Windows XML Event Log.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EventLog.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%environ_systemroot%%\\System32\\winevt\\Logs\\Microsoft-Windows-TerminalServices-LocalSessionManager%4Operational.evtx"
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


class WindowsApplicationCompatibilityShims(GRRArtifactBase):
    """
    Windows Application Compatibility Shim Database Files and Application
    Mappings
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "WindowsApplicationCompatibilityInstalledShimDatabases",
                    "WindowsApplicationCompatibilityShimDatabaseMappings",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "WindowsApplicationCompatibilityInstalledShimDatabases": WindowsApplicationCompatibilityInstalledShimDatabases,
        "WindowsApplicationCompatibilityShimDatabaseMappings": WindowsApplicationCompatibilityShimDatabaseMappings,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsEnvironmentVariableSystemDrive(GRRArtifactBase):
    """
    The %SystemDrive% environment variable contains the letter of the drive in
    which the system directory is located, typically "C:".

    This value is not present in the Windows Registry but can be derived from
    %SystemRoot%.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/EnvironmentVariables.html
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {"names": ["WindowsEnvironmentVariableSystemRoot"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "WindowsEnvironmentVariableSystemRoot": WindowsEnvironmentVariableSystemRoot
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsPersistenceRegistryKeys(GRRArtifactBase):
    """
    Windows Registry keys used for persistence.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "InternetExplorerBrowserHelperObjects",
                    "WindowsActiveDesktop",
                    "WindowsActiveSyncAutoStart",
                    "WindowsAlternateShell",
                    "WindowsAppCertDLLs",
                    "WindowsAppInitDLLs",
                    "WindowsBootVerificationProgram",
                    "WindowsCommandProcessorAutoRun",
                    "WindowsCredentialProviderFilters",
                    "WindowsCredentialProviders",
                    "WindowsDebugger",
                    "WindowsEnvironmentUserLoginScripts",
                    "WindowsExplorerAutoplayHandlers",
                    "WindowsFileTypeAutorunAssociations",
                    "WindowsFontDrivers",
                    "WindowsIconServiceLib",
                    "WindowsLSAAuthenticationPackages",
                    "WindowsLSANotificationPackages",
                    "WindowsLSASecurityPackages",
                    "WindowsMSDTCDLLs",
                    "WindowsMultiMediaDrivers",
                    "WindowsNetworkShellHelpers",
                    "WindowsPendingGPOs",
                    "WindowsPLAPProviders",
                    "WindowsPrintMonitors",
                    "WindowsRunGrpConv",
                    "WindowsRunKeys",
                    "WindowsRunServices",
                    "WindowsScreenSaverExecutable",
                    "WindowsSearchFilterHandlers",
                    "WindowsSecurityProviders",
                    "WindowsServiceControlManagerExtension",
                    "WindowsSessionManagerBootExecute",
                    "WindowsSessionManagerExecute",
                    "WindowsSessionManagerS0InitialCommand",
                    "WindowsSessionManagerSetupExecute",
                    "WindowsSessionManagerSubSystems",
                    "WindowsSessionManagerWOWCommandLine",
                    "WindowsSetupCommandLine",
                    "WindowsSharedTaskScheduler",
                    "WindowsShellExecuteHooks",
                    "WindowsShellExtensions",
                    "WindowsShellIconOverlayIdentifiers",
                    "WindowsShellLoadAndRun",
                    "WindowsShellOpenCommand",
                    "WindowsShellRunasCommand",
                    "WindowsShellServiceObjects",
                    "WindowsStubPaths",
                    "WindowsSystemPolicyShell",
                    "WindowsTerminalServerInitialProgram",
                    "WindowsTerminalServerRunKeys",
                    "WindowsTerminalServerStartupPrograms",
                    "WindowsToolPaths",
                    "WindowsWinlogonAppSetup",
                    "WindowsWinlogonAvailableShells",
                    "WindowsWinlogonGinaDLL",
                    "WindowsWinlogonGPExtensions",
                    "WindowsWinlogonNotify",
                    "WindowsWinlogonShell",
                    "WindowsWinlogonSystem",
                    "WindowsWinlogonTaskman",
                    "WindowsWinlogonUiHost",
                    "WindowsWinlogonUserinit",
                    "WindowsWinlogonVMApplet",
                    "WinSock2LayeredServiceProviders",
                    "WinSock2NamespaceProviders",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "WindowsPLAPProviders": WindowsPLAPProviders,
        "WindowsPrintMonitors": WindowsPrintMonitors,
        "WindowsLSANotificationPackages": WindowsLSANotificationPackages,
        "WindowsShellExecuteHooks": WindowsShellExecuteHooks,
        "WindowsSessionManagerBootExecute": WindowsSessionManagerBootExecute,
        "WindowsTerminalServerRunKeys": WindowsTerminalServerRunKeys,
        "WindowsLSASecurityPackages": WindowsLSASecurityPackages,
        "WindowsWinlogonAppSetup": WindowsWinlogonAppSetup,
        "WindowsCredentialProviders": WindowsCredentialProviders,
        "WindowsSessionManagerSubSystems": WindowsSessionManagerSubSystems,
        "WindowsRunKeys": WindowsRunKeys,
        "WindowsLSAAuthenticationPackages": WindowsLSAAuthenticationPackages,
        "WinSock2NamespaceProviders": WinSock2NamespaceProviders,
        "WindowsWinlogonNotify": WindowsWinlogonNotify,
        "WindowsCredentialProviderFilters": WindowsCredentialProviderFilters,
        "WindowsStubPaths": WindowsStubPaths,
        "WindowsShellRunasCommand": WindowsShellRunasCommand,
        "WindowsWinlogonSystem": WindowsWinlogonSystem,
        "WindowsSearchFilterHandlers": WindowsSearchFilterHandlers,
        "WindowsRunServices": WindowsRunServices,
        "WindowsAppInitDLLs": WindowsAppInitDLLs,
        "WindowsServiceControlManagerExtension": WindowsServiceControlManagerExtension,
        "WindowsWinlogonGPExtensions": WindowsWinlogonGPExtensions,
        "WindowsSessionManagerSetupExecute": WindowsSessionManagerSetupExecute,
        "WindowsShellServiceObjects": WindowsShellServiceObjects,
        "WindowsIconServiceLib": WindowsIconServiceLib,
        "WindowsShellExtensions": WindowsShellExtensions,
        "WindowsWinlogonAvailableShells": WindowsWinlogonAvailableShells,
        "InternetExplorerBrowserHelperObjects": webbrowser.InternetExplorerBrowserHelperObjects,
        "WindowsSystemPolicyShell": WindowsSystemPolicyShell,
        "WinSock2LayeredServiceProviders": WinSock2LayeredServiceProviders,
        "WindowsWinlogonShell": WindowsWinlogonShell,
        "WindowsWinlogonUserinit": WindowsWinlogonUserinit,
        "WindowsSetupCommandLine": WindowsSetupCommandLine,
        "WindowsWinlogonVMApplet": WindowsWinlogonVMApplet,
        "WindowsActiveSyncAutoStart": WindowsActiveSyncAutoStart,
        "WindowsMSDTCDLLs": WindowsMSDTCDLLs,
        "WindowsCommandProcessorAutoRun": WindowsCommandProcessorAutoRun,
        "WindowsSecurityProviders": WindowsSecurityProviders,
        "WindowsSessionManagerExecute": WindowsSessionManagerExecute,
        "WindowsScreenSaverExecutable": WindowsScreenSaverExecutable,
        "WindowsSharedTaskScheduler": WindowsSharedTaskScheduler,
        "WindowsShellOpenCommand": WindowsShellOpenCommand,
        "WindowsToolPaths": WindowsToolPaths,
        "WindowsNetworkShellHelpers": WindowsNetworkShellHelpers,
        "WindowsSessionManagerS0InitialCommand": WindowsSessionManagerS0InitialCommand,
        "WindowsDebugger": WindowsDebugger,
        "WindowsWinlogonGinaDLL": WindowsWinlogonGinaDLL,
        "WindowsTerminalServerStartupPrograms": WindowsTerminalServerStartupPrograms,
        "WindowsShellLoadAndRun": WindowsShellLoadAndRun,
        "WindowsRunGrpConv": WindowsRunGrpConv,
        "WindowsFontDrivers": WindowsFontDrivers,
        "WindowsWinlogonUiHost": WindowsWinlogonUiHost,
        "WindowsShellIconOverlayIdentifiers": WindowsShellIconOverlayIdentifiers,
        "WindowsEnvironmentUserLoginScripts": WindowsEnvironmentUserLoginScripts,
        "WindowsAlternateShell": WindowsAlternateShell,
        "WindowsExplorerAutoplayHandlers": WindowsExplorerAutoplayHandlers,
        "WindowsActiveDesktop": WindowsActiveDesktop,
        "WindowsAppCertDLLs": WindowsAppCertDLLs,
        "WindowsTerminalServerInitialProgram": WindowsTerminalServerInitialProgram,
        "WindowsWinlogonTaskman": WindowsWinlogonTaskman,
        "WindowsMultiMediaDrivers": WindowsMultiMediaDrivers,
        "WindowsSessionManagerWOWCommandLine": WindowsSessionManagerWOWCommandLine,
        "WindowsBootVerificationProgram": WindowsBootVerificationProgram,
        "WindowsFileTypeAutorunAssociations": WindowsFileTypeAutorunAssociations,
        "WindowsPendingGPOs": WindowsPendingGPOs,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSystemRegistryFilesAndTransactionLogs(GRRArtifactBase):
    """
    Windows system Registry files and transaction logs.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/RegistryFiles.html
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "WindowsSystemRegistryFiles",
                    "WindowsSystemRegistryTransactionLogFiles",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "WindowsSystemRegistryTransactionLogFiles": WindowsSystemRegistryTransactionLogFiles,
        "WindowsSystemRegistryFiles": WindowsSystemRegistryFiles,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsRegistryFilesAndTransactionLogs(GRRArtifactBase):
    """
    Windows user and system Registry files and transaction logs.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/RegistryFiles.html
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "WindowsSystemRegistryFiles",
                    "WindowsSystemRegistryTransactionLogFiles",
                    "WindowsUserRegistryFiles",
                    "WindowsUserRegistryTransactionLogFiles",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "WindowsUserRegistryFiles": WindowsUserRegistryFiles,
        "WindowsSystemRegistryTransactionLogFiles": WindowsSystemRegistryTransactionLogFiles,
        "WindowsSystemRegistryFiles": WindowsSystemRegistryFiles,
        "WindowsUserRegistryTransactionLogFiles": WindowsUserRegistryTransactionLogFiles,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsUserRegistryFilesAndTransactionLogs(GRRArtifactBase):
    """
    Windows user Registry files and transaction logs.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/RegistryFiles.html
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "WindowsUserRegistryFiles",
                    "WindowsUserRegistryTransactionLogFiles",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "WindowsUserRegistryFiles": WindowsUserRegistryFiles,
        "WindowsUserRegistryTransactionLogFiles": WindowsUserRegistryTransactionLogFiles,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsSystemRegistryFilesAndTransactionLogsBackup(GRRArtifactBase):
    """
    Backup of Windows system Registry files and transaction logs.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/RegistryFiles.html
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "WindowsSystemRegistryFilesBackup",
                    "WindowsSystemRegistryTransactionLogFilesBackup",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "WindowsSystemRegistryTransactionLogFilesBackup": WindowsSystemRegistryTransactionLogFilesBackup,
        "WindowsSystemRegistryFilesBackup": WindowsSystemRegistryFilesBackup,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsUserJumpLists(GRRArtifactBase):
    """
    Windows user Jump Lists.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/windows/JumpLists.html
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "WindowsProgramsCacheJumpLists",
                    "WindowsUserAutomaticDestinationsJumpLists",
                    "WindowsUserCustomDestinationsJumpLists",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "WindowsUserCustomDestinationsJumpLists": WindowsUserCustomDestinationsJumpLists,
        "WindowsUserAutomaticDestinationsJumpLists": WindowsUserAutomaticDestinationsJumpLists,
        "WindowsProgramsCacheJumpLists": WindowsProgramsCacheJumpLists,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class WindowsPersistenceMechanisms(GRRArtifactBase):
    """
    Persistence mechanisms in Windows.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "WindowsPersistenceRegistryKeys",
                    "WindowsPowerShellDefaultProfiles",
                    "WindowsServices",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "WindowsServices": WindowsServices,
        "WindowsPowerShellDefaultProfiles": WindowsPowerShellDefaultProfiles,
        "WindowsPersistenceRegistryKeys": WindowsPersistenceRegistryKeys,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None
