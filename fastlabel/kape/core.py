"""
Core definitions for the KAPE Python bindings.
"""

import concurrent.futures
import csv
import ctypes
import os
import re
import subprocess
from enum import Enum
from pathlib import Path
from types import ModuleType
from typing import ClassVar, Iterable, Optional, Type, TypeVar

from pydantic import AwareDatetime, BaseModel
from wcmatch import glob

from fastlabel.kape import util 
from fastlabel.uco.core import UcoObject


class KapeExportFormat(str, Enum):
    """
    One of the known available KAPE export formats.
    """

    # The default
    NONE = ""

    # Common, the three provided by the GUI
    CSV = "csv"
    HTML = "html"
    JSON = "json"

    # Uncommon, but exists
    TXT = "txt"
    DMP = "dmp"
    EFU = "efu"
    RAW = "raw"
    SQLITE3 = "sqlite3"
    XML = "xml"
    TSV = "tsv"
    DB = "db"
    LOG = "log"
    XLSX = "xlsx"
    GREPTEXT = "greptext"


T = TypeVar("T", bound="KapeModule")


class KapeModule(BaseModel):
    # The name of the module as it should be called on the KAPE CLI.
    name: ClassVar[str]
    # The supported export formats for this module. Attempting to use a module
    # with an unsupported type should raise an error before calling KAPE.
    supported_types: ClassVar[list[KapeExportFormat]]

    # Module-specific information should follow, as typical Pydantic fields.
    # When implementing `scan_module_destination`, you should assign these
    # field members as applicable.

    @classmethod
    def scan_module_destination(cls: Type[T], module_destination: Path) -> "T":
        """
        Process the module destination outputs into information specific to this
        class.

        This should be the same folder root that was set as KAPE's module
        destination.
        """
        raise NotImplementedError
    
    @staticmethod
    def get_module_dir() -> Path:
        """
        Get an absolute path to the directory where modules are stored.
        """
        return util.get_kape_subdir("modules")
    
    @classmethod
    def get_module_modules(cls, extra_prefix_dirs: Optional[dict[str, str]] = None) -> list[ModuleType]:
        """
        Get a handle to all modules found in /fastlabel/kape/modules.
        
        Here, "modules" refers to Python modules, not KAPE modules.
        """
        prefix_dirs = {"fastlabel.kape.modules.": str(cls.get_module_dir())}
        if extra_prefix_dirs:
            prefix_dirs = prefix_dirs | extra_prefix_dirs
        return util.import_modules_from_dir(prefix_dirs)
    
    @classmethod
    def get_module_classes(cls, extra_prefix_dirs: Optional[dict[str, str]] = None) -> list[Type["KapeModule"]]:
        """
        Get all known subclasses of KapeModule.
        """
        cls.get_module_modules(extra_prefix_dirs)
        return util.get_subclasses_recursive(cls)


class SourceDestPair(BaseModel):
    """
    A simple model for keeping track of source and destination files.
    """

    source: Path
    destination: Path

    def __str__(self) -> str:
        return f"{self.source} -> {self.destination}"


R = TypeVar("R", bound="KapeTarget")


