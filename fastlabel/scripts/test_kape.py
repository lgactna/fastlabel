"""
Test script for KAPE bindings.

You must run this script as an administrator after setting KAPE_PATH. The
simplest option is to start a new command prompt as an administrator and run
`python -m fastlabel.scripts.test_kape` from the root of the fastlabel repo.
"""

from pathlib import Path

import fastlabel.kape.core as core
from fastlabel.kape.targets.prefetch import Prefetch

# admin privileges required
KAPE_PATH = Path("C:\\Users\\Kisun\\Downloads\\kape\\kape.exe")


if __name__ == "__main__":
    # try:
    #     core.run_kape(
    #         kape_path=KAPE_PATH,
    #         targets=[Prefetch],
    #         target_json=None,
    #         modules=[PECmd],
    #         module_json=None,
    #         target_source=Path("C:\\"),
    #         target_destination=Path("C:\\Users\\Kisun\\Downloads\\kape_test\\targets"),
    #         module_destination=Path("C:\\Users\\Kisun\\Downloads\\kape_test\\module_out"),
    #     )
    # except core.AdminPrivilegeError as e:
    #     print(e)
    #     exit()

    core.process_kape_target_dir(
        Path("C:\\Users\\Kisun\\Downloads\\kape_test\\targets"),
        target_configs=[Prefetch],
    )
