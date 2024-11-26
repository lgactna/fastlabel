import fnmatch
import uuid
from collections import defaultdict
from pathlib import Path
from textwrap import dedent
from typing import Any, Optional

from pydantic import BaseModel
from ruamel.yaml import YAML

from fastlabel.kape.core import KapeExportFormat
from fastlabel.scripts._util import generate_docstring, to_valid_identifier


class KapeTargetDefinition(BaseModel):
    """
    A general KAPE target definition.

    These are the actual targets that KAPE uses. Each one of these represents a
    distinct target class that will be generated. The reasoning behind this is that
    KAPE target configurations may contain a collection of targets that cannot
    reasonably be "combined" into a single class for post-processing.

    A good example is the "Chrome" target configuration, which contains targets
    for bookmarks, cookies, history, and so on. While these are all technically
    related and *could* be represented as a single class, it makes much more sense
    to build individual classes for each target type so that their logic and attributes
    can be more granular.
    """

    # Always required.
    #
    # This is also true of compound targets. Because the actual logic of gathering
    # target files is offloaded to KAPE, we don't perform any resolution
    # for paths that actually refer to other .tkape files.
    name: str
    category: str
    path: str

    recursive: bool = False
    file_mask: str = "*"
    save_as_file_name: Optional[str] = None
    always_add_to_queue: bool = False
    comment: Optional[str] = None
    min_size: Optional[int] = None
    max_size: Optional[int] = None

    @classmethod
    def from_tkape_dict(self, tkape_data: dict[str, Any]) -> "KapeTargetDefinition":
        """
        Convert .tkape YAML keys to a Python-compatible format.
        """
        return KapeTargetDefinition(
            name=tkape_data["Name"],
            category=tkape_data["Category"],
            path=tkape_data["Path"],
            recursive=tkape_data.get("Recursive", False),
            file_mask=tkape_data.get("FileMask", "*"),
            save_as_file_name=tkape_data.get("SaveAsFileName", None),
            always_add_to_queue=tkape_data.get("AlwaysAddToQueue", False),
            comment=tkape_data.get("Comment", None),
            min_size=tkape_data.get("MinSize", None),
            max_size=tkape_data.get("MaxSize", None),
        )

    def to_pydantic_model(self) -> str:
        """
        Generate a Pydantic model for this target.
        """

        output = ""

        # Start with the class definition
        output += f"class {self.get_class_name()}(KapeTarget):\n"
        if self.comment:
            output += generate_docstring(self.comment)

        # Assign common class variables
        output += f'    name: ClassVar[str] = "{self.name}"\n'
        output += f'    base_path: ClassVar[Path] = Path("{self.path}")\n'
        output += f'    regex: ClassVar[str] = r"{fnmatch.translate(self.file_mask)}"\n'
        output += f"    recursive: ClassVar[bool] = {self.recursive}\n"
        output += "    associated_modules: ClassVar[list[Type[KapeModule]]] = []\n\n"

        output += "    # Add any instance variables specific to this target as Pydantic fields here.\n"

        return output

    def get_class_name(self) -> str:
        """
        Get the name of the class that represents this target.
        """
        return to_valid_identifier(self.name, remove_underscores=True)