# The class name needs to be converted to a valid Python identifier, if needed;
# some use hyphens and other weird symbols
class KapeTarget(BaseModel):

    # The name of the module as it should be called on the KAPE CLI.
    name: ClassVar[str]

    # The base path for the target. May be a valid path or a pattern to be converted.
    base_path: ClassVar[Path]
    # The file mask for this target.
    file_mask: ClassVar[str]
    # If `True`, search in all directories underneath base_path. From our side,
    # that just means updating our regex to support any number of directories
    # between the base path and the file regex above.
    recursive: ClassVar[bool]

    # A list of modules that are associated with this target, and can be used
    # to assign specific data to this target. These must be manually assigned
    # after automatic generation, since they are not directly defined in the KAPE
    # files.
    associated_modules: ClassVar[list[Type[KapeModule]]]

    # A set of instance variables specific to this target; broadly, artifact-specific
    # variables that we care about converting to CASE. These are Pydantic fields,
    # and MUST have default values defined.

    # All KapeTarget instances have a mapping of source to destination files.
    files: list[SourceDestPair] = []

    @classmethod
    def run_modules_on_module_dest(cls: Type[R], module_destination: Path) -> R:
        """
        Process all files in the provided module destination path with its associated
        modules, then return the new instance with attributes assigned.
        """
        raise NotImplementedError

    def to_case_objects(self) -> list[UcoObject]:
        """
        Convert all relevant information from this artifact to a set of valid
        CASE objects.
        """
        raise NotImplementedError

    @classmethod 
    def get_match_str(cls) -> str:
        """
        Get the string that will be used to match the base path.
        
        The following assumptions are used:
        - If the target is recursive, a ** wildcard is appended to the end of 
          the path
        - The drive letter is completely ignored for both the match and the path
        - All variables, enclosed in %, are replaced with a wildcard
        """
        match_str = str(cls.base_path).replace("\\", "/")
        
        # Always end in terminating slash
        if not match_str.endswith("/"):
            match_str += "/"
        
        # If recursive, tack on ** (or /**)
        if cls.recursive:
            match_str += "**/"
        
        # Ignore the drive letter
        match_str = re.sub(r"[A-Za-z]:/", "", match_str)
        
        # Replace all variables in the match string with a wildcard
        match_str = re.sub(r"%[^%]+%", "*", match_str)
        
        # Tack on the file mask
        return match_str + cls.file_mask

    @classmethod
    def path_matches(cls, path: Path) -> bool:
        """
        Determine if the provided path *could* match this target.
        
        This uses wcmatch, which has more powerful glob matching:
        https://stackoverflow.com/questions/66948794/how-to-match-python-paths-against-recursive-glob-patterns
        """        
        # wcmatch normalizes forward slashes, so it's safe to use them here
        path_str = str(path).replace("\\", "/")
        match_str = cls.get_match_str()
        
        # Ignore the drive letter
        path_str = re.sub(r"[A-Za-z]:/", "", path_str)

        # print(f"Matching {path_str} against {match_str}")
        
        return glob.globmatch(path_str, match_str, flags=glob.GLOBSTAR)
        
    

class KapeTargetConfiguration(BaseModel):
    """
    A collection of targets.
    """

    name: ClassVar[str]

    recreate_directories: ClassVar[bool]
    targets: ClassVar[list[Type[KapeTarget]]]
    
    @staticmethod
    def get_target_dir() -> Path:
        """
        Get an absolute path to the directory where targets are stored.
        """
        return util.get_kape_subdir("targets")
    
    @classmethod
    def get_target_modules(cls, extra_prefix_dirs: Optional[dict[str, str]] = None) -> list[ModuleType]:
        """
        Get a handle to all modules found in /fastlabel/kape/targets.
        
        Here, "modules" refers to Python modules, not KAPE modules.
        """
        prefix_dirs = {"fastlabel.kape.targets.": str(cls.get_target_dir())}
        if extra_prefix_dirs:
            prefix_dirs = prefix_dirs | extra_prefix_dirs
        return util.import_modules_from_dir(prefix_dirs)
    
    @classmethod
    def get_target_classes(cls, extra_prefix_dirs: Optional[dict[str, str]] = None) -> list[Type["KapeTarget"]]:
        """
        Get all known subclasses of KapeTarget.
        """
        cls.get_target_modules(extra_prefix_dirs)
        return util.get_subclasses_recursive(cls)


