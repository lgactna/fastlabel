"""
Auto-generated classes from the .tkape files for the Apps category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class _1Password1PasswordDatabase0(KapeTarget):
    """
    Database which holds information about 1Password installation, such as
    accounts, categories, settings and more
    """

    name: ClassVar[str] = "1Password Database"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\1password\\data"
    )
    regex: ClassVar[str] = r"(?s:1Password10\.sqlite)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class _1Password1PasswordBackupDatabases1(KapeTarget):
    """
    Backups of 1Password Database
    """

    name: ClassVar[str] = "1Password Backup Databases"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\1password\\backups"
    )
    regex: ClassVar[str] = r"(?s:1Password10\.sqlite)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class _1Password1PasswordLogs2(KapeTarget):
    """
    Log of usage of 1Password - can be useful for identifying periods of user
    activity
    """

    name: ClassVar[str] = "1Password Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\1password\\logs"
    )
    regex: ClassVar[str] = r"(?s:.*\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class _1Password(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 41a37dbf-3326-4d61-a9c7-7aa38d621973

    1Password Password Manager
    """

    name: ClassVar[str] = "1Password"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        _1Password1PasswordDatabase0,
        _1Password1PasswordBackupDatabases1,
        _1Password1PasswordLogs2,
    ]


class _4KVideoDownloader4KVideoDownloader0(KapeTarget):
    """
    Grabs database(s) that stores user download history
    """

    name: ClassVar[str] = "4K Video Downloader"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\4kdownload.com\\4K Video Downloader\\4K Video Downloader"
    )
    regex: ClassVar[str] = r"(?s:.*\.sqlite)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class _4KVideoDownloader(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: e33d4392-459b-459e-82e0-d9c624adbfbc

    4K Video Downloader
    """

    name: ClassVar[str] = "4KVideoDownloader"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [_4KVideoDownloader4KVideoDownloader0]


class AceTextAceTextClipboardHistory0(KapeTarget):
    """
    Locates the Clipboard history for AceText
    """

    name: ClassVar[str] = "AceText - Clipboard History"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Documents")
    regex: ClassVar[str] = r"(?s:.*\.atc)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AceText(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 0b7b9e23-5653-4075-9862-48cbdf1dda8a

    AceText
    """

    name: ClassVar[str] = "AceText"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [AceTextAceTextClipboardHistory0]


class AcronisTrueImageAcronisTrueImageLogs0(KapeTarget):
    """
    Copies out all log files
    """

    name: ClassVar[str] = "Acronis True Image - Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Acronis\\TrueImageHome\\Logs\\ti_demon\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AcronisTrueImageAcronisTrueImageDatabaseFiles1(KapeTarget):
    """
    Copies out the Database folder which appears to have important information
    """

    name: ClassVar[str] = "Acronis True Image - Database Files"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Acronis\\TrueImageHome\\Database"
    )
    regex: ClassVar[str] = r"(?s:archives\.db.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AcronisTrueImageAcronisTrueImageScriptsFolder2(KapeTarget):
    """
    Copies out all scripts files
    """

    name: ClassVar[str] = "Acronis True Image - Scripts Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Acronis\\TrueImageHome\\Scripts\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AcronisTrueImage(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 4f984e18-81fb-4520-9a01-69bf77a0f459

    Acronis True Image
    """

    name: ClassVar[str] = "AcronisTrueImage"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        AcronisTrueImageAcronisTrueImageLogs0,
        AcronisTrueImageAcronisTrueImageDatabaseFiles1,
        AcronisTrueImageAcronisTrueImageScriptsFolder2,
    ]


class BoxDriveMetadataBoxDriveApplicationMetadata0(KapeTarget):
    name: ClassVar[str] = "Box Drive Application Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Box\\Box\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BoxDriveMetadataBoxSyncApplicationMetadata1(KapeTarget):
    name: ClassVar[str] = "Box Sync Application Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Box Sync\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BoxDriveMetadata(KapeTargetConfiguration):
    """
    Author: Chad Tilbury

    Version: 1.1

    ID: 00d36d65-dbbc-45f5-801e-c78efb3dfcfa

    Box Cloud Storage Metadata
    """

    name: ClassVar[str] = "BoxDrive_Metadata"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        BoxDriveMetadataBoxDriveApplicationMetadata0,
        BoxDriveMetadataBoxSyncApplicationMetadata1,
    ]


class BoxDriveUserFilesBoxDriveUserFiles0(KapeTarget):
    """
    Caution! This target will collect Box Drive contents from the local drive
    AND on-demand cloud files. Ensure your scope of authority permits cloud
    collections before use or isolate system from network
    """

    name: ClassVar[str] = "Box Drive User Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Box\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BoxDriveUserFilesBoxSyncUserFiles1(KapeTarget):
    name: ClassVar[str] = "Box Sync User Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Box Sync\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BoxDriveUserFiles(KapeTargetConfiguration):
    """
    Author: Chad Tilbury

    Version: 1.0

    ID: 6c6cef0b-4213-4903-acc4-d85430226a19

    Box Cloud Storage Files
    """

    name: ClassVar[str] = "BoxDrive_UserFiles"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        BoxDriveUserFilesBoxDriveUserFiles0,
        BoxDriveUserFilesBoxSyncUserFiles1,
    ]


class ClipboardMasterClipboardMasterClipboardHistoryText0(KapeTarget):
    """
    Locates the user’s clipboard history (text) for ClipboardMaster
    """

    name: ClassVar[str] = "ClipboardMaster - Clipboard History - Text"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Jumping Bytes\\ClipboardMaster\\"
    )
    regex: ClassVar[str] = r"(?s:Clipboard\.clm4)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ClipboardMasterClipboardMasterClipboardHistoryImages1(KapeTarget):
    """
    Locates the user’s clipboard history (images) for ClipboardMaster
    """

    name: ClassVar[str] = "ClipboardMaster - Clipboard History - Images"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Jumping Bytes\\ClipboardMaster\\pics\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ClipboardMasterClipboardMasterClipboardHistoryBackups2(KapeTarget):
    """
    Locates the user’s clipboard history (backups) for ClipboardMaster
    """

    name: ClassVar[str] = "ClipboardMaster - Clipboard History - Backups"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Jumping Bytes\\ClipboardMaster\\"
    )
    regex: ClassVar[str] = r"(?s:Clipboard\.clm4\.ba.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ClipboardMaster(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 43decd24-2ab6-40cc-9b78-23c7f720906b

    ClipboardMaster
    """

    name: ClassVar[str] = "ClipboardMaster"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ClipboardMasterClipboardMasterClipboardHistoryText0,
        ClipboardMasterClipboardMasterClipboardHistoryImages1,
        ClipboardMasterClipboardMasterClipboardHistoryBackups2,
    ]


class DirectoryOpusDirectoryOpus0(KapeTarget):
    """
    Locates .osd file which contains names of folders that have been renamed
    manually by the user.
    """

    name: ClassVar[str] = "Directory Opus"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\GPSoftware\\Directory Opus\\State Data\\MRU\\"
    )
    regex: ClassVar[str] = r"(?s:rename_folders\.osd)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DirectoryOpusDirectoryOpus1(KapeTarget):
    """
    Locates .osd file which contains names of files that have been renamed
    manually by the user.
    """

    name: ClassVar[str] = "Directory Opus"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\GPSoftware\\Directory Opus\\State Data\\MRU\\"
    )
    regex: ClassVar[str] = r"(?s:rename_files\.osd)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DirectoryOpusDirectoryOpus2(KapeTarget):
    """
    Locates .osd file which contains search queries initiated by the user during
    a search for files with contents related to the search query.
    """

    name: ClassVar[str] = "Directory Opus"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\GPSoftware\\Directory Opus\\State Data\\MRU\\"
    )
    regex: ClassVar[str] = r"(?s:find_contains\.osd)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DirectoryOpusDirectoryOpus3(KapeTarget):
    """
    Locates .osd file which contains search queries initiated by the user during
    a search for files with a filename related to the search query.
    """

    name: ClassVar[str] = "Directory Opus"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\GPSoftware\\Directory Opus\\State Data\\MRU\\"
    )
    regex: ClassVar[str] = r"(?s:find_name\.osd)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DirectoryOpusDirectoryOpus4(KapeTarget):
    """
    Locates .osd file which contains file paths related to user activity - not
    exactly sure how these are generated at this time.
    """

    name: ClassVar[str] = "Directory Opus"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\GPSoftware\\Directory Opus\\State Data\\MRU\\"
    )
    regex: ClassVar[str] = r"(?s:find_path\.osd)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DirectoryOpusDirectoryOpus5(KapeTarget):
    """
    Locates .osd file which contains file paths related to recent user activity.
    Effectively the DOpus Shellbags-equivalent. Appears to be for last 10 folder
    visited within the Lister.
    """

    name: ClassVar[str] = "Directory Opus"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\GPSoftware\\Directory Opus\\State Data\\"
    )
    regex: ClassVar[str] = r"(?s:recent\.osd)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DirectoryOpusDirectoryOpus6(KapeTarget):
    """
    Locates .osd file which contains file paths related to the location of the
    backup settings files for Directory Opus.
    """

    name: ClassVar[str] = "Directory Opus"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\GPSoftware\\Directory Opus\\State Data\\"
    )
    regex: ClassVar[str] = r"(?s:backupconfig\.osd)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DirectoryOpusDirectoryOpus7(KapeTarget):
    """
    Locates .osd file which contains file paths related to the location of the
    backup settings files for Directory Opus.
    """

    name: ClassVar[str] = "Directory Opus"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\GPSoftware\\Directory Opus\\Thumbnail Cache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DirectoryOpusDirectoryOpus8(KapeTarget):
    """
    Locates .txt files that will be named with the IP address of the FTP server
    Directory Opus was used to connect to. All-activity.txt will simply be a
    combination of all other .txt files present in this directory.
    """

    name: ClassVar[str] = "Directory Opus"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\GPSoftware\\Directory Opus\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DirectoryOpus(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: 31a9022d-bd2e-4031-97c1-046b51bfcc7d

    Directory Opus
    """

    name: ClassVar[str] = "DirectoryOpus"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        DirectoryOpusDirectoryOpus0,
        DirectoryOpusDirectoryOpus1,
        DirectoryOpusDirectoryOpus2,
        DirectoryOpusDirectoryOpus3,
        DirectoryOpusDirectoryOpus4,
        DirectoryOpusDirectoryOpus5,
        DirectoryOpusDirectoryOpus6,
        DirectoryOpusDirectoryOpus7,
        DirectoryOpusDirectoryOpus8,
    ]


class DoubleCommanderDoubleCommanderhistoryxml0(KapeTarget):
    """
    Locates an .xml file that contains Shellbags-equivalent artifacts that are
    sorted in temporal order from bottom to top.
    """

    name: ClassVar[str] = "Double Commander - history.xml"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\doublecmd\\")
    regex: ClassVar[str] = r"(?s:history\.xml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DoubleCommanderDoubleCommanderdoublecmdxml1(KapeTarget):
    """
    Locates an .xml file that contains Shellbags-equivalent artifacts that are
    sorted in temporal order from top to bottom.
    """

    name: ClassVar[str] = "Double Commander - doublecmd.xml"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\doublecmd\\")
    regex: ClassVar[str] = r"(?s:doublecmd\.xml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DoubleCommanderDoubleCommanderFTPLog2(KapeTarget):
    """
    Locates log files that'll be named with the following naming convention:
    doublecmd_2021-04-03.log.
    """

    name: ClassVar[str] = "Double Commander - FTP Log"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\doublecmd\\")
    regex: ClassVar[str] = r"(?s:doublecmd.*\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DoubleCommanderDoubleCommandermultiarcini3(KapeTarget):
    name: ClassVar[str] = "Double Commander - multiarc.ini"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\doublecmd\\")
    regex: ClassVar[str] = r"(?s:multiarc\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DoubleCommanderDoubleCommandersessionini4(KapeTarget):
    name: ClassVar[str] = "Double Commander - session.ini"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\doublecmd\\")
    regex: ClassVar[str] = r"(?s:session\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DoubleCommanderDoubleCommanderpixmapstxt5(KapeTarget):
    name: ClassVar[str] = "Double Commander - pixmaps.txt"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\doublecmd\\")
    regex: ClassVar[str] = r"(?s:pixmaps\.txt)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DoubleCommanderDoubleCommandershortcutsscf6(KapeTarget):
    name: ClassVar[str] = "Double Commander - shortcuts.scf"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\doublecmd\\")
    regex: ClassVar[str] = r"(?s:shortcuts\.scf)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DoubleCommander(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.2

    ID: 80c608ac-0be4-4bbf-a09e-97d2f6cb90f4

    Double Commander
    """

    name: ClassVar[str] = "DoubleCommander"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        DoubleCommanderDoubleCommanderhistoryxml0,
        DoubleCommanderDoubleCommanderdoublecmdxml1,
        DoubleCommanderDoubleCommanderFTPLog2,
        DoubleCommanderDoubleCommandermultiarcini3,
        DoubleCommanderDoubleCommandersessionini4,
        DoubleCommanderDoubleCommanderpixmapstxt5,
        DoubleCommanderDoubleCommandershortcutsscf6,
    ]


