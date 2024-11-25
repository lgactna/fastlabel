"""
Auto-generated classes from the YAML declarations in java.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class JavaCacheFiles(GRRArtifactBase):
    """
    Java Plug-in cache.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/.java/deployment/cache/**"]},
            "supported_os": ["Linux"],
        },
        {
            "type": "FILE",
            "attributes": {"paths": ["%%users.homedir%%/Library/Caches/Java/cache/**"]},
            "supported_os": ["Darwin"],
        },
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.appdata%%\\Sun\\Java\\Deployment\\cache\\**",
                    "%%users.userprofile%%\\AppData\\LocalLow\\Sun\\Java\\Deployment\\cache\\**",
                ],
                "separator": "\\",
            },
            "supported_os": ["Windows"],
        },
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.WINDOWS,
        ArtifactSupportedOS.LINUX,
        ArtifactSupportedOS.DARWIN,
    ]
    aliases: ClassVar[Optional[list[str]]] = None
