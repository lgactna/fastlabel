"""
Auto-generated classes from the .tkape files for the Windows Subsystem for Linux category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class DebianDebianWSLetcdebianversion0(KapeTarget):
    name: ClassVar[str] = "Debian WSL /etc/debian_version"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:debian_version)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLetcfstab1(KapeTarget):
    name: ClassVar[str] = "Debian WSL /etc/fstab"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:fstab)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLetcosrelease2(KapeTarget):
    name: ClassVar[str] = "Debian WSL /etc/os-release"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:os\-release)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLetcpasswd3(KapeTarget):
    name: ClassVar[str] = "Debian WSL /etc/passwd"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:passwd)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLetcgroup4(KapeTarget):
    name: ClassVar[str] = "Debian WSL /etc/group"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:group)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLetcshadow5(KapeTarget):
    name: ClassVar[str] = "Debian WSL /etc/shadow"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:shadow)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLetctimezone6(KapeTarget):
    name: ClassVar[str] = "Debian WSL /etc/timezone"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:timezone)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLetchostname7(KapeTarget):
    name: ClassVar[str] = "Debian WSL /etc/hostname"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:hostname)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLetchosts8(KapeTarget):
    name: ClassVar[str] = "Debian WSL /etc/hosts"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:hosts)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLetccrontab9(KapeTarget):
    name: ClassVar[str] = "Debian WSL /etc/crontab"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:crontab)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLetcbashbashrc10(KapeTarget):
    name: ClassVar[str] = "Debian WSL /etc/bash.bashrc"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:bash\.bashrc)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLetcprofile11(KapeTarget):
    name: ClassVar[str] = "Debian WSL /etc/profile"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:profile)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLbashhistory12(KapeTarget):
    name: ClassVar[str] = "Debian WSL .bash_history"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.bash_history)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLbashrc13(KapeTarget):
    name: ClassVar[str] = "Debian WSL .bashrc"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.bashrc)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLprofile14(KapeTarget):
    name: ClassVar[str] = "Debian WSL .profile"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.profile)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLUserCrontabs15(KapeTarget):
    name: ClassVar[str] = "Debian WSL User Crontabs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\var\\spool\\cron\\crontabs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class DebianDebianWSLAptLogs16(KapeTarget):
    name: ClassVar[str] = "Debian WSL Apt Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_*\\LocalState\\rootfs\\var\\log\\apt\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.log)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Debian(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 3629bafb-16b5-41de-988f-6961c6d3b6e1

    Debian on Windows Subsystem for Linux
    """

    name: ClassVar[str] = "Debian"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        DebianDebianWSLetcdebianversion0,
        DebianDebianWSLetcfstab1,
        DebianDebianWSLetcosrelease2,
        DebianDebianWSLetcpasswd3,
        DebianDebianWSLetcgroup4,
        DebianDebianWSLetcshadow5,
        DebianDebianWSLetctimezone6,
        DebianDebianWSLetchostname7,
        DebianDebianWSLetchosts8,
        DebianDebianWSLetccrontab9,
        DebianDebianWSLetcbashbashrc10,
        DebianDebianWSLetcprofile11,
        DebianDebianWSLbashhistory12,
        DebianDebianWSLbashrc13,
        DebianDebianWSLprofile14,
        DebianDebianWSLUserCrontabs15,
        DebianDebianWSLAptLogs16,
    ]