class DropboxMetadataDropboxMetadata0(KapeTarget):
    """
    Getting individual files because folder may contain very large extraneous
    files. Info.json contains user's Dropbox folder location
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Dropbox\\")
    regex: ClassVar[str] = r"(?s:info\.json)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DropboxMetadataDropboxMetadata1(KapeTarget):
    """
    SQLite database which contains the local path of the user's Dropbox folder
    encoded in BASE64.
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Dropbox\\")
    regex: ClassVar[str] = r"(?s:host\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DropboxMetadataDropboxMetadata2(KapeTarget):
    """
    SQLite database containing references to image files at one time present in
    a user’s Dropbox instance.
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Dropbox\\machine_storage"
    )
    regex: ClassVar[str] = r"(?s:tray\-thumbnails\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DropboxMetadataDropboxMetadata3(KapeTarget):
    """
    SQLite database which contains the local path of the user's Dropbox folder
    encoded in BASE64. Decode each line separately, not together.
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Dropbox\\")
    regex: ClassVar[str] = r"(?s:host\.dbx)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DropboxMetadataWindowsProtectFolder4(KapeTarget):
    """
    Required for offline decryption of Dropbox databases
    """

    name: ClassVar[str] = "Windows Protect Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Protect\\*\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DropboxMetadataDropboxMetadata5(KapeTarget):
    """
    instance folder holds multiple SQLite databases related to Dropbox activity
    and contents
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Dropbox\\instance*\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DropboxMetadata(KapeTargetConfiguration):
    """
    Author: Chad Tilbury and Andrew Rathbun

    Version: 1.5

    ID: bc2be151-1ecb-4cba-8c74-11b411fcc7ef

    Dropbox Cloud Storage Metadata
    """

    name: ClassVar[str] = "Dropbox_Metadata"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        DropboxMetadataDropboxMetadata0,
        DropboxMetadataDropboxMetadata1,
        DropboxMetadataDropboxMetadata2,
        DropboxMetadataDropboxMetadata3,
        DropboxMetadataWindowsProtectFolder4,
        DropboxMetadataDropboxMetadata5,
    ]


class DropboxUserFilesDropboxUserFiles0(KapeTarget):
    """
    Default storage location for Dropbox Personal and Business (when using
    wildcard), but can be user-defined. Check info.json file in user Dropbox
    metadata files to identify default folder.
    """

    name: ClassVar[str] = "Dropbox User Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Dropbox*\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DropboxUserFiles(KapeTargetConfiguration):
    """
    Author: Chad Tilbury

    Version: 1.0

    ID: 6ed5ecbe-af8c-46fd-b827-58228824ea34

    Dropbox Cloud Storage Files
    """

    name: ClassVar[str] = "Dropbox_UserFiles"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [DropboxUserFilesDropboxUserFiles0]


class EFCommanderEFCommanderiniFile0(KapeTarget):
    """
    Locates folder where all configuration files reside
    """

    name: ClassVar[str] = "EF Commander - .ini File"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\EFSoftware\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EFCommander(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: e94a00dd-3206-4a2c-aa5c-a69f7a09b7b3

    EF Commander
    """

    name: ClassVar[str] = "EFCommander"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [EFCommanderEFCommanderiniFile0]


class ExchangeCve202126855ExchangeServerModifiedCompiledFiles0(KapeTarget):
    """
    Highly dependent on Exchange configuration
    """

    name: ClassVar[str] = "Exchange Server Modified Compiled Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows\\Microsoft.NET\\Framework*\\v*\\Temporary ASP.NET Files\\"
    )
    regex: ClassVar[str] = r"(?s:Regex:.*\.\\b[a-zA-Z0-9_\-]\{8\}\\b\.compiled)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ExchangeCve202126855ExchangeServerModifiedCompiledFiles1(KapeTarget):
    """
    Highly dependent on Exchange configuration
    """

    name: ClassVar[str] = "Exchange Server Modified Compiled Files"
    base_path: ClassVar[Path] = Path("C:\\inetpub\\wwwroot\\aspnet_client")
    regex: ClassVar[str] = r"(?s:Regex:.*\.\\b[a-zA-Z0-9_\-]\{8\}\\b\.compiled)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ExchangeCve202126855ExchangeServerModifiedCompiledFiles2(KapeTarget):
    """
    Highly dependent on Exchange configuration
    """

    name: ClassVar[str] = "Exchange Server Modified Compiled Files"
    base_path: ClassVar[Path] = Path(
        "C:\\inetpub\\wwwroot\\aspnet_client\\system_web\\"
    )
    regex: ClassVar[str] = r"(?s:Regex:.*\.\\b[a-zA-Z0-9_\-]\{8\}\\b\.compiled)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ExchangeCve202126855ExchangeServerModifiedCompiledFiles3(KapeTarget):
    """
    Highly dependent on Exchange configuration
    """

    name: ClassVar[str] = "Exchange Server Modified Compiled Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Program Files\\Microsoft\\Exchange Server\\V15\\FrontEnd\\HttpProxy\\owa\\auth\\"
    )
    regex: ClassVar[str] = r"(?s:Regex:.*\.\\b[a-zA-Z0-9_\-]\{8\}\\b\.compiled)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ExchangeCve202126855(KapeTargetConfiguration):
    """
    Author: Dennis Reneau

    Version: 1.0

    ID: e7dc72be-942c-4fef-aa45-252bf2364b1e

    Exchange Server Vulnerability *.Compiled Files
    """

    name: ClassVar[str] = "ExchangeCve-2021-26855"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ExchangeCve202126855ExchangeServerModifiedCompiledFiles0,
        ExchangeCve202126855ExchangeServerModifiedCompiledFiles1,
        ExchangeCve202126855ExchangeServerModifiedCompiledFiles2,
        ExchangeCve202126855ExchangeServerModifiedCompiledFiles3,
    ]


