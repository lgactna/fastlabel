"""
Auto-generated classes from the .tkape files for the Communications category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class AnyDeskAnyDeskLogsUserProfiletrace0(KapeTarget):
    """
    Collects the trace logs for AnyDesk from a user profile
    """

    name: ClassVar[str] = "AnyDesk Logs - User Profile - *.trace"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\AnyDesk\\")
    regex: ClassVar[str] = r"(?s:.*\.trace)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AnyDeskAnyDeskLogsProgramDatatrace1(KapeTarget):
    """
    Collects the trace logs for AnyDesk from ProgramData
    """

    name: ClassVar[str] = "AnyDesk Logs - ProgramData - *.trace"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\AnyDesk\\")
    regex: ClassVar[str] = r"(?s:.*\.trace)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AnyDeskAnyDeskLogsUserProfileconf2(KapeTarget):
    """
    Collects the conf logs for AnyDesk from a user profile
    """

    name: ClassVar[str] = "AnyDesk Logs - User Profile - *.conf"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\AnyDesk\\")
    regex: ClassVar[str] = r"(?s:.*\.conf)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AnyDeskAnyDeskLogsProgramDataconf3(KapeTarget):
    """
    Collects the conf logs for AnyDesk from ProgramData
    """

    name: ClassVar[str] = "AnyDesk Logs - ProgramData - *.conf"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\AnyDesk\\")
    regex: ClassVar[str] = r"(?s:.*\.conf)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AnyDeskAnyDeskVideos4(KapeTarget):
    """
    Collects any session recordings made by the user while using AnyDesk
    """

    name: ClassVar[str] = "AnyDesk Videos"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Videos\\AnyDesk\\")
    regex: ClassVar[str] = r"(?s:.*\.anydesk)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AnyDeskAnyDeskLogsUserProfileconnectiontracetxt5(KapeTarget):
    """
    Collects the connection trace log from user profile
    """

    name: ClassVar[str] = "AnyDesk Logs - User Profile - connection_trace.txt"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\AnyDesk\\")
    regex: ClassVar[str] = r"(?s:connection_trace\.txt)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AnyDeskAnyDeskLogsProgramDataconnectiontracetxt6(KapeTarget):
    """
    Collects the connection trace log from ProgramData
    """

    name: ClassVar[str] = "AnyDesk Logs - ProgramData - connection_trace.txt"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\AnyDesk\\")
    regex: ClassVar[str] = r"(?s:connection_trace\.txt)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AnyDeskAnyDeskLogsSystemUserAccount7(KapeTarget):
    """
    Collects the logs associated with the System user account
    """

    name: ClassVar[str] = "AnyDesk Logs - System User Account"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows\\SysWOW64\\config\\systemprofile\\AppData\\Roaming\\AnyDesk\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AnyDesk(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun, Scott Hanson, and Nicole Jao

    Version: 1.3

    ID: 6c3736f5-39e2-4cce-9af8-02c76c09b91c

    AnyDesk
    """

    name: ClassVar[str] = "AnyDesk"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        AnyDeskAnyDeskLogsUserProfiletrace0,
        AnyDeskAnyDeskLogsProgramDatatrace1,
        AnyDeskAnyDeskLogsUserProfileconf2,
        AnyDeskAnyDeskLogsProgramDataconf3,
        AnyDeskAnyDeskVideos4,
        AnyDeskAnyDeskLogsUserProfileconnectiontracetxt5,
        AnyDeskAnyDeskLogsProgramDataconnectiontracetxt6,
        AnyDeskAnyDeskLogsSystemUserAccount7,
    ]


class CiscoJabberCiscoJabberDatabase0(KapeTarget):
    """
    The Cisco Jabber process needs to be killed before database can be copied.
    """

    name: ClassVar[str] = "Cisco Jabber Database"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Cisco\\Unified Communications\\Jabber\\CSF\\History\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CiscoJabber(KapeTargetConfiguration):
    """
    Author: Andrew Bannon

    Version: 1.0

    ID: 69249cc7-2b04-47c4-8ba9-d8055fadc950

    Jabber
    """

    name: ClassVar[str] = "CiscoJabber"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [CiscoJabberCiscoJabberDatabase0]


class DiscordDiscordCacheFiles0(KapeTarget):
    """
    Gets cached data from Discord app
    """

    name: ClassVar[str] = "Discord Cache Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\discord\\cache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DiscordDiscordLocalStorageLevelDBFiles1(KapeTarget):
    """
    Gets LevelDB database from Discord app
    """

    name: ClassVar[str] = "Discord Local Storage LevelDB Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\discord\\local storage\\leveldb\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Discord(KapeTargetConfiguration):
    """
    Author: Christian Johansen and Matt Dawson

    Version: 2.0

    ID: 5a44a0ef-db56-4103-8748-797432487028

    Discord Cache and LevelDB Files
    """

    name: ClassVar[str] = "Discord"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        DiscordDiscordCacheFiles0,
        DiscordDiscordLocalStorageLevelDBFiles1,
    ]


class HexChatHexChatChatLogs0(KapeTarget):
    name: ClassVar[str] = "HexChat Chat Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\HexChat\\logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class HexChat(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: a26181fc-1931-4d48-9b5d-44f6f8f71ccc

    HexChat
    """

    name: ClassVar[str] = "HexChat"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [HexChatHexChatChatLogs0]


class IceChatIceChatChatLogs0(KapeTarget):
    name: ClassVar[str] = "IceChat Chat Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\IceChat Networks\\IceChat\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class IceChat(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 4c437510-9fba-4d36-8070-0a14c29f1033

    IceChat
    """

    name: ClassVar[str] = "IceChat"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [IceChatIceChatChatLogs0]


