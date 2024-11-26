"""
The base definitions for the GRR artifacts.
"""

from enum import Enum
from pathlib import Path
from typing import Any, ClassVar, Literal, Optional, Type

from pydantic import BaseModel, Field
from typing_extensions import Annotated

from fastlabel.uco.core import UcoObject


class ArtifactSupportedOS(str, Enum):
    ANDROID = "Android"
    DARWIN = "Darwin"
    IOS = "iOS"
    LINUX = "Linux"
    WINDOWS = "Windows"
    ESXI = "ESXi"


class ArtifactGroupAttributes(BaseModel):
    names: list[str]


class ArtifactGroupSource(BaseModel):
    type: Literal["ARTIFACT_GROUP"]
    attributes: ArtifactGroupAttributes
    supported_os: Optional[list[ArtifactSupportedOS]] = None

    def resolve_artifact_group(self, dependency_mapping: dict[str, str]) -> None:
        """
        Resolve the artifact group to its absolute import path.

        For example, if the artifact group is `["WindowsUserRegistryFiles"]`, then
        this this becomes `["windows.WindowsUserRegistryFiles"]`.
        """
        for i, name in enumerate(self.attributes.names):
            try:
                self.attributes.names[i] = dependency_mapping[name]
            except KeyError:
                raise ValueError(f"No library path could be found for {name}")


class CommandAttributes(BaseModel):
    args: list[str]
    cmd: str


class CommandSource(BaseModel):
    type: Literal["COMMAND"]
    attributes: CommandAttributes
    supported_os: Optional[list[ArtifactSupportedOS]] = None


class FileAttributes(BaseModel):
    paths: list[Path]
    separator: Optional[str] = None


class FileSource(BaseModel):
    type: Literal["FILE"]
    attributes: FileAttributes
    supported_os: Optional[list[ArtifactSupportedOS]] = None


class PathAttributes(BaseModel):
    paths: list[Path]
    separator: Optional[str] = None


class PathSource(BaseModel):
    type: Literal["PATH"]
    attributes: PathAttributes
    supported_os: Optional[list[ArtifactSupportedOS]] = None


class RegistryKeyAttributes(BaseModel):
    keys: list[str]


class RegistryKeySource(BaseModel):
    type: Literal["REGISTRY_KEY"]
    attributes: RegistryKeyAttributes
    supported_os: Optional[list[ArtifactSupportedOS]] = None


class RegistryKeyValuePair(BaseModel):
    key: str
    value: str


class RegistryValueAttributes(BaseModel):
    key_value_pairs: list[RegistryKeyValuePair]


class RegistryValueSource(BaseModel):
    type: Literal["REGISTRY_VALUE"]
    attributes: RegistryValueAttributes
    supported_os: Optional[list[ArtifactSupportedOS]] = None


class WMIAttributes(BaseModel):
    base_object: Optional[str] = None
    query: str


class WMISource(BaseModel):
    type: Literal["WMI"]
    attributes: WMIAttributes
    supported_os: Optional[list[ArtifactSupportedOS]] = None


# See https://stackoverflow.com/questions/70914419/how-to-get-pydantic-to-discriminate-on-a-field-within-listuniontypea-typeb

ArtifactSource = Annotated[
    ArtifactGroupSource
    | CommandSource
    | FileSource
    | PathSource
    | RegistryKeySource
    | RegistryValueSource
    | WMISource,
    Field(discriminator="type"),
]


class TemporarySourceContainer(BaseModel):
    sources: list[ArtifactSource]


def generate_sources(sources: list[dict[str, Any]]) -> list[ArtifactSource]:
    """
    Deserialize the sources from the class definition.

    References:
    - https://github.com/pydantic/pydantic/discussions/7367
    """

    # this is really hacky but oh well lol
    return TemporarySourceContainer.model_validate({"sources": sources}).sources


class GRRArtifactBase(BaseModel):
    """
    The base GRR artifact definition.
    """

    # The sources, as a serializable Python list of dictionaries
    SOURCES: ClassVar[list[dict[str, Any]]] = []
    # If this contains artifact groups, mappings of strings to their actual type
    # (so it doesn't have to resolved at runtime)
    ARTIFACT_MAP: ClassVar[dict[str, Type["GRRArtifactBase"]]] = {}

    # The serialized sources
    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)
    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = None

    aliases: ClassVar[Optional[list[str]]] = None

    # artifact-specific fields should follow (and should not be classvars)

    @classmethod
    def process_artifact(self, path: Path) -> "GRRArtifactBase":
        """
        Process a provided artifact and assign fields.

        TODO: how we gonna do this lmao
        """
        raise NotImplementedError

    def create_case_artifacts(self) -> UcoObject:
        """
        Generate the corresponding CASE entries from this artifact.
        """
        raise NotImplementedError
