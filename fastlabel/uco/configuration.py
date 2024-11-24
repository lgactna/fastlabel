"""
Auto-generated classes from the SHACL graph in configuration.ttl.

This file was generated using the `case_models.py` script.
"""

from fastlabel.uco import core


class ConfigurationEntry(core.UcoInherentCharacterizationThing):
    """
    A configuration entry is a grouping of characteristics unique to a
    particular parameter or initial setting for the use of a tool, application,
    software, or other cyber object.
    """

    itemObject: core.UcoObject | list[core.UcoObject] | None = []
    itemDescription: str | None = None
    itemName: str | None = None
    itemType: str | None = None
    itemValue: str | list[str] | None = []


class Dependency(core.UcoInherentCharacterizationThing):
    """
    A dependency is a grouping of characteristics unique to something that a
    tool or other software relies on to function as intended.
    """

    dependencyDescription: str | None = None
    dependencyType: str | None = None


class Configuration(core.UcoObject):
    """
    A configuration is a grouping of characteristics unique to a set of
    parameters or initial settings for the use of a tool, application, software,
    or other cyber object.
    """

    configurationEntry: ConfigurationEntry | list[ConfigurationEntry] | None = []
    dependencies: Dependency | list[Dependency] | None = []
    usageContextAssumptions: str | list[str] | None = []