class iTunesBackupiTunesBackupFolder0(KapeTarget):
    name: ClassVar[str] = "iTunes Backup Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Apple\\Mobilesync\\Backup\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class iTunesBackupiTunesBackupFolder1(KapeTarget):
    name: ClassVar[str] = "iTunes Backup Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Apple Computer\\Mobilesync\\Backup\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class iTunesBackupiTunesBackupFolderiOS132(KapeTarget):
    name: ClassVar[str] = "iTunes Backup Folder - iOS13"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Apple\\Mobilesync\\Backup\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class iTunesBackup(KapeTargetConfiguration):
    """
    Author: Tony Knutson

    Version: 2.0

    ID: 7b4a98d9-b36a-40be-bacc-ad0102b0a8c3

    iTunes Backups
    """

    name: ClassVar[str] = "iTunesBackup"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        iTunesBackupiTunesBackupFolder0,
        iTunesBackupiTunesBackupFolder1,
        iTunesBackupiTunesBackupFolderiOS132,
    ]


class mIRCmIRCChatLogsVista0(KapeTarget):
    name: ClassVar[str] = "mIRC Chat Logs (Vista+)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\mIRC\\logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class mIRCmIRCChatLogs2000XP1(KapeTarget):
    name: ClassVar[str] = "mIRC Chat Logs (2000/XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\mIRC\\logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class mIRC(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 284ffb97-076c-4990-b10a-044d40ac1901

    mIRC
    """

    name: ClassVar[str] = "mIRC"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        mIRCmIRCChatLogsVista0,
        mIRCmIRCChatLogs2000XP1,
    ]


class mRemoteNGmRemoteNGLogs0(KapeTarget):
    """
    Contains log entries for remote connections
    """

    name: ClassVar[str] = "mRemoteNG Logs"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\mRemoteNG\\")
    regex: ClassVar[str] = r"(?s:mRemoteNG\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class mRemoteNGmRemoteNGConnectionConfigurationandBackups1(KapeTarget):
    """
    Contains connection config, often with obfuscated credentials
    """

    name: ClassVar[str] = "mRemoteNG Connection Configuration and Backups"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\mRemoteNG\\")
    regex: ClassVar[str] = r"(?s:confCons\.xml.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class mRemoteNGmRemoteNGProgramSettings2(KapeTarget):
    """
    Contains user-specific program settings
    """

    name: ClassVar[str] = "mRemoteNG Program Settings"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\*\\mRemoteNG\\")
    regex: ClassVar[str] = r"(?s:user\.config)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class mRemoteNG(KapeTargetConfiguration):
    """
    Author: Markus Einarsson (@einarssonm)

    Version: 1.0

    ID: 486c2b29-ae39-4418-8fb4-2d855e9387f9

    mRemoteNG
    """

    name: ClassVar[str] = "mRemoteNG"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        mRemoteNGmRemoteNGLogs0,
        mRemoteNGmRemoteNGConnectionConfigurationandBackups1,
        mRemoteNGmRemoteNGProgramSettings2,
    ]


class OutlookPSTOSTPSTXP0(KapeTarget):
    name: ClassVar[str] = "PST XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Microsoft\\Outlook\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.pst)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OutlookPSTOSTOSTXP1(KapeTarget):
    name: ClassVar[str] = "OST XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Microsoft\\Outlook\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.ost)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OutlookPSTOSTPST2013or20162(KapeTarget):
    name: ClassVar[str] = "PST (2013 or 2016)"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Documents\\Outlook Files\\")
    regex: ClassVar[str] = r"(?s:.*\.pst)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OutlookPSTOSTOST2013or20163(KapeTarget):
    name: ClassVar[str] = "OST (2013 or 2016)"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Documents\\Outlook Files\\")
    regex: ClassVar[str] = r"(?s:.*\.ost)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OutlookPSTOSTPST4(KapeTarget):
    """
    Outlook Data File: POP accounts, archives, older installations
    """

    name: ClassVar[str] = "PST"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Outlook\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.pst)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OutlookPSTOSTOST5(KapeTarget):
    """
    Offline Outlook Data File: M365, Exchange, IMAP
    """

    name: ClassVar[str] = "OST"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Outlook\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.ost)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OutlookPSTOSTNST6(KapeTarget):
    """
    Outlook Group Storage File: Group conversations and calendar
    """

    name: ClassVar[str] = "NST"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Outlook\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.nst)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OutlookPSTOSTOutlookAttachmentTemporaryStorage7(KapeTarget):
    """
    Outlook temporary storage folder for user attachments
    """

    name: ClassVar[str] = "Outlook Attachment Temporary Storage"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\INetCache\\Content.Outlook\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OutlookPSTOST(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman and Chad Tilbury

    Version: 1.1

    ID: f91909c4-bba1-40d6-a3bc-39d060843a09

    Outlook PST and OST files
    """

    name: ClassVar[str] = "OutlookPSTOST"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        OutlookPSTOSTPSTXP0,
        OutlookPSTOSTOSTXP1,
        OutlookPSTOSTPST2013or20162,
        OutlookPSTOSTOST2013or20163,
        OutlookPSTOSTPST4,
        OutlookPSTOSTOST5,
        OutlookPSTOSTNST6,
        OutlookPSTOSTOutlookAttachmentTemporaryStorage7,
    ]


