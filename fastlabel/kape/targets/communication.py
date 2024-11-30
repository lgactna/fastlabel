"""
Auto-generated classes from the .tkape files for the Communication category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class JavaWebCacheJavaWebStartCacheUserLevelDefault0(KapeTarget):
    name: ClassVar[str] = "Java WebStart Cache User Level - Default"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Sun\\Java\\Deployment\\cache\\*\\*\\"
    )
    file_mask: ClassVar[str] = "*.idx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JavaWebCacheJavaWebStartCacheUserLevelIEProtectedMode1(KapeTarget):
    name: ClassVar[str] = "Java WebStart Cache User Level - IE Protected Mode"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\LocalLow\\Sun\\Java\\Deployment\\cache\\*\\*\\"
    )
    file_mask: ClassVar[str] = "*.idx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JavaWebCacheJavaWebStartCacheSystemlevel2(KapeTarget):
    name: ClassVar[str] = "Java WebStart Cache System level"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Sun\\Java\\Deployment\\cache\\*\\*\\"
    )
    file_mask: ClassVar[str] = "*.idx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JavaWebCacheJavaWebStartCacheSystemlevel3(KapeTarget):
    name: ClassVar[str] = "Java WebStart Cache System level"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\config\\systemprofile\\AppData\\Local\\Sun\\Java\\Deployment\\cache\\*\\*\\"
    )
    file_mask: ClassVar[str] = "*.idx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JavaWebCacheJavaWebStartCacheSystemlevelIEProtectedMode4(KapeTarget):
    name: ClassVar[str] = "Java WebStart Cache System level - IE Protected Mode"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows\\System32\\config\\systemprofile\\AppData\\LocalLow\\Sun\\Java\\Deployment\\cache\\*\\*\\"
    )
    file_mask: ClassVar[str] = "*.idx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JavaWebCacheJavaWebStartCacheSystemlevelIEProtectedMode5(KapeTarget):
    name: ClassVar[str] = "Java WebStart Cache System level - IE Protected Mode"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\config\\systemprofile\\AppData\\LocalLow\\Sun\\Java\\Deployment\\cache\\*\\*\\"
    )
    file_mask: ClassVar[str] = "*.idx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JavaWebCacheJavaWebStartCacheSystemlevelSysWow646(KapeTarget):
    name: ClassVar[str] = "Java WebStart Cache System level (SysWow64)"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows\\SysWOW64\\config\\systemprofile\\AppData\\Local\\Sun\\Java\\Deployment\\cache\\*\\*\\"
    )
    file_mask: ClassVar[str] = "*.idx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JavaWebCacheJavaWebStartCacheSystemlevelSysWow647(KapeTarget):
    name: ClassVar[str] = "Java WebStart Cache System level (SysWow64)"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\SysWOW64\\config\\systemprofile\\AppData\\Local\\Sun\\Java\\Deployment\\cache\\*\\*\\"
    )
    file_mask: ClassVar[str] = "*.idx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JavaWebCacheJavaWebStartCacheSystemlevelSysWow64IEProtectedMode8(KapeTarget):
    name: ClassVar[str] = (
        "Java WebStart Cache System level (SysWow64) - IE Protected Mode"
    )
    base_path: ClassVar[Path] = Path(
        "C:\\Windows\\SysWOW64\\config\\systemprofile\\AppData\\LocalLow\\Sun\\Java\\Deployment\\cache\\*\\*\\"
    )
    file_mask: ClassVar[str] = "*.idx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JavaWebCacheJavaWebStartCacheSystemlevelSysWow64IEProtectedMode9(KapeTarget):
    name: ClassVar[str] = (
        "Java WebStart Cache System level (SysWow64) - IE Protected Mode"
    )
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\SysWOW64\\config\\systemprofile\\AppData\\LocalLow\\Sun\\Java\\Deployment\\cache\\*\\*\\"
    )
    file_mask: ClassVar[str] = "*.idx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JavaWebCacheJavaWebStartCacheUserLevelXP10(KapeTarget):
    name: ClassVar[str] = "Java WebStart Cache User Level - XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Application Data\\Sun\\Java\\Deployment\\cache\\*\\*\\"
    )
    file_mask: ClassVar[str] = "*.idx"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class JavaWebCache(KapeTargetConfiguration):
    """
    Author: piesecurity

    Version: 1.0

    ID: 4dc2e35c-fc20-45f6-89a6-5d729596c522

    Java WebStart Cache - (IDX Files)
    """

    name: ClassVar[str] = "JavaWebCache"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        JavaWebCacheJavaWebStartCacheUserLevelDefault0,
        JavaWebCacheJavaWebStartCacheUserLevelIEProtectedMode1,
        JavaWebCacheJavaWebStartCacheSystemlevel2,
        JavaWebCacheJavaWebStartCacheSystemlevel3,
        JavaWebCacheJavaWebStartCacheSystemlevelIEProtectedMode4,
        JavaWebCacheJavaWebStartCacheSystemlevelIEProtectedMode5,
        JavaWebCacheJavaWebStartCacheSystemlevelSysWow646,
        JavaWebCacheJavaWebStartCacheSystemlevelSysWow647,
        JavaWebCacheJavaWebStartCacheSystemlevelSysWow64IEProtectedMode8,
        JavaWebCacheJavaWebStartCacheSystemlevelSysWow64IEProtectedMode9,
        JavaWebCacheJavaWebStartCacheUserLevelXP10,
    ]


class ChromeExtensionsChromeExtensionFiles0(KapeTarget):
    name: ClassVar[str] = "Chrome Extension Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\Extensions\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeExtensionsChromeExtensionFilesXP1(KapeTarget):
    name: ClassVar[str] = "Chrome Extension Files XP"
    base_path: ClassVar[Path] = Path(
        "C:\\Documents and Settings\\%user%\\Local Settings\\Application Data\\Google\\Chrome\\User Data\\*\\Extensions\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeExtensions(KapeTargetConfiguration):
    """
    Author: piesecurity

    Version: 1.0

    ID: e748b5e3-e279-4e4d-8083-74293e5b6cde

    Chrome Extension Files
    """

    name: ClassVar[str] = "ChromeExtensions"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ChromeExtensionsChromeExtensionFiles0,
        ChromeExtensionsChromeExtensionFilesXP1,
    ]


class ChromeFileSystemChromeHTML5FileSystemFolder0(KapeTarget):
    name: ClassVar[str] = "Chrome HTML5 File System Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Google\\Chrome\\User Data\\*\\File System\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class ChromeFileSystem(KapeTargetConfiguration):
    """
    Author: Chad Tilbury

    Version: 1.0

    ID: a135eb84-5407-4590-a3e8-02564ebc5fa9

    Chrome HTML5 File System Contents
    """

    name: ClassVar[str] = "ChromeFileSystem"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        ChromeFileSystemChromeHTML5FileSystemFolder0
    ]


class GroupPolicyLocalGroupPolicyINIFiles0(KapeTarget):
    name: ClassVar[str] = "Local Group Policy INI Files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\grouppolicy\\")
    file_mask: ClassVar[str] = "*.ini"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GroupPolicyLocalGroupPolicyINIFiles1(KapeTarget):
    name: ClassVar[str] = "Local Group Policy INI Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\grouppolicy\\"
    )
    file_mask: ClassVar[str] = "*.ini"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GroupPolicyLocalGroupPolicyFilesRegistryPolicyFiles2(KapeTarget):
    name: ClassVar[str] = "Local Group Policy Files - Registry Policy Files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\grouppolicy\\")
    file_mask: ClassVar[str] = "*.pol"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GroupPolicyLocalGroupPolicyFilesRegistryPolicyFiles3(KapeTarget):
    name: ClassVar[str] = "Local Group Policy Files - Registry Policy Files"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\grouppolicy\\"
    )
    file_mask: ClassVar[str] = "*.pol"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GroupPolicyLocalGroupPolicyFilesStartupShutdownScripts4(KapeTarget):
    name: ClassVar[str] = "Local Group Policy Files - Startup/Shutdown Scripts"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\grouppolicy\\*\\Scripts\\")
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GroupPolicyLocalGroupPolicyFilesStartupShutdownScripts5(KapeTarget):
    name: ClassVar[str] = "Local Group Policy Files - Startup/Shutdown Scripts"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\grouppolicy\\*\\Scripts\\"
    )
    file_mask: ClassVar[str] = "*"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class GroupPolicy(KapeTargetConfiguration):
    """
    Author: piesecurity

    Version: 1.0

    ID: e5595e9c-ebab-41db-a688-fdffe91f6fcb

    Current Group Policy Enforcement
    """

    name: ClassVar[str] = "GroupPolicy"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        GroupPolicyLocalGroupPolicyINIFiles0,
        GroupPolicyLocalGroupPolicyINIFiles1,
        GroupPolicyLocalGroupPolicyFilesRegistryPolicyFiles2,
        GroupPolicyLocalGroupPolicyFilesRegistryPolicyFiles3,
        GroupPolicyLocalGroupPolicyFilesStartupShutdownScripts4,
        GroupPolicyLocalGroupPolicyFilesStartupShutdownScripts5,
    ]
