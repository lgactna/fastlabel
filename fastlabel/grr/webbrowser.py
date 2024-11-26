"""
Auto-generated classes from the YAML declarations in webbrowser.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class InternetExplorerCache(GRRArtifactBase):
    """
    Microsoft Internet Explorer (MSIE) browser cache.

    * MSIE 4 - 9 Temporary Internet files. * MSIE 10 INetCache files.

    Reference URLs: https://forensics.wiki/internet_explorer
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Microsoft\\Windows\\Temporary Internet Files\\Content.IE5\\*\\*",
                    "%%users.localappdata%%\\Microsoft\\Windows\\Temporary Internet Files\\Low\\Content.IE5\\*\\*",
                    "%%users.localappdata%%\\Microsoft\\Windows\\INetCache\\IE\\*\\*",
                    "%%users.localappdata%%\\Microsoft\\Windows\\INetCache\\Low\\*\\*",
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


class FirefoxCache(GRRArtifactBase):
    """
    Mozilla Firefox browser caches.

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/webbrowser/FirefoxCache.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Caches/Firefox/Profiles/*.default/Cache/*",
                    "%%users.homedir%%/Library/Caches/Firefox/Profiles/*.default/cache2/*",
                    "%%users.homedir%%/Library/Caches/Firefox/Profiles/*.default/cache2/doomed/*",
                    "%%users.homedir%%/Library/Caches/Firefox/Profiles/*.default/cache2/entries/*",
                    "%%users.homedir%%/Library/Caches/Firefox/Profiles/*.default-*/Cache/*",
                    "%%users.homedir%%/Library/Caches/Firefox/Profiles/*.default-*/cache2/*",
                    "%%users.homedir%%/Library/Caches/Firefox/Profiles/*.default-*/cache2/doomed/*",
                    "%%users.homedir%%/Library/Caches/Firefox/Profiles/*.default-*/cache2/entries/*",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.mozilla/firefox/*.default/Cache/*",
                    "%%users.homedir%%/.cache/mozilla/firefox/*.default/Cache/*",
                    "%%users.homedir%%/.cache/mozilla/firefox/*.default/cache2/*",
                    "%%users.homedir%%/.cache/mozilla/firefox/*.default/cache2/doomed/*",
                    "%%users.homedir%%/.cache/mozilla/firefox/*.default/cache2/entries/*",
                    "%%users.homedir%%/.cache/mozilla/firefox/*.default-*/Cache/*",
                    "%%users.homedir%%/.cache/mozilla/firefox/*.default-*/cache2/*",
                    "%%users.homedir%%/.cache/mozilla/firefox/*.default-*/cache2/doomed/*",
                    "%%users.homedir%%/.cache/mozilla/firefox/*.default-*/cache2/entries/*",
                    "%%users.homedir%%/snap/firefox/common/.cache/mozilla/firefox/*.default/Cache/*",
                    "%%users.homedir%%/snap/firefox/common/.cache/mozilla/firefox/*.default/cache2/*",
                    "%%users.homedir%%/snap/firefox/common/.cache/mozilla/firefox/*.default/cache2/doomed/*",
                    "%%users.homedir%%/snap/firefox/common/.cache/mozilla/firefox/*.default/cache2/entries/*",
                    "%%users.homedir%%/snap/firefox/common/.cache/mozilla/firefox/*.default-*/Cache/*",
                    "%%users.homedir%%/snap/firefox/common/.cache/mozilla/firefox/*.default-*/cache2/*",
                    "%%users.homedir%%/snap/firefox/common/.cache/mozilla/firefox/*.default-*/cache2/doomed/*",
                    "%%users.homedir%%/snap/firefox/common/.cache/mozilla/firefox/*.default-*/cache2/entries/*",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*.default\\Cache\\*",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*.default\\cache2\\*",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*.default\\cache2\\doomed\\*",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*.default\\cache2\\entries\\*",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*.default-*\\Cache\\*",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*.default-*\\cache2\\*",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*.default-*\\cache2\\doomed\\*",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*.default-*\\cache2\\entries\\*",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SafariCacheSQLiteDatabaseFile(GRRArtifactBase):
    """
    Safari browser cache (cache.db) SQLite database file.

    Reference URLs: https://forensics.wiki/apple_safari
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Caches/com.apple.Safari/Cache.db",
                    "%%users.homedir%%/Library/Caches/com.apple.Safari/Cache.db-wal",
                    "%%users.homedir%%/Library/Containers/com.apple.Safari/Data/Library/Caches/com.apple.Safari/Cache.db",
                    "%%users.homedir%%/Library/Containers/com.apple.Safari/Data/Library/Caches/com.apple.Safari/Cache.db-wal",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.localappdata%%\\Apple Computer\\Safari\\cache.db"],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = ["SafariCache"]