class SignalSignalAttachmentscache0(KapeTarget):
    """
    Profile pictures (and possibly attachments) for users who this individual
    has as contacts or has communicated with
    """

    name: ClassVar[str] = "Signal Attachments cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Signal\\attachments.noindex\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SignalSignalLogs1(KapeTarget):
    """
    Logs for Signal. Most recent has the extension .log while old ones will have
    extension .log.0, .log.1 etc.
    """

    name: ClassVar[str] = "Signal Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Signal\\logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SignalSignalconfigjson2(KapeTarget):
    """
    config.json holds the db.sqlite SQLCipher raw key
    """

    name: ClassVar[str] = "Signal config.json"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\Signal\\")
    regex: ClassVar[str] = r"(?s:config\.json)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SignalSignalDatabase3(KapeTarget):
    """
    Stores attachment details, conversations, messages, and more
    """

    name: ClassVar[str] = "Signal Database"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Signal\\sql\\"
    )
    regex: ClassVar[str] = r"(?s:db\.sqlite)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Signal(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: bc021c91-a699-4265-9a7f-9c6792b1d823

    Signal (Please view this tkape file for documentation on decryption!)
    """

    name: ClassVar[str] = "Signal"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SignalSignalAttachmentscache0,
        SignalSignalLogs1,
        SignalSignalconfigjson2,
        SignalSignalDatabase3,
    ]


class SkypemaindbAppv120(KapeTarget):
    name: ClassVar[str] = "main.db (App <v12)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.SkypeApp_*\\LocalState\\*\\"
    )
    regex: ClassVar[str] = r"(?s:main\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SkypeskypedbAppv121(KapeTarget):
    name: ClassVar[str] = "skype.db (App +v12)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.SkypeApp_*\\LocalState\\*\\"
    )
    regex: ClassVar[str] = r"(?s:skype\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SkypemaindbXP2(KapeTarget):
    name: ClassVar[str] = "main.db XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Skype\\*\\"
    )
    regex: ClassVar[str] = r"(?s:main\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SkypemaindbWin73(KapeTarget):
    name: ClassVar[str] = "main.db Win7+"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\Skype\\*\\")
    regex: ClassVar[str] = r"(?s:main\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Skypes4lusernamedbAppv84(KapeTarget):
    name: ClassVar[str] = "s4l-[username].db (App +v8)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.SkypeApp_*\\LocalState\\"
    )
    regex: ClassVar[str] = r"(?s:s4l\-.*\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SkypeleveldbSkypeforDesktopv85(KapeTarget):
    name: ClassVar[str] = "leveldb (Skype for Desktop +v8)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Skype for Desktop\\IndexedDB\\*.leveldb\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SkypeSkypeforDestkopv8ChromiumCache6(KapeTarget):
    """
    Can be viewed with Nirsoft's ChromeCacheView
    """

    name: ClassVar[str] = "Skype for Destkop v8+ Chromium Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Skype for Desktop\\Cache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Skype(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman, Matt Dawson

    Version: 4.0

    ID: d7b0b49c-16bb-4b32-9f57-2d918acaebbc

    Skype
    """

    name: ClassVar[str] = "Skype"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SkypemaindbAppv120,
        SkypeskypedbAppv121,
        SkypemaindbXP2,
        SkypemaindbWin73,
        Skypes4lusernamedbAppv84,
        SkypeleveldbSkypeforDesktopv85,
        SkypeSkypeforDestkopv8ChromiumCache6,
    ]


class SupremoRemoteDesktopSupremoConnectionLogs0(KapeTarget):
    """
    Includes Supremo.00.Client.log and Supremo.00.Incoming.log
    """

    name: ClassVar[str] = "Supremo Connection Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\SupremoRemoteDesktop\\Log")
    regex: ClassVar[str] = r"(?s:.*\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SupremoRemoteDesktopSupremoFileTransferInbox1(KapeTarget):
    """
    Includes all files transferred to the inbox folder during a remote session
    """

    name: ClassVar[str] = "Supremo File Transfer Inbox"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\SupremoRemoteDesktop\\Inbox")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SupremoRemoteDesktop(KapeTargetConfiguration):
    """
    Author: Sandro Heckendorn

    Version: 1.0

    ID: 0d88cf87-bbc5-4bcf-bb4f-2bc9a3e300f0

    Supremo Remote Desktop Control Logs
    """

    name: ClassVar[str] = "SupremoRemoteDesktop"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SupremoRemoteDesktopSupremoConnectionLogs0,
        SupremoRemoteDesktopSupremoFileTransferInbox1,
    ]


class TeamViewerLogsTeamViewerConnectionLogs0(KapeTarget):
    """
    Includes connections_incoming.txt and connections.txt
    """

    name: ClassVar[str] = "TeamViewer Connection Logs"
    base_path: ClassVar[Path] = Path("C:\\Program Files*\\TeamViewer\\")
    regex: ClassVar[str] = r"(?s:connections.*\.txt)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TeamViewerLogsTeamViewerApplicationLogs1(KapeTarget):
    """
    Includes TeamViewer<version>_Logfile.log and
    TeamViewer<version>_Logfile_OLD.log
    """

    name: ClassVar[str] = "TeamViewer Application Logs"
    base_path: ClassVar[Path] = Path("C:\\Program Files*\\TeamViewer\\")
    regex: ClassVar[str] = r"(?s:TeamViewer(?>.*?_Logfile).*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TeamViewerLogsTeamViewerConfigurationFiles2(KapeTarget):
    """
    Includes miscellaneous config files
    """

    name: ClassVar[str] = "TeamViewer Configuration Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\TeamViewer\\MRU\\RemoteSupport\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TeamViewerLogs(KapeTargetConfiguration):
    """
    Author: Hadar Yudovich

    Version: 1.1

    ID: 6f2cd531-1f4b-4f0b-aa96-2426621b0a14

    TeamViewer Logs
    """

    name: ClassVar[str] = "TeamViewerLogs"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        TeamViewerLogsTeamViewerConnectionLogs0,
        TeamViewerLogsTeamViewerApplicationLogs1,
        TeamViewerLogsTeamViewerConfigurationFiles2,
    ]


