"""
Generate models from the GRR library.

Models and validation is based on the format specified at
https://artifacts.readthedocs.io/en/latest/sources/Format-specification.html.

This effectively replaces ArtifactDefinition from the official artifacts library,
but uses Pydantic for easier (de)serialization.
"""

from graphlib import TopologicalSorter
from pathlib import Path
from textwrap import dedent
from typing import Iterable, Optional

from pydantic import BaseModel
from ruamel.yaml import YAML

from fastlabel.grr._base import ArtifactGroupSource, ArtifactSource, ArtifactSupportedOS
from fastlabel.scripts._util import generate_docstring

# Absolute path to the GRR library
LIBRARY_PATH = "fastlabel.grr"


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

    # The library this is contained in.
    namespace: Optional[str] = None

    # Deprecated fields. All optional, generally not used.
    conditions: Optional[list[str]] = None
    labels: Optional[list[str]] = None
    provides: Optional[list[str]] = None

    def get_required_artifacts(self) -> set[str]:
        """
        Get all required artifacts for this artifact definition.
        """
        result = set()
        for source in self.sources:
            if isinstance(source, ArtifactGroupSource):
                result.update(source.attributes.names)

        return result

    def get_required_imports(self, dependency_mapping: dict[str, str]) -> set[str]:
        """
        Get all required imports for this artifact definition.

        `dependency_mapping` is a mapping of artifact names to their containing
        library under `fastlabel.grr`.

        Returns a set of libraries; for example, if `fastlabel.grr.antivirus` and
        `fastlabel.grr.applications` should be imported, then this returns
        `{"applications", "antivirus"}`.
        """
        result = set()
        for artifact in self.get_required_artifacts():
            result.add(dependency_mapping[artifact])

        # Remove self from dependencies, if it exists
        if self.namespace:
            result.discard(self.namespace)

        return result

    def resolve_artifact_groups(self, dependency_mapping: dict[str, str]) -> None:
        """
        Convert artifacts in artifact groups to absolute import paths. Returns
        a copy with these artifacts resolved.

        For example, an artifact group with WindowsUserRegistryFiles will instead
        be dumped out as `windows.WindowsUserRegistryFiles`.
        """
        for source in self.sources:
            if isinstance(source, ArtifactGroupSource):
                source.resolve_artifact_group(dependency_mapping)

    def generate_artifact_map(
        self, dependency_mapping: dict[str, str]
    ) -> dict[str, str]:
        """
        Generates the artifact map for this artifact definition. For example, if
        this depends on WindowsUserRegistryFiles, then this returns
        `{"WindowsUserRegistryFiles": "windows.WindowsUserRegistryFiles"}.
        """
        result = {}
        for artifact_name in self.get_required_artifacts():
            # If the artifact is local to our namespace, it doesn't need to be
            # absolute
            library = dependency_mapping[artifact_name]

            if library == self.namespace:
                result[artifact_name] = artifact_name
            else:
                result[artifact_name] = f"{library}.{artifact_name}"

        return result

    def to_pydantic_model(self, dependency_mapping: dict[str, str]) -> str:
        """
        Generate a Pydantic model from this artifact definition.

        Note that artifact groups, which declaree a list of artifacts,
        do not specify a namespace or libary to expect each artifact type in;
        instead, it is assumed to all be available in a single namespace.

        To account for this, we must know which module each artifact is in.
        This should be handled externally; that is, every artifact should be
        parsed, their final module path known, and then a list of absolute
        import paths can be done.

        :param dependency_mapping: A mapping of artifact names to their import path
            (e.g. `{"ApacheAccessLogs": "triage"}`)
        """
        output = ""

        # Generate header
        output += f"class {self.name}(GRRArtifactBase):\n"
        docstring = self.doc
        # If there are any URLs, attach them to the docstring
        if self.urls:
            docstring += "\n\n"
            docstring += "Reference URLs:\n"
            for url in self.urls:
                docstring += f"{url}\n"

        output += generate_docstring(docstring)

        # Get source list (equivalent to the "sources" list in the original YAML)
        sources_text = artifact.model_dump(
            mode="json", include={"sources"}, exclude_none=True
        )["sources"]
        output += f"    SOURCES = {sources_text}\n"

        # Generate mappings for any dependencies, allows for direct imports
        # without needing to resolve them at runtime
        artifact_map = self.generate_artifact_map(dependency_mapping)
        artifact_map_items = ",".join([f'"{k}": {v}' for k, v in artifact_map.items()])
        output += f"    ARTIFACT_MAP: ClassVar[dict[str, Type[GRRArtifactBase]]] = {{{artifact_map_items}}}\n\n"

        # Generate class vars
        output += (
            "    sources: ClassVar[list[ArtifactSource]] = generate_sources(SOURCES)\n"
        )

        # Convert supported OS to enum entities
        supported_os = []
        if self.supported_os:
            supported_os = [
                f"ArtifactSupportedOS.{os.name}" for os in self.supported_os
            ]
        output += f"    supported_os: ClassVar[Optional[list[ArtifactSupportedOS]]] = [{','.join(supported_os)}]\n"
        output += f"    aliases: ClassVar[Optional[list[str]]] = {self.aliases}\n"

        # TODO: Generate class variables

        return output + "\n"