class ChromiumBasedBrowsersCache(GRRArtifactBase):
    """
    Caches of multiple Chromium-based browsers (Google Chrome, Brave, Chromium,
    Yandex, Opera, Edge, EdgeBeta).

    Canary uses "Chrome SxS" on windows.

    * Disk cache (or Cache) * Media cache * Application cache * GPU shader cache
    * PNaCl translation cache

    Reference URLs:
    https://artifacts-kb.readthedocs.io/en/latest/sources/webbrowser/ChromeCache.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Brave\\*\\Application Cache\\Cache\\*",
                    "%%users.appdata%%\\Brave\\*\\Cache\\*",
                    "%%users.appdata%%\\Brave\\*\\Cache\\Cache_Data\\*",
                    "%%users.appdata%%\\Brave\\*\\GPUCache\\*",
                    "%%users.appdata%%\\Brave\\*\\Media Cache\\*",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\*\\Application Cache\\Cache\\*",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\*\\Cache\\*",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\*\\Cache\\Cache_Data\\*",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\*\\GPUCache\\*",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\*\\Media Cache\\*",
                    "%%users.localappdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\Application Cache\\Cache\\*",
                    "%%users.localappdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\Cache\\*",
                    "%%users.localappdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\Cache\\Cache_Data\\*",
                    "%%users.localappdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\GPUCache\\*",
                    "%%users.localappdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\Media Cache\\*",
                    "%%users.localappdata%%\\Chromium\\*\\Application Cache\\Cache\\*",
                    "%%users.localappdata%%\\Chromium\\*\\Cache\\*",
                    "%%users.localappdata%%\\Chromium\\*\\Cache\\Cache_Data\\*",
                    "%%users.localappdata%%\\Chromium\\*\\GPUCache\\*",
                    "%%users.localappdata%%\\Chromium\\*\\Media Cache\\*",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Application Cache\\Cache\\*",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Cache\\*",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Cache\\Cache_Data\\*",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\GPUCache\\*",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Media Cache\\*",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Application Cache\\Cache\\*",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Cache\\*",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Cache\\Cache_Data\\*",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\GPUCache\\*",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Media Cache\\*",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Application Cache\\Cache\\*",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Cache\\*",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Cache\\Cache_Data\\*",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\GPUCache\\*",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Media Cache\\*",
                    "%%users.localappdata%%\\Microsoft\\Edge Beta\\User Data\\*\\Application Cache\\Cache\\*",
                    "%%users.localappdata%%\\Microsoft\\Edge Beta\\User Data\\*\\Cache\\*",
                    "%%users.localappdata%%\\Microsoft\\Edge Beta\\User Data\\*\\Cache\\Cache_Data\\*",
                    "%%users.localappdata%%\\Microsoft\\Edge Beta\\User Data\\*\\GPUCache\\*",
                    "%%users.localappdata%%\\Microsoft\\Edge Beta\\User Data\\*\\Media Cache\\*",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Application Cache\\Cache\\*",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Cache\\*",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Cache\\Cache_Data\\*",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\GPUCache\\*",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Media Cache\\*",
                    "%%users.localappdata%%\\Opera Software\\Opera Stable\\*\\Cache_Data\\*",
                    "%%users.localappdata%%\\Yandex\\YandexBrowser\\User Data\\*\\Application Cache\\Cache\\*",
                    "%%users.localappdata%%\\Yandex\\YandexBrowser\\User Data\\*\\Cache\\*",
                    "%%users.localappdata%%\\Yandex\\YandexBrowser\\User Data\\*\\Cache\\Cache_Data\\*",
                    "%%users.localappdata%%\\Yandex\\YandexBrowser\\User Data\\*\\GPUCache\\*",
                    "%%users.localappdata%%\\Yandex\\YandexBrowser\\User Data\\*\\Media Cache\\*",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Caches/Chromium/*/Cache/*",
                    "%%users.homedir%%/Caches/Google/Chrome/*/Cache/*",
                    "%%users.homedir%%/Caches/Google/Chrome Beta/*/Cache/*",
                    "%%users.homedir%%/Caches/Google/Chrome Canary/*/Cache/*",
                    "%%users.homedir%%/Library/Application Support/BraveSoftware/Brave-Browser/*/Application Cache/*",
                    "%%users.homedir%%/Library/Application Support/BraveSoftware/Brave-Browser/*/Cache/*",
                    "%%users.homedir%%/Library/Application Support/BraveSoftware/Brave-Browser/Cache/*",
                    "%%users.homedir%%/Library/Application Support/BraveSoftware/Brave-Browser/*/GPUCache/*",
                    "%%users.homedir%%/Library/Application Support/BraveSoftware/Brave-Browser/*/Media Cache/*",
                    "%%users.homedir%%/Library/Application Support/BraveSoftware/Brave-Browser/PnaclTranslationCache/*",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Application Cache/*",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Application Cache/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Chromium/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/GPUCache/*",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Media Cache/*",
                    "%%users.homedir%%/Library/Application Support/Chromium/PnaclTranslationCache/*",
                    "%%users.homedir%%/Library/Application Support/com.operasoftware.Opera/*/Application Cache/*",
                    "%%users.homedir%%/Library/Application Support/com.operasoftware.Opera/*/Cache/*",
                    "%%users.homedir%%/Library/Application Support/com.operasoftware.Opera/Cache/*",
                    "%%users.homedir%%/Library/Application Support/com.operasoftware.Opera/*/GPUCache/*",
                    "%%users.homedir%%/Library/Application Support/com.operasoftware.Opera/*/Media Cache/*",
                    "%%users.homedir%%/Library/Application Support/com.operasoftware.Opera/PnaclTranslationCache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Application Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Application Cache/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Application Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Application Cache/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/GPUCache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Media Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/PnaclTranslationCache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Application Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Application Cache/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/GPUCache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Media Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/PnaclTranslationCache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/GPUCache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Media Cache/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/PnaclTranslationCache/*",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge/*/Application Cache/*",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge Beta/*/Application Cache/*",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge Beta/*/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge Beta/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge Beta/*/GPUCache/*",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge Beta/*/Media Cache/*",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge Beta/PnaclTranslationCache/*",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge/*/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge/*/GPUCache/*",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge/*/Media Cache/*",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge/PnaclTranslationCache/*",
                    "%%users.homedir%%/Library/Application Support/Yandex/YandexBrowser/*/Application Cache/*",
                    "%%users.homedir%%/Library/Application Support/Yandex/YandexBrowser/*/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Yandex/YandexBrowser/Cache/*",
                    "%%users.homedir%%/Library/Application Support/Yandex/YandexBrowser/*/GPUCache/*",
                    "%%users.homedir%%/Library/Application Support/Yandex/YandexBrowser/*/Media Cache/*",
                    "%%users.homedir%%/Library/Application Support/Yandex/YandexBrowser/PnaclTranslationCache/*",
                    "%%users.homedir%%/Library/Caches/Chromium/*/Application Cache/*",
                    "%%users.homedir%%/Library/Caches/Chromium/*/Cache/*",
                    "%%users.homedir%%/Library/Caches/Chromium/Cache/*",
                    "%%users.homedir%%/Library/Caches/Chromium/*/GPUCache/*",
                    "%%users.homedir%%/Library/Caches/Chromium/*/Media Cache/*",
                    "%%users.homedir%%/Library/Caches/Chromium/PnaclTranslationCache/*",
                    "%%users.homedir%%/Library/Caches/Google/Chrome/*/Cache/*",
                    "%%users.homedir%%/Library/Caches/Google/Chrome/Cache/*",
                    "%%users.homedir%%/Library/Caches/Google/Chrome Beta/*/Cache/*",
                    "%%users.homedir%%/Library/Caches/Google/Chrome Beta/Cache/*",
                    "%%users.homedir%%/Library/Caches/Google/Chrome Beta/*/Media Cache/*",
                    "%%users.homedir%%/Library/Caches/Google/Chrome Beta/PnaclTranslationCache/*",
                    "%%users.homedir%%/Library/Caches/Google/Chrome Canary/*/Cache/*",
                    "%%users.homedir%%/Library/Caches/Google/Chrome Canary/Cache/*",
                    "%%users.homedir%%/Library/Caches/Google/Chrome Canary/*/Media Cache/*",
                    "%%users.homedir%%/Library/Caches/Google/Chrome Canary/PnaclTranslationCache/*",
                    "%%users.homedir%%/Library/Caches/Google/Chrome/*/Media Cache/*",
                    "%%users.homedir%%/Library/Caches/Google/Chrome/PnaclTranslationCache/*",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.cache/BraveSoftware/Brave-Browser/*/Cache/Cache_Data/*",
                    "%%users.homedir%%/.cache/BraveSoftware/Brave-Browser/Cache/Cache_Data/*",
                    "%%users.homedir%%/.cache/chrome-remote-desktop/chrome-config/google-chrome/*/Cache/*",
                    "%%users.homedir%%/.cache/chrome-remote-desktop/chrome-config/google-chrome/Cache/*",
                    "%%users.homedir%%/.cache/chrome-remote-desktop/chrome-config/google-chrome/*/Cache/Cache_Data/*",
                    "%%users.homedir%%/.cache/chrome-remote-desktop/chrome-config/google-chrome/*/Media Cache/*",
                    "%%users.homedir%%/.cache/chrome-remote-desktop/chrome-config/google-chrome/PnaclTranslationCache/*",
                    "%%users.homedir%%/.cache/chrome-remote-desktop/chrome-profile/*/Cache/*",
                    "%%users.homedir%%/.cache/chrome-remote-desktop/chrome-profile/Cache/*",
                    "%%users.homedir%%/.cache/chrome-remote-desktop/chrome-profile/*/Cache/Cache_Data/*",
                    "%%users.homedir%%/.cache/chrome-remote-desktop/chrome-profile/*/Media Cache/*",
                    "%%users.homedir%%/.cache/chrome-remote-desktop/chrome-profile/PnaclTranslationCache/*",
                    "%%users.homedir%%/.cache/chromium/*/Cache/*",
                    "%%users.homedir%%/.cache/chromium/Cache/*",
                    "%%users.homedir%%/.cache/chromium/*/Cache/Cache_Data/*",
                    "%%users.homedir%%/.cache/chromium/*/Media Cache/*",
                    "%%users.homedir%%/.cache/chromium/PnaclTranslationCache/*",
                    "%%users.homedir%%/.cache/google-chrome/*/Cache/*",
                    "%%users.homedir%%/.cache/google-chrome/Cache/*",
                    "%%users.homedir%%/.cache/google-chrome/*/Cache/Cache_Data/*",
                    "%%users.homedir%%/.cache/google-chrome/*/Media Cache/*",
                    "%%users.homedir%%/.cache/google-chrome/PnaclTranslationCache/*",
                    "%%users.homedir%%/.cache/microsoft-edge/*/Cache/Cache_Data/*",
                    "%%users.homedir%%/.cache/opera/*/Cache_Data/*",
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Application Cache/*",
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Cache/*",
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/Cache/*",
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/GPUCache/*",
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Media Cache/*",
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/PnaclTranslationCache/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Application Cache/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Cache/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/Cache/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Cache/Cache_Data/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/GPUCache/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Media Cache/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/PnaclTranslationCache/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Application Cache/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Cache/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/Cache/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Cache/Cache_Data/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/GPUCache/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Media Cache/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/PnaclTranslationCache/*",
                    "%%users.homedir%%/.config/chromium/*/Application Cache/*",
                    "%%users.homedir%%/.config/chromium/*/Cache/*",
                    "%%users.homedir%%/.config/chromium/Cache/*",
                    "%%users.homedir%%/.config/chromium/*/Cache/Cache_Data/*",
                    "%%users.homedir%%/.config/chromium/*/GPUCache/*",
                    "%%users.homedir%%/.config/chromium/*/Media Cache/*",
                    "%%users.homedir%%/.config/chromium/PnaclTranslationCache/*",
                    "%%users.homedir%%/.config/google-chrome/*/Application Cache/*",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Application Cache/*",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Cache/*",
                    "%%users.homedir%%/.config/google-chrome-beta/Cache/*",
                    "%%users.homedir%%/.config/google-chrome-beta/*/GPUCache/*",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Media Cache/*",
                    "%%users.homedir%%/.config/google-chrome-beta/PnaclTranslationCache/*",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Application Cache/*",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Cache/*",
                    "%%users.homedir%%/.config/google-chrome-unstable/Cache/*",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/GPUCache/*",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Media Cache/*",
                    "%%users.homedir%%/.config/google-chrome-unstable/PnaclTranslationCache/*",
                    "%%users.homedir%%/.config/google-chrome/*/Cache/*",
                    "%%users.homedir%%/.config/google-chrome/Cache/*",
                    "%%users.homedir%%/.config/google-chrome/*/Cache/Cache_Data/*",
                    "%%users.homedir%%/.config/google-chrome/*/GPUCache/*",
                    "%%users.homedir%%/.config/google-chrome/*/Media Cache/*",
                    "%%users.homedir%%/.config/google-chrome/PnaclTranslationCache/*",
                    "%%users.homedir%%/.config/microsoft-edge/*/GPUCache/*",
                    "%%users.homedir%%/.config/opera/*/Application Cache/*",
                    "%%users.homedir%%/.config/opera/*/Cache/*",
                    "%%users.homedir%%/.config/opera/Cache/*",
                    "%%users.homedir%%/.config/opera/*/GPUCache/*",
                    "%%users.homedir%%/.config/opera/GPUCache/*",
                    "%%users.homedir%%/.config/opera/*/Media Cache/*",
                    "%%users.homedir%%/.config/opera/PnaclTranslationCache/*",
                    "%%users.homedir%%/.config/yandex-browser-beta/*/Application Cache/*",
                    "%%users.homedir%%/.config/yandex-browser-beta/*/Cache/*",
                    "%%users.homedir%%/.config/yandex-browser-beta/Cache/*",
                    "%%users.homedir%%/.config/yandex-browser-beta/*/GPUCache/*",
                    "%%users.homedir%%/.config/yandex-browser-beta/*/Media Cache/*",
                    "%%users.homedir%%/.config/yandex-browser-beta/PnaclTranslationCache/*",
                    "%%users.homedir%%/snap/chromium/common/chromium/*/Application Cache/*",
                    "%%users.homedir%%/snap/chromium/common/chromium/*/Cache/*",
                    "%%users.homedir%%/snap/chromium/common/chromium/Cache/*",
                    "%%users.homedir%%/snap/chromium/common/chromium/*/GPUCache/*",
                    "%%users.homedir%%/snap/chromium/common/chromium/*/Media Cache/*",
                    "%%users.homedir%%/snap/chromium/common/chromium/PnaclTranslationCache/*",
                ]
            },
            "supported_os": ["Linux"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = [
        "ChromeCache",
        "ChromiumCache",
        "EdgeCache",
    ]


class SafariHistoryPlistFile(GRRArtifactBase):
    """
    Safari browser history (History.plist) property list (plist) file.

    Reference URLs: https://forensics.wiki/apple_safari
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/Library/Safari/History.plist"]},
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Apple Computer\\Safari\\History.plist",
                    "%%users.appdata%%\\Apple Computer\\Safari\\History.plist",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SafariDownloadsPlistFile(GRRArtifactBase):
    """
    Safari downloads history (Downloads.plist) property list (plist) file.

    Reference URLs: https://forensics.wiki/apple_safari/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Safari/Downloads.plist"]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Apple Computer\\Safari\\Downloads.plist",
                    "%%users.appdata%%\\Apple Computer\\Safari\\Downloads.plist",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = ["SafariDownloads"]


class OperaHistoryFile(GRRArtifactBase):
    """
    Opera browser history (global_history.dat) file.

    Reference URLs: https://forensics.wiki/opera
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/Opera/global_history.dat"]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/.opera/global_history.dat"]},
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Opera\\Opera\\global_history.dat",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\History",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\History-journal",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = ["OperaHistory"]