class BraveBrowserBookmarks0(KapeTarget):
    name: ClassVar[str] = "Bookmarks"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Bookmarks.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserCookies1(KapeTarget):
    name: ClassVar[str] = "Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Cookies.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserCurrentSession2(KapeTarget):
    name: ClassVar[str] = "Current Session"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Current\ Session)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserCurrentTabs3(KapeTarget):
    name: ClassVar[str] = "Current Tabs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Current\ Tabs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserDownloadMetadata4(KapeTarget):
    name: ClassVar[str] = "Download Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:DownloadMetadata)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserFavicons5(KapeTarget):
    name: ClassVar[str] = "Favicons"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Favicons.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserHistory6(KapeTarget):
    name: ClassVar[str] = "History"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:History.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserSessionsFolder7(KapeTarget):
    name: ClassVar[str] = "Sessions Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Sessions\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserLoginData8(KapeTarget):
    name: ClassVar[str] = "Login Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Login\ Data)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserNetworkActionPredictor9(KapeTarget):
    name: ClassVar[str] = "Network Action Predictor"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Network\ Action\ Predictor)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserNetworkPersistentState10(KapeTarget):
    name: ClassVar[str] = "Network Persistent State"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Network\ Persistent\ State)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserPreferences11(KapeTarget):
    name: ClassVar[str] = "Preferences"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Preferences)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserQuotaManager12(KapeTarget):
    name: ClassVar[str] = "Quota Manager"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:QuotaManager)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserReportingandNEL13(KapeTarget):
    name: ClassVar[str] = "Reporting and NEL"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Reporting\ and\ NEL)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserShortcuts14(KapeTarget):
    name: ClassVar[str] = "Shortcuts"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Shortcuts.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserPublisherInfoDBBraveRewards15(KapeTarget):
    """
    SQLite Database related to "Brave Rewards" containing an event_log table
    """

    name: ClassVar[str] = "Publisher Info DB/Brave Rewards"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:publisher_info_db.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserTopSites16(KapeTarget):
    name: ClassVar[str] = "Top Sites"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Top\ Sites.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserVisitedLinks17(KapeTarget):
    name: ClassVar[str] = "Visited Links"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Visited\ Links.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserWebData18(KapeTarget):
    name: ClassVar[str] = "Web Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Web\ Data.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowserSecurePreferences19(KapeTarget):
    """
    Contains additional preferences data
    """

    name: ClassVar[str] = "Secure Preferences"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Secure\ Preferences.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BraveBrowser(KapeTargetConfiguration):
    """
    Author: Cassie Doemel

    Version: 1.0

    ID: 3801a96f-f402-41fd-8bde-e04e9ea7c7c2

    Brave Browser
    """

    name: ClassVar[str] = "BraveBrowser"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        BraveBrowserBookmarks0,
        BraveBrowserCookies1,
        BraveBrowserCurrentSession2,
        BraveBrowserCurrentTabs3,
        BraveBrowserDownloadMetadata4,
        BraveBrowserFavicons5,
        BraveBrowserHistory6,
        BraveBrowserSessionsFolder7,
        BraveBrowserLoginData8,
        BraveBrowserNetworkActionPredictor9,
        BraveBrowserNetworkPersistentState10,
        BraveBrowserPreferences11,
        BraveBrowserQuotaManager12,
        BraveBrowserReportingandNEL13,
        BraveBrowserShortcuts14,
        BraveBrowserPublisherInfoDBBraveRewards15,
        BraveBrowserTopSites16,
        BraveBrowserVisitedLinks17,
        BraveBrowserWebData18,
        BraveBrowserSecurePreferences19,
    ]


class BrowserCacheChromeCacheFolder0(KapeTarget):
    name: ClassVar[str] = "Chrome Cache Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\Cache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BrowserCacheChromiumEdgeCacheFolder1(KapeTarget):
    name: ClassVar[str] = "Chromium Edge Cache Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\Cache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BrowserCacheFirefoxCacheFolder2(KapeTarget):
    name: ClassVar[str] = "Firefox Cache Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BrowserCacheIE910Cache3(KapeTarget):
    name: ClassVar[str] = "IE 9/10 Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\Temporary Internet Files\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BrowserCacheIEIndexdattempinternetfiles4(KapeTarget):
    name: ClassVar[str] = "IE Index.dat temp internet files"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Temporary Internet Files\\Content.IE5\\"
    )
    regex: ClassVar[str] = r"(?s:index\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BrowserCacheIE11Cache5(KapeTarget):
    name: ClassVar[str] = "IE 11 Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\INetCache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BrowserCacheEdgeWebcacheV01dat6(KapeTarget):
    name: ClassVar[str] = "Edge WebcacheV01.dat"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\WebCache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BrowserCacheBraveCacheFolder7(KapeTarget):
    name: ClassVar[str] = "Brave Cache Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%users%\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Cache\\Cache_Data"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BrowserCache(KapeTargetConfiguration):
    """
    Author: Bjorn Vanhaeren

    Version: 1.1

    ID: bbb89525-6b8d-41f6-acdf-a4f513455703

    Browser Caches
    """

    name: ClassVar[str] = "BrowserCache"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        BrowserCacheChromeCacheFolder0,
        BrowserCacheChromiumEdgeCacheFolder1,
        BrowserCacheFirefoxCacheFolder2,
        BrowserCacheIE910Cache3,
        BrowserCacheIEIndexdattempinternetfiles4,
        BrowserCacheIE11Cache5,
        BrowserCacheEdgeWebcacheV01dat6,
        BrowserCacheBraveCacheFolder7,
    ]