class FencesFencesDesktopScreenshots0(KapeTarget):
    """
    Locates all screenshots taken automatically by the Fences application
    """

    name: ClassVar[str] = "Fences - Desktop Screenshots"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Stardock\\Fences\\Backups"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Fences(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: fbfd4a5b-130c-437b-b896-769813fd23e1

    Fences
    """

    name: ClassVar[str] = "Fences"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [FencesFencesDesktopScreenshots0]


class FreeCommanderFreeCommanderFreeCommanderini0(KapeTarget):
    """
    Locates an .ini file that contains Shellbags-equivalent artifacts.
    """

    name: ClassVar[str] = "Free Commander - FreeCommander.ini"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\FreeCommanderXE\\Settings\\"
    )
    regex: ClassVar[str] = r"(?s:FreeCommander\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreeCommanderFreeCommanderFreeCommanderftpini1(KapeTarget):
    """
    Locates an .ini file that contains the file path to the FTP log for Free
    Commander.
    """

    name: ClassVar[str] = "Free Commander - FreeCommander.ftp.ini"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\FreeCommanderXE\\Settings\\"
    )
    regex: ClassVar[str] = r"(?s:FreeCommander\.ftp\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreeCommanderFreeCommanderFreeCommanderhistini2(KapeTarget):
    """
    Locates an .ini file that contains Shellbags-equivalent artifacts that are
    sorted in temporal order from top to bottom for both left and right
    directory browsers.
    """

    name: ClassVar[str] = "Free Commander - FreeCommander.hist.ini"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\FreeCommanderXE\\Settings\\"
    )
    regex: ClassVar[str] = r"(?s:FreeCommander\.hist\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreeCommanderFreeCommanderFreeCommanderfavxml3(KapeTarget):
    """
    Locates an .xml file that contains favorited files/folder by the user.
    """

    name: ClassVar[str] = "Free Commander - FreeCommander.fav.xml"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\FreeCommanderXE\\Settings\\"
    )
    regex: ClassVar[str] = r"(?s:FreeCommander\.fav\.xml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreeCommanderFreeCommanderBackupSettings4(KapeTarget):
    """
    Locates an exact copy of the above files which will have a timestamped
    folder name, i.e. Bkp_Settings-YYYY-MM-DD HH-MM-SS.
    """

    name: ClassVar[str] = "Free Commander - Backup Settings"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\FreeCommanderXE\\Settings\\Bkp_Settings*\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreeCommanderFreeCommanderFTPLog5(KapeTarget):
    """
    Locates log file(s) that have a default naming convention of
    fc_ftplog_20210403 but can be modified by the user.
    """

    name: ClassVar[str] = "Free Commander - FTP Log"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Temp\\")
    regex: ClassVar[str] = r"(?s:fc.*\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreeCommanderFreeCommanderFTPRelatedInformation6(KapeTarget):
    """
    Locates a folder that may be named randomly that contains more FTP related
    information as well as .tmp files that are created while the user is
    traversing folders during an active FTP session. These files are deleted
    upon program exit.
    """

    name: ClassVar[str] = "Free Commander - FTP Related Information"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Temp\\FreeCommander*\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreeCommander(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: 418ce15d-2400-4deb-b7bf-546a99095804

    FreeCommander XE
    """

    name: ClassVar[str] = "FreeCommander"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        FreeCommanderFreeCommanderFreeCommanderini0,
        FreeCommanderFreeCommanderFreeCommanderftpini1,
        FreeCommanderFreeCommanderFreeCommanderhistini2,
        FreeCommanderFreeCommanderFreeCommanderfavxml3,
        FreeCommanderFreeCommanderBackupSettings4,
        FreeCommanderFreeCommanderFTPLog5,
        FreeCommanderFreeCommanderFTPRelatedInformation6,
    ]


class FreeFileSyncFreeFileSync0(KapeTarget):
    """
    Copies out all log files
    """

    name: ClassVar[str] = "FreeFileSync"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\FreeFileSync\\Logs"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreeFileSync(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 1525ef00-abe5-4fdf-8c3c-7c1f291c8866

    FreeFileSync
    """

    name: ClassVar[str] = "FreeFileSync"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [FreeFileSyncFreeFileSync0]


class GoogleDriveBackupSyncUserFilesGoogleDriveBackupandSyncUserFiles0(KapeTarget):
    """
    Older Google Drive Backup and Sync application only
    """

    name: ClassVar[str] = "Google Drive Backup and Sync User Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Google Drive*\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GoogleDriveBackupSyncUserFiles(KapeTargetConfiguration):
    """
    Author: Chad Tilbury

    Version: 1.0

    ID: 6ebae21e-2323-4605-b258-38ea3a43b283

    Google Backup and Sync Storage Files
    """

    name: ClassVar[str] = "GoogleDriveBackupSync_UserFiles"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        GoogleDriveBackupSyncUserFilesGoogleDriveBackupandSyncUserFiles0
    ]


class GoogleDriveMetadataGoogleDriveBackupandSyncMetadata0(KapeTarget):
    """
    Older version of Google Drive
    """

    name: ClassVar[str] = "Google Drive Backup and Sync Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Drive\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GoogleDriveMetadataGoogleDriveforDesktopMetadata1(KapeTarget):
    """
    Metadata folder the same for both newer Google Drive for Desktop and older
    Google File Stream application
    """

    name: ClassVar[str] = "Google Drive for Desktop Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\DriveFS\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GoogleDriveMetadata(KapeTargetConfiguration):
    """
    Author: Chad Tilbury

    Version: 1.1

    ID: 2bfd54a5-175f-48ad-a1bc-7be1dc0465e7

    Google Drive Metadata
    """

    name: ClassVar[str] = "GoogleDrive_Metadata"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        GoogleDriveMetadataGoogleDriveBackupandSyncMetadata0,
        GoogleDriveMetadataGoogleDriveforDesktopMetadata1,
    ]


class GoogleEarthGoogleEarthMyPlacesfile0(KapeTarget):
    """
    File which holds favorited locations
    """

    name: ClassVar[str] = "Google Earth My Places file"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\LocalLow\\Google\\GoogleEarth"
    )
    regex: ClassVar[str] = r"(?s:myplaces\.kml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GoogleEarthGoogleEarthMyPlacesBackupfile1(KapeTarget):
    """
    Backup file which holds favorited locations
    """

    name: ClassVar[str] = "Google Earth My Places Backup file"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\LocalLow\\Google\\GoogleEarth"
    )
    regex: ClassVar[str] = r"(?s:myplaces\.backup\.kml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GoogleEarthGoogleEarthMyPlacesfileXP2(KapeTarget):
    """
    File which holds favorited locations
    """

    name: ClassVar[str] = "Google Earth My Places file (XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Google\\GoogleEarth"
    )
    regex: ClassVar[str] = r"(?s:myplaces\.kml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GoogleEarthGoogleEarthMyPlacesBackupfileXP3(KapeTarget):
    """
    Backup file which holds favorited locations
    """

    name: ClassVar[str] = "Google Earth My Places Backup file (XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Google\\GoogleEarth"
    )
    regex: ClassVar[str] = r"(?s:myplaces\.backup\.kml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GoogleEarth(KapeTargetConfiguration):
    """
    Author: Guus Beckers

    Version: 1.0

    ID: 1ad35449-19a6-4e90-855e-e1b4bfb2748b

    Google Earth
    """

    name: ClassVar[str] = "GoogleEarth"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        GoogleEarthGoogleEarthMyPlacesfile0,
        GoogleEarthGoogleEarthMyPlacesBackupfile1,
        GoogleEarthGoogleEarthMyPlacesfileXP2,
        GoogleEarthGoogleEarthMyPlacesBackupfileXP3,
    ]


class HeidiSQLHeidiSQLBackupfilessql0(KapeTarget):
    name: ClassVar[str] = "HeidiSQL Backup files (*.sql)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\HeidiSQL\\Backups\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class HeidiSQLHeidiSQLtabsini1(KapeTarget):
    name: ClassVar[str] = "HeidiSQL (tabs.ini)"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\HeidiSQL\\")
    regex: ClassVar[str] = r"(?s:tabs\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class HeidiSQL(KapeTargetConfiguration):
    """
    Author: Hyun Yi @hyuunnn

    Version: 1.0

    ID: aac45152-ac7d-4a5e-9f51-523b45b0d9e6

    HeidiSQL
    """

    name: ClassVar[str] = "HeidiSQL"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        HeidiSQLHeidiSQLBackupfilessql0,
        HeidiSQLHeidiSQLtabsini1,
    ]


class MacriumReflectMacriumReflect0(KapeTarget):
    """
    Copies out all log files
    """

    name: ClassVar[str] = "Macrium Reflect"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Macrium\\Macrium Service\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MacriumReflectMacriumReflect1(KapeTarget):
    """
    Copies out the Reflect folder which contains many important logs
    """

    name: ClassVar[str] = "Macrium Reflect"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Macrium\\Reflect\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MacriumReflectMacriumReflect2(KapeTarget):
    """
    Copies out the Reflect folder which contains many important logs
    """

    name: ClassVar[str] = "Macrium Reflect"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\Macrium\\Reflect Launcher")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MacriumReflect(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: def63ed5-a10d-4508-9c6b-d32658de8dbd

    Macrium Reflect
    """

    name: ClassVar[str] = "MacriumReflect"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        MacriumReflectMacriumReflect0,
        MacriumReflectMacriumReflect1,
        MacriumReflectMacriumReflect2,
    ]


class MattermostMattermostChatLogs0(KapeTarget):
    """
    Locates Mattermost logs and copies them
    """

    name: ClassVar[str] = "Mattermost - Chat Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mattermost\\IndexedDB\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Mattermost(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 4adb02a8-149f-4aab-b570-98b02ee0b618

    Mattermost
    """

    name: ClassVar[str] = "Mattermost"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [MattermostMattermostChatLogs0]


class MediaMonkeyMediaMonkeyMediaSQLiteDatabase0(KapeTarget):
    """
    Locates SQLite DB that contains a complete enumeration of the user's media
    collection within MediaMonkey
    """

    name: ClassVar[str] = "MediaMonkey - Media SQLite Database"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\MediaMonkey")
    regex: ClassVar[str] = r"(?s:MM\.DB)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MediaMonkeyMediaMonkeyMediaMonkeyini1(KapeTarget):
    """
    Locates .ini file which contains information about the user's MediaMonkey
    application instance
    """

    name: ClassVar[str] = "MediaMonkey - MediaMonkey.ini"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\MediaMonkey")
    regex: ClassVar[str] = r"(?s:MediaMonkey\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MediaMonkey(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: d37bb0d2-6870-4159-8823-e0943fc42ae2

    MediaMonkey
    """

    name: ClassVar[str] = "MediaMonkey"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        MediaMonkeyMediaMonkeyMediaSQLiteDatabase0,
        MediaMonkeyMediaMonkeyMediaMonkeyini1,
    ]