class SafariHistorySQLiteDatabaseFile(GRRArtifactBase):
    """
    Safari browser history SQLite database file.

    Reference URLs: https://forensics.wiki/apple_safari
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Safari/History.db",
                    "%%users.homedir%%/Library/Safari/History.db-wal",
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


class ChromiumBasedBrowsersHistoryDatabaseFile(GRRArtifactBase):
    """
    Browsing history database file for multiple Chromium-based browsers, such as
    Google Chrome, Brave, Chromium, Yandex, Opera, Edge, EdgeBeta.

    Reference URLs: https://forensics.wiki/google_chrome
    https://forensics.wiki/google_chrome#chromium-based-browsers
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/BraveSoftware/Brave-Browser/*/Archived History",
                    "%%users.homedir%%/Library/Application Support/BraveSoftware/Brave-Browser/*/Archived History-journal",
                    "%%users.homedir%%/Library/Application Support/BraveSoftware/Brave-Browser/*/History",
                    "%%users.homedir%%/Library/Application Support/BraveSoftware/Brave-Browser/*/History-journal",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Archived History",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Archived History-journal",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/History",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/History-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Archived History",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Archived History-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/History",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/History-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Archived History",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Archived History-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/History",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/History-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Archived History",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Archived History-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/History",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/History-journal",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge Beta/*/Archived History",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge Beta/*/Archived History-journal",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge Beta/*/History",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge Beta/*/History-journal",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge/*/Archived History",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge/*/Archived History-journal",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge/*/History",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge/*/History-journal",
                    "%%users.homedir%%/Library/Application Support/Yandex/YandexBrowser/*/Archived History",
                    "%%users.homedir%%/Library/Application Support/Yandex/YandexBrowser/*/Archived History-journal",
                    "%%users.homedir%%/Library/Application Support/Yandex/YandexBrowser/*/History",
                    "%%users.homedir%%/Library/Application Support/Yandex/YandexBrowser/*/History-journal",
                    "%%users.homedir%%/Library/Application Support/com.operasoftware.Opera/*/Archived History",
                    "%%users.homedir%%/Library/Application Support/com.operasoftware.Opera/*/Archived History-journal",
                    "%%users.homedir%%/Library/Application Support/com.operasoftware.Opera/*/History",
                    "%%users.homedir%%/Library/Application Support/com.operasoftware.Opera/*/History-journal",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Archived History",
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Archived History-journal",
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/History",
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/History-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Archived History",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Archived History-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/History",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/History-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Archived History",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Archived History-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/History",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/History-journal",
                    "%%users.homedir%%/.config/chromium/*/Archived History",
                    "%%users.homedir%%/.config/chromium/*/Archived History-journal",
                    "%%users.homedir%%/.config/chromium/*/History",
                    "%%users.homedir%%/.config/chromium/*/History-journal",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Archived History",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Archived History-journal",
                    "%%users.homedir%%/.config/google-chrome-beta/*/History",
                    "%%users.homedir%%/.config/google-chrome-beta/*/History-journal",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Archived History",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Archived History-journal",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/History",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/History-journal",
                    "%%users.homedir%%/.config/google-chrome/*/Archived History",
                    "%%users.homedir%%/.config/google-chrome/*/Archived History-journal",
                    "%%users.homedir%%/.config/google-chrome/*/History",
                    "%%users.homedir%%/.config/google-chrome/*/History-journal",
                    "%%users.homedir%%/.config/microsoft-edge/*/Archived History",
                    "%%users.homedir%%/.config/microsoft-edge/*/Archived History-journal",
                    "%%users.homedir%%/.config/microsoft-edge/*/History",
                    "%%users.homedir%%/.config/microsoft-edge/*/History-journal",
                    "%%users.homedir%%/.config/opera/*/Archived History",
                    "%%users.homedir%%/.config/opera/*/Archived History-journal",
                    "%%users.homedir%%/.config/opera/*/History",
                    "%%users.homedir%%/.config/opera/*/History-journal",
                    "%%users.homedir%%/.config/yandex-browser-beta/*/Archived History",
                    "%%users.homedir%%/.config/yandex-browser-beta/*/Archived History-journal",
                    "%%users.homedir%%/.config/yandex-browser-beta/*/History",
                    "%%users.homedir%%/.config/yandex-browser-beta/*/History-journal",
                    "%%users.homedir%%/snap/chromium/common/chromium/*/Archived History",
                    "%%users.homedir%%/snap/chromium/common/chromium/*/Archived History-journal",
                    "%%users.homedir%%/snap/chromium/common/chromium/*/History",
                    "%%users.homedir%%/snap/chromium/common/chromium/*/History-journal",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Brave\\*\\Archived History",
                    "%%users.appdata%%\\Brave\\*\\Archived History-journal",
                    "%%users.appdata%%\\Brave\\*\\History",
                    "%%users.appdata%%\\Brave\\*\\History-journal",
                    "%%users.appdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\History",
                    "%%users.appdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\History-journal",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\*\\Archived History",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\*\\Archived History-journal",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\*\\History",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\*\\History-journal",
                    "%%users.localappdata%%\\Chromium\\*\\Archived History",
                    "%%users.localappdata%%\\Chromium\\*\\Archived History-journal",
                    "%%users.localappdata%%\\Chromium\\*\\History",
                    "%%users.localappdata%%\\Chromium\\*\\History-journal",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Archived History",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Archived History-journal",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\History",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\History-journal",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Archived History",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Archived History-journal",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\History",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\History-journal",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Archived History",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Archived History-journal",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\History",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\History-journal",
                    "%%users.localappdata%%\\Microsoft\\Edge Beta\\User Data\\*\\Archived History",
                    "%%users.localappdata%%\\Microsoft\\Edge Beta\\User Data\\*\\Archived History-journal",
                    "%%users.localappdata%%\\Microsoft\\Edge Beta\\User Data\\*\\History",
                    "%%users.localappdata%%\\Microsoft\\Edge Beta\\User Data\\*\\History-journal",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Archived History",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Archived History-journal",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\History",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\History-journal",
                    "%%users.localappdata%%\\Yandex\\YandexBrowser\\User Data\\*\\Archived History",
                    "%%users.localappdata%%\\Yandex\\YandexBrowser\\User Data\\*\\Archived History-journal",
                    "%%users.localappdata%%\\Yandex\\YandexBrowser\\User Data\\*\\History",
                    "%%users.localappdata%%\\Yandex\\YandexBrowser\\User Data\\*\\History-journal",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = [
        "ChromeHistory",
        "ChromiumBasedBrowsersHistory",
    ]