class ChromeChromebookmarksXP0(KapeTarget):
    name: ClassVar[str] = "Chrome bookmarks XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Bookmarks.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeCookiesXP1(KapeTarget):
    name: ClassVar[str] = "Chrome Cookies XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Cookies.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeCurrentSessionXP2(KapeTarget):
    name: ClassVar[str] = "Chrome Current Session XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Current\ Session)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeCurrentTabsXP3(KapeTarget):
    name: ClassVar[str] = "Chrome Current Tabs XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Current\ Tabs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeFaviconsXP4(KapeTarget):
    name: ClassVar[str] = "Chrome Favicons XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Favicons.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeHistoryXP5(KapeTarget):
    name: ClassVar[str] = "Chrome History XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:History.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeLastSessionXP6(KapeTarget):
    name: ClassVar[str] = "Chrome Last Session XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Last\ Session)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeLastTabsXP7(KapeTarget):
    name: ClassVar[str] = "Chrome Last Tabs XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Last\ Tabs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeLoginDataXP8(KapeTarget):
    name: ClassVar[str] = "Chrome Login Data XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Login\ Data)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromePreferencesXP9(KapeTarget):
    name: ClassVar[str] = "Chrome Preferences XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Preferences)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeShortcutsXP10(KapeTarget):
    name: ClassVar[str] = "Chrome Shortcuts XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Shortcuts.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeTopSitesXP11(KapeTarget):
    name: ClassVar[str] = "Chrome Top Sites XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Top\ Sites.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeVisitedLinksXP12(KapeTarget):
    name: ClassVar[str] = "Chrome Visited Links XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Visited\ Links)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeWebDataXP13(KapeTarget):
    name: ClassVar[str] = "Chrome Web Data XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Web\ Data.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromebookmarks14(KapeTarget):
    name: ClassVar[str] = "Chrome bookmarks"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Bookmarks.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeCookies15(KapeTarget):
    name: ClassVar[str] = "Chrome Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Cookies.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeCurrentSession16(KapeTarget):
    name: ClassVar[str] = "Chrome Current Session"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Current\ Session)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeCurrentTabs17(KapeTarget):
    name: ClassVar[str] = "Chrome Current Tabs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Current\ Tabs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeDownloadMetadata18(KapeTarget):
    name: ClassVar[str] = "Chrome Download Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:DownloadMetadata)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeExtensionCookies19(KapeTarget):
    name: ClassVar[str] = "Chrome Extension Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Extension\ Cookies)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeFavicons20(KapeTarget):
    name: ClassVar[str] = "Chrome Favicons"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Favicons.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeHistory21(KapeTarget):
    name: ClassVar[str] = "Chrome History"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:History.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeLastSession22(KapeTarget):
    name: ClassVar[str] = "Chrome Last Session"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Last\ Session)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeLastTabs23(KapeTarget):
    name: ClassVar[str] = "Chrome Last Tabs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Last\ Tabs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeSessionsFolder24(KapeTarget):
    name: ClassVar[str] = "Chrome Sessions Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\Sessions\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeLoginData25(KapeTarget):
    name: ClassVar[str] = "Chrome Login Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Login\ Data)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeMediaHistory26(KapeTarget):
    name: ClassVar[str] = "Chrome Media History"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Media\ History.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeNetworkActionPredictor27(KapeTarget):
    name: ClassVar[str] = "Chrome Network Action Predictor"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Network\ Action\ Predictor)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeNetworkPersistentState28(KapeTarget):
    name: ClassVar[str] = "Chrome Network Persistent State"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Network\ Persistent\ State)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromePreferences29(KapeTarget):
    name: ClassVar[str] = "Chrome Preferences"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Preferences)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeQuotaManager30(KapeTarget):
    name: ClassVar[str] = "Chrome Quota Manager"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:QuotaManager)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeReportingandNEL31(KapeTarget):
    name: ClassVar[str] = "Chrome Reporting and NEL"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Reporting\ and\ NEL)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeShortcuts32(KapeTarget):
    name: ClassVar[str] = "Chrome Shortcuts"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Shortcuts.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeTopSites33(KapeTarget):
    name: ClassVar[str] = "Chrome Top Sites"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Top\ Sites.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeTrustTokens34(KapeTarget):
    name: ClassVar[str] = "Chrome Trust Tokens"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Trust\ Tokens.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeSyncDataDatabase35(KapeTarget):
    name: ClassVar[str] = "Chrome SyncData Database"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\Sync Data"
    )
    regex: ClassVar[str] = r"(?s:SyncData\.sqlite3)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeVisitedLinks36(KapeTarget):
    name: ClassVar[str] = "Chrome Visited Links"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Visited\ Links)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeChromeWebData37(KapeTarget):
    name: ClassVar[str] = "Chrome Web Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Web\ Data.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeWindowsProtectFolder38(KapeTarget):
    """
    Required for offline decryption
    """

    name: ClassVar[str] = "Windows Protect Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Protect\\*\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Chrome(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman and Andrew Rathbun

    Version: 1.2

    ID: a56d0a8f-3229-489e-aea7-353d1f6f9639

    Chrome
    """

    name: ClassVar[str] = "Chrome"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ChromeChromebookmarksXP0,
        ChromeChromeCookiesXP1,
        ChromeChromeCurrentSessionXP2,
        ChromeChromeCurrentTabsXP3,
        ChromeChromeFaviconsXP4,
        ChromeChromeHistoryXP5,
        ChromeChromeLastSessionXP6,
        ChromeChromeLastTabsXP7,
        ChromeChromeLoginDataXP8,
        ChromeChromePreferencesXP9,
        ChromeChromeShortcutsXP10,
        ChromeChromeTopSitesXP11,
        ChromeChromeVisitedLinksXP12,
        ChromeChromeWebDataXP13,
        ChromeChromebookmarks14,
        ChromeChromeCookies15,
        ChromeChromeCurrentSession16,
        ChromeChromeCurrentTabs17,
        ChromeChromeDownloadMetadata18,
        ChromeChromeExtensionCookies19,
        ChromeChromeFavicons20,
        ChromeChromeHistory21,
        ChromeChromeLastSession22,
        ChromeChromeLastTabs23,
        ChromeChromeSessionsFolder24,
        ChromeChromeLoginData25,
        ChromeChromeMediaHistory26,
        ChromeChromeNetworkActionPredictor27,
        ChromeChromeNetworkPersistentState28,
        ChromeChromePreferences29,
        ChromeChromeQuotaManager30,
        ChromeChromeReportingandNEL31,
        ChromeChromeShortcuts32,
        ChromeChromeTopSites33,
        ChromeChromeTrustTokens34,
        ChromeChromeSyncDataDatabase35,
        ChromeChromeVisitedLinks36,
        ChromeChromeWebData37,
        ChromeWindowsProtectFolder38,
    ]


class EdgeEdgefolder0(KapeTarget):
    name: ClassVar[str] = "Edge folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Edge(KapeTargetConfiguration):
    """
    Author: Phill Moore

    Version: 1.0

    ID: c72bd45c-2a24-4df9-aa0b-3d7048c90337

    Edge
    """

    name: ClassVar[str] = "Edge"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [EdgeEdgefolder0]


class EdgeChromiumEdgebookmarks0(KapeTarget):
    name: ClassVar[str] = "Edge bookmarks"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Bookmarks.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeCollections1(KapeTarget):
    name: ClassVar[str] = "Edge Collections"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\Collections"
    )
    regex: ClassVar[str] = r"(?s:collectionsSQLite)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeCookies2(KapeTarget):
    name: ClassVar[str] = "Edge Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Cookies.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeCurrentSession3(KapeTarget):
    name: ClassVar[str] = "Edge Current Session"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Current\ Session)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeCurrentTabs4(KapeTarget):
    name: ClassVar[str] = "Edge Current Tabs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Current\ Tabs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeFavicons5(KapeTarget):
    name: ClassVar[str] = "Edge Favicons"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Favicons.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeHistory6(KapeTarget):
    name: ClassVar[str] = "Edge History"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:History.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeLastSession7(KapeTarget):
    name: ClassVar[str] = "Edge Last Session"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Last\ Session)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeLastTabs8(KapeTarget):
    name: ClassVar[str] = "Edge Last Tabs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Last\ Tabs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeSessionsFolder9(KapeTarget):
    name: ClassVar[str] = "Edge Sessions Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\Sessions\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeLoginData10(KapeTarget):
    name: ClassVar[str] = "Edge Login Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Login\ Data)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeMediaHistory11(KapeTarget):
    name: ClassVar[str] = "Edge Media History"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Media\ History.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeNetworkActionPredictor12(KapeTarget):
    name: ClassVar[str] = "Edge Network Action Predictor"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Network\ Action\ Predictor)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgePreferences13(KapeTarget):
    name: ClassVar[str] = "Edge Preferences"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Preferences)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeShortcuts14(KapeTarget):
    name: ClassVar[str] = "Edge Shortcuts"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Shortcuts.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeTopSites15(KapeTarget):
    name: ClassVar[str] = "Edge Top Sites"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Top\ Sites.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeSyncDataDatabase16(KapeTarget):
    name: ClassVar[str] = "Edge SyncData Database"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\Sync Data"
    )
    regex: ClassVar[str] = r"(?s:SyncData\.sqlite3)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeBookmarks17(KapeTarget):
    name: ClassVar[str] = "Edge Bookmarks"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Bookmarks.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeVisitedLinks18(KapeTarget):
    name: ClassVar[str] = "Edge Visited Links"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Visited\ Links)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeWebData19(KapeTarget):
    name: ClassVar[str] = "Edge Web Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Web\ Data.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumWindowsProtectFolder20(KapeTarget):
    """
    Required for offline DPAPI decryption
    """

    name: ClassVar[str] = "Windows Protect Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Protect\\*\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromiumEdgeSnapshotsFolder21(KapeTarget):
    """
    Grabs folder that appears to have snapshots of Edge Chromium SQLite DBs
    organized by version #. In testing, there were 3 previous versions of Edge
    Chromium separated into different folders
    """

    name: ClassVar[str] = "Edge Snapshots Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\Snapshots\\*\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EdgeChromium(KapeTargetConfiguration):
    """
    Author: Chad Tilbury and Andrew Rathbun

    Version: 1.1

    ID: 2844dba2-fb47-466c-8d57-dab2bc02294f

    Microsoft Edge Chromium Artifacts
    """

    name: ClassVar[str] = "EdgeChromium"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        EdgeChromiumEdgebookmarks0,
        EdgeChromiumEdgeCollections1,
        EdgeChromiumEdgeCookies2,
        EdgeChromiumEdgeCurrentSession3,
        EdgeChromiumEdgeCurrentTabs4,
        EdgeChromiumEdgeFavicons5,
        EdgeChromiumEdgeHistory6,
        EdgeChromiumEdgeLastSession7,
        EdgeChromiumEdgeLastTabs8,
        EdgeChromiumEdgeSessionsFolder9,
        EdgeChromiumEdgeLoginData10,
        EdgeChromiumEdgeMediaHistory11,
        EdgeChromiumEdgeNetworkActionPredictor12,
        EdgeChromiumEdgePreferences13,
        EdgeChromiumEdgeShortcuts14,
        EdgeChromiumEdgeTopSites15,
        EdgeChromiumEdgeSyncDataDatabase16,
        EdgeChromiumEdgeBookmarks17,
        EdgeChromiumEdgeVisitedLinks18,
        EdgeChromiumEdgeWebData19,
        EdgeChromiumWindowsProtectFolder20,
        EdgeChromiumEdgeSnapshotsFolder21,
    ]


class FirefoxAddons0(KapeTarget):
    name: ClassVar[str] = "Addons"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:addons\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxBookmarks1(KapeTarget):
    name: ClassVar[str] = "Bookmarks"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\weave\\"
    )
    regex: ClassVar[str] = r"(?s:bookmarks\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxBookmarks2(KapeTarget):
    name: ClassVar[str] = "Bookmarks"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\bookmarkbackups"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxCookies3(KapeTarget):
    name: ClassVar[str] = "Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:cookies\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxCookies4(KapeTarget):
    name: ClassVar[str] = "Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:firefox_cookies\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxDownloads5(KapeTarget):
    name: ClassVar[str] = "Downloads"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:downloads\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxExtensions6(KapeTarget):
    name: ClassVar[str] = "Extensions"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:extensions\.json)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxFavicons7(KapeTarget):
    name: ClassVar[str] = "Favicons"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:favicons\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxFormhistory8(KapeTarget):
    name: ClassVar[str] = "Form history"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:formhistory\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxPermissions9(KapeTarget):
    name: ClassVar[str] = "Permissions"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:permissions\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxPlaces10(KapeTarget):
    name: ClassVar[str] = "Places"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:places\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxProtections11(KapeTarget):
    name: ClassVar[str] = "Protections"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:protections\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxSearch12(KapeTarget):
    name: ClassVar[str] = "Search"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:search\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxSignons13(KapeTarget):
    name: ClassVar[str] = "Signons"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:signons\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxStorageSync14(KapeTarget):
    name: ClassVar[str] = "Storage Sync"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:storage\-sync\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxWebappstore15(KapeTarget):
    name: ClassVar[str] = "Webappstore"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:webappstore\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxPassword16(KapeTarget):
    name: ClassVar[str] = "Password"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:key.*\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxPassword17(KapeTarget):
    name: ClassVar[str] = "Password"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:signon(?>.*?\.).*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxPassword18(KapeTarget):
    name: ClassVar[str] = "Password"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:logins\.json)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxPreferences19(KapeTarget):
    name: ClassVar[str] = "Preferences"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:prefs\.js)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxSessionstore20(KapeTarget):
    name: ClassVar[str] = "Sessionstore"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:sessionstore.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxSessionstoreFolder21(KapeTarget):
    name: ClassVar[str] = "Sessionstore Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\sessionstore-backups"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxPlacesXP22(KapeTarget):
    name: ClassVar[str] = "Places XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:places\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxDownloadsXP23(KapeTarget):
    name: ClassVar[str] = "Downloads XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:downloads\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxFormhistoryXP24(KapeTarget):
    name: ClassVar[str] = "Form history XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:formhistory\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxCookiesXP25(KapeTarget):
    name: ClassVar[str] = "Cookies XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:cookies\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxSignonsXP26(KapeTarget):
    name: ClassVar[str] = "Signons XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:signons\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxWebappstoreXP27(KapeTarget):
    name: ClassVar[str] = "Webappstore XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:webappstore\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxFaviconsXP28(KapeTarget):
    name: ClassVar[str] = "Favicons XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:favicons\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxAddonsXP29(KapeTarget):
    name: ClassVar[str] = "Addons XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:addons\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxSearchXP30(KapeTarget):
    name: ClassVar[str] = "Search XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:search\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxPasswordXP31(KapeTarget):
    name: ClassVar[str] = "Password XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:key.*\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxPasswordXP32(KapeTarget):
    name: ClassVar[str] = "Password XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:signon(?>.*?\.).*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxPasswordXP33(KapeTarget):
    name: ClassVar[str] = "Password XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:logins\.json)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FirefoxSessionstoreXP34(KapeTarget):
    name: ClassVar[str] = "Sessionstore XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:sessionstore.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Firefox(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman and Andrew Rathbun

    Version: 1.2

    ID: 28801734-b95a-47e7-b84f-4ebd0c104862

    Firefox
    """

    name: ClassVar[str] = "Firefox"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        FirefoxAddons0,
        FirefoxBookmarks1,
        FirefoxBookmarks2,
        FirefoxCookies3,
        FirefoxCookies4,
        FirefoxDownloads5,
        FirefoxExtensions6,
        FirefoxFavicons7,
        FirefoxFormhistory8,
        FirefoxPermissions9,
        FirefoxPlaces10,
        FirefoxProtections11,
        FirefoxSearch12,
        FirefoxSignons13,
        FirefoxStorageSync14,
        FirefoxWebappstore15,
        FirefoxPassword16,
        FirefoxPassword17,
        FirefoxPassword18,
        FirefoxPreferences19,
        FirefoxSessionstore20,
        FirefoxSessionstoreFolder21,
        FirefoxPlacesXP22,
        FirefoxDownloadsXP23,
        FirefoxFormhistoryXP24,
        FirefoxCookiesXP25,
        FirefoxSignonsXP26,
        FirefoxWebappstoreXP27,
        FirefoxFaviconsXP28,
        FirefoxAddonsXP29,
        FirefoxSearchXP30,
        FirefoxPasswordXP31,
        FirefoxPasswordXP32,
        FirefoxPasswordXP33,
        FirefoxSessionstoreXP34,
    ]