class MicrosoftOneNoteMicrosoftOneNoteFullTextSearchIndex0(KapeTarget):
    """
    Grabs database(s) comprising of each OneNote notebook's text content
    """

    name: ClassVar[str] = "Microsoft OneNote - FullTextSearchIndex"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.Office.OneNote_8wekyb3d8bbwe\\LocalState\\AppData\\Local\\OneNote\\*\\FullTextSearchIndex"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftOneNoteMicrosoftOneNoteRecentNotebooksSeenURLs1(KapeTarget):
    """
    Grabs a file that appears to record recently seen OneNote notebooks
    """

    name: ClassVar[str] = "Microsoft OneNote - RecentNotebooks_SeenURLs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.Office.OneNote_8wekyb3d8bbwe\\LocalState\\AppData\\Local\\OneNote\\Notifications"
    )
    regex: ClassVar[str] = r"(?s:RecentNotebooks_SeenURLs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftOneNoteMicrosoftOneNoteAccessibilityCheckerIndex2(KapeTarget):
    """
    Grabs database(s) comprising of each OneNote notebook's version sync error
    history
    """

    name: ClassVar[str] = "Microsoft OneNote - AccessibilityCheckerIndex"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.Office.OneNote_8wekyb3d8bbwe\\LocalState\\AppData\\Local\\OneNote\\16.0\\AccessibilityCheckerIndex"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftOneNoteMicrosoftOneNoteUserNoteTags3(KapeTarget):
    """
    Grabs a database that stores the user specified tags within OneNote to be
    used application-wide
    """

    name: ClassVar[str] = "Microsoft OneNote - User NoteTags"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.Office.OneNote_8wekyb3d8bbwe\\LocalState\\AppData\\Local\\OneNote\\16.0\\NoteTags"
    )
    regex: ClassVar[str] = r"(?s:.*LiveId\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftOneNoteMicrosoftOneNoteRecentSearches4(KapeTarget):
    """
    Grabs a database that stores the user's recent searches within OneNote
    """

    name: ClassVar[str] = "Microsoft OneNote - RecentSearches"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.Office.OneNote_8wekyb3d8bbwe\\LocalState\\AppData\\Local\\OneNote\\16.0\\RecentSearches"
    )
    regex: ClassVar[str] = r"(?s:RecentSearches\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftOneNote(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: d528524b-12fd-493d-9e61-dd81dc7fa873

    Microsoft OneNote
    """

    name: ClassVar[str] = "MicrosoftOneNote"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        MicrosoftOneNoteMicrosoftOneNoteFullTextSearchIndex0,
        MicrosoftOneNoteMicrosoftOneNoteRecentNotebooksSeenURLs1,
        MicrosoftOneNoteMicrosoftOneNoteAccessibilityCheckerIndex2,
        MicrosoftOneNoteMicrosoftOneNoteUserNoteTags3,
        MicrosoftOneNoteMicrosoftOneNoteRecentSearches4,
    ]


class MicrosoftStickyNotesMicrosoftStickyNotesWindows78and10version1511andearlier0(
    KapeTarget
):
    name: ClassVar[str] = (
        "Microsoft Sticky Notes - Windows 7, 8, and 10 version 1511 and earlier"
    )
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\StickyNotes\\"
    )
    regex: ClassVar[str] = r"(?s:StickyNotes\.snt)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftStickyNotesMicrosoftStickyNotes1607andlater1(KapeTarget):
    name: ClassVar[str] = "Microsoft Sticky Notes - 1607 and later"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes*\\LocalState\\"
    )
    regex: ClassVar[str] = r"(?s:plum\.sqlite.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftStickyNotes(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: 759b36a9-3637-474e-9bc4-88dd4d54472e

    Microsoft Sticky Notes
    """

    name: ClassVar[str] = "MicrosoftStickyNotes"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        MicrosoftStickyNotesMicrosoftStickyNotesWindows78and10version1511andearlier0,
        MicrosoftStickyNotesMicrosoftStickyNotes1607andlater1,
    ]


class MicrosoftTeamsMicrosoftTeamsIndexedDBCache0(KapeTarget):
    """
    LevelDB database which can contain inbound/outbound chat messages, call
    history and more
    """

    name: ClassVar[str] = "Microsoft Teams IndexedDB Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Teams\\IndexedDB\\https_teams.microsoft.com_0.indexeddb.leveldb\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftTeamsMicrosoftTeamsLocalStorageCache1(KapeTarget):
    """
    LevelDB database which can contain meeting history, file transfer logs and
    more
    """

    name: ClassVar[str] = "Microsoft Teams Local Storage Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Teams\\Local Storage\\leveldb\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftTeamsMicrosoftTeamsCache2(KapeTarget):
    """
    Chromium cache which can be viewed with Nirsoft's ChromeCacheView
    """

    name: ClassVar[str] = "Microsoft Teams Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Teams\\Cache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftTeamsMicrosoftTeamsConfig3(KapeTarget):
    """
    JSON config file for Teams
    """

    name: ClassVar[str] = "Microsoft Teams Config"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Microsoft\\Teams\\"
    )
    regex: ClassVar[str] = r"(?s:desktop\-config\.json)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftTeamsMicrosoftTeamsLogsWindows114(KapeTarget):
    """
    Lots of log files for MS Teams
    """

    name: ClassVar[str] = "Microsoft Teams Logs (Windows 11)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%User%\\AppData\\Local\\Packages\\MicrosoftTeams_8wekyb3d8bbwe\\LocalCache\\Microsoft\\MSTeams\\Logs"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftTeams(KapeTargetConfiguration):
    """
    Author: Matt Dawson and Andrew Rathbun

    Version: 3.0

    ID: 7d449255-917e-4894-a46d-dcbeee2289b5

    Microsoft Teams
    """

    name: ClassVar[str] = "MicrosoftTeams"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        MicrosoftTeamsMicrosoftTeamsIndexedDBCache0,
        MicrosoftTeamsMicrosoftTeamsLocalStorageCache1,
        MicrosoftTeamsMicrosoftTeamsCache2,
        MicrosoftTeamsMicrosoftTeamsConfig3,
        MicrosoftTeamsMicrosoftTeamsLogsWindows114,
    ]


class MicrosoftToDoMicrosoftToDoSQLiteDatabaseofToDotasks0(KapeTarget):
    name: ClassVar[str] = "Microsoft To Do - SQLite Database of To Do tasks"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.Todos_8wekyb3d8bbwe\\LocalState\\AccountsRoot\\*\\"
    )
    regex: ClassVar[str] = r"(?s:todosqlite\.db.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftToDoMicrosoftToDoUserAvatar1(KapeTarget):
    name: ClassVar[str] = "Microsoft To Do - User Avatar"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.Todos_8wekyb3d8bbwe\\LocalState\\AccountsRoot\\4c444a17ebb042fb92df97d00d1c802a\\avatars\\"
    )
    regex: ClassVar[str] = r"(?s:UserAvatar\.jpg)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MicrosoftToDo(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: cb2ad0a7-690b-47da-89db-6cd7e10e0c2d

    Microsoft To Do
    """

    name: ClassVar[str] = "MicrosoftToDo"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        MicrosoftToDoMicrosoftToDoSQLiteDatabaseofToDotasks0,
        MicrosoftToDoMicrosoftToDoUserAvatar1,
    ]


class MidnightCommanderMidnightCommanderAllConfiguationFiles0(KapeTarget):
    """
    Locates folder where all configuration files reside
    """

    name: ClassVar[str] = "Midnight Commander -- All Configuation Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Midnight Commander\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MidnightCommander(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: c02a2310-8ec2-4c0f-8a8a-b20ac0820e46

    Midnight Commander
    """

    name: ClassVar[str] = "MidnightCommander"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        MidnightCommanderMidnightCommanderAllConfiguationFiles0
    ]


class MultiCommanderMultiCommanderApplicationFolder0(KapeTarget):
    """
    Locates the contents of the Application folder.
    """

    name: ClassVar[str] = "Multi Commander - Application Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\MultiCommander*\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MultiCommanderMultiCommanderConfigFolder1(KapeTarget):
    """
    Locates the contents of the Config folder.
    """

    name: ClassVar[str] = "Multi Commander - Config Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\MultiCommander*\\Config\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MultiCommanderMultiCommanderLogFolder2(KapeTarget):
    """
    Locates log file(s) related to user activity within Multi Commander.
    """

    name: ClassVar[str] = "Multi Commander - Log Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\MultiCommander*\\Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MultiCommanderMultiCommanderUserDataFolder3(KapeTarget):
    """
    Locates the contents of the UserData folder.
    """

    name: ClassVar[str] = "Multi Commander - UserData Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\MultiCommander*\\UserData\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MultiCommanderMultiCommanderLogFile4(KapeTarget):
    """
    Locates log file(s) associated with Milti Commander. Commonly in YYYY-MM-DD
    (numbers)-MultiCommander.log naming convention.
    """

    name: ClassVar[str] = "Multi Commander - Log File"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\MultiCommander*\\"
    )
    regex: ClassVar[str] = r"(?s:.*MultiCommander\.log)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class MultiCommander(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 9a28ae40-1ff0-4e99-8ed0-ac60083c98b5

    Multi Commander
    """

    name: ClassVar[str] = "MultiCommander"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        MultiCommanderMultiCommanderApplicationFolder0,
        MultiCommanderMultiCommanderConfigFolder1,
        MultiCommanderMultiCommanderLogFolder2,
        MultiCommanderMultiCommanderUserDataFolder3,
        MultiCommanderMultiCommanderLogFile4,
    ]


class OneCommanderOneCommanderAllConfigurationFiles0(KapeTarget):
    """
    Locates folder where all configuration files reside
    """

    name: ClassVar[str] = "One Commander - All Configuration Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\OneCommander\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OneCommanderOneCommanderOtherConfigurationFiles1(KapeTarget):
    """
    Locates folder where all configuration files reside
    """

    name: ClassVar[str] = "One Commander - Other Configuration Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Apps\\2.0\\*\\*\\onec*\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OneCommander(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 5b532f4e-f6cb-4d59-bd44-91b9f9d94a54

    One Commander
    """

    name: ClassVar[str] = "OneCommander"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        OneCommanderOneCommanderAllConfigurationFiles0,
        OneCommanderOneCommanderOtherConfigurationFiles1,
    ]


class OneDriveMetadataOneDriveMetadataLogs0(KapeTarget):
    name: ClassVar[str] = "OneDrive Metadata Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\OneDrive\\logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OneDriveMetadataOneDriveMetadataSettings1(KapeTarget):
    name: ClassVar[str] = "OneDrive Metadata Settings"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\OneDrive\\settings\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OneDriveMetadata(KapeTargetConfiguration):
    """
    Author: Chad Tilbury

    Version: 1.1

    ID: 726ca098-6c5b-40e3-ade8-60730c5ec4f8

    Microsoft OneDrive Storage Metadata
    """

    name: ClassVar[str] = "OneDrive_Metadata"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        OneDriveMetadataOneDriveMetadataLogs0,
        OneDriveMetadataOneDriveMetadataSettings1,
    ]


class OneDriveUserFilesOneDriveUserFiles0(KapeTarget):
    """
    Caution -- This target will collect OneDrive contents from the local drive
    AND on-demand cloud files. Ensure your scope of authority permits cloud
    collections before use or isolate system from network.
    """

    name: ClassVar[str] = "OneDrive User Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\OneDrive*\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OneDriveUserFiles(KapeTargetConfiguration):
    """
    Author: Chad Tilbury

    Version: 1.0

    ID: e222254a-518d-4ded-8566-60a4d3654a65

    Microsoft OneDrive Storage Files
    """

    name: ClassVar[str] = "OneDrive_UserFiles"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [OneDriveUserFilesOneDriveUserFiles0]