class FirefoxHistory(GRRArtifactBase):
    """
    Firefox browser history (places.sqlite).

    Reference URLs: https://forensics.wiki/mozilla_firefox
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Firefox/Profiles/*/places.sqlite",
                    "%%users.homedir%%/Library/Application Support/Firefox/Profiles/*/places.sqlite-wal",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.mozilla/firefox/*/places.sqlite",
                    "%%users.homedir%%/.mozilla/firefox/*/places.sqlite-wal",
                    "%%users.homedir%%/snap/firefox/common/.mozilla/firefox/*/places.sqlite",
                    "%%users.homedir%%/snap/firefox/common/.mozilla/firefox/*/places.sqlite-wal",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*\\places.sqlite",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*\\places.sqlite-wal",
                    "%%users.appdata%%\\Mozilla\\Firefox\\Profiles\\*\\places.sqlite",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*\\places.sqlite-wal",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class FirefoxDownloads(GRRArtifactBase):
    """
    Firefox browser downloads (downloads.sqlite).

    Reference URLs: https://forensics.wiki/mozilla_firefox
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Firefox/Profiles/*/downloads.sqlite",
                    "%%users.homedir%%/Library/Application Support/Firefox/Profiles/*/downloads.sqlite-wal",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.mozilla/firefox/*/downloads.sqlite",
                    "%%users.homedir%%/.mozilla/firefox/*/downloads.sqlite-wal",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*\\downloads.sqlite",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*\\downloads.sqlite-wal",
                    "%%users.appdata%%\\Mozilla\\Firefox\\Profiles\\*\\downloads.sqlite",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*\\downloads.sqlite-wal",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ChromeExtensionRegistryKeys(GRRArtifactBase):
    """
    Chrome extensions installed by writing windows registry keys.

    Reference URLs:
    https://developer.chrome.com/extensions/external_extensions#registry
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Google\\Chrome\\Extensions\\**5",
                    "HKEY_LOCAL_MACHINE\\Software\\Wow6432Node\\Google\\Chrome\\Extensions\\**5",
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


class ChromeFileSystem(GRRArtifactBase):
    """
    Google Chrome, Beta, Canary and Chromium File System files.

    The File System directory backs Chrome's fileSystem API. Inside this
    directory are a mixture of the data files saved using the fileSystem API and
    LevelDB directories that track the logical structure of the virtual file
    system.

    Reference URLs: https://developer.chrome.com/apps/fileSystem
    https://developer.mozilla.org/en-US/docs/Web/API/FileSystem
    https://dfir.blog/deciphering-browser-hieroglyphics-leveldb-filesystem/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\File System\\**5",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\File System\\**5",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\File System\\**5",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\File System\\**5",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/google-chrome/*/File System/**5",
                    "%%users.homedir%%/.config/chromium/*/File System/**5",
                    "%%users.homedir%%/.config/google-chrome-beta/*/File System/**5",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/File System/**5",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/File System/**5",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/File System/**5",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Chromium/*/File System/**5",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/File System/**5",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/File System/**5",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/File System/**5",
                ]
            },
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ChromeIndexedDB(GRRArtifactBase):
    """
    Google Chrome, Beta, Canary and Chromium IndexedDB files.

    The IndexedDB directory contains one directory per origin that uses
    IndexedDB, named like https_www.example.com_0.indexeddb.leveldb,
    chrome-extension_app-id-xxx_0.indexeddb.leveldb, or
    https_www.example.com_0.indexeddb.blob. Inside each of the *.leveldb
    directories are the files the comprise a LevelDB database, which in turn
    holds IndexedDB data for that origin. There may be an accompanying .blob
    directory, which contains a nested folder structure of blobs.

    Reference URLs:
    https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\IndexedDB\\**5",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\IndexedDB\\**5",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\IndexedDB\\**5",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\IndexedDB\\**5",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/google-chrome/*/IndexedDB/**5",
                    "%%users.homedir%%/.config/chromium/*/IndexedDB/**5",
                    "%%users.homedir%%/.config/google-chrome-beta/*/IndexedDB/**5",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/IndexedDB/**5",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/IndexedDB/**5",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/IndexedDB/**5",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Chromium/*/IndexedDB/**5",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/IndexedDB/**5",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/IndexedDB/**5",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/IndexedDB/**5",
                ]
            },
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ChromeLocalStorage(GRRArtifactBase):
    """
    Google Chrome, Beta, Canary and Chromium Local Storage files.

    Chrome 60 and earlier versions used individual .sqlite files per origin for
    Local Storage, stored in the Local Storage directory root. In Chrome 61, a
    leveldb directory was added inside the root Local Storage directory, and new
    origins saved Local Storage data in a single LevelDB there.

    Existing .sqlite files are kept (not moved to leveldb), so it is possible
    for a single Chrome profile to use both SQLite and LevelDB for Local
    Storage.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Local Storage/**",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Local Storage/**",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Local Storage/**",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Local Storage/**",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/google-chrome/*/Local Storage/**",
                    "%%users.homedir%%/.config/chromium/*/Local Storage/**",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Local Storage/**",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Local Storage/**",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Local Storage/**",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Local Storage/**",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Local Storage\\**",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Local Storage\\**",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Local Storage\\**",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Local Storage\\**",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ChromeSessionStorage(GRRArtifactBase):
    """
    Google Chrome, Beta, Canary and Chromium Sessions and Session Storage files.

    The Sessions directory contains information for restoring tabs and windows
    from a browsing session.

    The Session Storage directory contains the files that comprise a LevelDB
    database, which in turn holds the Session Storage data.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Session Storage/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Session Storage/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Session Storage/*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Session Storage/*",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Sessions/Session_*",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Sessions/Tabs_*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Sessions/Session_*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Sessions/Tabs_*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Sessions/Session_*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Sessions/Tabs_*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Sessions/Session_*",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Sessions/Tabs_*",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/google-chrome/*/Session Storage/*",
                    "%%users.homedir%%/.config/chromium/*/Session Storage/*",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Session Storage/*",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Session Storage/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Session Storage/*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Session Storage/*",
                    "%%users.homedir%%/.config/google-chrome/*/Sessions/Session_*",
                    "%%users.homedir%%/.config/google-chrome/*/Sessions/Tabs_*",
                    "%%users.homedir%%/.config/chromium/*/Sessions/Session_*",
                    "%%users.homedir%%/.config/chromium/*/Sessions/Tabs_*",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Sessions/Session_*",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Sessions/Session_*",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Sessions/Tabs_*",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Sessions/Tabs_*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Sessions/Session_*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Sessions/Tabs_*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Sessions/Session_*",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Sessions/Tabs_*",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Session Storage\\*",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Session Storage\\*",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Session Storage\\*",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Session Storage\\*",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Sessions\\Session_*",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Sessions\\Tabs_*",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Sessions\\Session_*",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Sessions\\Tabs_*",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Sessions\\Session_*",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Sessions\\Tabs_*",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Sessions\\Session_*",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Sessions\\Tabs_*",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ChromePlatformNotifications(GRRArtifactBase):
    """
    Google Chrome Platform Notifications LevelDB.

    The Platform Notifications directory contains the files that comprise a
    LevelDB database, which in turn holds platform notification data.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Platform Notifications/*"
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/google-chrome/*/Platform Notifications/*"
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Platform Notifications\\*"
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = [
        "ChromeNotifications",
        "ChromePlatformNotificationsDatabase",
    ]


class ChromePreferences(GRRArtifactBase):
    """
    Chrome Preferences file.

    Reference URLs: https://forensics.wiki/google_chrome#configuration
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Preferences",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Secure Preferences",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Preferences",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Secure Preferences",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Preferences",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Secure Preferences",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Preferences",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Secure Preferences",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Preferences",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Secure Preferences",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Preferences",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Secure Preferences",
                    "%%users.homedir%%/.config/chromium/*/Preferences",
                    "%%users.homedir%%/.config/chromium/*/Secure Preferences",
                    "%%users.homedir%%/.config/google-chrome/*/Preferences",
                    "%%users.homedir%%/.config/google-chrome/*/Secure Preferences",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Preferences",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Secure Preferences",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Preferences",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Secure Preferences",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Preferences",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Secure Preferences",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Preferences",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ChromiumBasedBrowsersCookiesDatabaseFile(GRRArtifactBase):
    """
    Cookies database file for multiple Chromium-based browsers, such as Google
    Chrome, Brave, Chromium, Yandex, Opera, Edge, EdgeBeta.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\Network\\Cookies",
                    "%%users.localappdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\Network\\Cookies-journal",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Cookies",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Cookies-journal",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Network\\Cookies",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Network\\Cookies-journal",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Cookies",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Cookies-journal",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Network\\Cookies",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Network\\Cookies-journal",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Cookies",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Cookies-journal",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Network\\Cookies",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Network\\Cookies-journal",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Cookies",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Cookies-journal",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Network\\Cookies",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Network\\Cookies-journal",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\Network\\Cookies",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\Network\\Cookies-journal",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Cookies",
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Cookies-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Cookies",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Cookies-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Network/Cookies",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Network/Cookies-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Cookies",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Cookies-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Network/Cookies",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Network/Cookies-journal",
                    "%%users.homedir%%/.config/chromium/*/Cookies",
                    "%%users.homedir%%/.config/chromium/*/Cookies-journal",
                    "%%users.homedir%%/.config/chromium/*/Network/Cookies",
                    "%%users.homedir%%/.config/chromium/*/Network/Cookies-journal",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Cookies",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Cookies-journal",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Network/Cookies",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Network/Cookies-journal",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Cookies",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Cookies-journal",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Network/Cookies",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Network/Cookies-journal",
                    "%%users.homedir%%/.config/google-chrome/*/Cookies",
                    "%%users.homedir%%/.config/google-chrome/*/Cookies-journal",
                    "%%users.homedir%%/.config/google-chrome/*/Network/Cookies",
                    "%%users.homedir%%/.config/google-chrome/*/Network/Cookies-journal",
                    "%%users.homedir%%/.config/microsoft-edge/*/Cookies",
                    "%%users.homedir%%/.config/microsoft-edge/*/Cookies-journal",
                    "%%users.homedir%%/.config/opera/Cookies",
                    "%%users.homedir%%/.config/opera/Cookies-journal",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Cookies",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Cookies-journal",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Network/Cookies",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Network/Cookies-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Cookies",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Cookies-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Network/Cookies",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Network/Cookies-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Cookies",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Cookies-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Network/Cookies",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Network/Cookies-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Cookies",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Cookies-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Network/Cookies",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Network/Cookies-journal",
                ]
            },
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = ["ChromeCookies"]


class ChromiumBasedBrowsersExtensions(GRRArtifactBase):
    """
    Browser extension files for multiple Chromium-based browsers, such as Google
    Chrome, Brave, Chromium, Yandex, Opera, Edge, EdgeBeta.

    Reference URLs: https://forensics.wiki/google_chrome#chromium-based-browsers
    https://forensics.wiki/google_chrome#extensions
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/BraveSoftware/Brave-Browser/*/Extensions/**10",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Extensions/**10",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Extensions/**10",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Extensions/**10",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Extensions/**10",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge Beta/*/Extensions/**10",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge/*/Extensions/**10",
                    "%%users.homedir%%/Library/Application Support/Yandex/YandexBrowser/*/Extensions/**10",
                    "%%users.homedir%%/Library/Application Support/com.operasoftware.Opera/*/Extensions/**10",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Extensions/**10",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Extensions/**10",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Extensions/**10",
                    "%%users.homedir%%/.config/chromium/*/Extensions/**10",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Extensions/**10",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Extensions/**10",
                    "%%users.homedir%%/.config/google-chrome/*/Extensions/**10",
                    "%%users.homedir%%/.config/opera/*/Extensions/**10",
                    "%%users.homedir%%/.config/yandex-browser-beta/*/Extensions/**10",
                    "%%users.homedir%%/snap/chromium/common/chromium/*/Extensions/**10",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\*\\Extensions\\**10",
                    "%%users.appdata%%\\Brave\\*\\Extensions\\**10",
                    "%%users.localappdata%%\\Chromium\\*\\Extensions\\**10",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Extensions\\**10",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Extensions\\**10",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Extensions\\**10",
                    "%%users.localappdata%%\\Microsoft\\Edge Beta\\User Data\\*\\Extensions\\**10",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Extensions\\**10",
                    "%%users.localappdata%%\\Yandex\\YandexBrowser\\User Data\\*\\Extensions\\**10",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = ["ChromeExtensions"]


class ChromiumBasedBrowsersExtensionActivitySQLiteDatabaseFile(GRRArtifactBase):
    """
    Browser Extension Activity SQLite database file for Chromium-based browsers,
    such as Google Chrome, Brave, Chromium, Yandex, Opera, Edge, EdgeBeta.

    Reference URLs: https://forensics.wiki/google_chrome#chromium-based-browsers
    https://forensics.wiki/google_chrome#extension-activity-database
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/BraveSoftware/Brave-Browser/*/Extension Activity",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Extension Activity",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Extension Activity",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Extension Activity",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Extension Activity",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge Beta/*/Extension Activity",
                    "%%users.homedir%%/Library/Application Support/Microsoft Edge/*/Extension Activity",
                    "%%users.homedir%%/Library/Application Support/Yandex/YandexBrowser/*/Extension Activity",
                    "%%users.homedir%%/Library/Application Support/com.operasoftware.Opera/*/Extension Activity",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Extension Activity",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Extension Activity",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Extension Activity",
                    "%%users.homedir%%/.config/chromium/*/Extension Activity",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Extension Activity",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Extension Activity",
                    "%%users.homedir%%/.config/google-chrome/*/Extension Activity",
                    "%%users.homedir%%/.config/opera/*/Extension Activity",
                    "%%users.homedir%%/.config/yandex-browser-beta/*/Extension Activity",
                    "%%users.homedir%%/snap/chromium/common/chromium/*/Extension Activity",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Brave\\*\\Extension Activity",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\*\\Extension Activity",
                    "%%users.localappdata%%\\Chromium\\*\\Extension Activity",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Extension Activity",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Extension Activity",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Extension Activity",
                    "%%users.localappdata%%\\Microsoft\\Edge Beta\\User Data\\*\\Extension Activity",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Extension Activity",
                    "%%users.localappdata%%\\Yandex\\YandexBrowser\\User Data\\*\\Extension Activity",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = [
        "ChromeExtensionActivity",
        "ChromiumBasedBrowsersExtensionActivity",
    ]


