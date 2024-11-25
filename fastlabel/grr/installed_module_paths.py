"""
Auto-generated classes from the YAML declarations in installed_module_paths.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class FlatpakAppPaths(GRRArtifactBase):
    """
    Get paths of installed Flatpak app.

    Reference URLs: https://docs.flatpak.org/
    """

    SOURCES = [
        {
            "type": "PATH",
            "attributes": {"paths": ["/var/lib/flatpak/app/*"]},
            "supported_os": ["Linux"],
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class NpmPackagesPath(GRRArtifactBase):
    """
    Get path of NPM packages that are globally installed (currently linux only).

    Reference URLs: https://docs.npmjs.com/
    """

    SOURCES = [
        {
            "type": "PATH",
            "attributes": {
                "paths": ["/usr/local/lib/node_modules/*", "/usr/lib/node_modules/*"]
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


class PythonDistInfoPath(GRRArtifactBase):
    """
    Get the path of Python module files distributed in the dist-info format of
    PEP-0376 (currently Linux only).

    dist-info is always a directory that must contain METADATA, RECORD and
    INSTALLER. It may also contain REQUESTED.

    Reference URLs: https://www.python.org/dev/peps/pep-0376/
    """

    SOURCES = [
        {
            "type": "PATH",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.local/lib/python*/dist-packages/*.dist-info",
                    "%%users.homedir%%/.local/lib/python*/site-packages/*.dist-info",
                    "/usr/lib/python*/dist-packages/*.dist-info",
                    "/usr/lib/python*/site-packages/*.dist-info",
                    "/usr/lib64/python*/dist-packages/*.dist-info",
                    "/usr/lib64/python*/site-packages/*.dist-info",
                    "/usr/local/lib/python*/dist-packages/*.dist-info",
                    "/usr/local/lib/python*/site-packages/*.dist-info",
                    "/usr/local/lib64/python*/dist-packages/*.dist-info",
                    "/usr/local/lib64/python*/site-packages/*.dist-info",
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


class VSCodeExtensionsPath(GRRArtifactBase):
    """
    Get paths of Visual Studio Code extensions

    Reference URLs: https://code.visualstudio.com/
    """

    SOURCES = [
        {
            "type": "PATH",
            "attributes": {"paths": ["%%users.userprofile%%/.vscode/extensions/*"]},
            "supported_os": ["Windows"],
        },
        {
            "type": "PATH",
            "attributes": {"paths": ["%%users.homedir%%/.vscode/extensions/*"]},
            "supported_os": ["Darwin", "Linux"],
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