class OpenSSHClientOpenSSHConfigFile0(KapeTarget):
    """
    Config file can hold usernames, IP addresses and ports, key locations and
    configured shortcuts for servers e.g. ssh web-server
    """

    name: ClassVar[str] = "OpenSSH Config File"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.ssh\\")
    regex: ClassVar[str] = r"(?s:config)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHClientOpenSSHKnownHosts1(KapeTarget):
    """
    Known hosts file can hold a list of connected FQDNs/IP Addresses and ports
    if they are non-default, as well as public key fingerprints
    """

    name: ClassVar[str] = "OpenSSH Known Hosts"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.ssh\\")
    regex: ClassVar[str] = r"(?s:known_hosts)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHClientOpenSSHPublicKeys2(KapeTarget):
    """
    Gets all public keys (*.pub). It is more difficult to find private keys as
    they typically do not have a file extension. However, the .pub files should
    be able to help find the private keys as they are typically named the same.
    """

    name: ClassVar[str] = "OpenSSH Public Keys"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.ssh\\")
    regex: ClassVar[str] = r"(?s:.*\.pub)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHClientOpenSSHDefaultRSAPrivateKey3(KapeTarget):
    """
    Default name for an auto-generated SSH RSA private key
    """

    name: ClassVar[str] = "OpenSSH Default RSA Private Key"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.ssh\\")
    regex: ClassVar[str] = r"(?s:id_rsa)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHClientOpenSSHDefaultECDSAPrivateKey4(KapeTarget):
    """
    Default name for an auto-generated SSH ECDSA private key
    """

    name: ClassVar[str] = "OpenSSH Default ECDSA Private Key"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.ssh\\")
    regex: ClassVar[str] = r"(?s:id_ecdsa)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHClientOpenSSHDefaultECDSASKPrivateKey5(KapeTarget):
    """
    Default name for an auto-generated SSH ECDSA private key using a Security
    Key
    """

    name: ClassVar[str] = "OpenSSH Default ECDSA-SK Private Key"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.ssh\\")
    regex: ClassVar[str] = r"(?s:id_ecdsa_sk)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHClientOpenSSHDefaultED25519PrivateKey6(KapeTarget):
    """
    Default name for an auto-generated SSH ED25519 private key
    """

    name: ClassVar[str] = "OpenSSH Default ED25519 Private Key"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.ssh\\")
    regex: ClassVar[str] = r"(?s:id_ed25519)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHClientOpenSSHDefaultED25519SKPrivateKey7(KapeTarget):
    """
    Default name for an auto-generated SSH ED25519 private key using a Security
    Key
    """

    name: ClassVar[str] = "OpenSSH Default ED25519-SK Private Key"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.ssh\\")
    regex: ClassVar[str] = r"(?s:id_ed25519_sk)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHClientOpenSSHDefaultDSAPrivateKey8(KapeTarget):
    """
    Default name for an auto-generated SSH DSA private key
    """

    name: ClassVar[str] = "OpenSSH Default DSA Private Key"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.ssh\\")
    regex: ClassVar[str] = r"(?s:id_dsa)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHClient(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 77f56ec6-61ae-450f-b90e-ac60352093ef

    OpenSSH Client config, known hosts and keys
    """

    name: ClassVar[str] = "OpenSSHClient"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        OpenSSHClientOpenSSHConfigFile0,
        OpenSSHClientOpenSSHKnownHosts1,
        OpenSSHClientOpenSSHPublicKeys2,
        OpenSSHClientOpenSSHDefaultRSAPrivateKey3,
        OpenSSHClientOpenSSHDefaultECDSAPrivateKey4,
        OpenSSHClientOpenSSHDefaultECDSASKPrivateKey5,
        OpenSSHClientOpenSSHDefaultED25519PrivateKey6,
        OpenSSHClientOpenSSHDefaultED25519SKPrivateKey7,
        OpenSSHClientOpenSSHDefaultDSAPrivateKey8,
    ]


class OpenSSHServerOpenSSHServerConfigFile0(KapeTarget):
    """
    Config file can hold information on allowed/denied users
    """

    name: ClassVar[str] = "OpenSSH Server Config File"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\ssh\\")
    regex: ClassVar[str] = r"(?s:sshd_config)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHServerOpenSSHServerLogs1(KapeTarget):
    """
    OpenSSH server logs
    """

    name: ClassVar[str] = "OpenSSH Server Logs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\ssh\\logs\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHServerOpenSSHHostECDSAKey2(KapeTarget):
    """
    Retrieves the host ECDSA key
    """

    name: ClassVar[str] = "OpenSSH Host ECDSA Key"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\ssh\\")
    regex: ClassVar[str] = r"(?s:ssh_host_ecdsa_key)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHServerOpenSSHHostED25519Key3(KapeTarget):
    """
    Retrieves the host ED25519 key
    """

    name: ClassVar[str] = "OpenSSH Host ED25519 Key"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\ssh\\")
    regex: ClassVar[str] = r"(?s:ssh_host_ed25519_key)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHServerOpenSSHHostDSAKey4(KapeTarget):
    """
    Retrieves the host DSA key
    """

    name: ClassVar[str] = "OpenSSH Host DSA Key"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\ssh\\")
    regex: ClassVar[str] = r"(?s:ssh_host_dsa_key)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHServerOpenSSHHostRSAKey5(KapeTarget):
    """
    Retrieves the host RSA key
    """

    name: ClassVar[str] = "OpenSSH Host RSA Key"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\ssh\\")
    regex: ClassVar[str] = r"(?s:ssh_host_rsa_key)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHServerOpenSSHUserAuthorizedKeys6(KapeTarget):
    """
    Retrieves the user's authorised public keys
    """

    name: ClassVar[str] = "OpenSSH User Authorized Keys"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.ssh\\")
    regex: ClassVar[str] = r"(?s:authorized_keys)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHServerOpenSSHUserAuthorizedKeys27(KapeTarget):
    """
    Retrieves the user's authorised public keys from the second file
    """

    name: ClassVar[str] = "OpenSSH User Authorized Keys 2"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.ssh\\")
    regex: ClassVar[str] = r"(?s:authorized_keys2)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHServerOpenSSHAuthorizedAdministratorKeys8(KapeTarget):
    """
    Retrieves the administrator group's authorised public keys
    """

    name: ClassVar[str] = "OpenSSH Authorized Administrator Keys"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\ssh\\")
    regex: ClassVar[str] = r"(?s:administrators_authorized_keys)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class OpenSSHServer(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 6c290fef-f9be-43af-a987-44709d8f7921

    OpenSSH Server Config and Logs
    """

    name: ClassVar[str] = "OpenSSHServer"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        OpenSSHServerOpenSSHServerConfigFile0,
        OpenSSHServerOpenSSHServerLogs1,
        OpenSSHServerOpenSSHHostECDSAKey2,
        OpenSSHServerOpenSSHHostED25519Key3,
        OpenSSHServerOpenSSHHostDSAKey4,
        OpenSSHServerOpenSSHHostRSAKey5,
        OpenSSHServerOpenSSHUserAuthorizedKeys6,
        OpenSSHServerOpenSSHUserAuthorizedKeys27,
        OpenSSHServerOpenSSHAuthorizedAdministratorKeys8,
    ]


class pCloudDatabasepCloudDatabase0(KapeTarget):
    """
    Database contains all files sync'd with pCloud account.
    """

    name: ClassVar[str] = "pCloud Database"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\pCloud\\")
    regex: ClassVar[str] = r"(?s:.*\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class pCloudDatabasepCloudDatabaseWALFile1(KapeTarget):
    """
    Write-Ahead Log for pCloud database file.
    """

    name: ClassVar[str] = "pCloud Database WAL File"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\pCloud\\")
    regex: ClassVar[str] = r"(?s:.*\.db\-wal)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class pCloudDatabasepCloudDatabaseSharedMemoryFile2(KapeTarget):
    """
    Shared Memory for the pCloud database file.
    """

    name: ClassVar[str] = "pCloud Database Shared Memory File"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\pCloud\\")
    regex: ClassVar[str] = r"(?s:.*\.db\-shm)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class pCloudDatabase(KapeTargetConfiguration):
    """
    Author: Josh Hickman

    Version: 1.0

    ID: dc6750d8-ee91-45d4-9f53-fa3f8513ada3

    pCloud Database
    """

    name: ClassVar[str] = "pCloudDatabase"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        pCloudDatabasepCloudDatabase0,
        pCloudDatabasepCloudDatabaseWALFile1,
        pCloudDatabasepCloudDatabaseSharedMemoryFile2,
    ]


class QDirQDiriniFile0(KapeTarget):
    """
    Locates .ini file associated with Q-Dir which stores useful user activity
    information.
    """

    name: ClassVar[str] = "Q-Dir - .ini File"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\Q-Dir\\")
    regex: ClassVar[str] = r"(?s:Q\-Dir\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class QDirQDirqdrfile1(KapeTarget):
    """
    Locates .qdr file associated with Q-Dir which stores useful user activity
    information, including the last 4 folders opened (encoded, unfortunately).
    """

    name: ClassVar[str] = "Q-Dir - .qdr file"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\Q-Dir\\")
    regex: ClassVar[str] = r"(?s:start\.qdr)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class QDir(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 1233adac-a6ec-4bba-abe6-c827ba5e27ea

    Q-Dir
    """

    name: ClassVar[str] = "Q-Dir"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [QDirQDiriniFile0, QDirQDirqdrfile1]


class QFinderProQNAPQFinderPro0(KapeTarget):
    """
    Locates a JSON file that provides network location information for any QNAP
    connected devices.
    """

    name: ClassVar[str] = "QFinderPro"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\QNAP\\QfinderPro"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class QFinderProQNAP(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 7323637e-de45-47c4-8f2f-6b11a4f82919

    QFinderPro (QNAP)
    """

    name: ClassVar[str] = "QFinderPro (QNAP)"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [QFinderProQNAPQFinderPro0]