class KapeTargetConfigurationDefinition(BaseModel):
    """
    Generic definition of a Kape target configuration.

    More precisely, this is the contents of a single .tkape file.
    These are used to automatically generate KAPE target/artifact classes.

    A single "container" class, whose sole attribute is a list of the underlying
    classes generated out of `targets`, is also generated.

    This adheres to the documentation provided at the following link:
    https://ericzimmerman.github.io/KapeDocs/#!Pages\2.1-Targets.md.
    """

    # This is the target name that needs to be used on the Kape CLI, and is simply
    # the stem of the .tkape file.
    name: str

    description: str
    author: str
    version: str
    id: uuid.UUID
    recreate_directories: bool
    targets: list[KapeTargetDefinition]

    @classmethod
    def from_tkape_dict(
        self, tkape_data: dict[str, Any], name: str
    ) -> "KapeTargetConfigurationDefinition":
        """
        Convert .tkape YAML keys to a Python-compatible format.
        """
        return KapeTargetConfigurationDefinition(
            name=name,
            description=tkape_data["Description"],
            author=tkape_data["Author"],
            version=str(tkape_data["Version"]),  # Force interpret as string
            id=uuid.UUID(tkape_data["Id"]),
            recreate_directories=tkape_data.get("RecreateDirectories", False),
            targets=[
                KapeTargetDefinition.from_tkape_dict(target)
                for target in tkape_data["Targets"]
            ],
        )

    @classmethod
    def generate_target_config_from_yaml(
        cls, tkape_file: Path
    ) -> "KapeTargetConfigurationDefinition":
        """
        Generate a KAPE target configuration definition from a .mkape file.
        """
        yaml = YAML()
        with tkape_file.open("r") as f:
            tkape_doc = yaml.load(f)
        return cls.from_tkape_dict(tkape_doc, tkape_file.stem)

    def to_pydantic_model(self) -> str:
        """
        Generate a Pydantic model for this target configuration.

        This simply generates a class for each of the targets in the configuration,
        as well as one "container" class that contains all of the targets.
        """

        output = ""

        # Start with the class definitions of every target
        for target in self.targets:
            output += target.to_pydantic_model()
            output += "\n\n"

        # Then, write the definition for the container class
        output += f"class {to_valid_identifier(self.name, remove_underscores=True)}(KapeTargetConfiguration):\n"

        docstring = f"Author: {self.author}\n\n"
        docstring += f"Version: {self.version}\n\n"
        docstring += f"ID: {self.id}\n\n"
        docstring += self.description
        output += generate_docstring(docstring) + "\n"

        output += f'    name: ClassVar[str] = "{self.name}"\n'
        output += (
            f"    recreate_directories: ClassVar[bool] = {self.recreate_directories}\n"
        )

        target_list = ",".join([x.get_class_name() for x in self.targets])
        output += f"    targets: ClassVar[list[Type[KapeTarget]]] = [{target_list}]\n"

        return output + "\n\n"


class KapeProcessorDefinition(BaseModel):
    """
    General definition of a KAPE processor.

    Exactly one of these processors is chosen by KAPE at runtime based on the
    export format selected.
    """

    executable: str
    command_line: str
    append: Optional[bool] = None
    export_file: Optional[str] = None
    export_format: KapeExportFormat

    @classmethod
    def from_mkape_dict(self, mkape_data: dict[str, Any]) -> "KapeProcessorDefinition":
        """
        Convert .mkape YAML keys to a Python-compatible format.
        """
        return KapeProcessorDefinition(
            executable=mkape_data["Executable"],
            command_line=mkape_data["CommandLine"],
            append=mkape_data.get("Append", None),
            export_file=mkape_data.get("ExportFile", None),
            export_format=KapeExportFormat(mkape_data["ExportFormat"]),
        )


