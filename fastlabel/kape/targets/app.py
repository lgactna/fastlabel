"""
Auto-generated classes from the .tkape files for the App category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class EvernoteEvernoteAccounts0(KapeTarget):
    """
    Holds username and email of accounts
    """

    name: ClassVar[str] = "Evernote Accounts"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Evernote\\Evernote\\Databases\\"
    )
    file_mask: ClassVar[str] = ".accounts"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EvernoteEvernoteNotebooks1(KapeTarget):
    """
    SQLite Database of the notes
    """

    name: ClassVar[str] = "Evernote Notebooks"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Evernote\\Evernote\\Databases\\"
    )
    file_mask: ClassVar[str] = "*.exb"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class EvernoteEvernoteNotebookSnippets2(KapeTarget):
    """
    Note 'Snippets'
    """

    name: ClassVar[str] = "Evernote Notebook Snippets"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Evernote\\Evernote\\Databases\\"
    )
    file_mask: ClassVar[str] = "*.exb.snippets"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Evernote(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: acea0975-6610-4813-8a27-8e78186c87d5

    Evernote
    """

    name: ClassVar[str] = "Evernote"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        EvernoteEvernoteAccounts0,
        EvernoteEvernoteNotebooks1,
        EvernoteEvernoteNotebookSnippets2,
    ]


class FreeDownloadManagerFDMDatabase0(KapeTarget):
    """
    fdm.sqlite shows Torrents, downloads, folder history, auth credentials and
    more. Will also pull fdm.sqlite in db_backup/
    """

    name: ClassVar[str] = "FDM Database"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Free Download Manager\\"
    )
    file_mask: ClassVar[str] = "fdm.sqlite"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreeDownloadManagerFDMBackupInfo1(KapeTarget):
    """
    Backup info file - can change backup name from userdata.zip, so could give
    indication of file name
    """

    name: ClassVar[str] = "FDM Backup Info"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Free Download Manager\\backup\\"
    )
    file_mask: ClassVar[str] = "backup.info"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreeDownloadManagerFDMDatabaseuserdatazip2(KapeTarget):
    """
    fdm.sqlite can also appear in the backup folder in a compressed userdata.zip
    file
    """

    name: ClassVar[str] = "FDM Database (userdata.zip)"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Free Download Manager\\backup\\"
    )
    file_mask: ClassVar[str] = "userdata.zip"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FreeDownloadManager(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 328c98bc-f5f8-4aff-93c1-53fbf02f5ec7

    Free Download Manager
    """

    name: ClassVar[str] = "FreeDownloadManager"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        FreeDownloadManagerFDMDatabase0,
        FreeDownloadManagerFDMBackupInfo1,
        FreeDownloadManagerFDMDatabaseuserdatazip2,
    ]


class JDownloader2JDownloader20DownloadLists0(KapeTarget):
    """
    Zip folder which contains several files (00,00_00 and extraInfo) which list
    the download folder, the time it was created, the name of the download,
    origin URL, referral URL and more
    """

    name: ClassVar[str] = "JDownloader 2.0 Download Lists"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\JDownloader 2.0\\cfg"
    )
    file_mask: ClassVar[str] = "downloadList*.zip"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JDownloader2JDownloader20LinkCollector1(KapeTarget):
    """
    Zip folder which contains several files (0X,0X_00 and extraInfo) which list
    the websites crawled for links, the referral URLs, timestamps and more
    """

    name: ClassVar[str] = "JDownloader 2.0 Link Collector"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\JDownloader 2.0\\cfg"
    )
    file_mask: ClassVar[str] = "linkcollector*.zip"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JDownloader2JDownloader20GeneralSettings2(KapeTarget):
    """
    General user config for JDownloader 2.0. Holds default download folder.
    """

    name: ClassVar[str] = "JDownloader 2.0 General Settings"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\JDownloader 2.0\\cfg"
    )
    file_mask: ClassVar[str] = "org.jdownloader.settings.GeneralSettings.json"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JDownloader2JDownloader20LinkGrabberSettings3(KapeTarget):
    """
    Linkgrabber Settings for JDownloader 2.0. Holds latest download destination
    folder.
    """

    name: ClassVar[str] = "JDownloader 2.0 Link Grabber Settings"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\JDownloader 2.0\\cfg"
    )
    file_mask: ClassVar[str] = (
        "org.jdownloader.gui.views.linkgrabber.addlinksdialog.LinkgrabberSettings.json"
    )
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JDownloader2JDownloader20ProxySettings4(KapeTarget):
    """
    Proxy configuration for JDownloader 2.0
    """

    name: ClassVar[str] = "JDownloader 2.0 Proxy Settings"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\JDownloader 2.0\\cfg"
    )
    file_mask: ClassVar[str] = (
        "org.jdownloader.settings.InternetConnectionSettings.customproxylist.json"
    )
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JDownloader2(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 41b218bd-c886-442d-b3a6-7a18a1cd4091

    JDownloader 2
    """

    name: ClassVar[str] = "JDownloader2"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        JDownloader2JDownloader20DownloadLists0,
        JDownloader2JDownloader20LinkCollector1,
        JDownloader2JDownloader20GeneralSettings2,
        JDownloader2JDownloader20LinkGrabberSettings3,
        JDownloader2JDownloader20ProxySettings4,
    ]