def get_artifacts_dir() -> Path:
    """
    Get a resolved path to `/artifacts/grr`.
    """
    # Go up three directories from this source file
    return (Path(__file__).parents[2] / "artifacts" / "grr").resolve()


def get_target_dir() -> Path:
    """
    Get a resolved path to "/fastlabel/grr".
    """
    return (Path(__file__).parents[1] / "grr").resolve()


def generate_classes_from_yaml(artifact_file: Path) -> list[ArtifactDefinition]:
    """
    Generate a list of ArtifactDefinition objects from a YAML file.

    All GRR artifact files are multi-document YAML files.

    Returns a list of ArtifactDefinition objects.
    """
    artifacts = []
    with open(artifact_file, "rt") as fp:
        yaml = YAML(typ="safe")
        for doc in yaml.load_all(fp):
            try:
                artifact = ArtifactDefinition.model_validate(doc)
                artifact.namespace = artifact_file.stem
                artifacts.append(artifact)
            except Exception as e:
                print(f"Error validating {doc}")
                raise e
    return artifacts


def generate_import_list(libraries: Iterable[str]) -> str:
    """
    Generate a list of import statements for the given libraries.
    """
    output = ""

    output += "from typing import ClassVar, Optional, Type\n"
    output += f"from {LIBRARY_PATH}._base import ArtifactSource, ArtifactSupportedOS, GRRArtifactBase, generate_sources\n"

    # Remaining imports
    if libraries:
        output += f"from {LIBRARY_PATH} import ({', '.join(libraries)})\n"

    return output + "\n"


if __name__ == "__main__":
    # Map an artifact name to its actual definition.
    name_mapping: dict[str, ArtifactDefinition] = {}
    # Maps artifact names to their containing module path. Note that we don't do
    # any import validation (e.g. a topological sort).
    dependency_mapping: dict[str, str] = {}
    # Maps module paths to a list of artifacts, allowing them to be grouped
    # as a single file
    module_groups: dict[str, list[ArtifactDefinition]] = {}

    for artifact_file in get_artifacts_dir().glob("*.yaml"):
        print(f"Parsing {artifact_file}")

        artifacts = generate_classes_from_yaml(artifact_file)

        # The module name, relative to `fastlabel.grr`
        module_name = artifact_file.stem

        module_groups[module_name] = artifacts
        for artifact in artifacts:
            dependency_mapping[artifact.name] = module_name
            name_mapping[artifact.name] = artifact

    # Generate the Pydantic models for each module group
    for group_name, members in module_groups.items():
        target_file = get_target_dir() / f"{group_name}.py"
        print(
            f"Generating models for {group_name} -> {target_file.relative_to(get_target_dir())}"
        )

        docstring = dedent(
            f'''
            """
            Auto-generated classes from the YAML declarations in {group_name}.yaml.
            
            This file was generated using the `generate_grr.py` script.
            """
            '''  # noqa: W293
        )

        # Collect dependencies
        dependencies = set()
        for artifact in members:
            dependencies.update(artifact.get_required_imports(dependency_mapping))
        imports = generate_import_list(dependencies)

        # Enforce ordering + import order
        dep_graph = {
            artifact.name: artifact.get_required_artifacts() for artifact in members
        }
        dep_graph = {k: dep_graph[k] for k in sorted(dep_graph)}

        class_order = tuple(TopologicalSorter(dep_graph).static_order())
        class_defs = ""
        for class_name in class_order:
            artifact = name_mapping[class_name]

            # TopologicalSorter includes items that aren't keys of the original
            # graph, but are values. We don't want to include these.
            if artifact not in members:
                continue

            class_defs += artifact.to_pydantic_model(dependency_mapping) + "\n"

        class_file = docstring + "\n" + imports + "\n\n" + class_defs

        with open(target_file, "wt") as fp:
            fp.write(class_file)