class ShareXShareX0(KapeTarget):
    """
    Locates and captures all files within the default ShareX folder path
    """

    name: ClassVar[str] = "ShareX"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Documents\\ShareX")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ShareX(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: a8409b28-70ac-4961-a1d0-94bdf1b3e7e2

    ShareX
    """

    name: ClassVar[str] = "ShareX"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [ShareXShareX0]


class SlackSlackChatLogs0(KapeTarget):
    """
    Locates Slack logs and copies them
    """

    name: ClassVar[str] = "Slack - Chat Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Slack\\IndexedDB\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SlackSlackLevelDBFiles1(KapeTarget):
    name: ClassVar[str] = "Slack LevelDB Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Slack\\Local Storage\\leveldb"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SlackSlackElectronLogs2(KapeTarget):
    """
    Current Slack application is based on Electron and additional logging can be
    found here.
    """

    name: ClassVar[str] = "Slack Electron Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Slack\\logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SlackSlackCache3(KapeTarget):
    """
    Collects Slack cache files. This folder can be parsed like a Chrome Browser
    cache using a tool like Nirsoft ChromeCacheView
    """

    name: ClassVar[str] = "Slack Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Slack\\Cache"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SlackSlackStorage4(KapeTarget):
    """
    User activity logs can be present including slack-downloads log
    """

    name: ClassVar[str] = "Slack Storage"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Slack\\storage\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Slack(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun and Chad Tilbury

    Version: 1.1

    ID: 67ec52aa-1a0e-4dfa-8b9f-8d94de28b02f

    Slack
    """

    name: ClassVar[str] = "Slack"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SlackSlackChatLogs0,
        SlackSlackLevelDBFiles1,
        SlackSlackElectronLogs2,
        SlackSlackCache3,
        SlackSlackStorage4,
    ]


class SnagitSnagitCaptures0(KapeTarget):
    """
    Locates all Snagit captures
    """

    name: ClassVar[str] = "Snagit - Captures"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\TechSmith\\Snagit\\DataStore"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Snagit(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: b2281102-476c-4aa2-804d-4c906a20415a

    Snagit
    """

    name: ClassVar[str] = "Snagit"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [SnagitSnagitCaptures0]


class SpeedCommanderSpeedCommanderiniFile0(KapeTarget):
    """
    Locates folder where all configuration files reside
    """

    name: ClassVar[str] = "SpeedCommander - .ini File"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\SpeedProject\\SpeedCommander 19\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SpeedCommander(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 237f2355-4ae1-4461-812f-2833003aabc3

    SpeedCommander
    """

    name: ClassVar[str] = "SpeedCommander"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [SpeedCommanderSpeedCommanderiniFile0]


class SugarSyncSugarSyncLogFile0(KapeTarget):
    """
    Locates a log file the gives a play-by-play of what the user synced when.
    """

    name: ClassVar[str] = "SugarSync Log File"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\SugarSync\\")
    regex: ClassVar[str] = r"(?s:sc1\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SugarSyncSugarSyncSharedFoldersDefaultLocation1(KapeTarget):
    name: ClassVar[str] = "SugarSync - Shared Folders (Default Location)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\Documents\\SugarSync Shared Folders\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SugarSyncSugarSyncMySugarSyncDefaultLocation2(KapeTarget):
    name: ClassVar[str] = "SugarSync - My SugarSync (Default Location)"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Documents\\My SugarSync\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SugarSync(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 91e7965c-d9ed-440e-93b7-65d7ebdb3584

    SugarSync
    """

    name: ClassVar[str] = "SugarSync"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SugarSyncSugarSyncLogFile0,
        SugarSyncSugarSyncSharedFoldersDefaultLocation1,
        SugarSyncSugarSyncMySugarSyncDefaultLocation2,
    ]


class TelegramTelegramappfolder0(KapeTarget):
    """
    Telegram app folder structure
    """

    name: ClassVar[str] = "Telegram app folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Telegram Desktop\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TelegramTelegramdownloadedfiles1(KapeTarget):
    """
    Chat Attachments
    """

    name: ClassVar[str] = "Telegram downloaded files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Downloads\\Telegram Desktop\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Telegram(KapeTargetConfiguration):
    """
    Author: Simone Marinari

    Version: 1.0

    ID: 7f836137-1479-46b4-91a9-83624b8a8e26

    Telegram Desktop
    """

    name: ClassVar[str] = "Telegram"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        TelegramTelegramappfolder0,
        TelegramTelegramdownloadedfiles1,
    ]


class ThunderbirdMozillaThunderbirdInstallDate0(KapeTarget):
    """
    Holds install time in Unix Seconds timestamp
    """

    name: ClassVar[str] = "Mozilla Thunderbird Install Date"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Thunderbird\\Crash Reports\\"
    )
    regex: ClassVar[str] = r"(?s:InstallTime.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ThunderbirdMozillaThunderbirdProfilesini1(KapeTarget):
    """
    Profiles list - can hold references to other profiles held elsewhere on the
    device
    """

    name: ClassVar[str] = "Mozilla Thunderbird Profiles.ini"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Thunderbird\\"
    )
    regex: ClassVar[str] = r"(?s:profiles\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ThunderbirdMozillaThunderbirdprefsjs2(KapeTarget):
    """
    User Preferences for that profile
    """

    name: ClassVar[str] = "Mozilla Thunderbird prefs.js"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Thunderbird\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:prefs\.js)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ThunderbirdMozillaThunderbirdGlobalMessagesDatabase3(KapeTarget):
    """
    Holds list of contacts, emails, and other potentially useful artifacts
    """

    name: ClassVar[str] = "Mozilla Thunderbird Global Messages Database"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Thunderbird\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:global\-messages\-db\.sqlite)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ThunderbirdMozillaThunderbirdloginsjson4(KapeTarget):
    """
    Holds last time online login used, last time password changed, hostname,
    HTTP(s) URL and more
    """

    name: ClassVar[str] = "Mozilla Thunderbird logins.json"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Thunderbird\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:logins\.json)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ThunderbirdMozillaThunderbirdplacessqlite5(KapeTarget):
    """
    Holds history for Thunderbird - as it contains portions of Firefox embedded,
    it can be used to visit websites too
    """

    name: ClassVar[str] = "Mozilla Thunderbird places.sqlite"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Thunderbird\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:places\.sqlite)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ThunderbirdMozillaThunderbirdImapMailINBOX6(KapeTarget):
    """
    Holds all email files with headers, content etc
    """

    name: ClassVar[str] = "Mozilla Thunderbird ImapMail INBOX"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Thunderbird\\Profiles\\*\\ImapMail\\"
    )
    regex: ClassVar[str] = r"(?s:INBOX)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ThunderbirdMozillaThunderbirdMailINBOX7(KapeTarget):
    """
    Holds all email files with headers, content etc
    """

    name: ClassVar[str] = "Mozilla Thunderbird Mail INBOX"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Thunderbird\\Profiles\\*\\Mail\\"
    )
    regex: ClassVar[str] = r"(?s:INBOX)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ThunderbirdMozillaThunderbirdCalendarData8(KapeTarget):
    """
    Holds local calendar data
    """

    name: ClassVar[str] = "Mozilla Thunderbird Calendar Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Thunderbird\\Profiles\\*\\calendar-data\\"
    )
    regex: ClassVar[str] = r"(?s:local\.sqlite)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ThunderbirdMozillaThunderbirdAttachments9(KapeTarget):
    """
    Holds attachments
    """

    name: ClassVar[str] = "Mozilla Thunderbird Attachments"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Thunderbird\\Profiles\\*\\Attachments\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ThunderbirdMozillaThunderbirdAddressBook10(KapeTarget):
    """
    Holds local address book
    """

    name: ClassVar[str] = "Mozilla Thunderbird Address Book"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Thunderbird\\Profiles\\*\\"
    )
    regex: ClassVar[str] = r"(?s:abook\.sqlite)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Thunderbird(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: e9a06689-bbd9-4540-be17-2633d9b7412c

    Mozilla Thunderbird Email Client
    """

    name: ClassVar[str] = "Thunderbird"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ThunderbirdMozillaThunderbirdInstallDate0,
        ThunderbirdMozillaThunderbirdProfilesini1,
        ThunderbirdMozillaThunderbirdprefsjs2,
        ThunderbirdMozillaThunderbirdGlobalMessagesDatabase3,
        ThunderbirdMozillaThunderbirdloginsjson4,
        ThunderbirdMozillaThunderbirdplacessqlite5,
        ThunderbirdMozillaThunderbirdImapMailINBOX6,
        ThunderbirdMozillaThunderbirdMailINBOX7,
        ThunderbirdMozillaThunderbirdCalendarData8,
        ThunderbirdMozillaThunderbirdAttachments9,
        ThunderbirdMozillaThunderbirdAddressBook10,
    ]


class TotalCommanderTotalCommanderiniFile0(KapeTarget):
    """
    Locates .ini file associated with Total Commander which stores useful user
    activity information.
    """

    name: ClassVar[str] = "Total Commander - .ini File"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\GHISLER\\")
    regex: ClassVar[str] = r"(?s:wincmd\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TotalCommanderTotalCommanderLogFile1(KapeTarget):
    """
    Locates log file associated with Total Commander. NOTE: this log file is NOT
    enabled by default and the filename can be modified.
    """

    name: ClassVar[str] = "Total Commander - Log File"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:totalcmd\.log)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TotalCommanderTotalCommanderTempFilesCreatedDuringFolderTraversal2(KapeTarget):
    """
    Locates .tmp files which are created during the user's folder traversal and
    provide insight into contents of each folder traversed.
    """

    name: ClassVar[str] = "Total Commander - Temp Files Created During Folder Traversal"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Temp\\")
    regex: ClassVar[str] = r"(?s:FTP.*\.tmp)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TotalCommanderTotalCommanderFTPiniFile3(KapeTarget):
    """
    Locates .ini file associated with Total Commander which stores useful FTP
    information.
    """

    name: ClassVar[str] = "Total Commander - FTP .ini File"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\GHISLER\\")
    regex: ClassVar[str] = r"(?s:wcx_ftp\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TotalCommanderTotalCommanderFileTree4(KapeTarget):
    """
    Locates a file that contains an exhaustive file tree of a user's file
    system.
    """

    name: ClassVar[str] = "Total Commander - File Tree"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\GHISLER\\")
    regex: ClassVar[str] = r"(?s:treeinfo.*\.wc)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TotalCommanderTotalCommanderFTPLogs5(KapeTarget):
    """
    Locates a file that contains the Total Commander FTP logs.
    """

    name: ClassVar[str] = "Total Commander - FTP Logs"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Temp\\")
    regex: ClassVar[str] = r"(?s:tcftp\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TotalCommander(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun and Jessica Venturo

    Version: 1.3

    ID: ae5bfc3d-cc1c-41ec-a11a-19233ae82877

    Total Commander
    """

    name: ClassVar[str] = "TotalCommander"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        TotalCommanderTotalCommanderiniFile0,
        TotalCommanderTotalCommanderLogFile1,
        TotalCommanderTotalCommanderTempFilesCreatedDuringFolderTraversal2,
        TotalCommanderTotalCommanderFTPiniFile3,
        TotalCommanderTotalCommanderFileTree4,
        TotalCommanderTotalCommanderFTPLogs5,
    ]


class TreeSizeTreeSizeScanHistoryXML0(KapeTarget):
    """
    Locates XML file that provides a list of previously scanned directories by
    the user.
    """

    name: ClassVar[str] = "TreeSize - ScanHistory.XML"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\JAM Software\\TreeSize"
    )
    regex: ClassVar[str] = r"(?s:scanhistory\.xml)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TreeSize(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: b7e88f6b-3474-46b1-9c0b-1eed65dfc379

    TreeSize - Scan History
    """

    name: ClassVar[str] = "TreeSize"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [TreeSizeTreeSizeScanHistoryXML0]