class KapeModuleDefinition(BaseModel):
    """
    General definition of a KAPE module.

    For all intents and purposes, this represents a single, coherent unit that
    processes artifacts of a particular type, based on FileMask. Each processor
    *does not* operate on different files; it only changes the format of the output.

    In turn, a single module definition turns into a single module class. This is
    in contrast to the target definitions, which generate a distinct class for
    each available target in the configuration file.
    """

    # This is the target name that needs to be used on the Kape CLI, and is simply
    # the stem of the .mkape file.
    name: str

    description: str
    category: str
    author: str
    version: str
    id: uuid.UUID
    binary_url: Optional[str] = None
    export_format: KapeExportFormat
    wait_timeout: Optional[int] = None
    file_mask: Optional[str] = None

    processors: list[KapeProcessorDefinition]

    @classmethod
    def from_mkape_dict(
        self, mkape_data: dict[str, Any], name: str
    ) -> "KapeModuleDefinition":
        """
        Convert .mkape YAML keys to a Python-compatible format.
        """
        return KapeModuleDefinition(
            name=name,
            description=mkape_data["Description"],
            category=mkape_data["Category"],
            author=mkape_data["Author"],
            version=str(mkape_data["Version"]),  # Force interpret as string
            id=uuid.UUID(mkape_data["Id"]),
            binary_url=mkape_data.get("BinaryUrl", None),
            export_format=KapeExportFormat(mkape_data["ExportFormat"]),
            wait_timeout=mkape_data.get("WaitTimeout", None),
            file_mask=mkape_data.get("FileMask", None),
            processors=[
                KapeProcessorDefinition.from_mkape_dict(processor)
                for processor in mkape_data["Processors"]
            ],
        )

    @classmethod
    def generate_module_from_yaml(cls, mkape_file: Path) -> "KapeModuleDefinition":
        """
        Generate a KAPE module definition from a .mkape file.
        """
        yaml = YAML()
        with mkape_file.open("r") as f:
            mkape_doc = yaml.load(f)
        return cls.from_mkape_dict(mkape_doc, mkape_file.stem)


def get_artifacts_dir() -> Path:
    """
    Get a resolved path to `/artifacts/kape`.

    You still need to tack on either "Modules" or "Targets" to get your tkape
    and mkape files, respectively.
    """
    # Go up three directories from this source file
    return (Path(__file__).parents[2] / "artifacts" / "kape").resolve()


def get_target_dir() -> Path:
    """
    Get a resolved path to "/fastlabel/kape".

    You still need to tack on either "modules" or "targets".
    """
    return (Path(__file__).parents[1] / "kape").resolve()


def generate_class_file_from_targets(
    targets: list[KapeTargetConfigurationDefinition],
) -> str:
    """
    Generate a Python file containing all of the KAPE target classes.
    """
    output = ""

    # let's just assume it's the same category for all targets
    category = targets[0].targets[0].category
    docstring = dedent(
        f'''
        """
        Auto-generated classes from the .tkape files for the {category} category.
        
        This file was generated using the `generate_kape.py` script.
        """
        '''  # noqa: W293
    )
    output += docstring + "\n\n"

    # Imports are static, it's up to the user to add any extras as needed
    output += "from pathlib import Path\n"
    output += "from typing import ClassVar, Type\n\n"
    output += "from fastlabel.kape.core import KapeTarget\n\n"

    # Generate the target classes
    for target in targets:
        output += target.to_pydantic_model()
        output += "\n\n"

    return output


if __name__ == "__main__":
    # Start by processing all of the .tkape files we have
    tkape_root = get_artifacts_dir() / "targets"

    # Recursively search for all .tkape files under the targets directory
    target_configs: list[KapeTargetConfigurationDefinition] = []
    for tkape_file in tkape_root.glob("**/*.tkape"):
        print(f"Processing {tkape_file.relative_to(get_artifacts_dir())}")
        target_config = (
            KapeTargetConfigurationDefinition.generate_target_config_from_yaml(
                tkape_file
            )
        )
        target_configs.append(target_config)

    # Group each target config by category name
    target_groups = defaultdict(list)
    for target in target_configs:
        target_groups[target.targets[0].category].append(target)

    # Write each category to a separate file
    for _category, targets in target_groups.items():
        output = generate_class_file_from_targets(targets)
        print(output)
        # with get_target_dir() / "targets" / f"{to_valid_identifier(category)}.py" as f:
        #     f.write(output)

    # # Next, process all of the .mkape files we have
    # mkape_root = get_artifacts_dir() / "modules"

    # # Recursively search for all .mkape files under the modules directory
    # for mkape_file in mkape_root.glob("**/*.mkape"):
    #     print(f"Processing {mkape_file.relative_to(get_artifacts_dir())}")
    #     module = KapeModuleDefinition.generate_module_from_yaml(mkape_file)
