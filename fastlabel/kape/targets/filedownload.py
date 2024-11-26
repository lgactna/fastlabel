"""
Auto-generated classes from the .tkape files for the FileDownload category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class AsperaConnectAsperaClientLogs0(KapeTarget):
    name: ClassVar[str] = "Aspera Client Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Aspera\\Aspera Connect\\var\\log\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.log)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AsperaConnectAsperaServerLogs1(KapeTarget):
    name: ClassVar[str] = "Aspera Server Logs"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.aspera\\connect\\var\\log\\")
    regex: ClassVar[str] = r"(?s:.*\.log)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class AsperaConnect(KapeTargetConfiguration):
    """
    Author: Dennis Reneau

    Version: 1.0

    ID: 1f311765-a5c0-496a-a5d5-e79cbd0702e2

    Aspera Connect Log Files
    """

    name: ClassVar[str] = "AsperaConnect"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        AsperaConnectAsperaClientLogs0,
        AsperaConnectAsperaServerLogs1,
    ]


class P2PClientsDC0(KapeTarget):
    name: ClassVar[str] = "DC++"
    base_path: ClassVar[Path] = Path("DC++.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class P2PClientsFrostWire1(KapeTarget):
    name: ClassVar[str] = "FrostWire"
    base_path: ClassVar[Path] = Path("FrostWire.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class P2PClientsGigatribe2(KapeTarget):
    name: ClassVar[str] = "Gigatribe"
    base_path: ClassVar[Path] = Path("Gigatribe.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class P2PClientsShareaza3(KapeTarget):
    name: ClassVar[str] = "Shareaza"
    base_path: ClassVar[Path] = Path("Shareaza.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class P2PClientsSoulseek4(KapeTarget):
    name: ClassVar[str] = "Soulseek"
    base_path: ClassVar[Path] = Path("Soulseek.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class P2PClients(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 4357b5ff-0bd4-41c0-a644-463ea0e14c48

    P2P Clients
    """

    name: ClassVar[str] = "P2PClients"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        P2PClientsDC0,
        P2PClientsFrostWire1,
        P2PClientsGigatribe2,
        P2PClientsShareaza3,
        P2PClientsSoulseek4,
    ]