class ChromiumBasedBrowsersFaviconsDatabaseFile(GRRArtifactBase):
    """
    Favicons database file for multiple Chromium-based browsers, such as Google
    Chrome, Brave, Chromium, Yandex, Opera, Edge, EdgeBeta.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\Network\\Favicons",
                    "%%users.localappdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\Network\\Favicons-journal",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Favicons",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Favicons-journal",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Network\\Favicons",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Network\\Favicons-journal",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Favicons",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Favicons-journal",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Network\\Favicons",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Network\\Favicons-journal",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Favicons",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Favicons-journal",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Network\\Favicons",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Network\\Favicons-journal",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Favicons",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Favicons-journal",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Network\\Favicons",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Network\\Favicons-journal",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\Network\\Favicons",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\Network\\Favicons-journal",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Favicons",
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Favicons-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Favicons",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Favicons-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Network/Favicons",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Network/Favicons-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Favicons",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Favicons-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Network/Favicons",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Network/Favicons-journal",
                    "%%users.homedir%%/.config/chromium/*/Favicons",
                    "%%users.homedir%%/.config/chromium/*/Favicons-journal",
                    "%%users.homedir%%/.config/chromium/*/Network/Favicons",
                    "%%users.homedir%%/.config/chromium/*/Network/Favicons-journal",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Favicons",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Favicons-journal",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Network/Favicons",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Network/Favicons-journal",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Favicons",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Favicons-journal",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Network/Favicons",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Network/Favicons-journal",
                    "%%users.homedir%%/.config/google-chrome/*/Favicons",
                    "%%users.homedir%%/.config/google-chrome/*/Favicons-journal",
                    "%%users.homedir%%/.config/google-chrome/*/Network/Favicons",
                    "%%users.homedir%%/.config/google-chrome/*/Network/Favicons-journal",
                    "%%users.homedir%%/.config/microsoft-edge/*/Favicons",
                    "%%users.homedir%%/.config/microsoft-edge/*/Favicons-journal",
                    "%%users.homedir%%/.config/opera/Favicons",
                    "%%users.homedir%%/.config/opera/Favicons-journal",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Favicons",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Favicons-journal",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Network/Favicons",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Network/Favicons-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Favicons",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Favicons-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Network/Favicons",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Network/Favicons-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Favicons",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Favicons-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Network/Favicons",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Network/Favicons-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Favicons",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Favicons-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Network/Favicons",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Network/Favicons-journal",
                ]
            },
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ChromiumBasedBrowsersLoginDataDatabaseFile(GRRArtifactBase):
    """
    Login Data database file for multiple Chromium-based browsers, such as
    Google Chrome, Brave, Chromium, Yandex, Opera, Edge, EdgeBeta.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\Network\\Login Data",
                    "%%users.localappdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\Network\\Login Data-journal",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Login Data",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Login Data-journal",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Network\\Login Data",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Network\\Login Data-journal",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Login Data",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Login Data-journal",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Network\\Login Data",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Network\\Login Data-journal",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Login Data",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Login Data-journal",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Network\\Login Data",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Network\\Login Data-journal",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Login Data",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Login Data-journal",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Network\\Login Data",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Network\\Login Data-journal",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\Network\\Login Data",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\Network\\Login Data-journal",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Login Data",
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Login Data-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Login Data",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Login Data-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Network/Login Data",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Network/Login Data-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Login Data",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Login Data-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Network/Login Data",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Network/Login Data-journal",
                    "%%users.homedir%%/.config/chromium/*/Login Data",
                    "%%users.homedir%%/.config/chromium/*/Login Data-journal",
                    "%%users.homedir%%/.config/chromium/*/Network/Login Data",
                    "%%users.homedir%%/.config/chromium/*/Network/Login Data-journal",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Login Data",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Login Data-journal",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Network/Login Data",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Network/Login Data-journal",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Login Data",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Login Data-journal",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Network/Login Data",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Network/Login Data-journal",
                    "%%users.homedir%%/.config/google-chrome/*/Login Data",
                    "%%users.homedir%%/.config/google-chrome/*/Login Data-journal",
                    "%%users.homedir%%/.config/google-chrome/*/Network/Login Data",
                    "%%users.homedir%%/.config/google-chrome/*/Network/Login Data-journal",
                    "%%users.homedir%%/.config/microsoft-edge/*/Login Data",
                    "%%users.homedir%%/.config/microsoft-edge/*/Login Data-journal",
                    "%%users.homedir%%/.config/opera/Login Data",
                    "%%users.homedir%%/.config/opera/Login Data-journal",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Login Data",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Login Data-journal",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Network/Login Data",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Network/Login Data-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Login Data",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Login Data-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Network/Login Data",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Network/Login Data-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Login Data",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Login Data-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Network/Login Data",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Network/Login Data-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Login Data",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Login Data-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Network/Login Data",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Network/Login Data-journal",
                ]
            },
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ChromiumBasedBrowsersWebDataDatabaseFile(GRRArtifactBase):
    """
    Web Data database file for multiple Chromium-based browsers, such as Google
    Chrome, Brave, Chromium, Yandex, Opera, Edge, EdgeBeta.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\Network\\Web Data",
                    "%%users.localappdata%%\\BraveSoftware\\Brave-Browser\\User Data\\*\\Network\\Web Data-journal",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Web Data",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Web Data-journal",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Network\\Web Data",
                    "%%users.localappdata%%\\Chromium\\User Data\\*\\Network\\Web Data-journal",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Web Data",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Web Data-journal",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Network\\Web Data",
                    "%%users.localappdata%%\\Google\\Chrome SxS\\User Data\\*\\Network\\Web Data-journal",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Web Data",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Web Data-journal",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Network\\Web Data",
                    "%%users.localappdata%%\\Google\\Chrome\\User Data\\*\\Network\\Web Data-journal",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Web Data",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Web Data-journal",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Network\\Web Data",
                    "%%users.localappdata%%\\Microsoft\\Edge\\User Data\\*\\Network\\Web Data-journal",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\Network\\Web Data",
                    "%%users.appdata%%\\Opera Software\\Opera Stable\\Network\\Web Data-journal",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Web Data",
                    "%%users.homedir%%/.config/BraveSoftware/Brave-Browser/*/Web Data-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Web Data",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Web Data-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Network/Web Data",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-config/google-chrome/*/Network/Web Data-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Web Data",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Web Data-journal",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Network/Web Data",
                    "%%users.homedir%%/.config/chrome-remote-desktop/chrome-profile/*/Network/Web Data-journal",
                    "%%users.homedir%%/.config/chromium/*/Web Data",
                    "%%users.homedir%%/.config/chromium/*/Web Data-journal",
                    "%%users.homedir%%/.config/chromium/*/Network/Web Data",
                    "%%users.homedir%%/.config/chromium/*/Network/Web Data-journal",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Web Data",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Web Data-journal",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Network/Web Data",
                    "%%users.homedir%%/.config/google-chrome-beta/*/Network/Web Data-journal",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Web Data",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Web Data-journal",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Network/Web Data",
                    "%%users.homedir%%/.config/google-chrome-unstable/*/Network/Web Data-journal",
                    "%%users.homedir%%/.config/google-chrome/*/Web Data",
                    "%%users.homedir%%/.config/google-chrome/*/Web Data-journal",
                    "%%users.homedir%%/.config/google-chrome/*/Network/Web Data",
                    "%%users.homedir%%/.config/google-chrome/*/Network/Web Data-journal",
                    "%%users.homedir%%/.config/microsoft-edge/*/Web Data",
                    "%%users.homedir%%/.config/microsoft-edge/*/Web Data-journal",
                    "%%users.homedir%%/.config/opera/Web Data",
                    "%%users.homedir%%/.config/opera/Web Data-journal",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Web Data",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Web Data-journal",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Network/Web Data",
                    "%%users.homedir%%/Library/Application Support/Chromium/*/Network/Web Data-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Web Data",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Web Data-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Network/Web Data",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Beta/*/Network/Web Data-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Web Data",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Web Data-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Network/Web Data",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome Canary/*/Network/Web Data-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Web Data",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Web Data-journal",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Network/Web Data",
                    "%%users.homedir%%/Library/Application Support/Google/Chrome/*/Network/Web Data-journal",
                ]
            },
            "supported_os": ["Darwin"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class FirefoxCookies(GRRArtifactBase):
    """
    Firefox browser cookies (cookies.sqlite).

    Reference URLs: https://forensics.wiki/mozilla_firefox
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Firefox/Profiles/*/cookies.sqlite",
                    "%%users.homedir%%/Library/Application Support/Firefox/Profiles/*/cookies.sqlite-wal",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.mozilla/firefox/*/cookies.sqlite",
                    "%%users.homedir%%/.mozilla/firefox/*/cookies.sqlite-shm",
                    "%%users.homedir%%/.mozilla/firefox/*/cookies.sqlite-wal",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*\\cookies.sqlite",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*\\cookies.sqlite-wal",
                    "%%users.appdata%%\\Mozilla\\Firefox\\Profiles\\*\\cookies.sqlite",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*\\cookies.sqlite-wal",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class FirefoxAddOns(GRRArtifactBase):
    """
    Firefox browser add-ons/extensions.

    Reference URLs:
    https://github.com/osquery/osquery/blob/6969e075fd4118e36f6cab54b0956e53dde5ba3f/osquery/tables/applications/browser_firefox.cpp#
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Application Support/Firefox/Profiles/*/addons.json",
                    "%%users.homedir%%/Library/Application Support/Firefox/Profiles/*/extensions.json",
                    "%%users.homedir%%/Library/Application Support/Firefox/Profiles/*/webapps/webapps.json",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.mozilla/firefox/*/addons.json",
                    "%%users.homedir%%/.mozilla/firefox/*/extensions.json",
                    "%%users.homedir%%/.mozilla/firefox/*/webapps/webapps.json",
                ]
            },
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Mozilla\\Firefox\\Profiles\\*\\addons.json",
                    "%%users.appdata%%\\Mozilla\\Firefox\\Profiles\\*\\extensions.json",
                    "%%users.appdata%%\\Mozilla\\Firefox\\Profiles\\*\\webapps\\webapps.json",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*\\addons.json",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*\\extensions.json",
                    "%%users.localappdata%%\\Mozilla\\Firefox\\Profiles\\*\\webapps\\webapps.json",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
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


class InternetExplorerCookies(GRRArtifactBase):
    """
    Microsoft Internet Explorer (MSIE) browser cookies.

    * MSIE 4 - 9 Cache files (index.dat)

    Reference URLs: https://forensics.wiki/internet_explorer
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Microsoft\\Windows\\Cookies\\index.dat",
                    "%%users.appdata%%\\Microsoft\\Windows\\Cookies\\Low\\index.dat",
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