class InternetExplorerIndexdatHistory0(KapeTarget):
    name: ClassVar[str] = "Index.dat History"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\History\\History.IE5\\"
    )
    regex: ClassVar[str] = r"(?s:index\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class InternetExplorerIndexdatHistorysubdirectory1(KapeTarget):
    name: ClassVar[str] = "Index.dat History subdirectory"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\History\\History.IE5\\*\\"
    )
    regex: ClassVar[str] = r"(?s:index\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class InternetExplorerIndexdatcookies2(KapeTarget):
    name: ClassVar[str] = "Index.dat cookies"
    base_path: ClassVar[Path] = Path("C:\\Documents and Settings\\%user%\\Cookies\\")
    regex: ClassVar[str] = r"(?s:index\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class InternetExplorerIndexdatUserData3(KapeTarget):
    name: ClassVar[str] = "Index.dat UserData"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Microsoft\\Internet Explorer\\UserData\\"
    )
    regex: ClassVar[str] = r"(?s:index\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class InternetExplorerIndexdatOfficeXP4(KapeTarget):
    name: ClassVar[str] = "Index.dat Office XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Microsoft\\Office\\Recent\\"
    )
    regex: ClassVar[str] = r"(?s:index\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class InternetExplorerIndexdatOffice5(KapeTarget):
    name: ClassVar[str] = "Index.dat Office"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Office\\Recent\\"
    )
    regex: ClassVar[str] = r"(?s:index\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class InternetExplorerLocalInternetExplorerfolder6(KapeTarget):
    name: ClassVar[str] = "Local Internet Explorer folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Internet Explorer\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class InternetExplorerRoamingInternetExplorerfolder7(KapeTarget):
    name: ClassVar[str] = "Roaming Internet Explorer folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Internet Explorer\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class InternetExplorerIE910History8(KapeTarget):
    name: ClassVar[str] = "IE 9/10 History"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\History\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class InternetExplorerIE910Cookies9(KapeTarget):
    name: ClassVar[str] = "IE 9/10 Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\Cookies\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class InternetExplorerIE910DownloadHistory10(KapeTarget):
    name: ClassVar[str] = "IE 9/10 Download History"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\IEDownloadHistory\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class InternetExplorerIE11Metadata11(KapeTarget):
    name: ClassVar[str] = "IE 11 Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\WebCache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class InternetExplorerIE11Cookies12(KapeTarget):
    name: ClassVar[str] = "IE 11 Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\INetCookies\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class InternetExplorer(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: b1e1d79b-324d-4587-a002-cc81144588ff

    Internet Explorer
    """

    name: ClassVar[str] = "InternetExplorer"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        InternetExplorerIndexdatHistory0,
        InternetExplorerIndexdatHistorysubdirectory1,
        InternetExplorerIndexdatcookies2,
        InternetExplorerIndexdatUserData3,
        InternetExplorerIndexdatOfficeXP4,
        InternetExplorerIndexdatOffice5,
        InternetExplorerLocalInternetExplorerfolder6,
        InternetExplorerRoamingInternetExplorerfolder7,
        InternetExplorerIE910History8,
        InternetExplorerIE910Cookies9,
        InternetExplorerIE910DownloadHistory10,
        InternetExplorerIE11Metadata11,
        InternetExplorerIE11Cookies12,
    ]


class OperaOperaLocalFolder0(KapeTarget):
    """
    Grabs entire contents of the Opera AppData/Local folder
    """

    name: ClassVar[str] = "Opera - Local Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Opera Software\\Opera Stable"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OperaOperaRoamingFolder1(KapeTarget):
    """
    Grabs entire contents of the Opera AppData/Roaming folder
    """

    name: ClassVar[str] = "Opera - Roaming Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Opera Software\\Opera Stable"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Opera(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 29e3154b-7d33-4f74-8d0c-c4b8980cf989

    Opera
    """

    name: ClassVar[str] = "Opera"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        OperaOperaLocalFolder0,
        OperaOperaRoamingFolder1,
    ]


