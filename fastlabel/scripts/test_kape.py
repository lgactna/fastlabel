"""
Test script for KAPE bindings.

You must run this script as an administrator after setting KAPE_PATH. The
simplest option is to start a new command prompt as an administrator and run
`python -m fastlabel.scripts.test_kape` from the root of the fastlabel repo.
"""

import datetime
import json
from pathlib import Path

import fastlabel.kape.core as core
import fastlabel.uco as uco
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

    bundle_identity = uco.identity.Identity()
    bundle_identity_name = uco.identity.SimpleNameFacet(givenName="fastlabel")
    bundle_identity.hasFacet.append(bundle_identity_name)

    bundle_created_time = datetime.datetime.now(datetime.UTC)

    bundle = uco.core.Bundle(
        createdBy=[bundle_identity.ref()],
        name="fastlabel demo",
        description="Auto-generated demonstration bundle",
        objectCreatedTime=bundle_created_time,
        modifiedTime=bundle_created_time,
        specVersion="UCO/CASE 2.0",
    )
    bundle.object.append(bundle_identity)
    for target in targets:
        bundle.object.extend(target.to_case_objects())

    with open("fastlabel.jsonld", "wt+") as f:
        # model_dump_json doesn't work because XMLSchema doesn't have any JSOON
        # serializers provided - this is fine, though not great
        data = bundle.model_dump(serialize_as_any=True)
        f.write(json.dumps(data, indent=2))