class InternetExplorerHistoryDatabaseFile(GRRArtifactBase):
    """
    Microsoft Internet Explorer (MSIE) 10 browser history database file
    (WebCacheV*.dat).

    Reference URLs: https://forensics.wiki/internet_explorer
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Microsoft\\Windows\\WebCache\\WebCacheV*.dat"
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


class InternetExplorerIndexDatFiles(GRRArtifactBase):
    """
    Microsoft Internet Explorer (MSIE) 4 - 9 cache and history files
    (index.dat).

    Reference URLs: https://forensics.wiki/internet_explorer
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Microsoft\\Windows\\IEDownloadHistory\\index.dat",
                    "%%users.localappdata%%\\Microsoft\\Feeds Cache\\index.dat",
                    "%%users.localappdata%%\\Microsoft\\Windows\\History\\History.IE5\\*\\index.dat",
                    "%%users.localappdata%%\\Microsoft\\Windows\\History\\History.IE5\\index.dat",
                    "%%users.localappdata%%\\Microsoft\\Windows\\History\\Low\\History.IE5\\*\\index.dat",
                    "%%users.localappdata%%\\Microsoft\\Windows\\History\\Low\\History.IE5\\index.dat",
                    "%%users.localappdata%%\\Microsoft\\Windows\\Temporary Internet Files\\Content.IE5\\index.dat",
                    "%%users.localappdata%%\\Microsoft\\Windows\\Temporary Internet Files\\Low\\Content.IE5\\index.dat",
                    "%%users.userprofile%%\\Local Settings\\History\\History.IE5\\index.dat",
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