class PuffinSecureBrowserPuffindatadb0(KapeTarget):
    """
    Grabs an important database file that contains browser history
    """

    name: ClassVar[str] = "Puffin - data.db"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\PuffinSecureBrowser"
    )
    regex: ClassVar[str] = r"(?s:data\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class PuffinSecureBrowserPuffinAutocompleteData1(KapeTarget):
    """
    Grabs a file that stores autocomplete data
    """

    name: ClassVar[str] = "Puffin - Autocomplete Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\PuffinSecureBrowser"
    )
    regex: ClassVar[str] = r"(?s:autocompletes\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class PuffinSecureBrowserPuffinPasswordFormsData2(KapeTarget):
    """
    Grabs a file that stores some saved password data
    """

    name: ClassVar[str] = "Puffin - Password Forms Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\PuffinSecureBrowser"
    )
    regex: ClassVar[str] = r"(?s:passwordForms\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class PuffinSecureBrowserPuffinPasswordEncrypted3(KapeTarget):
    """
    Grabs a file that stores passwords in an encrypted format
    """

    name: ClassVar[str] = "Puffin - Password (Encrypted)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\PuffinSecureBrowser"
    )
    regex: ClassVar[str] = r"(?s:credential\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class PuffinSecureBrowserPuffinSubscriptionData4(KapeTarget):
    """
    Grabs a file that stores the user's email address that's associated with
    their Puffin subscription
    """

    name: ClassVar[str] = "Puffin - Subscription Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\PuffinSecureBrowser"
    )
    regex: ClassVar[str] = r"(?s:subscription)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class PuffinSecureBrowserPuffinCookies5(KapeTarget):
    """
    Grabs a file that stores information related to cookies
    """

    name: ClassVar[str] = "Puffin - Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\PuffinSecureBrowser"
    )
    regex: ClassVar[str] = r"(?s:cookies\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class PuffinSecureBrowserPuffinImageCache6(KapeTarget):
    """
    Grabs a directory that caches images from websites visited
    """

    name: ClassVar[str] = "Puffin - Image Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\PuffinSecureBrowser\\image_cache"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class PuffinSecureBrowser(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 0adfdd1e-16e7-4b2e-808a-8643f42ebe16

    Puffin Secure Browser
    """

    name: ClassVar[str] = "PuffinSecureBrowser"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        PuffinSecureBrowserPuffindatadb0,
        PuffinSecureBrowserPuffinAutocompleteData1,
        PuffinSecureBrowserPuffinPasswordFormsData2,
        PuffinSecureBrowserPuffinPasswordEncrypted3,
        PuffinSecureBrowserPuffinSubscriptionData4,
        PuffinSecureBrowserPuffinCookies5,
        PuffinSecureBrowserPuffinImageCache6,
    ]


class IRCClientsHexChat0(KapeTarget):
    name: ClassVar[str] = "HexChat"
    base_path: ClassVar[Path] = Path("HexChat.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class IRCClientsIceChat1(KapeTarget):
    name: ClassVar[str] = "IceChat"
    base_path: ClassVar[Path] = Path("IceChat.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class IRCClientsmIRC2(KapeTarget):
    name: ClassVar[str] = "mIRC"
    base_path: ClassVar[Path] = Path("mIRC.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class IRCClients(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 295e5eeb-a836-4ff8-88b7-1caf47c95701

    IRC Clients
    """

    name: ClassVar[str] = "IRCClients"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        IRCClientsHexChat0,
        IRCClientsIceChat1,
        IRCClientsmIRC2,
    ]


