"""
Core definitions for the KAPE Python bindings.
"""

import csv
import ctypes
import datetime
from enum import Enum
from pathlib import Path
from typing import ClassVar, Optional, Type
import subprocess

from pydantic import AwareDatetime, BaseModel

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


class KapeModule(BaseModel):
    # The name of the module as it should be called on the KAPE CLI.
    name: ClassVar[str]
    # The supported export formats for this module. Attempting to use a module
    # with an unsupported type should raise an error before calling KAPE.
    # TODO: i don't actually do this yet
    supported_types: ClassVar[list[KapeExportFormat]]

    # Module-specific information should follow, as typical Pydantic fields.
    # When implementing `scan_module_outputs`, you should assign these field members
    # as applicable.

    @classmethod
    def read_module_outputs(cls, module_destination: Path) -> "KapeModule":
        """
        Process the module destination outputs into information specific to this
        class.

        This should be the same folder root that was set as KAPE's module
        destination.
        """
        raise NotImplementedError


# The class name needs to be converted to a valid Python identifier, if needed;
# some use hyphens and other weird symbols
class KapeTarget(BaseModel):
    # The name of the module as it should be called on the KAPE CLI.
    name: ClassVar[str]

    # The base path for the target.
    base_path: ClassVar[Path]
    # The regex to use in each directory to search in, beginning at `base_path`.
    regex: ClassVar[str]
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
    # variables that we care about converting to CASE. These are Pydantic fields.

    # The *original* filepaths of any target files collected.
    # TODO: do we want the copied filepaths as well?
    associated_files: list[Path]

    @classmethod
    def from_target_destination(
        self, target_destination: Path, run_modules: bool = True
    ) -> "KapeTarget":
        """
        Process all files in the provided target destination path with
        the associated modules, then return the resulting updated artifact(s)
        """
        raise NotImplementedError

    def to_case_objects(self) -> list[UcoObject]:
        """
        Convert all relevant information from this artifact to a set of valid
        CASE objects.
        """
        raise NotImplementedError


class KapeTargetConfiguration(BaseModel):
    """
    A collection of targets.
    """

    name: ClassVar[str]

    recreate_directories: ClassVar[bool]
    targets: ClassVar[list[Type[KapeTarget]]]


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
    
    @staticmethod
    def to_aware_datetime(date_str: str) -> datetime:
        # KAPE uses 7 decimal places after the second, but %f is only 6
        # so we need to truncate the last digit
        date_str = date_str[:-1]
        
        return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f").astimezone(datetime.UTC)
    
    @classmethod
    def from_csv_line(cls, line: list[str]) -> "KapeTargetLogEntry":
        """
        Parse a single line from a KAPE target log CSV file.
        """
        return cls(
            copied_time=cls.to_aware_datetime(line[0]),
            source=Path(line[1]),
            destination=Path(line[2]),
            file_size=int(line[3]),
            sha1=line[4],
            deferred_copy=line[5] == "True",
            created_on=cls.to_aware_datetime(line[6]),
            modified_on=cls.to_aware_datetime(line[7]),
            last_accessed=cls.to_aware_datetime(line[8])            
        )

def is_admin():
    """
    https://stackoverflow.com/questions/130763/request-uac-elevation-from-within-a-python-script
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

class AdminPrivilegeError(RuntimeError):
    pass

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
    
    This function will 

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
        raise AdminPrivilegeError("KAPE will not run without administrator privileges. Rerun this script as an administrator.")
    
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
        args += ["--mef", export_format.value]

    print(f"Running command: {' '.join(args)}")
    s = subprocess.run(args, capture_output=True, check=True)

    return (s.stdout, s.stderr)

def process_kape_target_dir(
    target_destination: Path,
    targets: list[Type[KapeTarget]]
)-> list[KapeTarget]:
    """
    Process all files in the provided target destination path with
    the associated modules, then return the resulting updated artifact(s)
    """
    # Search for a file of the format *_CopyLog.csv
    copy_log = next(target_destination.glob("*_CopyLog.csv"))
    
    # Read the copy log using the csv library
    with open(copy_log, "r") as f:
        reader = csv.reader(f)
        # Skip the header
        next(reader)
        # Read the rest of the lines
        target_log_entries = [KapeTargetLogEntry.from_csv_line(line) for line in reader]

    # Now we need to associate the log entries with the targets
    

    print(target_log_entries)