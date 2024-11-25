"""
Generate models from the GRR library.

Models and validation is based on the format specified at
https://artifacts.readthedocs.io/en/latest/sources/Format-specification.html.

This effectively replaces ArtifactDefinition from the official artifacts library,
but uses Pydantic for easier (de)serialization.
"""

from enum import Enum
from pathlib import Path
from typing import Literal, Optional

from pydantic import BaseModel, Field
from ruamel.yaml import YAML
from typing_extensions import Annotated


class ArtifactGroupAttributes(BaseModel):
    names: list[str]


class ArtifactGroupSource(BaseModel):
    type: Literal["ARTIFACT_GROUP"]
    attributes: ArtifactGroupAttributes


class CommandAttributes(BaseModel):
    args: list[str]
    cmd: str


class CommandSource(BaseModel):
    type: Literal["COMMAND"]
    attributes: CommandAttributes


class FileAttributes(BaseModel):
    paths: list[Path]
    separator: Optional[str] = None


class FileSource(BaseModel):
    type: Literal["FILE"]
    attributes: FileAttributes


class PathAttributes(BaseModel):
    paths: list[Path]
    separator: Optional[str] = None


class PathSource(BaseModel):
    type: Literal["PATH"]
    attributes: PathAttributes


class RegistryKeyAttributes(BaseModel):
    keys: list[str]


class RegistryKeySource(BaseModel):
    type: Literal["REGISTRY_KEY"]
    attributes: RegistryKeyAttributes


class RegistryKeyValuePair(BaseModel):
    key: str
    value: str


class RegistryValueAttributes(BaseModel):
    key_value_pairs: list[RegistryKeyValuePair]


class RegistryValueSource(BaseModel):
    type: Literal["REGISTRY_VALUE"]
    attributes: RegistryValueAttributes


class WMIAttributes(BaseModel):
    base_object: Optional[str] = None
    query: str


class WMISource(BaseModel):
    type: Literal["WMI"]
    attributes: WMIAttributes


class ArtifactSupportedOS(str, Enum):
    ANDROID = "Android"
    DARWIN = "Darwin"
    IOS = "iOS"
    LINUX = "Linux"
    WINDOWS = "Windows"
    ESXI = "ESXi"


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

# class ArtifactSource(BaseModel):
#     source: ArtifactGroupSource | CommandSource | FileSource | PathSource | RegistryKeySource | RegistryValueSource | WMISource = Field(discriminator="type")


class ArtifactDefinition(BaseModel):
    """
    Generic definition of a GRR artifact.
    """

    aliases: Optional[list[str]] = None
    doc: str
    name: str
    sources: list[ArtifactSource]
    supported_os: Optional[list[ArtifactSupportedOS]] = None
    urls: Optional[list[str]] = None

    # Deprecated fields. All optional, generally not used.
    conditions: Optional[list[str]] = None
    labels: Optional[list[str]] = None
    provides: Optional[list[str]] = None

    # TODO: turn this into its own model


def get_artifacts_dir() -> Path:
    """
    Get a resolved path to `/grr_artifacts`.
    """
    # Go up three directories from this source file
    return (Path(__file__).parents[2] / "grr_artifacts").resolve()


if __name__ == "__main__":
    # print(list(get_artifacts_dir().glob("*.yaml")))

    # TODO: actually write these in the same manner as generate_case.py

    for artifact_file in get_artifacts_dir().glob("*.yaml"):
        print(f"Validating {artifact_file}")
        with open(artifact_file, "rt") as fp:
            yaml = YAML(typ="safe")
            for d in yaml.load_all(fp):
                try:
                    x = ArtifactDefinition.model_validate(d)
                except Exception as e:
                    print(f"Error validating {d}")
                    raise e

    print("ok")

    # with open("./grr_artifacts/antivirus.yaml", "rt") as fp:
    #     yaml = YAML(typ="safe")
    #     for d in yaml.load_all(fp):
    #         x = ArtifactDefinition.model_validate(d)
