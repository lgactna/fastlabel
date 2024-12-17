from pathlib import Path
from typing import Type
from types import ModuleType
import datetime
import importlib
import pkgutil

def get_kape_subdir(folder: Path) -> Path:
    """
    Get a resolved path to `/fastlabel/kape/<folder>`.
    """
    return (Path(__file__).parent / folder).resolve()

def import_modules_from_dir(prefix_dirs: dict[str, str]) -> list[ModuleType]:
    """
    Get a handle to all modules found in the specified directories through
    a recursive import.

    Note that this unit will make *all* imports and classes visible; this *will*
    lead to nasty namespace pollution if you're not careful!

    `prefix_dirs` is a dictionary of prefixes to the corresponding directory where
    that prefix is rooted. A simple example is the following:

    ```python
    {
        "fastlabel.kape.targets": "/fastlabel/kape/targets"
    }
    ```

    which will attempt to import everything under /fastlabel/kape/targets as
    `fastlabel.kape.targets.<module_name>`.

    :param prefix_dirs: Mapping of prefixes to directories as described above.
    :returns: A list of modules discovered and imported.
    """
    modules: list[ModuleType] = []
    for prefix, search_dir in prefix_dirs.items():
        for _importer, name, _ispkg in pkgutil.walk_packages([search_dir], prefix):
            module = importlib.import_module(name)
            modules.append(module)

    return modules

def get_subclasses_recursive(type: Type) -> list[Type]:
    """
    Get all visible subclasses of `type`, recursive.

    From https://stackoverflow.com/questions/3862310
    """
    subclasses = set(type.__subclasses__()).union(
        [s for c in type.__subclasses__() for s in get_subclasses_recursive(c)]
    )

    return list(subclasses)

def ez_to_aware_datetime(date_str: str) -> datetime.datetime:
    """
    Convert an Eric Zimmerman datetime to an aware datetime object, assumed to
    be UTC.
    """

    # KAPE uses 7 decimal places after the second, but %f is only 6
    # so we need to truncate the last digit
    date_str = date_str[:-1]

    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S.%f").astimezone(
            datetime.UTC
        )
    except OSError:
        # Return epoch time if we can't parse the date; usually this is because
        # it exceeds the minimum/maximum representable date
        return datetime.datetime.fromtimestamp(0, datetime.UTC)