class KapeTargetLogEntry(BaseModel):
    copied_time: AwareDatetime
    source: Path
    destination: Path
    file_size: int
    sha1: str
    deferred_copy: bool
    created_on: AwareDatetime
    modified_on: AwareDatetime
    last_accessed: AwareDatetime

    # What target this log entry has been assigned to, if any.
    assigned_target: Optional[Type[KapeTarget]] = None

    @classmethod
    def from_csv_line(cls, line: list[str]) -> "KapeTargetLogEntry":
        """
        Parse a single line from a KAPE target log CSV file.
        """
        return cls(
            copied_time=util.ez_to_aware_datetime(line[0]),
            source=Path(line[1]),
            destination=Path(line[2]),
            file_size=int(line[3]),
            sha1=line[4],
            deferred_copy=line[5] == "True",
            created_on=util.ez_to_aware_datetime(line[6]),
            modified_on=util.ez_to_aware_datetime(line[7]),
            last_accessed=util.ez_to_aware_datetime(line[8]),
        )


def is_admin() -> bool:
    """
    https://stackoverflow.com/questions/130763/request-uac-elevation-from-within-a-python-script
    """
    if os.name != "nt":
        raise RuntimeError("This function is only implemented for Windows.")

    try:
        return ctypes.windll.shell32.IsUserAnAdmin()  # type: ignore[attr-defined, no-any-return]
    except Exception:
        return False


class AdminPrivilegeError(RuntimeError):
    pass


def get_target_types(
    target_configs: Iterable[Type[KapeTargetConfiguration]],
) -> list[Type[KapeTarget]]:
    """
    Flatten the set of available target types.
    """
    target_types: list[Type[KapeTarget]] = []
    for target_config in target_configs:
        target_types += target_config.targets
    return target_types


def run_kape(
    kape_path: Path,
    targets: Optional[list[Type[KapeTargetConfiguration]]] = None,
    target_json: Optional[Path] = None,
    modules: Optional[list[Type[KapeModule]]] = None,
    module_json: Optional[Path] = None,
    *,
    target_source: Path,
    target_destination: Path,
    module_source: Optional[Path] = None,
    module_destination: Path,
    target_flush: bool = True,
    module_flush: bool = True,
    export_format: KapeExportFormat = KapeExportFormat.NONE,
    target_variables: Optional[dict[str, str]] = None,
    module_variables: Optional[dict[str, str]] = None,
    deduplicate: bool = True,
) -> tuple[bytes, bytes]:
    """
    Run KAPE with the provided targets and modules, then process the resulting
    outputs. Generate a set of targets and modules associated with the result.

    This function will raise AdminPrivilegeError (a subclass of RuntimeError) if
    run without administrator privileges. This function also indirectly raises
    RuntimeError if run on a non-Windows system.

    :param kape_path: The path to the KAPE CLI.
    :param target: A list of targets to pass to KAPE. If empty, targets are disabled.
    :param target_json: Where to dump the generated KapeTarget instances to.
    :param modules: A list of modules to pass to KAPE.
    :param module_json: Where to dump the generated KapeModule instances to.

    :param target_source: The root at which KAPE should begin searching for target files.
    :param target_destination: The root to which KAPE copies target files.
    :param module_source: The root at which KAPE should begin searching for copied target files.
    :param module_destination: The root to which KAPE generates module outputs.
    :param target_flush: Destroy the contents of the target destination before running KAPE.
    :param module_flush: Destroy the contents of the module destination before running KAPE.
    :param export_format: The export type to use.
    :param target_variables: Any variables to pass to the target system.
    :param module_variables: Any variables to pass to the module system.
    :param deduplicate: Indicates KAPE should deduplicate files based on SHA256.
    """
    if not is_admin():
        raise AdminPrivilegeError(
            "KAPE will not run without administrator privileges. Rerun this script as an administrator."
        )

    args: list[str] = []

    # Add the binary itself
    args += [str(kape_path.resolve())]

    # tsource, tdest must be defined simultaneously if set
    if targets:
        if bool(target_source) ^ bool(target_destination):
            raise ValueError("You must define both target source and destination.")
        args += ["--tsource", str(target_source.resolve())]
        args += ["--tdest", str(target_destination.resolve())]

        if target_flush:
            args += ["--tflush"]

        target_names = [target.name for target in targets]
        args += ["--target", ",".join(target_names)]

        if target_variables:
            args += [
                "--tvars",
                "^".join([f"{k}:{v}" for k, v in target_variables.items()]),
            ]

    if modules:
        if bool(module_source) ^ bool(module_destination):
            # If the target destination is set, then it's fine if the module source
            # is not set
            if (not target_destination) and (not module_destination):
                raise ValueError(
                    "target_destination/module_source and module_destination must be set"
                )

        if module_source:
            args += ["--msource", str(module_source.resolve())]
        args += ["--mdest", str(module_destination.resolve())]

        if module_flush:
            args += ["--mflush"]

        module_names = [module.name for module in modules]
        args += ["--module", ",".join(module_names)]

        if module_variables:
            args += [
                "--mvars",
                "^".join([f"{k}:{v}" for k, v in module_variables.items()]),
            ]

    if not deduplicate:
        args += ["--tdd", "false"]

    if export_format != KapeExportFormat.NONE:
        # Check that the declared export format is compatible with all provided
        # modules
        if modules:
            for module in modules:
                if export_format not in module.supported_types:
                    raise ValueError(
                        f"Export format {export_format} is not supported by module {module.name}"
                    )

        args += ["--mef", export_format.value]

    print(f"Running command: {' '.join(args)}")
    s = subprocess.run(args, capture_output=True, check=True)

    return (s.stdout, s.stderr)

