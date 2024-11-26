"""
Auto-generated classes from the .tkape files for the Registry category.

This file was generated using the `generate_kape.py` script.
"""

from pathlib import Path
from typing import ClassVar, Type

from fastlabel.kape.core import KapeModule, KapeTarget, KapeTargetConfiguration


class RegistryHivesSystemRegistryFiles0(KapeTarget):
    name: ClassVar[str] = "System Registry Files"
    base_path: ClassVar[Path] = Path("RegistryHivesSystem.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesUserLevelRegistryFiles1(KapeTarget):
    name: ClassVar[str] = "User Level Registry Files"
    base_path: ClassVar[Path] = Path("RegistryHivesUser.tkape")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHives(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman

    Version: 1.1

    ID: 76af6086-bd0b-429f-bfd7-4a8e8ff8138f

    System and user related Registry hives
    """

    name: ClassVar[str] = "RegistryHives"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RegistryHivesSystemRegistryFiles0,
        RegistryHivesUserLevelRegistryFiles1,
    ]


class BCDBCD0(KapeTarget):
    name: ClassVar[str] = "BCD"
    base_path: ClassVar[Path] = Path("C:\\Boot\\")
    regex: ClassVar[str] = r"(?s:BCD)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BCDBCDLogs1(KapeTarget):
    name: ClassVar[str] = "BCD Logs"
    base_path: ClassVar[Path] = Path("C:\\Boot\\")
    regex: ClassVar[str] = r"(?s:BCD\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class BCD(KapeTargetConfiguration):
    """
    Author: Troy Larson

    Version: 1.0

    ID: eedec61a-bae4-4e96-a2cd-b6b30aa5a786

    Boot Configuration Files
    """

    name: ClassVar[str] = "BCD"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [BCDBCD0, BCDBCDLogs1]


class RegistryHivesOtherBBIregistryhive0(KapeTarget):
    name: ClassVar[str] = "BBI registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:BBI)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherBBIregistryhive1(KapeTarget):
    name: ClassVar[str] = "BBI registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:BBI)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherBBIregistrytransactionfiles2(KapeTarget):
    name: ClassVar[str] = "BBI registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:BBI\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherBBIregistrytransactionfiles3(KapeTarget):
    name: ClassVar[str] = "BBI registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:BBI\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherBCDTemplateregistryhive4(KapeTarget):
    name: ClassVar[str] = "BCD-Template registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:BCD\-Template)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherBCDTemplateregistryhive5(KapeTarget):
    name: ClassVar[str] = "BCD-Template registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:BCD\-Template)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherBCDTemplateregistrytransactionfiles6(KapeTarget):
    name: ClassVar[str] = "BCD-Template registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:BCD\-Template\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherBCDTemplateregistrytransactionfiles7(KapeTarget):
    name: ClassVar[str] = "BCD-Template registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:BCD\-Template\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherCOMPONENTSregistryhive8(KapeTarget):
    name: ClassVar[str] = "COMPONENTS registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:COMPONENTS)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherCOMPONENTSregistryhive9(KapeTarget):
    name: ClassVar[str] = "COMPONENTS registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:COMPONENTS)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherCOMPONENTSregistrytransactionfiles10(KapeTarget):
    name: ClassVar[str] = "COMPONENTS registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:COMPONENTS\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherCOMPONENTSregistrytransactionfiles11(KapeTarget):
    name: ClassVar[str] = "COMPONENTS registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:COMPONENTS\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherDRIVERSregistryhive12(KapeTarget):
    name: ClassVar[str] = "DRIVERS registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:DRIVERS)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherDRIVERSregistryhive13(KapeTarget):
    name: ClassVar[str] = "DRIVERS registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:DRIVERS)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherDRIVERSregistrytransactionfiles14(KapeTarget):
    name: ClassVar[str] = "DRIVERS registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:DRIVERS\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherDRIVERSregistrytransactionfiles15(KapeTarget):
    name: ClassVar[str] = "DRIVERS registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:DRIVERS\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherELAMregistryhive16(KapeTarget):
    name: ClassVar[str] = "ELAM registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:ELAM)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherELAMregistryhive17(KapeTarget):
    name: ClassVar[str] = "ELAM registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:ELAM)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherELAMregistrytransactionfiles18(KapeTarget):
    name: ClassVar[str] = "ELAM registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:ELAM\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherELAMregistrytransactionfiles19(KapeTarget):
    name: ClassVar[str] = "ELAM registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:ELAM\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtheruserdiffregistryhive20(KapeTarget):
    name: ClassVar[str] = "userdiff registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:userdiff)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtheruserdiffregistryhive21(KapeTarget):
    name: ClassVar[str] = "userdiff registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:userdiff)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtheruserdiffregistrytransactionfiles22(KapeTarget):
    name: ClassVar[str] = "userdiff registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:userdiff\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtheruserdiffregistrytransactionfiles23(KapeTarget):
    name: ClassVar[str] = "userdiff registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:userdiff\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherVSMIDKregistryhive24(KapeTarget):
    name: ClassVar[str] = "VSMIDK registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:VSMIDK)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherVSMIDKregistryhive25(KapeTarget):
    name: ClassVar[str] = "VSMIDK registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:VSMIDK)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherVSMIDKregistrytransactionfiles26(KapeTarget):
    name: ClassVar[str] = "VSMIDK registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:VSMIDK\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOtherVSMIDKregistrytransactionfiles27(KapeTarget):
    name: ClassVar[str] = "VSMIDK registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:VSMIDK\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesOther(KapeTargetConfiguration):
    """
    Author: Andrew Rathbun

    Version: 1.1

    ID: ea765ae7-b932-41a3-bd84-41fcdf236754

    Other Registry Hives
    """

    name: ClassVar[str] = "RegistryHivesOther"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RegistryHivesOtherBBIregistryhive0,
        RegistryHivesOtherBBIregistryhive1,
        RegistryHivesOtherBBIregistrytransactionfiles2,
        RegistryHivesOtherBBIregistrytransactionfiles3,
        RegistryHivesOtherBCDTemplateregistryhive4,
        RegistryHivesOtherBCDTemplateregistryhive5,
        RegistryHivesOtherBCDTemplateregistrytransactionfiles6,
        RegistryHivesOtherBCDTemplateregistrytransactionfiles7,
        RegistryHivesOtherCOMPONENTSregistryhive8,
        RegistryHivesOtherCOMPONENTSregistryhive9,
        RegistryHivesOtherCOMPONENTSregistrytransactionfiles10,
        RegistryHivesOtherCOMPONENTSregistrytransactionfiles11,
        RegistryHivesOtherDRIVERSregistryhive12,
        RegistryHivesOtherDRIVERSregistryhive13,
        RegistryHivesOtherDRIVERSregistrytransactionfiles14,
        RegistryHivesOtherDRIVERSregistrytransactionfiles15,
        RegistryHivesOtherELAMregistryhive16,
        RegistryHivesOtherELAMregistryhive17,
        RegistryHivesOtherELAMregistrytransactionfiles18,
        RegistryHivesOtherELAMregistrytransactionfiles19,
        RegistryHivesOtheruserdiffregistryhive20,
        RegistryHivesOtheruserdiffregistryhive21,
        RegistryHivesOtheruserdiffregistrytransactionfiles22,
        RegistryHivesOtheruserdiffregistrytransactionfiles23,
        RegistryHivesOtherVSMIDKregistryhive24,
        RegistryHivesOtherVSMIDKregistryhive25,
        RegistryHivesOtherVSMIDKregistrytransactionfiles26,
        RegistryHivesOtherVSMIDKregistrytransactionfiles27,
    ]


class RegistryHivesSystemSAMregistrytransactionfiles0(KapeTarget):
    name: ClassVar[str] = "SAM registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SAM\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSAMregistrytransactionfiles1(KapeTarget):
    name: ClassVar[str] = "SAM registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SAM\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSECURITYregistrytransactionfiles2(KapeTarget):
    name: ClassVar[str] = "SECURITY registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SECURITY\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSECURITYregistrytransactionfiles3(KapeTarget):
    name: ClassVar[str] = "SECURITY registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SECURITY\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSOFTWAREregistrytransactionfiles4(KapeTarget):
    name: ClassVar[str] = "SOFTWARE registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SOFTWARE\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSOFTWAREregistrytransactionfiles5(KapeTarget):
    name: ClassVar[str] = "SOFTWARE registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SOFTWARE\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSYSTEMregistrytransactionfiles6(KapeTarget):
    name: ClassVar[str] = "SYSTEM registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SYSTEM\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSYSTEMregistrytransactionfiles7(KapeTarget):
    name: ClassVar[str] = "SYSTEM registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SYSTEM\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSAMregistryhive8(KapeTarget):
    name: ClassVar[str] = "SAM registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SAM)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSAMregistryhive9(KapeTarget):
    name: ClassVar[str] = "SAM registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SAM)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSECURITYregistryhive10(KapeTarget):
    name: ClassVar[str] = "SECURITY registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SECURITY)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSECURITYregistryhive11(KapeTarget):
    name: ClassVar[str] = "SECURITY registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SECURITY)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSOFTWAREregistryhive12(KapeTarget):
    name: ClassVar[str] = "SOFTWARE registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SOFTWARE)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSOFTWAREregistryhive13(KapeTarget):
    name: ClassVar[str] = "SOFTWARE registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SOFTWARE)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSYSTEMregistryhive14(KapeTarget):
    name: ClassVar[str] = "SYSTEM registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SYSTEM)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSYSTEMregistryhive15(KapeTarget):
    name: ClassVar[str] = "SYSTEM registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:SYSTEM)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemRegBackregistrytransactionfiles16(KapeTarget):
    name: ClassVar[str] = "RegBack registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\RegBack\\")
    regex: ClassVar[str] = r"(?s:(?>.*?\.LOG).*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemRegBackregistrytransactionfiles17(KapeTarget):
    name: ClassVar[str] = "RegBack registry transaction files"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\config\\RegBack\\"
    )
    regex: ClassVar[str] = r"(?s:(?>.*?\.LOG).*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSAMregistryhiveRegBack18(KapeTarget):
    name: ClassVar[str] = "SAM registry hive (RegBack)"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\RegBack\\")
    regex: ClassVar[str] = r"(?s:SAM)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSAMregistryhiveRegBack19(KapeTarget):
    name: ClassVar[str] = "SAM registry hive (RegBack)"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\config\\RegBack\\"
    )
    regex: ClassVar[str] = r"(?s:SAM)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSECURITYregistryhiveRegBack20(KapeTarget):
    name: ClassVar[str] = "SECURITY registry hive (RegBack)"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\RegBack\\")
    regex: ClassVar[str] = r"(?s:SECURITY)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSECURITYregistryhiveRegBack21(KapeTarget):
    name: ClassVar[str] = "SECURITY registry hive (RegBack)"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\config\\RegBack\\"
    )
    regex: ClassVar[str] = r"(?s:SECURITY)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSOFTWAREregistryhiveRegBack22(KapeTarget):
    name: ClassVar[str] = "SOFTWARE registry hive (RegBack)"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\RegBack\\")
    regex: ClassVar[str] = r"(?s:SOFTWARE)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSOFTWAREregistryhiveRegBack23(KapeTarget):
    name: ClassVar[str] = "SOFTWARE registry hive (RegBack)"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\config\\RegBack\\"
    )
    regex: ClassVar[str] = r"(?s:SOFTWARE)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSYSTEMregistryhiveRegBack24(KapeTarget):
    name: ClassVar[str] = "SYSTEM registry hive (RegBack)"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\RegBack\\")
    regex: ClassVar[str] = r"(?s:SYSTEM)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSYSTEMregistryhiveRegBack25(KapeTarget):
    name: ClassVar[str] = "SYSTEM registry hive (RegBack)"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\config\\RegBack\\"
    )
    regex: ClassVar[str] = r"(?s:SYSTEM)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSYSTEMregistryhiveRegBack26(KapeTarget):
    name: ClassVar[str] = "SYSTEM registry hive (RegBack)"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\RegBack\\")
    regex: ClassVar[str] = r"(?s:SYSTEM1)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSYSTEMregistryhiveRegBack27(KapeTarget):
    name: ClassVar[str] = "SYSTEM registry hive (RegBack)"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\config\\RegBack\\"
    )
    regex: ClassVar[str] = r"(?s:SYSTEM1)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSystemProfileregistryhive28(KapeTarget):
    name: ClassVar[str] = "System Profile registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\systemprofile\\")
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSystemProfileregistryhive29(KapeTarget):
    name: ClassVar[str] = "System Profile registry hive"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\config\\systemprofile\\"
    )
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSystemProfileregistrytransactionfiles30(KapeTarget):
    name: ClassVar[str] = "System Profile registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\systemprofile\\")
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSystemProfileregistrytransactionfiles31(KapeTarget):
    name: ClassVar[str] = "System Profile registry transaction files"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\System32\\config\\systemprofile\\"
    )
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemLocalServiceregistryhive32(KapeTarget):
    name: ClassVar[str] = "Local Service registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\ServiceProfiles\\LocalService\\")
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemLocalServiceregistryhive33(KapeTarget):
    name: ClassVar[str] = "Local Service registry hive"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\ServiceProfiles\\LocalService\\"
    )
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemLocalServiceregistrytransactionfiles34(KapeTarget):
    name: ClassVar[str] = "Local Service registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\ServiceProfiles\\LocalService\\")
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemLocalServiceregistrytransactionfiles35(KapeTarget):
    name: ClassVar[str] = "Local Service registry transaction files"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\ServiceProfiles\\LocalService\\"
    )
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemNetworkServiceregistryhive36(KapeTarget):
    name: ClassVar[str] = "Network Service registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\ServiceProfiles\\NetworkService\\")
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemNetworkServiceregistryhive37(KapeTarget):
    name: ClassVar[str] = "Network Service registry hive"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\ServiceProfiles\\NetworkService\\"
    )
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemNetworkServiceregistrytransactionfiles38(KapeTarget):
    name: ClassVar[str] = "Network Service registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\ServiceProfiles\\NetworkService\\")
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemNetworkServiceregistrytransactionfiles39(KapeTarget):
    name: ClassVar[str] = "Network Service registry transaction files"
    base_path: ClassVar[Path] = Path(
        "C:\\Windows.old\\Windows\\ServiceProfiles\\NetworkService\\"
    )
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystemSystemRestorePointsRegistryHivesXP40(KapeTarget):
    name: ClassVar[str] = "System Restore Points Registry Hives (XP)"
    base_path: ClassVar[Path] = Path(
        "C:\\System Volume Information\\_restore*\\RP*\\snapshot\\"
    )
    regex: ClassVar[str] = r"(?s:_REGISTRY_.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesSystem(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman / Mark Hallman

    Version: 1.0

    ID: 2b7f40fd-cd02-47da-87da-9966fa5d8159

    System level/related Registry hives
    """

    name: ClassVar[str] = "RegistryHivesSystem"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RegistryHivesSystemSAMregistrytransactionfiles0,
        RegistryHivesSystemSAMregistrytransactionfiles1,
        RegistryHivesSystemSECURITYregistrytransactionfiles2,
        RegistryHivesSystemSECURITYregistrytransactionfiles3,
        RegistryHivesSystemSOFTWAREregistrytransactionfiles4,
        RegistryHivesSystemSOFTWAREregistrytransactionfiles5,
        RegistryHivesSystemSYSTEMregistrytransactionfiles6,
        RegistryHivesSystemSYSTEMregistrytransactionfiles7,
        RegistryHivesSystemSAMregistryhive8,
        RegistryHivesSystemSAMregistryhive9,
        RegistryHivesSystemSECURITYregistryhive10,
        RegistryHivesSystemSECURITYregistryhive11,
        RegistryHivesSystemSOFTWAREregistryhive12,
        RegistryHivesSystemSOFTWAREregistryhive13,
        RegistryHivesSystemSYSTEMregistryhive14,
        RegistryHivesSystemSYSTEMregistryhive15,
        RegistryHivesSystemRegBackregistrytransactionfiles16,
        RegistryHivesSystemRegBackregistrytransactionfiles17,
        RegistryHivesSystemSAMregistryhiveRegBack18,
        RegistryHivesSystemSAMregistryhiveRegBack19,
        RegistryHivesSystemSECURITYregistryhiveRegBack20,
        RegistryHivesSystemSECURITYregistryhiveRegBack21,
        RegistryHivesSystemSOFTWAREregistryhiveRegBack22,
        RegistryHivesSystemSOFTWAREregistryhiveRegBack23,
        RegistryHivesSystemSYSTEMregistryhiveRegBack24,
        RegistryHivesSystemSYSTEMregistryhiveRegBack25,
        RegistryHivesSystemSYSTEMregistryhiveRegBack26,
        RegistryHivesSystemSYSTEMregistryhiveRegBack27,
        RegistryHivesSystemSystemProfileregistryhive28,
        RegistryHivesSystemSystemProfileregistryhive29,
        RegistryHivesSystemSystemProfileregistrytransactionfiles30,
        RegistryHivesSystemSystemProfileregistrytransactionfiles31,
        RegistryHivesSystemLocalServiceregistryhive32,
        RegistryHivesSystemLocalServiceregistryhive33,
        RegistryHivesSystemLocalServiceregistrytransactionfiles34,
        RegistryHivesSystemLocalServiceregistrytransactionfiles35,
        RegistryHivesSystemNetworkServiceregistryhive36,
        RegistryHivesSystemNetworkServiceregistryhive37,
        RegistryHivesSystemNetworkServiceregistrytransactionfiles38,
        RegistryHivesSystemNetworkServiceregistrytransactionfiles39,
        RegistryHivesSystemSystemRestorePointsRegistryHivesXP40,
    ]


class RegistryHivesUserNTUSERDATregistryhiveXP0(KapeTarget):
    name: ClassVar[str] = "NTUSER.DAT registry hive XP"
    base_path: ClassVar[Path] = Path("C:\\Documents and Settings\\%user%\\")
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesUserNTUSERDATregistryhive1(KapeTarget):
    name: ClassVar[str] = "NTUSER.DAT registry hive"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\")
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesUserNTUSERDATregistrytransactionfiles2(KapeTarget):
    name: ClassVar[str] = "NTUSER.DAT registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\Users\\%user%\\")
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesUserNTUSERDATDEFAULTregistryhive3(KapeTarget):
    name: ClassVar[str] = "NTUSER.DAT DEFAULT registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:DEFAULT)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesUserNTUSERDATDEFAULTregistryhive4(KapeTarget):
    name: ClassVar[str] = "NTUSER.DAT DEFAULT registry hive"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:DEFAULT)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesUserNTUSERDATDEFAULTtransactionfiles5(KapeTarget):
    name: ClassVar[str] = "NTUSER.DAT DEFAULT transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:DEFAULT\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesUserNTUSERDATDEFAULTtransactionfiles6(KapeTarget):
    name: ClassVar[str] = "NTUSER.DAT DEFAULT transaction files"
    base_path: ClassVar[Path] = Path("C:\\Windows.old\\Windows\\System32\\config\\")
    regex: ClassVar[str] = r"(?s:DEFAULT\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesUserUsrClassdatregistryhive7(KapeTarget):
    name: ClassVar[str] = "UsrClass.dat registry hive"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\"
    )
    regex: ClassVar[str] = r"(?s:UsrClass\.dat)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesUserUsrClassdatregistrytransactionfiles8(KapeTarget):
    name: ClassVar[str] = "UsrClass.dat registry transaction files"
    base_path: ClassVar[Path] = Path(
        "C:\\Users\\%user%\\AppData\\Local\\Microsoft\\Windows\\"
    )
    regex: ClassVar[str] = r"(?s:UsrClass\.dat\.LOG.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RegistryHivesUser(KapeTargetConfiguration):
    """
    Author: Eric Zimmerman / Mark Hallman

    Version: 1.0

    ID: 635fbfd3-4a47-45b5-aae4-0a1bb6545d08

    User Related Registry hives
    """

    name: ClassVar[str] = "RegistryHivesUser"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RegistryHivesUserNTUSERDATregistryhiveXP0,
        RegistryHivesUserNTUSERDATregistryhive1,
        RegistryHivesUserNTUSERDATregistrytransactionfiles2,
        RegistryHivesUserNTUSERDATDEFAULTregistryhive3,
        RegistryHivesUserNTUSERDATDEFAULTregistryhive4,
        RegistryHivesUserNTUSERDATDEFAULTtransactionfiles5,
        RegistryHivesUserNTUSERDATDEFAULTtransactionfiles6,
        RegistryHivesUserUsrClassdatregistryhive7,
        RegistryHivesUserUsrClassdatregistrytransactionfiles8,
    ]