class TorrentClientsBitTorrent0(KapeTarget):
    name: ClassVar[str] = "BitTorrent"
    base_path: ClassVar[Path] = Path("BitTorrent.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TorrentClientsqBittorrent1(KapeTarget):
    name: ClassVar[str] = "qBittorrent"
    base_path: ClassVar[Path] = Path("qBittorrent.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TorrentClientsuTorrent2(KapeTarget):
    name: ClassVar[str] = "uTorrent"
    base_path: ClassVar[Path] = Path("uTorrent.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class TorrentClients(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: c409301a-0147-41e1-bb01-ffb8ec49a67a

    Torrent Clients
    """

    name: ClassVar[str] = "TorrentClients"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        TorrentClientsBitTorrent0,
        TorrentClientsqBittorrent1,
        TorrentClientsuTorrent2,
    ]


class UsenetClientsNewsbinPro0(KapeTarget):
    name: ClassVar[str] = "NewsbinPro"
    base_path: ClassVar[Path] = Path("NewsbinPro.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UsenetClientsNewsleecher1(KapeTarget):
    name: ClassVar[str] = "Newsleecher"
    base_path: ClassVar[Path] = Path("Newsleecher.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UsenetClientsNZBGet2(KapeTarget):
    name: ClassVar[str] = "NZBGet"
    base_path: ClassVar[Path] = Path("NZBGet.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UsenetClientsSABnbzd3(KapeTarget):
    name: ClassVar[str] = "SABnbzd"
    base_path: ClassVar[Path] = Path("SABnbzd.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UsenetClients(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 2aef5440-16f8-4720-ae40-c2cad380da8d

    Usenet Clients
    """

    name: ClassVar[str] = "UsenetClients"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        UsenetClientsNewsbinPro0,
        UsenetClientsNewsleecher1,
        UsenetClientsNZBGet2,
        UsenetClientsSABnbzd3,
    ]


class BitTorrentTorrentClientsBitTorrent0(KapeTarget):
    name: ClassVar[str] = "TorrentClients - BitTorrent"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\BitTorrent\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BitTorrent(KapeTargetConfiguration):
    """
    Author: Banaanhangwagen

    Version: 1.0

    ID: ea203900-3f49-4ebf-a213-21d82ccae5db

    BitTorrent
    """

    name: ClassVar[str] = "BitTorrent"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [BitTorrentTorrentClientsBitTorrent0]


class DCDCChatLogs0(KapeTarget):
    """
    Locates DC++ hub/chat logs and copies them. Current as of version 0.868.
    """

    name: ClassVar[str] = "DC++ Chat Logs"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\DC++\\Logs\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DC(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 577569f8-e10f-4513-9c59-19d17a10eccb

    DC++
    """

    name: ClassVar[str] = "DC++"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [DCDCChatLogs0]


class FrostWireFrostWireDownloads0(KapeTarget):
    """
    Locates files downloaded that land in the default location as specified by
    FrostWire
    """

    name: ClassVar[str] = "FrostWire Downloads"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\Documents\\FrostWire\\Torrent Data"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FrostWireFrostWireAppData1(KapeTarget):
    """
    Locates a file that contains important information about the instance of
    FrostWire on the user's system
    """

    name: ClassVar[str] = "FrostWire AppData"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.frostwire5")
    regex: ClassVar[str] = r"(?s:frostwire\.props)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FrostWireFrostWireAppData2(KapeTarget):
    """
    Locates a file that contains important information about the instance of
    FrostWire on the user's system
    """

    name: ClassVar[str] = "FrostWire AppData"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\.frostwire5")
    regex: ClassVar[str] = r"(?s:itunes\.props)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class FrostWire(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 7e78190f-e21e-4d55-ae8a-a84e130fb1b1

    FrostWire
    """

    name: ClassVar[str] = "FrostWire"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        FrostWireFrostWireDownloads0,
        FrostWireFrostWireAppData1,
        FrostWireFrostWireAppData2,
    ]


class GigatribeGigatribeFilesWindowsVista78100(KapeTarget):
    """
    Locates Gigatribe files and copies them
    """

    name: ClassVar[str] = "Gigatribe Files Windows Vista/7/8/10"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Shalsoft\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GigatribeGigatribeFilesWindowsXP1(KapeTarget):
    """
    Locates Gigatribe files and copies them. Different path depending on the
    Operating System language. In Swedish the location is C:/Documents and
    Settings/<username>/Lokala Inställningar/Application Data/Gigatribe
    """

    name: ClassVar[str] = "Gigatribe Files Windows XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\*\\Application Data\\Gigatribe\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GigatribeGigatribeFilesWindowsXP2(KapeTarget):
    """
    Locates Gigatribe files and copies them. Different path depending on the
    Operating System language. In Swedish the location is C:/Documents and
    Settings/<username>/Lokala Inställningar/Application Data/Shalsoft
    """

    name: ClassVar[str] = "Gigatribe Files Windows XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\*\\Application Data\\Shalsoft\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Gigatribe(KapeTargetConfiguration):
    """
    Author: Linus Nissi

    Version: 2.0

    ID: 64726d74-1a68-463a-bb26-929054a20b71

    Gigatribe Files
    """

    name: ClassVar[str] = "Gigatribe"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        GigatribeGigatribeFilesWindowsVista78100,
        GigatribeGigatribeFilesWindowsXP1,
        GigatribeGigatribeFilesWindowsXP2,
    ]


class NewsbinProUsenetClientsNewsbinPro0(KapeTarget):
    """
    Locates Newsbin Pro download log database
    """

    name: ClassVar[str] = "Usenet Clients - Newsbin Pro"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Local\\Newsbin\\")
    regex: ClassVar[str] = r"(?s:Downloaded\.db3)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NewsbinPro(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: be5a322b-0093-4944-ad6c-5429f176e515

    Newsbin Pro
    """

    name: ClassVar[str] = "NewsbinPro"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [NewsbinProUsenetClientsNewsbinPro0]


class NewsleecherUsenetClientsNewsleecher0(KapeTarget):
    """
    Locates Newsleecher download .dat file
    """

    name: ClassVar[str] = "Usenet Clients - Newsleecher"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\NewsLeecher\\"
    )
    regex: ClassVar[str] = r"(?s:downloaded\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Newsleecher(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 82920bd3-68bf-42c5-ba3c-55d59af35f64

    Newsleecher
    """

    name: ClassVar[str] = "Newsleecher"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [NewsleecherUsenetClientsNewsleecher0]


class NicotineNicotineLogs0(KapeTarget):
    """
    Locates Nicotine++ chat logs, room logs, transfer logs, and debug logs (if
    enabled)
    """

    name: ClassVar[str] = "Nicotine++ Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%User%\\AppData\\Roaming\\nicotine\\logs"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NicotineNicotineIncompleteDownloads1(KapeTarget):
    """
    Locates files that did not finish downloading
    """

    name: ClassVar[str] = "Nicotine++ Incomplete Downloads"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%User%\\AppData\\Roaming\\nicotine\\incomplete"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NicotineNicotineBuddyfilesdb2(KapeTarget):
    """
    Locates a DB that appears to include shared files from a user's buddy list
    """

    name: ClassVar[str] = "Nicotine++ Buddyfiles.db"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%User%\\AppData\\Roaming\\nicotine\\buddyfiles.db"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NicotineNicotineBuddystreamsdb3(KapeTarget):
    """
    Locates a DB that appears to include shared files from a user's buddy list
    """

    name: ClassVar[str] = "Nicotine++ Buddystreams.db"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%User%\\AppData\\Roaming\\nicotine\\buddystreams.db"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NicotineNicotineBuddymtimesdb4(KapeTarget):
    """
    Locates a DB that appears to enumerate which files the user is sharing to
    their buddy list, from a folder level
    """

    name: ClassVar[str] = "Nicotine++ Buddymtimes.db"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%User%\\AppData\\Roaming\\nicotine\\buddymtimes.db"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NicotineNicotineBuddyfileindexdb5(KapeTarget):
    """
    Locates a DB that appears to enumerate which files the user is sharing to
    their buddy list, from a file level
    """

    name: ClassVar[str] = "Nicotine++ Buddyfileindex.db"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%User%\\AppData\\Roaming\\nicotine\\buddyfileindex.db"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NicotineNicotineBuddywordindexdb6(KapeTarget):
    """
    Unknown what this is for at this time
    """

    name: ClassVar[str] = "Nicotine++ Buddywordindex.db"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%User%\\AppData\\Roaming\\nicotine\\buddywordindex.db"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NicotineNicotineConfigFiles7(KapeTarget):
    """
    Locates config files
    """

    name: ClassVar[str] = "Nicotine++ Config Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%User%\\AppData\\Roaming\\nicotine\\config"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NicotineNicotineUserShares8(KapeTarget):
    """
    Locates a DB that appears to store a list of files per user that they are
    sharing within Nicotine++. Note: this requires the user to right-click ->
    browse files shared by that user
    """

    name: ClassVar[str] = "Nicotine++ User Shares"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%User%\\AppData\\Roaming\\nicotine\\usershares"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NicotineNicotineDownloadsjson9(KapeTarget):
    """
    Locates downloads.json
    """

    name: ClassVar[str] = "Nicotine++ Downloads.json"
    base_path: ClassVar[Path] = Path("C:\\Users\\%User%\\AppData\\Roaming\\nicotine")
    regex: ClassVar[str] = r"(?s:downloads\.json.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NicotineNicotineUploadsjson10(KapeTarget):
    """
    Locates uploads.json
    """

    name: ClassVar[str] = "Nicotine++ Uploads.json"
    base_path: ClassVar[Path] = Path("C:\\Users\\%User%\\AppData\\Roaming\\nicotine")
    regex: ClassVar[str] = r"(?s:uploads\.json.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Nicotine(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: c0b393d5-865e-479d-ac50-fe892ac40e8e

    Nicotine++
    """

    name: ClassVar[str] = "Nicotine++"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        NicotineNicotineLogs0,
        NicotineNicotineIncompleteDownloads1,
        NicotineNicotineBuddyfilesdb2,
        NicotineNicotineBuddystreamsdb3,
        NicotineNicotineBuddymtimesdb4,
        NicotineNicotineBuddyfileindexdb5,
        NicotineNicotineBuddywordindexdb6,
        NicotineNicotineConfigFiles7,
        NicotineNicotineUserShares8,
        NicotineNicotineDownloadsjson9,
        NicotineNicotineUploadsjson10,
    ]


class NZBGetUsenetClientsNZBGetLogFile0(KapeTarget):
    """
    Locates NZBGet download log file
    """

    name: ClassVar[str] = "Usenet Clients - NZBGet Log File"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\NZBGet\\")
    regex: ClassVar[str] = r"(?s:nzbget\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NZBGetUsenetClientsNZBGetNZBs1(KapeTarget):
    """
    Locates NZBGet NZB files that were used by the user
    """

    name: ClassVar[str] = "Usenet Clients - NZBGet NZBs"
    base_path: ClassVar[Path] = Path("C:\\ProgramData\\NZBGet\\nzb\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class NZBGet(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 2c6ffe1d-f884-4065-a4e7-f81dd0d50ea7

    NZBGet
    """

    name: ClassVar[str] = "NZBGet"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        NZBGetUsenetClientsNZBGetLogFile0,
        NZBGetUsenetClientsNZBGetNZBs1,
    ]


