from pathlib import Path
from types import ModuleType
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