class RoamingProfileNTUSERDATregistryhive0(KapeTarget):
    name: ClassVar[str] = "NTUSER.DAT registry hive"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileNTUSERDATregistrytransactionfiles1(KapeTarget):
    name: ClassVar[str] = "NTUSER.DAT registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:NTUSER\.DAT\.LOG.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileNTUSERDATDEFAULTregistryhive2(KapeTarget):
    name: ClassVar[str] = "NTUSER.DAT DEFAULT registry hive"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:DEFAULT)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileNTUSERDATDEFAULTtransactionfiles3(KapeTarget):
    name: ClassVar[str] = "NTUSER.DAT DEFAULT transaction files"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:DEFAULT\.LOG.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileUsrClassdatregistryhive4(KapeTarget):
    name: ClassVar[str] = "UsrClass.dat registry hive"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:UsrClass\.dat)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileUsrClassdatregistrytransactionfiles5(KapeTarget):
    name: ClassVar[str] = "UsrClass.dat registry transaction files"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:UsrClass\.dat\.LOG.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileLNKFiles6(KapeTarget):
    name: ClassVar[str] = "LNK Files"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.LNK)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileWordAutosaveLocation7(KapeTarget):
    name: ClassVar[str] = "Word Autosave Location"
    base_path: ClassVar[Path] = Path("C:\\AppData\\Roaming\\Microsoft\\Word\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileExcelAutosaveLocation8(KapeTarget):
    name: ClassVar[str] = "Excel Autosave Location"
    base_path: ClassVar[Path] = Path("C:\\AppData\\Roaming\\Microsoft\\Word\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfilePowerpointAutosaveLocation9(KapeTarget):
    name: ClassVar[str] = "Powerpoint Autosave Location"
    base_path: ClassVar[Path] = Path("C:\\AppData\\Roaming\\Microsoft\\Word\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfilePublisherAutosaveLocation10(KapeTarget):
    name: ClassVar[str] = "Publisher Autosave Location"
    base_path: ClassVar[Path] = Path("C:\\AppData\\Roaming\\Microsoft\\Word\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfilePublisherAutosaveLocation11(KapeTarget):
    name: ClassVar[str] = "Publisher Autosave Location"
    base_path: ClassVar[Path] = Path("C:\\*\\AppData\\Roaming\\Microsoft\\Word\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileOfficeDocumentCache12(KapeTarget):
    name: ClassVar[str] = "Office Document Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Microsoft\\Office\\*\\OfficeFileCache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileOfficeDocumentCache13(KapeTarget):
    name: ClassVar[str] = "Office Document Cache"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Microsoft\\Office\\*\\OfficeFileCache\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromebookmarks14(KapeTarget):
    name: ClassVar[str] = "Chrome bookmarks"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Bookmarks.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromebookmarks15(KapeTarget):
    name: ClassVar[str] = "Chrome bookmarks"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Bookmarks.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeCookies16(KapeTarget):
    name: ClassVar[str] = "Chrome Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Cookies.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeCookies17(KapeTarget):
    name: ClassVar[str] = "Chrome Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Cookies.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeCurrentSession18(KapeTarget):
    name: ClassVar[str] = "Chrome Current Session"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Current\ Session)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeCurrentSession19(KapeTarget):
    name: ClassVar[str] = "Chrome Current Session"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Current\ Session)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeCurrentTabs20(KapeTarget):
    name: ClassVar[str] = "Chrome Current Tabs"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Current\ Tabs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeCurrentTabs21(KapeTarget):
    name: ClassVar[str] = "Chrome Current Tabs"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Current\ Tabs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeDownloadMetadata22(KapeTarget):
    name: ClassVar[str] = "Chrome Download Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Download\ Metadata)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeDownloadMetadata23(KapeTarget):
    name: ClassVar[str] = "Chrome Download Metadata"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Download\ Metadata)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeExtensionCookies24(KapeTarget):
    name: ClassVar[str] = "Chrome Extension Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Extension\ Cookies)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeExtensionCookies25(KapeTarget):
    name: ClassVar[str] = "Chrome Extension Cookies"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Extension\ Cookies)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeFavicons26(KapeTarget):
    name: ClassVar[str] = "Chrome Favicons"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Favicons.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeFavicons27(KapeTarget):
    name: ClassVar[str] = "Chrome Favicons"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Favicons.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeHistory28(KapeTarget):
    name: ClassVar[str] = "Chrome History"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:History.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeHistory29(KapeTarget):
    name: ClassVar[str] = "Chrome History"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:History.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeLastSession30(KapeTarget):
    name: ClassVar[str] = "Chrome Last Session"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Last\ Session)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeLastSession31(KapeTarget):
    name: ClassVar[str] = "Chrome Last Session"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Last\ Session)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeLastTabs32(KapeTarget):
    name: ClassVar[str] = "Chrome Last Tabs"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Last\ Tabs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeLastTabs33(KapeTarget):
    name: ClassVar[str] = "Chrome Last Tabs"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Last\ Tabs)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeSessionsFolder34(KapeTarget):
    name: ClassVar[str] = "Chrome Sessions Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\Sessions\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeSessionsFolder35(KapeTarget):
    name: ClassVar[str] = "Chrome Sessions Folder"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\Sessions\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeLoginData36(KapeTarget):
    name: ClassVar[str] = "Chrome Login Data"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Login\ Data)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeLoginData37(KapeTarget):
    name: ClassVar[str] = "Chrome Login Data"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Login\ Data)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeMediaHistory38(KapeTarget):
    name: ClassVar[str] = "Chrome Media History"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Media\ History.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeMediaHistory39(KapeTarget):
    name: ClassVar[str] = "Chrome Media History"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Media\ History.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeNetworkActionPredictor40(KapeTarget):
    name: ClassVar[str] = "Chrome Network Action Predictor"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Network\ Action\ Predictor)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeNetworkActionPredictor41(KapeTarget):
    name: ClassVar[str] = "Chrome Network Action Predictor"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Network\ Action\ Predictor)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeNetworkPersistentState42(KapeTarget):
    name: ClassVar[str] = "Chrome Network Persistent State"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Network\ Persistent\ State)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeNetworkPersistentState43(KapeTarget):
    name: ClassVar[str] = "Chrome Network Persistent State"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Network\ Persistent\ State)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromePreferences44(KapeTarget):
    name: ClassVar[str] = "Chrome Preferences"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Preferences)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromePreferences45(KapeTarget):
    name: ClassVar[str] = "Chrome Preferences"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Preferences)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeQuotaManager46(KapeTarget):
    name: ClassVar[str] = "Chrome Quota Manager"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:QuotaManager)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeQuotaManager47(KapeTarget):
    name: ClassVar[str] = "Chrome Quota Manager"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:QuotaManager)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeReportingandNEL48(KapeTarget):
    name: ClassVar[str] = "Chrome Reporting and NEL"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Reporting\ and\ NEL)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeReportingandNEL49(KapeTarget):
    name: ClassVar[str] = "Chrome Reporting and NEL"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Reporting\ and\ NEL)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeShortcuts50(KapeTarget):
    name: ClassVar[str] = "Chrome Shortcuts"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Shortcuts.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeShortcuts51(KapeTarget):
    name: ClassVar[str] = "Chrome Shortcuts"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Shortcuts.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeTopSites52(KapeTarget):
    name: ClassVar[str] = "Chrome Top Sites"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Top\ Sites.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeTopSites53(KapeTarget):
    name: ClassVar[str] = "Chrome Top Sites"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Top\ Sites.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeTrustTokens54(KapeTarget):
    name: ClassVar[str] = "Chrome Trust Tokens"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Trust\ Tokens.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeTrustTokens55(KapeTarget):
    name: ClassVar[str] = "Chrome Trust Tokens"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Trust\ Tokens.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeSyncDataDatabase56(KapeTarget):
    name: ClassVar[str] = "Chrome SyncData Database"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\Sync Data"
    )
    regex: ClassVar[str] = r"(?s:SyncData\.sqlite3)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeSyncDataDatabase57(KapeTarget):
    name: ClassVar[str] = "Chrome SyncData Database"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\Sync Data"
    )
    regex: ClassVar[str] = r"(?s:SyncData\.sqlite3)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeVisitedLinks58(KapeTarget):
    name: ClassVar[str] = "Chrome Visited Links"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Visited\ Links)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeVisitedLinks59(KapeTarget):
    name: ClassVar[str] = "Chrome Visited Links"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Visited\ Links)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeWebData60(KapeTarget):
    name: ClassVar[str] = "Chrome Web Data"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Web\ Data.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileChromeWebData61(KapeTarget):
    name: ClassVar[str] = "Chrome Web Data"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Google\\Chrome\\User Data\\*\\"
    )
    regex: ClassVar[str] = r"(?s:Web\ Data.*)\Z"
    recursive: ClassVar[bool] = False
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileWindowsProtectFolder62(KapeTarget):
    """
    Required for offline decryption
    """

    name: ClassVar[str] = "Windows Protect Folder"
    base_path: ClassVar[Path] = Path("C:\\AppData\\Roaming\\Microsoft\\Protect\\*\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileWindowsProtectFolder63(KapeTarget):
    """
    Required for offline decryption
    """

    name: ClassVar[str] = "Windows Protect Folder"
    base_path: ClassVar[Path] = Path("C:\\*\\AppData\\Roaming\\Microsoft\\Protect\\*\\")
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileEdgefolder64(KapeTarget):
    name: ClassVar[str] = "Edge folder"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileEdgefolder65(KapeTarget):
    name: ClassVar[str] = "Edge folder"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Local\\Packages\\Microsoft.MicrosoftEdge_8wekyb3d8bbwe\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileAmcache66(KapeTarget):
    name: ClassVar[str] = "Amcache"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:Amcache\.hve)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileAmcachetransactionfiles67(KapeTarget):
    name: ClassVar[str] = "Amcache transaction files"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:Amcache\.hve\.LOG.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileLNKFilesfromRecent68(KapeTarget):
    name: ClassVar[str] = "LNK Files from Recent"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Roaming\\Microsoft\\Windows\\Recent\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileLNKFilesfromRecent69(KapeTarget):
    name: ClassVar[str] = "LNK Files from Recent"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Roaming\\Microsoft\\Windows\\Recent\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileLNKFilesfromMicrosoftOfficeRecent70(KapeTarget):
    name: ClassVar[str] = "LNK Files from Microsoft Office Recent"
    base_path: ClassVar[Path] = Path(
        "C:\\AppData\\Roaming\\Microsoft\\Office\\Recent\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileLNKFilesfromMicrosoftOfficeRecent71(KapeTarget):
    name: ClassVar[str] = "LNK Files from Microsoft Office Recent"
    base_path: ClassVar[Path] = Path(
        "C:\\*\\AppData\\Roaming\\Microsoft\\Office\\Recent\\"
    )
    regex: ClassVar[str] = r"(?s:.*)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfileDesktopLNKFiles72(KapeTarget):
    name: ClassVar[str] = "Desktop LNK Files"
    base_path: ClassVar[Path] = Path("C:\\")
    regex: ClassVar[str] = r"(?s:.*\.LNK)\Z"
    recursive: ClassVar[bool] = True
    associated_modules: ClassVar[list[Type[KapeModule]]] = []

    # Add any instance variables specific to this target as Pydantic fields here.


class RoamingProfile(KapeTargetConfiguration):
    """
    Author: Scott Downie

    Version: 1.0

    ID: ffa5fb2a-403c-11ed-b878-0242ac120002

    User Related Registry Hives, LNK files, etc
    """

    name: ClassVar[str] = "RoamingProfile"
    recreate_directories: ClassVar[bool] = True
    targets: ClassVar[list[Type[KapeTarget]]] = [
        RoamingProfileNTUSERDATregistryhive0,
        RoamingProfileNTUSERDATregistrytransactionfiles1,
        RoamingProfileNTUSERDATDEFAULTregistryhive2,
        RoamingProfileNTUSERDATDEFAULTtransactionfiles3,
        RoamingProfileUsrClassdatregistryhive4,
        RoamingProfileUsrClassdatregistrytransactionfiles5,
        RoamingProfileLNKFiles6,
        RoamingProfileWordAutosaveLocation7,
        RoamingProfileExcelAutosaveLocation8,
        RoamingProfilePowerpointAutosaveLocation9,
        RoamingProfilePublisherAutosaveLocation10,
        RoamingProfilePublisherAutosaveLocation11,
        RoamingProfileOfficeDocumentCache12,
        RoamingProfileOfficeDocumentCache13,
        RoamingProfileChromebookmarks14,
        RoamingProfileChromebookmarks15,
        RoamingProfileChromeCookies16,
        RoamingProfileChromeCookies17,
        RoamingProfileChromeCurrentSession18,
        RoamingProfileChromeCurrentSession19,
        RoamingProfileChromeCurrentTabs20,
        RoamingProfileChromeCurrentTabs21,
        RoamingProfileChromeDownloadMetadata22,
        RoamingProfileChromeDownloadMetadata23,
        RoamingProfileChromeExtensionCookies24,
        RoamingProfileChromeExtensionCookies25,
        RoamingProfileChromeFavicons26,
        RoamingProfileChromeFavicons27,
        RoamingProfileChromeHistory28,
        RoamingProfileChromeHistory29,
        RoamingProfileChromeLastSession30,
        RoamingProfileChromeLastSession31,
        RoamingProfileChromeLastTabs32,
        RoamingProfileChromeLastTabs33,
        RoamingProfileChromeSessionsFolder34,
        RoamingProfileChromeSessionsFolder35,
        RoamingProfileChromeLoginData36,
        RoamingProfileChromeLoginData37,
        RoamingProfileChromeMediaHistory38,
        RoamingProfileChromeMediaHistory39,
        RoamingProfileChromeNetworkActionPredictor40,
        RoamingProfileChromeNetworkActionPredictor41,
        RoamingProfileChromeNetworkPersistentState42,
        RoamingProfileChromeNetworkPersistentState43,
        RoamingProfileChromePreferences44,
        RoamingProfileChromePreferences45,
        RoamingProfileChromeQuotaManager46,
        RoamingProfileChromeQuotaManager47,
        RoamingProfileChromeReportingandNEL48,
        RoamingProfileChromeReportingandNEL49,
        RoamingProfileChromeShortcuts50,
        RoamingProfileChromeShortcuts51,
        RoamingProfileChromeTopSites52,
        RoamingProfileChromeTopSites53,
        RoamingProfileChromeTrustTokens54,
        RoamingProfileChromeTrustTokens55,
        RoamingProfileChromeSyncDataDatabase56,
        RoamingProfileChromeSyncDataDatabase57,
        RoamingProfileChromeVisitedLinks58,
        RoamingProfileChromeVisitedLinks59,
        RoamingProfileChromeWebData60,
        RoamingProfileChromeWebData61,
        RoamingProfileWindowsProtectFolder62,
        RoamingProfileWindowsProtectFolder63,
        RoamingProfileEdgefolder64,
        RoamingProfileEdgefolder65,
        RoamingProfileAmcache66,
        RoamingProfileAmcachetransactionfiles67,
        RoamingProfileLNKFilesfromRecent68,
        RoamingProfileLNKFilesfromRecent69,
        RoamingProfileLNKFilesfromMicrosoftOfficeRecent70,
        RoamingProfileLNKFilesfromMicrosoftOfficeRecent71,
        RoamingProfileDesktopLNKFiles72,
    ]
