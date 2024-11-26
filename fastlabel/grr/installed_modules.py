"""
Auto-generated classes from the YAML declarations in installed_modules.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class PythonDistInfo(GRRArtifactBase):
    """
    Python module files distributed in the dist-info format of PEP-0376
    (currently linux only).

    dist-info is always a directory that must contain METADATA, RECORD and
    INSTALLER. It may also contain REQUESTED.

    Reference URLs: https://www.python.org/dev/peps/pep-0376/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.local/lib/python*/dist-packages/*.dist-info/*",
                    "%%users.homedir%%/.local/lib/python*/site-packages/*.dist-info/*",
                    "/usr/lib/python*/dist-packages/*.dist-info/*",
                    "/usr/lib/python*/site-packages/*.dist-info/*",
                    "/usr/lib64/python*/dist-packages/*.dist-info/*",
                    "/usr/lib64/python*/site-packages/*.dist-info/*",
                    "/usr/local/lib/python*/dist-packages/*.dist-info/*",
                    "/usr/local/lib/python*/site-packages/*.dist-info/*",
                    "/usr/local/lib64/python*/dist-packages/*.dist-info/*",
                    "/usr/local/lib64/python*/site-packages/*.dist-info/*",
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


class PythonEggInfo(GRRArtifactBase):
    """
    Python module files distributed in .egg formats (currently linux only).

    Python eggs can have multiple formats, as described by setuptools.

    .egg files can be either a zipfile or a directory that contains an info
    file. .egg-info files can be either a directory or a file. If they are
    directories, they should contain a MANIFEST that identifies the installed
    module.

    PEP-0370 describes a default install location for per-user modules.

    Reference URLs: https://pythonhosted.org/setuptools/formats.html
    https://www.python.org/dev/peps/pep-0370/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.local/lib/python*/site-packages/*.egg",
                    "%%users.homedir%%/.local/lib/python*/site-packages/*.egg-info",
                    "%%users.homedir%%/.cache/pip/*.egg",
                    "%%users.homedir%%/.cache/pip/*.egg-info",
                    "/usr/lib/python*/dist-packages/*.egg",
                    "/usr/lib/python*/dist-packages/*.egg-info",
                    "/usr/lib/python*/site-packages/*.egg",
                    "/usr/lib/python*/site-packages/*.egg-info",
                    "/usr/lib64/python*/dist-packages/*.egg",
                    "/usr/lib64/python*/dist-packages/*.egg-info",
                    "/usr/lib64/python*/site-packages/*.egg",
                    "/usr/lib64/python*/site-packages/*.egg-info",
                    "/usr/local/lib/python*/dist-packages/*.egg",
                    "/usr/local/lib/python*/dist-packages/*.egg-info",
                    "/usr/local/lib/python*/site-packages/*.egg",
                    "/usr/local/lib/python*/site-packages/*.egg-info",
                    "/usr/local/lib64/python*/dist-packages/*.egg",
                    "/usr/local/lib64/python*/dist-packages/*.egg-info",
                    "/usr/local/lib64/python*/site-packages/*.egg",
                    "/usr/local/lib64/python*/site-packages/*.egg-info",
                    "/usr/share/pyshared/*.egg",
                    "/usr/share/pyshared/*.egg-info",
                    "%%users.homedir%%/.local/lib/python*/site-packages/*.egg/*",
                    "%%users.homedir%%/.local/lib/python*/site-packages/*.egg-info/*",
                    "%%users.homedir%%/.cache/pip/*.egg/*",
                    "%%users.homedir%%/.cache/pip/*.egg-info/*",
                    "/usr/lib/python*/dist-packages/*.egg/*",
                    "/usr/lib/python*/dist-packages/*.egg-info/*",
                    "/usr/lib/python*/site-packages/*.egg/*",
                    "/usr/lib/python*/site-packages/*.egg-info/*",
                    "/usr/lib64/python*/dist-packages/*.egg/*",
                    "/usr/lib64/python*/dist-packages/*.egg-info/*",
                    "/usr/lib64/python*/site-packages/*.egg/*",
                    "/usr/lib64/python*/site-packages/*.egg-info/*",
                    "/usr/local/lib/python*/dist-packages/*.egg/*",
                    "/usr/local/lib/python*/dist-packages/*.egg-info/*",
                    "/usr/local/lib/python*/site-packages/*.egg/*",
                    "/usr/local/lib/python*/site-packages/*.egg-info/*",
                    "/usr/local/lib64/python*/dist-packages/*.egg/*",
                    "/usr/local/lib64/python*/dist-packages/*.egg-info/*",
                    "/usr/local/lib64/python*/site-packages/*.egg/*",
                    "/usr/local/lib64/python*/site-packages/*.egg-info/*",
                    "/usr/share/pyshared/*.egg/*",
                    "/usr/share/pyshared/*.egg-info/*",
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


class PythonWheelInfo(GRRArtifactBase):
    """
    Python module files distributed in the wheel format (currently linux only).

    Zip archives with the .whl extension.

    Wheels are installed per the standard installer described in PEP-0376, so
    should mostly be discoverable as dist-info entries.

    Reference URLs: https://wheel.readthedocs.org/en/latest/
    http://pip.readthedocs.org/en/stable/reference/pip_install/
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/usr/share/python-wheels/*.whl",
                    "%%users.homedir%%/.cache/pip/wheels/*.whl",
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


class RubyGems(GRRArtifactBase):
    """
    Ruby Gems (currently linux only).

    Reference URLs: http://guides.rubygems.org
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "%%users.homedir%%/.gem/ruby/**2/*.gemspec",
                    "/var/lib/gems/**2/*.gemspec",
                    "/usr/share/rubygems-integration/**2/*.gemspec",
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


class PythonModuleInfo(GRRArtifactBase):
    """
    Python module installation information.
    """

    SOURCES = [
        {
            "type": "ARTIFACT_GROUP",
            "attributes": {
                "names": ["PythonDistInfo", "PythonEggInfo", "PythonWheelInfo"]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {
        "PythonDistInfo": PythonDistInfo,
        "PythonWheelInfo": PythonWheelInfo,
        "PythonEggInfo": PythonEggInfo,
    }

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = []
    aliases: ClassVar[Optional[list[str]]] = None
