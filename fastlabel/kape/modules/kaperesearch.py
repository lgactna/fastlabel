"""
Auto-generated classes from the .mkape files for the KapeResearch category.

This file was generated using the `generate_kape.py` script.
"""

from typing import ClassVar

from fastlabel.kape.core import KapeExportFormat, KapeModule


class KapeResearchRegistryJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.2

    ID: b99570f0-2fce-499d-b13a-d20cbb962f25

    RECmd: Convert Registry hives to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
        KapeExportFormat.NONE,
    ]


class KapeResearchEventLogsXML(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 09b93d8e-c417-4e79-aaef-a2af3f46fd08

    EvtxECmd: Convert Windows Event Log files (.evtx) to XML for research
    """

    name: ClassVar[str] = "KapeResearch_EventLogs_XML"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.XML]


class KapeResearchRegistryAmcacheJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: b8e15fde-3af7-40ce-86da-b71fb95b3e14

    RECmd: Convert Amcache.hve Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_Amcache_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistryBBIJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 00e73e06-c934-4e91-9e4c-37d86ce71d96

    RECmd: Convert BBI Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_BBI_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistryBCDTemplateJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: b55c36c8-7214-433c-90c6-168b425b3400

    RECmd: Convert BCD-Template Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_BCD-Template_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistryCOMPONENTSJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 077e505c-192f-4142-a9e1-b359949f8e6d

    RECmd: Convert COMPONENTS Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_COMPONENTS_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistryDEFAULTJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 380721d4-b47b-4654-8306-5bfda686b2e2

    RECmd: Convert DEFAULT Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_DEFAULT_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistryDRIVERSJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: c9522956-71e2-44fd-8384-01513a34ffbd

    RECmd: Convert DRIVERS Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_DRIVERS_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistryELAMJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 27f6f114-b5cf-46e0-b344-2998506535d7

    RECmd: Convert ELAM Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_ELAM_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistryNTUSERJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 64903403-bbf0-4bb5-bec0-023753f273d3

    RECmd: Convert NTUSER.dat Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_NTUSER_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistrySAMJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 8bf99655-d244-42dd-bbef-43d089cd1f1a

    RECmd: Convert SAM Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_SAM_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistrySECURITYJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 2ef7dd84-58b7-4d17-a5e8-fd39cda3be4b

    RECmd: Convert SECURITY Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_SECURITY_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistrySOFTWAREJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 89b05524-78a1-428f-8b46-4de445df8716

    RECmd: Convert SOFTWARE Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_SOFTWARE_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistrySysCacheJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: e867ca47-0938-4f10-8aad-3f5aa2240222

    RECmd: Convert SysCache Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_SysCache_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistrySYSTEMJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 97f567c7-4f9e-4136-a488-630838daf37a

    RECmd: Convert SYSTEM Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_SYSTEM_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistryuserdiffJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: a3c22935-eac7-41aa-8e6c-6261ad8d25ac

    RECmd: Convert userdiff Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_userdiff_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistryUsrClassJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 47442088-63d1-4f1d-9c7c-3ef47d100a13

    RECmd: Convert UsrClass.dat Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_UsrClass_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]


class KapeResearchRegistryVSMIDKJSON(KapeModule):
    """
    Author: Andrew Rathbun

    Version: 1.0

    ID: 031191d2-aca8-48b1-82e5-df138f0af6ca

    RECmd: Convert VSMIDK Registry hive to JSON for research
    """

    name: ClassVar[str] = "KapeResearch_Registry_VSMIDK_JSON"
    supported_types: ClassVar[list[KapeExportFormat]] = [KapeExportFormat.JSON]