class qBittorrentTorrentClientsqBittorrent0(KapeTarget):
    name: ClassVar[str] = "TorrentClients - qBittorrent"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Roaming\\qBittorrent\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.ini)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class qBittorrentTorrentClientsqBittorrent1(KapeTarget):
    name: ClassVar[str] = "TorrentClients - qBittorrent"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\qBittorrent\\logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class qBittorrent(KapeTargetConfiguration):
    """
    Author: Banaanhangwagen

    Version: 1.0

    ID: 17956359-4d7b-4428-8207-2d745d7f6267

    qBittorrent
    """

    name: ClassVar[str] = "qBittorrent"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        qBittorrentTorrentClientsqBittorrent0,
        qBittorrentTorrentClientsqBittorrent1,
    ]


class SABnbzdUsenetClientsSABnzbdDownloadLogs0(KapeTarget):
    """
    Locates SABnzbd download log
    """

    name: ClassVar[str] = "Usenet Clients - SABnzbd Download Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\sabnzbd\\logs\\"
    )
    regex: ClassVar[str] = r"(?s:sabnzbd\.log)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SABnbzdUsenetClientsSABnzbdHistorydb1(KapeTarget):
    """
    Locates SABnzbd history log
    """

    name: ClassVar[str] = "Usenet Clients - SABnzbd History.db"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\sabnzbd\\admin\\"
    )
    regex: ClassVar[str] = r"(?s:history1\.db)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SABnbzd(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 315fb563-fe32-4efb-a1b8-1be4d05023ef

    SABnbzd
    """

    name: ClassVar[str] = "SABnbzd"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SABnbzdUsenetClientsSABnzbdDownloadLogs0,
        SABnbzdUsenetClientsSABnzbdHistorydb1,
    ]


class ShareazaShareazaLogs0(KapeTarget):
    """
    Locates Shareaza logs and copies them.
    """

    name: ClassVar[str] = "Shareaza Logs"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\Shareaza\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Shareaza(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 3d3203ae-e753-4c37-ac82-d67735972d44

    Shareaza
    """

    name: ClassVar[str] = "Shareaza"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [ShareazaShareazaLogs0]