def match_entry(entry: KapeTargetLogEntry, target_types: list[Type[KapeTarget]]) -> Optional[Type[KapeTarget]]:
    for target_type in target_types:
        if target_type.path_matches(entry.source):
            # print(f"Matched {entry.source} to {target_type.name} ({target_type.get_match_str()})")
            return target_type
    return None

def process_kape_results(
    target_destination: Path,
    target_types: list[Type[KapeTarget]],
    module_destination: Optional[Path] = None,
    *,
    workers: Optional[int] = None
) -> list[KapeTarget]:
    """
    Process all files in the provided target destination using the logfile, giving
    you a list of KapeTarget instances tied to the files they came from.

    Note that targets are matched in the order they are passed in `targets`. If
    multiple targets *could* match a file, the first match by its regex wins.

    If `module_destination` is set, then any modules associated with matched
    targets will be scanned in the module destination folder. That is, it is
    assumed that any associated modules for each target type has already run.
    The information from gathering module output will be added to the target.
    If it is not set, the target will be returned without any target-specific
    information attached (that would have been generated by module-specific
    information).
    """
    # Search for a file of the format *_CopyLog.csv
    try:
        copy_log = next(target_destination.glob("*_CopyLog.csv"))
    except StopIteration:
        raise RuntimeError(f"No copy log found in target destination {target_destination}")

    # Read the copy log using the csv library
    with open(copy_log, "r") as f:
        reader = csv.reader(f)
        # Skip the header
        next(reader)
        # Read the rest of the lines
        target_log_entries = [KapeTargetLogEntry.from_csv_line(line) for line in reader]

    # For each target entry we have, test it against each available target type
    # and assign if it matches. First target type that matches wins.
    matched_types: set[Type[KapeTarget]] = set()
    future_to_entry: dict[concurrent.futures.Future, KapeTargetLogEntry] = {}
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=None) as executor:
        future_to_entry = {executor.submit(match_entry, entry, target_types): entry for entry in target_log_entries}
        for future in concurrent.futures.as_completed(future_to_entry):
            target_type = future.result()
            entry = future_to_entry[future]
            if target_type:
                matched_types.add(target_type)
                entry.assigned_target = target_type
            else:
                print(f"No target type matched {entry.source} - skipping")

    # Now, generate target instances from anything that matched
    targets = []
    for target_type in matched_types:
        target: KapeTarget = target_type()
        if module_destination:
            try:
                target = target_type.run_modules_on_module_dest(module_destination)
            except NotImplementedError:
                pass

        # Assign the source and destination files to the target instance
        target.files = [
            SourceDestPair(source=entry.source, destination=entry.destination)
            for entry in target_log_entries
            if entry.assigned_target == target_type
        ]
        targets.append(target)

    return targets