class InternetExplorerProtectedModeElevationPolicies(GRRArtifactBase):
    """
    Trust levels of apps launched from low rights IE sessions.

    The ElevationPolicy dictates how IE handles applications that want to
    execute in other applications that reside outside of the Low Rights IE
    session.

    AppName is the executable * AppPath is the directory * CLSID is used if it
    launches a COM server through CoCreateInstance * Policy (DWORD) is the trust
    level, of 0 through 3.

    * 3 Protected Mode silently launches the broker as a medium integrity
    process. * 2 Protected Mode prompts the user for permission to launch the
    process. If permission is granted, the process is launched as a medium
    integrity process. * 1 Protected Mode silently launches the broker as a low
    integrity process. * 0 Protected Mode prevents the process from launching.

    Reference URLs:
    http://blogs.technet.com/b/juanand/archive/2010/10/29/internet-explorer-protected-mode-elevation-policy-and-administrative-templates.aspx
    https://msdn.microsoft.com/en-us/library/bb250462(VS.85).aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer\\Low Rights\\ElevationPolicy\\*",
                        "value": "Policy",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer\\Low Rights\\ElevationPolicy\\*",
                        "value": "AppName",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer\\Low Rights\\ElevationPolicy\\*",
                        "value": "AppPath",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer\\Low Rights\\ElevationPolicy\\*",
                        "value": "CLSID",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer\\Low Rights\\ElevationPolicy\\*",
                        "value": "Policy",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer\\Low Rights\\ElevationPolicy\\*",
                        "value": "AppName",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer\\Low Rights\\ElevationPolicy\\*",
                        "value": "AppPath",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer\\Low Rights\\ElevationPolicy\\*",
                        "value": "CLSID",
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


class InternetExplorerProtectedModeDisable(GRRArtifactBase):
    """
    Microsoft Internet Explorer (MSIE) Protected Mode Banner can be suppressed
    by setting NoProtectedModeBanner.

    * Applies to versions 7-11

    Reference URLs:
    http://www.blackforce.co.uk/2014/01/07/disable-protected-mode-is-turned-off-for-the-internet-zone-group-policy
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer\\Main\\NoProtectedModeBanner"
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


