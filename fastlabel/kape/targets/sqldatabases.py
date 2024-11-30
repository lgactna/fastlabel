"""
Auto-generated classes from the .tkape files for the SQLDatabases category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class SQLiteDatabases4KVideoDownloader0(KapeTarget):
    """
    Grabs database(s) that stores user download history
    """

    name: ClassVar[str] = "4K Video Downloader"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\4kdownload.com\\4K Video Downloader\\4K Video Downloader"
    )
    file_mask: ClassVar[str] = "*.sqlite"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesMicrosoftOneNoteFullTextSearchIndex1(KapeTarget):
    """
    Grabs database(s) comprising of each OneNote notebook's text content
    """

    name: ClassVar[str] = "Microsoft OneNote - FullTextSearchIndex"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.Office.OneNote_8wekyb3d8bbwe\\LocalState\\AppData\\Local\\OneNote\\*\\FullTextSearchIndex"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesMicrosoftOneNoteRecentNotebooksSeenURLs2(KapeTarget):
    """
    Grabs a file that appears to record recently seen OneNote notebooks
    """

    name: ClassVar[str] = "Microsoft OneNote - RecentNotebooks_SeenURLs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.Office.OneNote_8wekyb3d8bbwe\\LocalState\\AppData\\Local\\OneNote\\Notifications"
    )
    file_mask: ClassVar[str] = "RecentNotebooks_SeenURLs"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesMicrosoftOneNoteAccessibilityCheckerIndex3(KapeTarget):
    """
    Grabs database(s) comprising of each OneNote notebook's version sync error
    history
    """

    name: ClassVar[str] = "Microsoft OneNote - AccessibilityCheckerIndex"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.Office.OneNote_8wekyb3d8bbwe\\LocalState\\AppData\\Local\\OneNote\\16.0\\AccessibilityCheckerIndex"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesMicrosoftOneNoteUserNoteTags4(KapeTarget):
    """
    Grabs a database that stores the user specified tags within OneNote to be
    used application-wide
    """

    name: ClassVar[str] = "Microsoft OneNote - User NoteTags"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.Office.OneNote_8wekyb3d8bbwe\\LocalState\\AppData\\Local\\OneNote\\16.0\\NoteTags"
    )
    file_mask: ClassVar[str] = "*LiveId.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesMicrosoftOneNoteRecentSearches5(KapeTarget):
    """
    Grabs a database that stores the user's recent searches within OneNote
    """

    name: ClassVar[str] = "Microsoft OneNote - RecentSearches"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.Office.OneNote_8wekyb3d8bbwe\\LocalState\\AppData\\Local\\OneNote\\16.0\\RecentSearches"
    )
    file_mask: ClassVar[str] = "RecentSearches.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesMicrosoftStickyNotes1607andlater6(KapeTarget):
    name: ClassVar[str] = "Microsoft Sticky Notes - 1607 and later"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.MicrosoftStickyNotes*\\LocalState\\"
    )
    file_mask: ClassVar[str] = "plum.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesMicrosoftToDoSQLiteDatabaseofToDotasks7(KapeTarget):
    name: ClassVar[str] = "Microsoft To Do - SQLite Database of To Do tasks"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\Microsoft.Todos_8wekyb3d8bbwe\\LocalState\\AccountsRoot\\*\\"
    )
    file_mask: ClassVar[str] = "todosqlite.db*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesTeraCopyHistoryDatabases8(KapeTarget):
    name: ClassVar[str] = "TeraCopy - History Databases"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\TeraCopy\\History"
    )
    file_mask: ClassVar[str] = "*.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesTeraCopyMainDatabase9(KapeTarget):
    name: ClassVar[str] = "TeraCopy - Main Database"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\TeraCopy\\")
    file_mask: ClassVar[str] = "main.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesDropboxMetadata10(KapeTarget):
    """
    Getting individual files because folder may contain very large extraneous
    files
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Dropbox\\*\\")
    file_mask: ClassVar[str] = "filecache.db*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesDropboxMetadata11(KapeTarget):
    """
    Getting individual files because folder may contain very large extraneous
    files
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Dropbox\\*\\")
    file_mask: ClassVar[str] = "config.dbx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesDropboxMetadata12(KapeTarget):
    """
    SQlite database which appears to keep track of the user's recent Dropbox
    activity
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Dropbox\\*\\")
    file_mask: ClassVar[str] = "home.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesDropboxMetadata13(KapeTarget):
    """
    SQLite database which appears to keep track of icons in the user's Drobox
    sync history which can give an indication as to which files and folders are
    present
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Dropbox\\*\\")
    file_mask: ClassVar[str] = "icon.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesDropboxMetadata14(KapeTarget):
    """
    SQLite database which appears to keep track of the user's Drobox sync
    history
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Dropbox\\*\\")
    file_mask: ClassVar[str] = "sync_history.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesDropboxMetadata15(KapeTarget):
    """
    SQLite database which appears to contain a table for deleted files
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Dropbox\\*\\sync\\"
    )
    file_mask: ClassVar[str] = "nucleus.sqlite3*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesDropboxMetadata16(KapeTarget):
    """
    SQLite database which contains the local path of the user's Dropbox folder
    encoded in BASE64. Decode each line separately, not together.
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Dropbox\\")
    file_mask: ClassVar[str] = "host.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesDropboxMetadata17(KapeTarget):
    """
    SQLite database which contains the local path of the user's Dropbox folder
    encoded in BASE64. Decode each line separately, not together.
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Dropbox\\")
    file_mask: ClassVar[str] = "host.dbx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesDropboxMetadata18(KapeTarget):
    """
    SQLite database which appears to contain snapshot table of the user's
    Dropbox contents in JSON with timestamps in UNIX Epoch
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Dropbox\\*\\sync\\"
    )
    file_mask: ClassVar[str] = "aggregation.dbx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesDropboxMetadata19(KapeTarget):
    """
    SQLite database which appears to contain the ID's of account(s) on the
    user's system where Dropbox is installed
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Dropbox\\*\\")
    file_mask: ClassVar[str] = "avatarcache.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesDropboxMetadata20(KapeTarget):
    """
    SQLite database which appears to contain the ID's of account(s) on the
    user's system where Dropbox is installed
    """

    name: ClassVar[str] = "Dropbox Metadata"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Dropbox\\*\\")
    file_mask: ClassVar[str] = "avatarcache.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesGoogleFileStreamMetadata21(KapeTarget):
    """
    Windows_GoogleDrive_CloudGraphDB.smap
    """

    name: ClassVar[str] = "Google File Stream Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Drive\\*\\cloud_graph\\"
    )
    file_mask: ClassVar[str] = "cloud_graph.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesGoogleFileStreamMetadata22(KapeTarget):
    """
    DB(s) with seemingly randomized filename(s) that track file system changes
    within Google Drive
    """

    name: ClassVar[str] = "Google File Stream Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Drive\\*\\TempData\\*\\change_buffer\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesGoogleFileStreamMetadata23(KapeTarget):
    """
    Windows_GoogleDrive_SnapshotDB.smap
    """

    name: ClassVar[str] = "Google File Stream Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Drive\\*\\"
    )
    file_mask: ClassVar[str] = "snapshot.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesGoogleFileStreamMetadata24(KapeTarget):
    """
    Windows_GoogleDrive_SyncConfigDB.smap
    """

    name: ClassVar[str] = "Google File Stream Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Drive\\*\\"
    )
    file_mask: ClassVar[str] = "sync_config.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesFileZillaSQLite3LogFiles25(KapeTarget):
    name: ClassVar[str] = "FileZilla SQLite3 Log Files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\FileZilla\\")
    file_mask: ClassVar[str] = "*.sqlite3*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromebookmarksXP26(KapeTarget):
    name: ClassVar[str] = "Chrome bookmarks XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Bookmarks*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeCookiesXP27(KapeTarget):
    name: ClassVar[str] = "Chrome Cookies XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Cookies*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeCurrentSessionXP28(KapeTarget):
    name: ClassVar[str] = "Chrome Current Session XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Current Session"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeCurrentTabsXP29(KapeTarget):
    name: ClassVar[str] = "Chrome Current Tabs XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Current Tabs"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeFaviconsXP30(KapeTarget):
    name: ClassVar[str] = "Chrome Favicons XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Favicons*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeHistoryXP31(KapeTarget):
    name: ClassVar[str] = "Chrome History XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "History*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeLastSessionXP32(KapeTarget):
    name: ClassVar[str] = "Chrome Last Session XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Last Session"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeLastTabsXP33(KapeTarget):
    name: ClassVar[str] = "Chrome Last Tabs XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Last Tabs"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeLoginDataXP34(KapeTarget):
    name: ClassVar[str] = "Chrome Login Data XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Login Data"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromePreferencesXP35(KapeTarget):
    name: ClassVar[str] = "Chrome Preferences XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Preferences"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeShortcutsXP36(KapeTarget):
    name: ClassVar[str] = "Chrome Shortcuts XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Shortcuts*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeTopSitesXP37(KapeTarget):
    name: ClassVar[str] = "Chrome Top Sites XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Top Sites*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeVisitedLinksXP38(KapeTarget):
    name: ClassVar[str] = "Chrome Visited Links XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Visited Links"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeWebDataXP39(KapeTarget):
    name: ClassVar[str] = "Chrome Web Data XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Web Data*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromebookmarks40(KapeTarget):
    name: ClassVar[str] = "Chrome bookmarks"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Bookmarks*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeCookies41(KapeTarget):
    name: ClassVar[str] = "Chrome Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Cookies*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeCurrentSession42(KapeTarget):
    name: ClassVar[str] = "Chrome Current Session"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Current Session"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeCurrentTabs43(KapeTarget):
    name: ClassVar[str] = "Chrome Current Tabs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Current Tabs"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeDownloadMetadata44(KapeTarget):
    name: ClassVar[str] = "Chrome Download Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Download Metadata"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeExtensionCookies45(KapeTarget):
    name: ClassVar[str] = "Chrome Extension Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Extension Cookies"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeFavicons46(KapeTarget):
    name: ClassVar[str] = "Chrome Favicons"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Favicons*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeHistory47(KapeTarget):
    name: ClassVar[str] = "Chrome History"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "History*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeLastSession48(KapeTarget):
    name: ClassVar[str] = "Chrome Last Session"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Last Session"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeLastTabs49(KapeTarget):
    name: ClassVar[str] = "Chrome Last Tabs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Last Tabs"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeLoginData50(KapeTarget):
    name: ClassVar[str] = "Chrome Login Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Login Data"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeMediaHistory51(KapeTarget):
    name: ClassVar[str] = "Chrome Media History"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Media History*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeNetworkActionPredictor52(KapeTarget):
    name: ClassVar[str] = "Chrome Network Action Predictor"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Network Action Predictor"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeNetworkPersistentState53(KapeTarget):
    name: ClassVar[str] = "Chrome Network Persistent State"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Network Persistent State"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromePreferences54(KapeTarget):
    name: ClassVar[str] = "Chrome Preferences"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Preferences"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeQuotaManager55(KapeTarget):
    name: ClassVar[str] = "Chrome Quota Manager"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "QuotaManager"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeReportingandNEL56(KapeTarget):
    name: ClassVar[str] = "Chrome Reporting and NEL"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Reporting and NEL"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeShortcuts57(KapeTarget):
    name: ClassVar[str] = "Chrome Shortcuts"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Shortcuts*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeTopSites58(KapeTarget):
    name: ClassVar[str] = "Chrome Top Sites"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Top Sites*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeTrustTokens59(KapeTarget):
    name: ClassVar[str] = "Chrome Trust Tokens"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Trust Tokens*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeSyncDataDatabase60(KapeTarget):
    name: ClassVar[str] = "Chrome SyncData Database"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\Sync Data"
    )
    file_mask: ClassVar[str] = "SyncData.sqlite3"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeVisitedLinks61(KapeTarget):
    name: ClassVar[str] = "Chrome Visited Links"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Visited Links"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesChromeWebData62(KapeTarget):
    name: ClassVar[str] = "Chrome Web Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Web Data*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgebookmarks63(KapeTarget):
    name: ClassVar[str] = "Edge bookmarks"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Bookmarks*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeCollections64(KapeTarget):
    name: ClassVar[str] = "Edge Collections"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\Collections"
    )
    file_mask: ClassVar[str] = "collectionsSQLite"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeCookies65(KapeTarget):
    name: ClassVar[str] = "Edge Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Cookies*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeCurrentSession66(KapeTarget):
    name: ClassVar[str] = "Edge Current Session"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Current Session"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeCurrentTabs67(KapeTarget):
    name: ClassVar[str] = "Edge Current Tabs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Current Tabs"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeFavicons68(KapeTarget):
    name: ClassVar[str] = "Edge Favicons"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Favicons*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeHistory69(KapeTarget):
    name: ClassVar[str] = "Edge History"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "History*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeLastSession70(KapeTarget):
    name: ClassVar[str] = "Edge Last Session"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Last Session"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeLastTabs71(KapeTarget):
    name: ClassVar[str] = "Edge Last Tabs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Last Tabs"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeLoginData72(KapeTarget):
    name: ClassVar[str] = "Edge Login Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Login Data"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeMediaHistory73(KapeTarget):
    name: ClassVar[str] = "Edge Media History"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Media History*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeNetworkActionPredictor74(KapeTarget):
    name: ClassVar[str] = "Edge Network Action Predictor"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Network Action Predictor"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgePreferences75(KapeTarget):
    name: ClassVar[str] = "Edge Preferences"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Preferences"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeShortcuts76(KapeTarget):
    name: ClassVar[str] = "Edge Shortcuts"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Shortcuts*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeTopSites77(KapeTarget):
    name: ClassVar[str] = "Edge Top Sites"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Top Sites*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeSyncDataDatabase78(KapeTarget):
    name: ClassVar[str] = "Edge SyncData Database"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\Sync Data"
    )
    file_mask: ClassVar[str] = "SyncData.sqlite3"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeBookmarks79(KapeTarget):
    name: ClassVar[str] = "Edge Bookmarks"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Bookmarks*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeVisitedLinks80(KapeTarget):
    name: ClassVar[str] = "Edge Visited Links"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Visited Links"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEdgeWebData81(KapeTarget):
    name: ClassVar[str] = "Edge Web Data"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Edge\\User Data\\*\\"
    )
    file_mask: ClassVar[str] = "Web Data*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesAddons82(KapeTarget):
    name: ClassVar[str] = "Addons"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    file_mask: ClassVar[str] = "addons.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesBookmarks83(KapeTarget):
    name: ClassVar[str] = "Bookmarks"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\weave\\"
    )
    file_mask: ClassVar[str] = "bookmarks.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesCookies84(KapeTarget):
    name: ClassVar[str] = "Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    file_mask: ClassVar[str] = "cookies.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesCookies85(KapeTarget):
    name: ClassVar[str] = "Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    file_mask: ClassVar[str] = "firefox_cookies.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesDownloads86(KapeTarget):
    name: ClassVar[str] = "Downloads"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    file_mask: ClassVar[str] = "downloads.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesFavicons87(KapeTarget):
    name: ClassVar[str] = "Favicons"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    file_mask: ClassVar[str] = "favicons.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesFormhistory88(KapeTarget):
    name: ClassVar[str] = "Form history"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    file_mask: ClassVar[str] = "formhistory.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesPermissions89(KapeTarget):
    name: ClassVar[str] = "Permissions"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    file_mask: ClassVar[str] = "permissions.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesPlaces90(KapeTarget):
    name: ClassVar[str] = "Places"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    file_mask: ClassVar[str] = "places.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesProtections91(KapeTarget):
    name: ClassVar[str] = "Protections"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    file_mask: ClassVar[str] = "protections.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesSearch92(KapeTarget):
    name: ClassVar[str] = "Search"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    file_mask: ClassVar[str] = "search.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesSignons93(KapeTarget):
    name: ClassVar[str] = "Signons"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    file_mask: ClassVar[str] = "signons.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesStorageSync94(KapeTarget):
    name: ClassVar[str] = "Storage Sync"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    file_mask: ClassVar[str] = "storage-sync.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesWebappstore95(KapeTarget):
    name: ClassVar[str] = "Webappstore"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\*\\"
    )
    file_mask: ClassVar[str] = "webappstore.sqlite*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesWindows10NotificationDB96(KapeTarget):
    name: ClassVar[str] = "Windows 10 Notification DB"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\Notifications\\"
    )
    file_mask: ClassVar[str] = "wpndatabase.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesWindows10NotificationDB97(KapeTarget):
    name: ClassVar[str] = "Windows 10 Notification DB"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\Notifications\\"
    )
    file_mask: ClassVar[str] = "appdb.dat"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesActivitiesCachedb98(KapeTarget):
    name: ClassVar[str] = "ActivitiesCache.db"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\ConnectedDevicesPlatform\\*\\"
    )
    file_mask: ClassVar[str] = "ActivitiesCache.db*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesUpdateStoredb99(KapeTarget):
    name: ClassVar[str] = "Update Store.db"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\USOPrivate\\UpdateStore")
    file_mask: ClassVar[str] = "store.db"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesBitdefenderSQLiteDBFiles100(KapeTarget):
    """
    Bitdefender SQLite databases
    """

    name: ClassVar[str] = "Bitdefender SQLite DB Files"
    base_path: ClassVar[Path] = Path("C:\\Program Files*\\Bitdefender*\\")
    file_mask: ClassVar[str] = "regex:*.+\\.(db|db-wal|db-shm)"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEventTranscriptdb101(KapeTarget):
    name: ClassVar[str] = "EventTranscript.db"
    base_path: ClassVar[Path] = Path(
        "C:\\ProgramData\\Microsoft\\Diagnosis\\EventTranscript"
    )
    file_mask: ClassVar[str] = "EventTranscript.db*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabasesEventTranscriptdb102(KapeTarget):
    name: ClassVar[str] = "EventTranscript.db"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\ProgramData\\Microsoft\\Diagnosis\\EventTranscript"
    )
    file_mask: ClassVar[str] = "EventTranscript.db*"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SQLiteDatabases(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.3

    ID: 61d2909c-dcf2-481f-9169-53ea0c2455ba

    SQLDatabases Target for use with SQLECmd Module
    """

    name: ClassVar[str] = "SQLiteDatabases"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SQLiteDatabases4KVideoDownloader0,
        SQLiteDatabasesMicrosoftOneNoteFullTextSearchIndex1,
        SQLiteDatabasesMicrosoftOneNoteRecentNotebooksSeenURLs2,
        SQLiteDatabasesMicrosoftOneNoteAccessibilityCheckerIndex3,
        SQLiteDatabasesMicrosoftOneNoteUserNoteTags4,
        SQLiteDatabasesMicrosoftOneNoteRecentSearches5,
        SQLiteDatabasesMicrosoftStickyNotes1607andlater6,
        SQLiteDatabasesMicrosoftToDoSQLiteDatabaseofToDotasks7,
        SQLiteDatabasesTeraCopyHistoryDatabases8,
        SQLiteDatabasesTeraCopyMainDatabase9,
        SQLiteDatabasesDropboxMetadata10,
        SQLiteDatabasesDropboxMetadata11,
        SQLiteDatabasesDropboxMetadata12,
        SQLiteDatabasesDropboxMetadata13,
        SQLiteDatabasesDropboxMetadata14,
        SQLiteDatabasesDropboxMetadata15,
        SQLiteDatabasesDropboxMetadata16,
        SQLiteDatabasesDropboxMetadata17,
        SQLiteDatabasesDropboxMetadata18,
        SQLiteDatabasesDropboxMetadata19,
        SQLiteDatabasesDropboxMetadata20,
        SQLiteDatabasesGoogleFileStreamMetadata21,
        SQLiteDatabasesGoogleFileStreamMetadata22,
        SQLiteDatabasesGoogleFileStreamMetadata23,
        SQLiteDatabasesGoogleFileStreamMetadata24,
        SQLiteDatabasesFileZillaSQLite3LogFiles25,
        SQLiteDatabasesChromebookmarksXP26,
        SQLiteDatabasesChromeCookiesXP27,
        SQLiteDatabasesChromeCurrentSessionXP28,
        SQLiteDatabasesChromeCurrentTabsXP29,
        SQLiteDatabasesChromeFaviconsXP30,
        SQLiteDatabasesChromeHistoryXP31,
        SQLiteDatabasesChromeLastSessionXP32,
        SQLiteDatabasesChromeLastTabsXP33,
        SQLiteDatabasesChromeLoginDataXP34,
        SQLiteDatabasesChromePreferencesXP35,
        SQLiteDatabasesChromeShortcutsXP36,
        SQLiteDatabasesChromeTopSitesXP37,
        SQLiteDatabasesChromeVisitedLinksXP38,
        SQLiteDatabasesChromeWebDataXP39,
        SQLiteDatabasesChromebookmarks40,
        SQLiteDatabasesChromeCookies41,
        SQLiteDatabasesChromeCurrentSession42,
        SQLiteDatabasesChromeCurrentTabs43,
        SQLiteDatabasesChromeDownloadMetadata44,
        SQLiteDatabasesChromeExtensionCookies45,
        SQLiteDatabasesChromeFavicons46,
        SQLiteDatabasesChromeHistory47,
        SQLiteDatabasesChromeLastSession48,
        SQLiteDatabasesChromeLastTabs49,
        SQLiteDatabasesChromeLoginData50,
        SQLiteDatabasesChromeMediaHistory51,
        SQLiteDatabasesChromeNetworkActionPredictor52,
        SQLiteDatabasesChromeNetworkPersistentState53,
        SQLiteDatabasesChromePreferences54,
        SQLiteDatabasesChromeQuotaManager55,
        SQLiteDatabasesChromeReportingandNEL56,
        SQLiteDatabasesChromeShortcuts57,
        SQLiteDatabasesChromeTopSites58,
        SQLiteDatabasesChromeTrustTokens59,
        SQLiteDatabasesChromeSyncDataDatabase60,
        SQLiteDatabasesChromeVisitedLinks61,
        SQLiteDatabasesChromeWebData62,
        SQLiteDatabasesEdgebookmarks63,
        SQLiteDatabasesEdgeCollections64,
        SQLiteDatabasesEdgeCookies65,
        SQLiteDatabasesEdgeCurrentSession66,
        SQLiteDatabasesEdgeCurrentTabs67,
        SQLiteDatabasesEdgeFavicons68,
        SQLiteDatabasesEdgeHistory69,
        SQLiteDatabasesEdgeLastSession70,
        SQLiteDatabasesEdgeLastTabs71,
        SQLiteDatabasesEdgeLoginData72,
        SQLiteDatabasesEdgeMediaHistory73,
        SQLiteDatabasesEdgeNetworkActionPredictor74,
        SQLiteDatabasesEdgePreferences75,
        SQLiteDatabasesEdgeShortcuts76,
        SQLiteDatabasesEdgeTopSites77,
        SQLiteDatabasesEdgeSyncDataDatabase78,
        SQLiteDatabasesEdgeBookmarks79,
        SQLiteDatabasesEdgeVisitedLinks80,
        SQLiteDatabasesEdgeWebData81,
        SQLiteDatabasesAddons82,
        SQLiteDatabasesBookmarks83,
        SQLiteDatabasesCookies84,
        SQLiteDatabasesCookies85,
        SQLiteDatabasesDownloads86,
        SQLiteDatabasesFavicons87,
        SQLiteDatabasesFormhistory88,
        SQLiteDatabasesPermissions89,
        SQLiteDatabasesPlaces90,
        SQLiteDatabasesProtections91,
        SQLiteDatabasesSearch92,
        SQLiteDatabasesSignons93,
        SQLiteDatabasesStorageSync94,
        SQLiteDatabasesWebappstore95,
        SQLiteDatabasesWindows10NotificationDB96,
        SQLiteDatabasesWindows10NotificationDB97,
        SQLiteDatabasesActivitiesCachedb98,
        SQLiteDatabasesUpdateStoredb99,
        SQLiteDatabasesBitdefenderSQLiteDBFiles100,
        SQLiteDatabasesEventTranscriptdb101,
        SQLiteDatabasesEventTranscriptdb102,
    ]