class KaliKaliWSLetcdebianversion0(KapeTarget):
    name: ClassVar[str] = "Kali WSL /etc/debian_version"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:debian_version)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLetcfstab1(KapeTarget):
    name: ClassVar[str] = "Kali WSL /etc/fstab"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:fstab)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLetcosrelease2(KapeTarget):
    name: ClassVar[str] = "Kali WSL /etc/os-release"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:os\-release)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLetcpasswd3(KapeTarget):
    name: ClassVar[str] = "Kali WSL /etc/passwd"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:passwd)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLetcgroup4(KapeTarget):
    name: ClassVar[str] = "Kali WSL /etc/group"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:group)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLetcshadow5(KapeTarget):
    name: ClassVar[str] = "Kali WSL /etc/shadow"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:shadow)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLetctimezone6(KapeTarget):
    name: ClassVar[str] = "Kali WSL /etc/timezone"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:timezone)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLetchostname7(KapeTarget):
    name: ClassVar[str] = "Kali WSL /etc/hostname"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:hostname)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLetchosts8(KapeTarget):
    name: ClassVar[str] = "Kali WSL /etc/hosts"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:hosts)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLetccrontab9(KapeTarget):
    name: ClassVar[str] = "Kali WSL /etc/crontab"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:crontab)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLetcbashbashrc10(KapeTarget):
    name: ClassVar[str] = "Kali WSL /etc/bash.bashrc"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:bash\.bashrc)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLetcprofile11(KapeTarget):
    name: ClassVar[str] = "Kali WSL /etc/profile"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:profile)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLbashhistory12(KapeTarget):
    name: ClassVar[str] = "Kali WSL .bash_history"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.bash_history)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLbashrc13(KapeTarget):
    name: ClassVar[str] = "Kali WSL .bashrc"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.bashrc)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLprofile14(KapeTarget):
    name: ClassVar[str] = "Kali WSL .profile"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.profile)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLUserCrontabs15(KapeTarget):
    name: ClassVar[str] = "Kali WSL User Crontabs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\var\\spool\\cron\\crontabs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class KaliKaliWSLAptLogs16(KapeTarget):
    name: ClassVar[str] = "Kali WSL Apt Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\KaliLinux.54290C8133FEE_*\\LocalState\\rootfs\\var\\log\\apt\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.log)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Kali(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 6ea14af7-6217-4a39-9455-76ab5a1c0b2d

    Kali on Windows Subsystem for Linux
    """

    name: ClassVar[str] = "Kali"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        KaliKaliWSLetcdebianversion0,
        KaliKaliWSLetcfstab1,
        KaliKaliWSLetcosrelease2,
        KaliKaliWSLetcpasswd3,
        KaliKaliWSLetcgroup4,
        KaliKaliWSLetcshadow5,
        KaliKaliWSLetctimezone6,
        KaliKaliWSLetchostname7,
        KaliKaliWSLetchosts8,
        KaliKaliWSLetccrontab9,
        KaliKaliWSLetcbashbashrc10,
        KaliKaliWSLetcprofile11,
        KaliKaliWSLbashhistory12,
        KaliKaliWSLbashrc13,
        KaliKaliWSLprofile14,
        KaliKaliWSLUserCrontabs15,
        KaliKaliWSLAptLogs16,
    ]


class openSUSEopenSUSEWSLetcosrelease0(KapeTarget):
    name: ClassVar[str] = "openSUSE WSL /etc/os-release"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.openSUSE*Leap*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:os\-release)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class openSUSEopenSUSEWSLetcfstab1(KapeTarget):
    name: ClassVar[str] = "openSUSE WSL /etc/fstab"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.openSUSE*Leap*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:fstab)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class openSUSEopenSUSEWSLetcpasswd2(KapeTarget):
    name: ClassVar[str] = "openSUSE WSL /etc/passwd"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.openSUSE*Leap*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:passwd)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class openSUSEopenSUSEWSLetcgroup3(KapeTarget):
    name: ClassVar[str] = "openSUSE WSL /etc/group"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.openSUSE*Leap*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:group)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class openSUSEopenSUSEWSLetcshadow4(KapeTarget):
    name: ClassVar[str] = "openSUSE WSL /etc/shadow"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.openSUSE*Leap*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:shadow)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class openSUSEopenSUSEWSLetctimezone5(KapeTarget):
    name: ClassVar[str] = "openSUSE WSL /etc/timezone"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.openSUSE*Leap*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:timezone)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class openSUSEopenSUSEWSLetchostname6(KapeTarget):
    name: ClassVar[str] = "openSUSE WSL /etc/hostname"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.openSUSE*Leap*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:hostname)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class openSUSEopenSUSEWSLetchosts7(KapeTarget):
    name: ClassVar[str] = "openSUSE WSL /etc/hosts"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.openSUSE*Leap*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:hosts)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class openSUSEopenSUSEWSLetcbashbashrc8(KapeTarget):
    name: ClassVar[str] = "openSUSE WSL /etc/bash.bashrc"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.openSUSE*Leap*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:bash\.bashrc)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class openSUSEopenSUSEWSLetcprofile9(KapeTarget):
    name: ClassVar[str] = "openSUSE WSL /etc/profile"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.openSUSE*Leap*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:profile)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class openSUSEopenSUSEWSLbashhistory10(KapeTarget):
    name: ClassVar[str] = "openSUSE WSL .bash_history"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.openSUSE*Leap*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.bash_history)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class openSUSEopenSUSEWSLbashrc11(KapeTarget):
    name: ClassVar[str] = "openSUSE WSL .bashrc"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.openSUSE*Leap*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.bashrc)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class openSUSEopenSUSEWSLprofile12(KapeTarget):
    name: ClassVar[str] = "openSUSE WSL .profile"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.openSUSE*Leap*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.profile)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class openSUSE(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 9b3ad543-b86b-4a9c-b305-ed9dac48ab86

    openSUSE on Windows Subsystem for Linux
    """

    name: ClassVar[str] = "openSUSE"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        openSUSEopenSUSEWSLetcosrelease0,
        openSUSEopenSUSEWSLetcfstab1,
        openSUSEopenSUSEWSLetcpasswd2,
        openSUSEopenSUSEWSLetcgroup3,
        openSUSEopenSUSEWSLetcshadow4,
        openSUSEopenSUSEWSLetctimezone5,
        openSUSEopenSUSEWSLetchostname6,
        openSUSEopenSUSEWSLetchosts7,
        openSUSEopenSUSEWSLetcbashbashrc8,
        openSUSEopenSUSEWSLetcprofile9,
        openSUSEopenSUSEWSLbashhistory10,
        openSUSEopenSUSEWSLbashrc11,
        openSUSEopenSUSEWSLprofile12,
    ]


class SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcosrelease0(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server WSL /etc/os-release"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.SUSELinuxEnterpriseServer*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:os\-release)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcfstab1(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server WSL /etc/fstab"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.SUSELinuxEnterpriseServer*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:fstab)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcpasswd2(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server WSL /etc/passwd"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.SUSELinuxEnterpriseServer*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:passwd)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcgroup3(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server WSL /etc/group"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.SUSELinuxEnterpriseServer*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:group)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcshadow4(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server WSL /etc/shadow"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.SUSELinuxEnterpriseServer*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:shadow)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetctimezone5(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server WSL /etc/timezone"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.SUSELinuxEnterpriseServer*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:timezone)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetchostname6(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server WSL /etc/hostname"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.SUSELinuxEnterpriseServer*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:hostname)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetchosts7(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server WSL /etc/hosts"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.SUSELinuxEnterpriseServer*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:hosts)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcbashbashrc8(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server WSL /etc/bash.bashrc"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.SUSELinuxEnterpriseServer*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:bash\.bashrc)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcprofile9(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server WSL /etc/profile"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.SUSELinuxEnterpriseServer*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:profile)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLbashhistory10(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server WSL .bash_history"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.SUSELinuxEnterpriseServer*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.bash_history)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLbashrc11(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server WSL .bashrc"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.SUSELinuxEnterpriseServer*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.bashrc)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLprofile12(KapeTarget):
    name: ClassVar[str] = "SUSE Linux Enterprise Server WSL .profile"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\46932SUSE.SUSELinuxEnterpriseServer*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.profile)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class SUSELinuxEnterpriseServer(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 367ab533-8f34-4913-b145-8052294ad633

    SUSE Linux Enterprise Server on Windows Subsystem for Linux
    """

    name: ClassVar[str] = "SUSELinuxEnterpriseServer"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcosrelease0,
        SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcfstab1,
        SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcpasswd2,
        SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcgroup3,
        SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcshadow4,
        SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetctimezone5,
        SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetchostname6,
        SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetchosts7,
        SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcbashbashrc8,
        SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLetcprofile9,
        SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLbashhistory10,
        SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLbashrc11,
        SUSELinuxEnterpriseServerSUSELinuxEnterpriseServerWSLprofile12,
    ]


class UbuntuUbuntuWSLetcosrelease0(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL /etc/os-release"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:os\-release)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLetcfstab1(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL /etc/fstab"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:fstab)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLetcpasswd2(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL /etc/passwd"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:passwd)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLetcgroup3(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL /etc/group"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:group)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLetcshadow4(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL /etc/shadow"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:shadow)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLetctimezone5(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL /etc/timezone"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:timezone)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLetchostname6(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL /etc/hostname"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:hostname)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLetchosts7(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL /etc/hosts"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:hosts)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLetccrontab8(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL /etc/crontab"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:crontab)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLetcbashbashrc9(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL /etc/bash.bashrc"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:bash\.bashrc)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLetcprofile10(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL /etc/profile"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\etc\\"
    )
    regex: ClassVar[str] = r"(?s:profile)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLbashhistory11(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL .bash_history"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.bash_history)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLbashrc12(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL .bashrc"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.bashrc)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLprofile13(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL .profile"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\"
    )
    regex: ClassVar[str] = r"(?s:\.profile)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLUserCrontabs14(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL User Crontabs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\var\\spool\\cron\\crontabs\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class UbuntuUbuntuWSLAptLogs15(KapeTarget):
    name: ClassVar[str] = "Ubuntu WSL Apt Logs"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Packages\\CanonicalGroupLimited.Ubuntu*\\LocalState\\rootfs\\var\\log\\apt\\"
    )
    regex: ClassVar[str] = r"(?s:.*\.log)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class Ubuntu(KapeTargetConfiguration):
    """
    Author: Matt Dawson

    Version: 1.0

    ID: 08b27869-b454-403a-84af-2aa1f2f69a37

    Ubuntu on Windows Subsystem for Linux
    """

    name: ClassVar[str] = "Ubuntu"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        UbuntuUbuntuWSLetcosrelease0,
        UbuntuUbuntuWSLetcfstab1,
        UbuntuUbuntuWSLetcpasswd2,
        UbuntuUbuntuWSLetcgroup3,
        UbuntuUbuntuWSLetcshadow4,
        UbuntuUbuntuWSLetctimezone5,
        UbuntuUbuntuWSLetchostname6,
        UbuntuUbuntuWSLetchosts7,
        UbuntuUbuntuWSLetccrontab8,
        UbuntuUbuntuWSLetcbashbashrc9,
        UbuntuUbuntuWSLetcprofile10,
        UbuntuUbuntuWSLbashhistory11,
        UbuntuUbuntuWSLbashrc12,
        UbuntuUbuntuWSLprofile13,
        UbuntuUbuntuWSLUserCrontabs14,
        UbuntuUbuntuWSLAptLogs15,
    ]