class WebBrowsersChrome0(KapeTarget):
    name: ClassVar[str] = "Chrome"
    base_path: ClassVar[Path] = Path("Chrome.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WebBrowsersEdge1(KapeTarget):
    name: ClassVar[str] = "Edge"
    base_path: ClassVar[Path] = Path("Edge.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WebBrowsersEdgeChromium2(KapeTarget):
    name: ClassVar[str] = "Edge Chromium"
    base_path: ClassVar[Path] = Path("EdgeChromium.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WebBrowsersFirefox3(KapeTarget):
    name: ClassVar[str] = "Firefox"
    base_path: ClassVar[Path] = Path("Firefox.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WebBrowsersInternetExplorer4(KapeTarget):
    name: ClassVar[str] = "Internet Explorer"
    base_path: ClassVar[Path] = Path("InternetExplorer.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WebBrowsersOpera5(KapeTarget):
    name: ClassVar[str] = "Opera"
    base_path: ClassVar[Path] = Path("Opera.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WebBrowsersPuffinSecureBrowser6(KapeTarget):
    name: ClassVar[str] = "Puffin Secure Browser"
    base_path: ClassVar[Path] = Path("PuffinSecureBrowser.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WebBrowsersBraveBrowser7(KapeTarget):
    name: ClassVar[str] = "Brave Browser"
    base_path: ClassVar[Path] = Path("BraveBrowser.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WebBrowsers(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.0

    ID: e4ffb938-dcc0-4d91-9c77-3aa303d38512

    Web browser history, bookmarks, etc.
    """

    name: ClassVar[str] = "WebBrowsers"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WebBrowsersChrome0,
        WebBrowsersEdge1,
        WebBrowsersEdgeChromium2,
        WebBrowsersFirefox3,
        WebBrowsersInternetExplorer4,
        WebBrowsersOpera5,
        WebBrowsersPuffinSecureBrowser6,
        WebBrowsersBraveBrowser7,
    ]