class ViberViberConfigDatabase0(KapeTarget):
    """
    Configuration file for Viber
    """

    name: ClassVar[str] = "Viber Config Database"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\ViberPC\\")
    regex: ClassVar[str] = r"(?s:config\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ViberViberUsersDataDatabase1(KapeTarget):
    """
    Viber data for that user, containing Calls, Chat Messages, Contacts and more
    """

    name: ClassVar[str] = "Viber Users Data Database"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\ViberPC\\*\\"
    )
    regex: ClassVar[str] = r"(?s:viber\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ViberViberUsersAvatarsCache2(KapeTarget):
    """
    Cache of the Avatars for other Viber users
    """

    name: ClassVar[str] = "Viber Users Avatars Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\ViberPC\\*\\Avatars"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ViberViberUsersBackgroundsCache3(KapeTarget):
    """
    Store of the backgrounds
    """

    name: ClassVar[str] = "Viber Users Backgrounds Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\ViberPC\\*\\Backgrounds"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ViberViberUsersThumbnailsCache4(KapeTarget):
    """
    Cache of the thumbnails for uploaded/downloaded images
    """

    name: ClassVar[str] = "Viber Users Thumbnails Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\ViberPC\\*\\Thumbnails"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Viber(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 61e74d50-5e97-4bc8-a78b-c2fb393d2f9f

    ViberPC Messaging App
    """

    name: ClassVar[str] = "Viber"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ViberViberConfigDatabase0,
        ViberViberUsersDataDatabase1,
        ViberViberUsersAvatarsCache2,
        ViberViberUsersBackgroundsCache3,
        ViberViberUsersThumbnailsCache4,
    ]


class VirtualBoxConfigVirtualBoxVMconfigs0(KapeTarget):
    """
    Locates all .vbox VM configuration files on disk
    """

    name: ClassVar[str] = "VirtualBox VM configs"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.vbox)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualBoxConfigVirtualBoxVMbackupconfigs1(KapeTarget):
    """
    Locates all backup .vbox VM configuration files on disk
    """

    name: ClassVar[str] = "VirtualBox VM backup configs"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.vbox\-prev)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualBoxConfig(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 0983f8c9-721b-4dd5-b4d2-f16ee289b1c3

    Collects VirtualBox configuration files
    """

    name: ClassVar[str] = "VirtualBoxConfig"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        VirtualBoxConfigVirtualBoxVMconfigs0,
        VirtualBoxConfigVirtualBoxVMbackupconfigs1,
    ]


class VirtualBoxLogsVirtualBoxLogs0(KapeTarget):
    """
    Locates all VBox.log files on disk
    """

    name: ClassVar[str] = "VirtualBox Logs"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:VBox\.log)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualBoxLogsVirtualBoxBackupLogs1(KapeTarget):
    """
    Locates all backup VBox.log files on disk - these can show historic VM usage
    """

    name: ClassVar[str] = "VirtualBox Backup Logs"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:VBox\.log\..*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualBoxLogsVirtualBoxHardeningLogs2(KapeTarget):
    """
    Locates all VBoxHardening.log files on disk
    """

    name: ClassVar[str] = "VirtualBox Hardening Logs"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:VBoxHardening\.log)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualBoxLogs(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 3d5398fc-5774-4329-a268-29ed1a6d4d9e

    Collects VirtualBox log files
    """

    name: ClassVar[str] = "VirtualBoxLogs"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        VirtualBoxLogsVirtualBoxLogs0,
        VirtualBoxLogsVirtualBoxBackupLogs1,
        VirtualBoxLogsVirtualBoxHardeningLogs2,
    ]


class VLCMediaPlayerVLCRecentlyOpenedFiles0(KapeTarget):
    """
    Configuration file for VLC. Holds [RecentsMRL] key which lists recently
    opened files as well as sometimes retaining timestamps for file opening
    """

    name: ClassVar[str] = "VLC Recently Opened Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\vlc\\")
    regex: ClassVar[str] = r"(?s:vlc\-qt\-interface\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VLCMediaPlayerVLCRecordedFiles1(KapeTarget):
    """
    Recorded files in VLC. Sometimes the Record button may be pressed instead of
    Play by suspects, which can record them watching content with VLC
    """

    name: ClassVar[str] = "VLC Recorded Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Videos\\")
    regex: ClassVar[str] = r"(?s:vlc\-.*\.avi)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VLCMediaPlayer(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: f7187e39-0410-41cb-b7e0-243d92090c9c

    VLC Media Player
    """

    name: ClassVar[str] = "VLC Media Player"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        VLCMediaPlayerVLCRecentlyOpenedFiles0,
        VLCMediaPlayerVLCRecordedFiles1,
    ]


class VMwareInventoryVMwareVirtualMachineInventory0(KapeTarget):
    """
    Locates an inventory of all Virtual Machines on disk.
    """

    name: ClassVar[str] = "VMware - Virtual Machine Inventory"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\VMware")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VMwareInventory(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 92d4917d-54a3-48a1-873b-ea2ddad58b84

    VMware - Virtual Machine Inventory
    """

    name: ClassVar[str] = "VMwareInventory"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        VMwareInventoryVMwareVirtualMachineInventory0
    ]


class WhatsAppWhatsAppCache0(KapeTarget):
    """
    Copies the cache of WhatsApp. Can be opened with Chrome Cache Viewer for
    viewing embedded thumbnails and other image artefacts, as well as extracting
    .enc message files or other files
    """

    name: ClassVar[str] = "WhatsApp Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\WhatsApp\\Cache"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WhatsAppWhatsAppLocalStorage1(KapeTarget):
    """
    Copies the Local Storage leveldb of WhatsApp. Contains phone model and name
    of user, plus encrypted base64 strings which can be viewed with
    LevelDBDumper
    """

    name: ClassVar[str] = "WhatsApp Local Storage"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\WhatsApp\\Local Storage\\leveldb"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WhatsApp(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: a6f739e3-21fc-4942-9272-26d567f014da

    WhatsApp Local Files
    """

    name: ClassVar[str] = "WhatsApp"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WhatsAppWhatsAppCache0,
        WhatsAppWhatsAppLocalStorage1,
    ]


class WindowsYourPhoneWindowsYourPhoneAllDatabases0(KapeTarget):
    """
    Locates all Your Phone database files
    """

    name: ClassVar[str] = "Windows Your Phone - All Databases"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.YourPhone_8wekyb3d8bbwe\\LocalCache\\Indexed"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class WindowsYourPhone(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 2151d28a-3b2b-4784-a91f-72622a97a17b

    Windows Your Phone
    """

    name: ClassVar[str] = "WindowsYourPhone"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        WindowsYourPhoneWindowsYourPhoneAllDatabases0
    ]


class XYplorerXYplorerinifile0(KapeTarget):
    """
    Locates .ini file associated with Total Commander which stores useful user
    activity information.
    """

    name: ClassVar[str] = "XYplorer - .ini file"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\XYplorer\\")
    regex: ClassVar[str] = r"(?s:XYplorer\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class XYplorerXYplorerinifileforeachrespectivepane1(KapeTarget):
    """
    Locates the .ini file for the left and right pane.
    """

    name: ClassVar[str] = "XYplorer - .ini file for each respective pane"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\XYplorer\\Panes\\*\\"
    )
    regex: ClassVar[str] = r"(?s:pane\.ini)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class XYplorerXYplorerAutoBackupfolder2(KapeTarget):
    """
    Locates the AutoBackup folder and copies its contents.
    """

    name: ClassVar[str] = "XYplorer - AutoBackup folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\XYplorer\\AutoBackup"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class XYplorerXYplorerdatfiles3(KapeTarget):
    """
    Locates the .dat files in the XYplorer's AppData folder, all of which are
    updated upon program's exit.
    """

    name: ClassVar[str] = "XYplorer - .dat files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\XYplorer")
    regex: ClassVar[str] = r"(?s:.*\.dat)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class XYplorer(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: b350302a-bf5a-4908-a6c5-9e3418aca23c

    XYplorer
    """

    name: ClassVar[str] = "XYplorer"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        XYplorerXYplorerinifile0,
        XYplorerXYplorerinifileforeachrespectivepane1,
        XYplorerXYplorerAutoBackupfolder2,
        XYplorerXYplorerdatfiles3,
    ]


class ZoomZoomclientlogs0(KapeTarget):
    """
    Zoom client artifacts
    """

    name: ClassVar[str] = "Zoom client logs"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\Zoom\\logs")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ZoomZoomclientlogsWindowsXP1(KapeTarget):
    """
    Zoom client artifacts (Windows XP)
    """

    name: ClassVar[str] = "Zoom client logs (Windows XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Zoom\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ZoomZoomclientrecordings2(KapeTarget):
    """
    Zoom recording artifacts
    """

    name: ClassVar[str] = "Zoom client recordings"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\Documents\\Zoom\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ZoomZoompluginOutlook3(KapeTarget):
    """
    Zoom plugin artifacts
    """

    name: ClassVar[str] = "Zoom plugin (Outlook)"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\Zoom Plugin")
    regex: ClassVar[str] = r"(?s:.*\.json)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Zoom(KapeTargetConfiguration):
    """
    Author: Ryan McVicar

    Version: 1.0

    ID: 420ce1b0-bfc0-40de-a0fe-f154bbc5eec8

    Zoom client artifacts
    """

    name: ClassVar[str] = "Zoom"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ZoomZoomclientlogs0,
        ZoomZoomclientlogsWindowsXP1,
        ZoomZoomclientrecordings2,
        ZoomZoompluginOutlook3,
    ]