class InternetExplorer6Settings(GRRArtifactBase):
    """
    Registry keys affecting default behavior for Microsoft Internet Explorer 6.

    Reference URLs: https://support.microsoft.com/en-us/kb/895339
    http://gladiator-antivirus.com/forum/index.php?showtopic=24610
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer",
                        "value": "AboutURLs",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer",
                        "value": "UrlSearchHooks",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer",
                        "value": "Extensions",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer",
                        "value": "ExplorerBars",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer",
                        "value": "Toolbar",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer",
                        "value": "SearchURL",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer\\Main",
                        "value": "Default_Page_URL",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer\\Main",
                        "value": "Default_Search_URL",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer\\Main",
                        "value": "Search Page",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer\\Main",
                        "value": "Start Page",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer\\Main",
                        "value": "Search Bar",
                    },
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Internet Explorer\\Search",
                        "value": "CustomizeSearch",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer",
                        "value": "UrlSearchHooks",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer",
                        "value": "Extensions",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer",
                        "value": "ExplorerBars",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer",
                        "value": "Toolbar",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer",
                        "value": "SearchURL",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer\\Main",
                        "value": "Default_Page_URL",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer\\Main",
                        "value": "Default_Search_URL",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer\\Main",
                        "value": "Search Page",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer\\Main",
                        "value": "Start Page",
                    },
                    {
                        "key": "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer\\Main",
                        "value": "Search Bar",
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


class InternetExplorerTypedURLsKeys(GRRArtifactBase):
    """
    Microsoft Internet Explorer TypedUrls keys.

    Reference URLs: https://forensics.wiki/internet_explorer#typed-urls
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_USERS\\%%users.sid%%\\Software\\Microsoft\\Internet Explorer\\TypedURLs\\*"
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


class SafariAutoFillCorrectionsSQLiteDatabaseFile(GRRArtifactBase):
    """
    Safari browser auto-fill corrections SQLite database file.

    Reference URLs: https://forensics.wiki/apple_safari
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Safari/AutoFillCorrections.db",
                    "%%users.homedir%%/Library/Safari/AutoFillCorrections.db-wal",
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


class SafariCloudAutoFillCorrectionsSQLiteDatabaseFile(GRRArtifactBase):
    """
    Safari browser cloud auto-fill corrections SQLite database file.

    Reference URLs: https://forensics.wiki/apple_safari
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Safari/CloudAutoFillCorrections.db",
                    "%%users.homedir%%/Library/Safari/CloudAutoFillCorrections.db-wal",
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


class SafariCookies(GRRArtifactBase):
    """
    Safari Cookies database.

    Reference URLs: https://forensics.wiki/apple_safari
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Cookies/Cookies.binarycookies",
                    "%%users.homedir%%/Library/Containers/com.apple.Safari/Data/Library/Cookies/Cookies.binarycookies",
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


class SafariExtensions(GRRArtifactBase):
    """
    Safari browser extensions.

    Reference URLs: https://forensics.wiki/apple_safari/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/Library/Safari/Extensions/**"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SafariFaviconsCacheSQLiteDatabaseFile(GRRArtifactBase):
    """
    Safari browser favicons cache SQLite database file.

    Reference URLs: https://forensics.wiki/apple_safari
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Safari/Favicon Cache/favicons.db",
                    "%%users.homedir%%/Library/Safari/Favicon Cache/favicons.db-wal",
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


class SafariPerSitePreferencesSQLiteDatabaseFile(GRRArtifactBase):
    """
    Safari browser per site preferences SQLite database file.

    Reference URLs: https://forensics.wiki/apple_safari
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Safari/PerSitePreferences.db",
                    "%%users.homedir%%/Library/Safari/PerSitePreferences.db-wal",
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


class SafariTabSnapshotsMetadataSQLiteDatabaseFile(GRRArtifactBase):
    """
    Safari browser tab snapshots metadata SQLite database file.

    Reference URLs: https://forensics.wiki/apple_safari
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Caches/com.apple.Safari/TabSnapshots/Metadata.db"
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


class SafariTouchIconCacheSettingsSQLiteDatabaseFile(GRRArtifactBase):
    """
    Safari browser touch icon cache settings SQLite database file.

    Reference URLs: https://forensics.wiki/apple_safari
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/Library/Safari/Touch Icons Cache/TouchIconCacheSettings.db",
                    "%%users.homedir%%/Library/Safari/Touch Icons Cache/TouchIconCacheSettings.db-wal",
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


class WebKitPubSubSQLiteDatabaseFile(GRRArtifactBase):
    """
    WebKit RSS feed (PubSub) SQLite database file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/Library/PubSub/Database/Database.sqlite3"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class BrowserCache(GRRArtifactBase):
    """
    Web browser cache of multiple web browsers.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "ChromiumBasedBrowsersCache",
                    "FirefoxCache",
                    "InternetExplorerCache",
                    "SafariCacheSQLiteDatabaseFile",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "InternetExplorerCache": InternetExplorerCache,
        "FirefoxCache": FirefoxCache,
        "SafariCacheSQLiteDatabaseFile": SafariCacheSQLiteDatabaseFile,
        "ChromiumBasedBrowsersCache": ChromiumBasedBrowsersCache,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SafariHistory(GRRArtifactBase):
    """
    Safari browser history.

    Reference URLs: https://forensics.wiki/apple_safari
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": ["SafariHistorySQLiteDatabaseFile", "SafariHistoryPlistFile"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "SafariHistoryPlistFile": SafariHistoryPlistFile,
        "SafariHistorySQLiteDatabaseFile": SafariHistorySQLiteDatabaseFile,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ChromeStorage(GRRArtifactBase):
    """
    Google Chrome, Canary and Chromium browser artifacts for Storage APIs.

    Includes Web Storage (sessionStorage for session-only data and localStorage
    for persistent data), IndexedDB (used for structured data), and FileSystem
    (object storage in a virtual file system).

    Reference URLs:
    https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API
    https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API
    https://developer.mozilla.org/en-US/docs/Web/API/FileSystem
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "ChromeLocalStorage",
                    "ChromeSessionStorage",
                    "ChromeFileSystem",
                    "ChromeIndexedDB",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "ChromeFileSystem": ChromeFileSystem,
        "ChromeLocalStorage": ChromeLocalStorage,
        "ChromeSessionStorage": ChromeSessionStorage,
        "ChromeIndexedDB": ChromeIndexedDB,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class InternetExplorerHistory(GRRArtifactBase):
    """
    Microsoft Internet Explorer (MSIE) browser history.

    * MSIE 4 - 9 Cache files (index.dat); * MSIE 10 WebCacheV*.dat files.

    Reference URLs: https://forensics.wiki/internet_explorer
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "InternetExplorerHistoryDatabaseFile",
                    "InternetExplorerIndexDatFiles",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "InternetExplorerHistoryDatabaseFile": InternetExplorerHistoryDatabaseFile,
        "InternetExplorerIndexDatFiles": InternetExplorerIndexDatFiles,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class BrowserHistory(GRRArtifactBase):
    """
    Web browser history of multiple web browsers.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "ChromiumBasedBrowsersHistoryDatabaseFile",
                    "FirefoxHistory",
                    "FirefoxDownloads",
                    "InternetExplorerHistory",
                    "OperaHistoryFile",
                    "SafariDownloadsPlistFile",
                    "SafariHistorySQLiteDatabaseFile",
                    "SafariHistoryPlistFile",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "SafariHistoryPlistFile": SafariHistoryPlistFile,
        "SafariDownloadsPlistFile": SafariDownloadsPlistFile,
        "InternetExplorerHistory": InternetExplorerHistory,
        "OperaHistoryFile": OperaHistoryFile,
        "SafariHistorySQLiteDatabaseFile": SafariHistorySQLiteDatabaseFile,
        "ChromiumBasedBrowsersHistoryDatabaseFile": ChromiumBasedBrowsersHistoryDatabaseFile,
        "FirefoxHistory": FirefoxHistory,
        "FirefoxDownloads": FirefoxDownloads,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = None
