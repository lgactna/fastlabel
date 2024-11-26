"""
Auto-generated classes from the YAML declarations in shell.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class BashShellConfigurationFile(GRRArtifactBase):
    """
    Bourne Again shell (bash) configuration files.

    Reference URLs: https://forensics.wiki/bash_shell
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.bash_logout",
                    "%%users.homedir%%/.bash_profile",
                    "%%users.homedir%%/.bashrc",
                    "/etc/bash.bashrc",
                    "/etc/bashrc",
                ]
            },
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": ["/private/etc/bash.bashrc", "/private/etc/bashrc"]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.bash_logout",
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.bash_profile",
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.bashrc",
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


class BashShellHistoryFile(GRRArtifactBase):
    """
    Bourne Again shell (bash) history files.

    Reference URLs: https://forensics.wiki/bash_shell
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/.bash_history"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.bash_history"
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
    aliases: ClassVar[Optional[list[str]]] = ["MacOSBashHistory"]


class BashShellSessionFile(GRRArtifactBase):
    """
    Bourne Again shell (bash) session files.

    Reference URLs: https://forensics.wiki/bash_shell
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/.bash_sessions/*"]},
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN
    ]
    aliases: ClassVar[Optional[list[str]]] = ["MacOSBashSessions"]


class BourneShellHistoryFile(GRRArtifactBase):
    """
    Bourne shell (sh) history files.

    Reference URLs: https://en.wikipedia.org/wiki/Bourne_shell
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/.sh_history"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.sh_history"
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


class CShellConfigurationFile(GRRArtifactBase):
    """
    C shell (csh) configuration files.

    Reference URLs: https://en.wikipedia.org/wiki/C_shell
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.cshrc",
                    "/etc/csh.cshrc",
                    "/etc/csh.login",
                    "/etc/csh.logout",
                ]
            },
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/etc/csh.cshrc",
                    "/private/etc/csh.login",
                    "/private/etc/csh.logout",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.cshrc"
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


class FishShellConfigurationFile(GRRArtifactBase):
    """
    FishShell (fish) configuration files.

    Reference URLs:
    https://fishshell.com/docs/current/language.html#configuration
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.config/fish/conf.d/config.fish",
                    "/etc/fish/conf.d/*.fish",
                    "%%users.homedir%%/.config/fish/config.fish",
                    "/etc/fish/config.fish",
                ]
            },
            "supported_os": ["Linux"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class FishShellHistoryFile(GRRArtifactBase):
    """
    Fish shell (fish) history files.

    Reference URLs: https://fishshell.com/docs/current/cmds/history.html
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": ["%%users.homedir%%/.local/share/fish/fish_history"]
            },
            "supported_os": ["Linux"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class KornShellConfigurationFile(GRRArtifactBase):
    """
    KornShell (ksh) configuration files.

    Reference URLs: https://en.wikipedia.org/wiki/KornShell
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/.ksh", "/etc/kshrc"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/private/etc/kshrc"]},
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.ksh"
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


class RootUserShellConfigs(GRRArtifactBase):
    """
    Common Unix root shell configuration files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/root/.bash_logout",
                    "/root/.bash_profile",
                    "/root/.bashrc",
                    "/root/.cshrc",
                    "/root/.ksh",
                    "/root/.config/fish/config.fish",
                    "/root/.logout",
                    "/root/.profile",
                    "/root/.tcsh",
                    "/root/.zlogin",
                    "/root/.zlogout",
                    "/root/.zprofile",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class RootUserShellHistory(GRRArtifactBase):
    """
    Common Unix root shell history files.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/root/.bash_history",
                    "/root/.local/share/fish/fish_history",
                    "/root/.sh_history",
                    "/root/.zhistory",
                    "/root/.zsh_history",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class ZShellConfigurationFile(GRRArtifactBase):
    """
    Z shell (zsh) configuration files.

    Reference URLs: https://en.wikipedia.org/wiki/Z_shell
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.zlogin",
                    "%%users.homedir%%/.zlogout",
                    "%%users.homedir%%/.zprofile",
                    "/etc/zshenv",
                    "/etc/zshrc",
                    "/etc/zsh/zlogin",
                    "/etc/zsh/zlogout",
                    "/etc/zsh/zprofile",
                    "/etc/zsh/zshenv",
                    "/etc/zsh/zshrc",
                ]
            },
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/private/etc/zshenv",
                    "/private/etc/zshrc",
                    "/private/etc/zsh/zlogin",
                    "/private/etc/zsh/zlogout",
                    "/private/etc/zsh/zprofile",
                    "/private/etc/zsh/zshenv",
                    "/private/etc/zsh/zshrc",
                ]
            },
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.zlogin",
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.zlogout",
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.zprofile",
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


class ShellLogoutFile(GRRArtifactBase):
    """
    Shell logout file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/.logout"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.logout"
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


class ShellProfileFile(GRRArtifactBase):
    """
    Shell profile file.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/.profile", "/etc/profile"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["/private/etc/profile"]},
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.profile"
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


class TeeShellConfigurationFile(GRRArtifactBase):
    """
    Tee shell (tcsh) configuration files.

    Reference URLs: https://en.wikipedia.org/wiki/Tcsh
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/.tcsh"]},
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.tcsh"
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


class ZShellHistoryFile(GRRArtifactBase):
    """
    Z shell (zsh) history files.

    Reference URLs: https://en.wikipedia.org/wiki/Z_shell
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.zhistory",
                    "%%users.homedir%%/.zsh_history",
                ]
            },
            "supported_os": ["Darwin", "Linux"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.zhistory",
                    "%%users.localappdata%%\\Packages\\*\\LocalState\\rootfs\\home\\*\\.zsh_history",
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


class ShellConfigurationFile(GRRArtifactBase):
    """
    Group of shell configuration files.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "BashShellConfigurationFile",
                    "CShellConfigurationFile",
                    "FishShellConfigurationFile",
                    "KornShellConfigurationFile",
                    "ShellLogoutFile",
                    "ShellProfileFile",
                    "TeeShellConfigurationFile",
                    "ZShellConfigurationFile",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "CShellConfigurationFile": CShellConfigurationFile,
        "FishShellConfigurationFile": FishShellConfigurationFile,
        "KornShellConfigurationFile": KornShellConfigurationFile,
        "ZShellConfigurationFile": ZShellConfigurationFile,
        "ShellLogoutFile": ShellLogoutFile,
        "ShellProfileFile": ShellProfileFile,
        "TeeShellConfigurationFile": TeeShellConfigurationFile,
        "BashShellConfigurationFile": BashShellConfigurationFile,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = [
        "AllShellConfigs",
        "GlobalShellConfigs",
        "UsersShellConfigs",
    ]


class ShellHistoryFile(GRRArtifactBase):
    """
    Group of shell history files.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": [
                    "BashShellHistoryFile",
                    "BourneShellHistoryFile",
                    "FishShellHistoryFile",
                    "ZShellHistoryFile",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "ZShellHistoryFile": ZShellHistoryFile,
        "BourneShellHistoryFile": BourneShellHistoryFile,
        "BashShellHistoryFile": BashShellHistoryFile,
        "FishShellHistoryFile": FishShellHistoryFile,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.DARWIN,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.WINDOWS,
    ]
    aliases: ClassVar[Optional[list[str]]] = [
        "AllUsersShellHistory",
        "UserShellHistory",
    ]