class SoulseekSoulseekChatLogs0(KapeTarget):
    """
    Locates Soulseek chat logs and copies them. Chat logs are in plaintext.
    Current as of version 2019.7.22.
    """

    name: ClassVar[str] = "Soulseek Chat Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\SoulseekQt\\Soulseek Chat Logs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SoulseekSoulseekSearchHistorySharedFoldersSettings1(KapeTarget):
    """
    Locates .dat file(s) containing: search history, active searches
    (search_record), current shared folders (shared_file_folder), and wish list
    items (wish_list_item).
    """

    name: ClassVar[str] = "Soulseek Search History/Shared Folders/Settings"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\SoulseekQt\\1\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Soulseek(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: c68061f4-9f79-4d7d-9e95-30636103ed19

    Soulseek
    """

    name: ClassVar[str] = "Soulseek"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SoulseekSoulseekChatLogs0,
        SoulseekSoulseekSearchHistorySharedFoldersSettings1,
    ]


class TorrentsTorrents0(KapeTarget):
    name: ClassVar[str] = "Torrents"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.torrent)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Torrents(KapeTargetConfiguration):
    """
    Author: Tony Knutson

    Version: 2.0

    ID: 082de7fa-17b4-4e10-a4e8-94ef2fb27ec2

    Torrent Files
    """

    name: ClassVar[str] = "Torrents"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [TorrentsTorrents0]


class UsenetUsenetNZBFiles0(KapeTarget):
    name: ClassVar[str] = "Usenet (NZB) Files"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.nzb)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Usenet(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: bae4da97-b565-4cae-b090-dd992839983f

    Usenet (NZB) Files
    """

    name: ClassVar[str] = "Usenet"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [UsenetUsenetNZBFiles0]


class uTorrentTorrentClientsuTorrent0(KapeTarget):
    name: ClassVar[str] = "TorrentClients - uTorrent"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\AppData\\Roaming\\uTorrent\\")
    regex: ClassVar[str] = r"(?s:.*\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class uTorrent(KapeTargetConfiguration):
    """
    Author: Banaanhangwagen

    Version: 1.0

    ID: df8ed278-cd5e-4345-bb30-9b25182bf2d4

    uTorrent
    """

    name: ClassVar[str] = "uTorrent"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [uTorrentTorrentClientsuTorrent0]
