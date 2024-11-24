"""
Auto-generated classes from the SHACL graph in configuration.ttl.

This file was generated using the `case_models.py` script.
"""

from typing import Any, Optional

from fastlabel.case import core


class Dependency(core.UcoInherentCharacterizationThing):
    """
    A dependency is a grouping of characteristics unique to something that a
    tool or other software relies on to function as intended.
    """

    dependencyDescription: Optional[str] = None
    dependencyType: Optional[str] = None


class ConfigurationEntry(core.UcoInherentCharacterizationThing):
    """
    A configuration entry is a grouping of characteristics unique to a
    particular parameter or initial setting for the use of a tool, application,
    software, or other cyber object.
    """

    itemObject: Optional[core.UcoObject] = None
    itemDescription: Optional[str] = None
    itemName: Optional[str] = None
    itemType: Optional[str] = None
    itemValue: Optional[str] = None


class Configuration(core.UcoObject):
    """
    A configuration is a grouping of characteristics unique to a set of
    parameters or initial settings for the use of a tool, application, software,
    or other cyber object.
    """

    configurationEntry: Optional[ConfigurationEntry] = None
    dependencies: Optional[Dependency] = None
    usageContextAssumptions: Optional[str] = None