class CloudStorageAllBoxMetadata0(KapeTarget):
    name: ClassVar[str] = "Box Metadata"
    base_path: ClassVar[Path] = Path("BoxDrive_Metadata.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageAllBoxUserFiles1(KapeTarget):
    name: ClassVar[str] = "Box User Files"
    base_path: ClassVar[Path] = Path("BoxDrive_UserFiles.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageAllDropboxMetadata2(KapeTarget):
    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("Dropbox_Metadata.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageAllDropboxUserFiles3(KapeTarget):
    name: ClassVar[str] = "Dropbox User Files"
    base_path: ClassVar[Path] = Path("Dropbox_UserFiles.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageAllGoogleDriveMetadata4(KapeTarget):
    name: ClassVar[str] = "Google Drive Metadata"
    base_path: ClassVar[Path] = Path("GoogleDrive_Metadata.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageAllGoogleDriveBackupandSyncUserFiles5(KapeTarget):
    name: ClassVar[str] = "Google Drive Backup and Sync User Files"
    base_path: ClassVar[Path] = Path("GoogleDriveBackupSync_UserFiles.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageAllOneDriveMetadata6(KapeTarget):
    name: ClassVar[str] = "OneDrive Metadata"
    base_path: ClassVar[Path] = Path("OneDrive_Metadata.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageAllOneDriveUserFiles7(KapeTarget):
    name: ClassVar[str] = "OneDrive User Files"
    base_path: ClassVar[Path] = Path("OneDrive_UserFiles.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageAllpCloudDatabase8(KapeTarget):
    name: ClassVar[str] = "pCloudDatabase"
    base_path: ClassVar[Path] = Path("pCloudDatabase.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageAllSugarSync9(KapeTarget):
    name: ClassVar[str] = "SugarSync"
    base_path: ClassVar[Path] = Path("SugarSync.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageAll(KapeTargetConfiguration):
    """
    Author: Chad Tilbury and Andrew Rathbun

    Version: 1.3

    ID: 63c7ff1e-0fcb-45ae-9d72-29bf8458b6db

    Cloud Storage Contents and Metadata
    """

    name: ClassVar[str] = "CloudStorage_All"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        CloudStorageAllBoxMetadata0,
        CloudStorageAllBoxUserFiles1,
        CloudStorageAllDropboxMetadata2,
        CloudStorageAllDropboxUserFiles3,
        CloudStorageAllGoogleDriveMetadata4,
        CloudStorageAllGoogleDriveBackupandSyncUserFiles5,
        CloudStorageAllOneDriveMetadata6,
        CloudStorageAllOneDriveUserFiles7,
        CloudStorageAllpCloudDatabase8,
        CloudStorageAllSugarSync9,
    ]


class CloudStorageMetadataBoxMetadata0(KapeTarget):
    name: ClassVar[str] = "Box Metadata"
    base_path: ClassVar[Path] = Path("BoxDrive_Metadata.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageMetadataDropboxMetadata1(KapeTarget):
    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("Dropbox_Metadata.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageMetadataGoogleDriveMetadata2(KapeTarget):
    name: ClassVar[str] = "Google Drive Metadata"
    base_path: ClassVar[Path] = Path("GoogleDrive_Metadata.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageMetadataOneDriveMetadata3(KapeTarget):
    name: ClassVar[str] = "OneDrive Metadata"
    base_path: ClassVar[Path] = Path("OneDrive_Metadata.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageMetadata(KapeTargetConfiguration):
    """
    Author: Chad Tilbury and Andrew Rathbun

    Version: 1.0

    ID: 136ca523-2f99-4203-bd66-6aa50fe8d3a8

    Cloud Storage Metadata
    """

    name: ClassVar[str] = "CloudStorage_Metadata"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        CloudStorageMetadataBoxMetadata0,
        CloudStorageMetadataDropboxMetadata1,
        CloudStorageMetadataGoogleDriveMetadata2,
        CloudStorageMetadataOneDriveMetadata3,
    ]


class CloudStorageOneDriveExplorerOneDriveMetadata0(KapeTarget):
    name: ClassVar[str] = "OneDrive Metadata"
    base_path: ClassVar[Path] = Path("OneDrive_Metadata.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageOneDriveExplorerUserRelatedRegistryhives1(KapeTarget):
    name: ClassVar[str] = "User Related Registry hives"
    base_path: ClassVar[Path] = Path("RegistryHivesUser.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageOneDriveExplorerRecycleBinDataAndInfo2(KapeTarget):
    name: ClassVar[str] = "Recycle Bin DataAndInfo"
    base_path: ClassVar[Path] = Path("RecycleBin.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class CloudStorageOneDriveExplorer(KapeTargetConfiguration):
    """
    Author: Brian Maloney

    Version: 1.0

    ID: 9783ccfe-42c2-440b-82c6-428afc5d9a61

    OneDrive and other files used with OneDriveExplorer
    """

    name: ClassVar[str] = "CloudStorage_OneDriveExplorer"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        CloudStorageOneDriveExplorerOneDriveMetadata0,
        CloudStorageOneDriveExplorerUserRelatedRegistryhives1,
        CloudStorageOneDriveExplorerRecycleBinDataAndInfo2,
    ]


class FileExplorerReplacementsDirectoryOpus0(KapeTarget):
    name: ClassVar[str] = "Directory Opus"
    base_path: ClassVar[Path] = Path("DirectoryOpus.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileExplorerReplacementsDoubleCommander1(KapeTarget):
    name: ClassVar[str] = "Double Commander"
    base_path: ClassVar[Path] = Path("DoubleCommander.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileExplorerReplacementsEFCommander2(KapeTarget):
    name: ClassVar[str] = "EF Commander"
    base_path: ClassVar[Path] = Path("EFCommander.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileExplorerReplacementsFreeCommanderXE3(KapeTarget):
    name: ClassVar[str] = "FreeCommander XE"
    base_path: ClassVar[Path] = Path("FreeCommander.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileExplorerReplacementsMidnightCommander4(KapeTarget):
    name: ClassVar[str] = "Midnight Commander"
    base_path: ClassVar[Path] = Path("MidnightCommander.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileExplorerReplacementsMultiCommander5(KapeTarget):
    name: ClassVar[str] = "Multi Commander"
    base_path: ClassVar[Path] = Path("MultiCommander.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileExplorerReplacementsOneCommander6(KapeTarget):
    name: ClassVar[str] = "One Commander"
    base_path: ClassVar[Path] = Path("OneCommander.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileExplorerReplacementsQDir7(KapeTarget):
    name: ClassVar[str] = "Q-Dir"
    base_path: ClassVar[Path] = Path("Q-Dir.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileExplorerReplacementsSpeedCommander8(KapeTarget):
    name: ClassVar[str] = "SpeedCommander"
    base_path: ClassVar[Path] = Path("SpeedCommander.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileExplorerReplacementsTablacusExplorer9(KapeTarget):
    name: ClassVar[str] = "Tablacus Explorer"
    base_path: ClassVar[Path] = Path("TablacusExplorer.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileExplorerReplacementsTotalCommander10(KapeTarget):
    name: ClassVar[str] = "Total Commander"
    base_path: ClassVar[Path] = Path("TotalCommander.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileExplorerReplacementsXYplorer11(KapeTarget):
    name: ClassVar[str] = "XYplorer"
    base_path: ClassVar[Path] = Path("XYplorer.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FileExplorerReplacements(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.3

    ID: 8e1cb436-dada-413f-845d-f2ed0823cb3a

    File Explorer Replacements
    """

    name: ClassVar[str] = "FileExplorerReplacements"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        FileExplorerReplacementsDirectoryOpus0,
        FileExplorerReplacementsDoubleCommander1,
        FileExplorerReplacementsEFCommander2,
        FileExplorerReplacementsFreeCommanderXE3,
        FileExplorerReplacementsMidnightCommander4,
        FileExplorerReplacementsMultiCommander5,
        FileExplorerReplacementsOneCommander6,
        FileExplorerReplacementsQDir7,
        FileExplorerReplacementsSpeedCommander8,
        FileExplorerReplacementsTablacusExplorer9,
        FileExplorerReplacementsTotalCommander10,
        FileExplorerReplacementsXYplorer11,
    ]


class VirtualBoxVirtualBoxLogs0(KapeTarget):
    name: ClassVar[str] = "VirtualBox Logs"
    base_path: ClassVar[Path] = Path("VirtualBoxLogs.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualBoxVirtualBoxMemory1(KapeTarget):
    name: ClassVar[str] = "VirtualBox Memory"
    base_path: ClassVar[Path] = Path("VirtualBoxMemory.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualBoxVirtualBoxConfigs2(KapeTarget):
    name: ClassVar[str] = "VirtualBox Configs"
    base_path: ClassVar[Path] = Path("VirtualBoxConfig.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualBoxVirtualHardDrives3(KapeTarget):
    name: ClassVar[str] = "Virtual Hard Drives"
    base_path: ClassVar[Path] = Path("VirtualDisks.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VirtualBox(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: b6ce74ad-11a1-4e3c-851e-f8772749894b

    Runs all VirtualBox modules to collect Virtualbox VM config files, logs and
    Virtual Hard Disks
    """

    name: ClassVar[str] = "VirtualBox"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        VirtualBoxVirtualBoxLogs0,
        VirtualBoxVirtualBoxMemory1,
        VirtualBoxVirtualBoxConfigs2,
        VirtualBoxVirtualHardDrives3,
    ]


class VMwareVMwareInventory0(KapeTarget):
    name: ClassVar[str] = "VMware Inventory"
    base_path: ClassVar[Path] = Path("VMwareInventory.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VMwareVMwareMemory1(KapeTarget):
    name: ClassVar[str] = "VMware Memory"
    base_path: ClassVar[Path] = Path("VMwareMemory.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VMwareVirtualHardDrives2(KapeTarget):
    name: ClassVar[str] = "Virtual Hard Drives"
    base_path: ClassVar[Path] = Path("VirtualDisks.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class VMware(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 386c40b5-8fc4-495e-b34e-47508e6c3f73

    Runs all VMware modules to collect VMware VM config files, logs and Virtual
    Hard Disks
    """

    name: ClassVar[str] = "VMware"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        VMwareVMwareInventory0,
        VMwareVMwareMemory1,
        VMwareVirtualHardDrives2,
    ]
