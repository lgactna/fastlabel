"""
Auto-generated classes from the YAML declarations in legacy.yaml.

This file was generated using the `generate_grr.py` script.
"""

from typing import ClassVar, Optional, Type

from fastlabel.grr._base import (
    ArtifactSource,
    ArtifactSupportedOS,
    GRRArtifactBase,
    generate_sources,
)


class AllUsersAppDataEnvironmentVariable(GRRArtifactBase):
    """
    The %ProgramData% environment variable.

    Reference URLs: http://environmentvariables.org/ProgramData
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList",
                        "value": "ProgramData",
                    }
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


class AllUsersProfileEnvironmentVariable(GRRArtifactBase):
    """
    The %AllUsersProfile% environment variable.

    Reference URLs: http://support.microsoft.com/kb//214653
    """

    SOURCES = [
        {
            "type": "REGISTRY_KEY",
            "attributes": {
                "keys": [
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList\\ProfilesDirectory",
                    "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList\\AllUsersProfile",
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


class LinuxRelease(GRRArtifactBase):
    """
    Linux specific distribution information.

    See: lsb_release(1) man page, or the LSB Specification under the 'Command
    Behaviour' section.
    """

    SOURCES = [
        {
            "type": "FILE",
            "attributes": {
                "paths": [
                    "/etc/enterprise-release",
                    "/etc/lsb-release",
                    "/etc/oracle-release",
                    "/etc/redhat-release",
                    "/etc/system-release",
                ]
            },
        }
    ]
    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {}

    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [
        ArtifactSupportedOS.LINUX
    ]
    aliases: ClassVar[Optional[list[str]]] = None


class SystemDriveEnvironmentVariable(GRRArtifactBase):
    """
    The %SystemDrive% environment variable, usually "C:".

    This value isn't actually present in the Registry but with some parsing we
    can figure it out from SystemRoot.

    Reference URLs: http://environmentvariables.org/SystemDrive
    https://msdn.microsoft.com/en-us/library/cc231436.aspx
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion",
                        "value": "SystemRoot",
                    }
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


class WinDomainName(GRRArtifactBase):
    """
    The Windows domain the system is connected to.
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\System\\CurrentControlSet\\Services\\Tcpip\\Parameters",
                        "value": "Domain",
                    }
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


class WindowsEnvironmentVariableAllUsersAppData(GRRArtifactBase):
    """
    The %ProgramData% environment variable.

    Reference URLs: http://environmentvariables.org/ProgramData
    """

    SOURCES = [
        {
            "type": "REGISTRY_VALUE",
            "attributes": {
                "key_value_pairs": [
                    {
                        "key": "HKEY_LOCAL_MACHINE\\Software\\Microsoft\\Windows NT\\CurrentVersion\\ProfileList",
                        "value": "ProgramData",
                    }
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
