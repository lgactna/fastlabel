"""
Test script for KAPE bindings.

You must run this script as an administrator after setting KAPE_PATH. The
simplest option is to start a new command prompt as an administrator and run
`python -m fastlabel.scripts.test_kape` from the root of the fastlabel repo.
"""

from pathlib import Path

import fastlabel.kape.core as core
from fastlabel.kape.modules.programexecution import PECmd
from fastlabel.kape.targets.prefetch import Prefetch

# admin privileges required
KAPE_PATH = Path("C:\\Users\\Kisun\\Downloads\\kape\\kape.exe")


if __name__ == "__main__":
    TARGET_SOURCE = Path("C:\\")
    TARGET_DESTINATION = Path("C:\\Users\\Kisun\\Downloads\\kape_test\\targets")
    MODULE_DESTINATION = Path("C:\\Users\\Kisun\\Downloads\\kape_test\\module_out")

    TARGETS = [Prefetch]
    MODULES = [PECmd]

    # TODO: integrate that one python image mounting library

    # try:
    #     core.run_kape(
    #         kape_path=KAPE_PATH,
    #         targets=TARGETS,
    #         target_json=None,
    #         modules=MODULES,
    #         module_json=None,
    #         target_source=TARGET_SOURCE,
    #         target_destination=TARGET_DESTINATION,
    #         module_destination=MODULE_DESTINATION,
    #     )
    # except core.AdminPrivilegeError as e:
    #     print(e)
    #     exit()

    targets = core.process_kape_results(
        target_destination=TARGET_DESTINATION,
        module_destination=MODULE_DESTINATION,
        target_types=core.get_target_types(TARGETS),
    )

    for target in targets:
        # print(type(target))
        print(target.to_case_objects())
