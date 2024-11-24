"""
Auto-generated classes from the SHACL graph in tool.ttl.

This file was generated using the `case_models.py` script.
"""

from pydantic import AwareDatetime, Field

from fastlabel.uco import XMLSchema, configuration, core, identity


class BuildUtilityType(core.UcoInherentCharacterizationThing):
    """
    A build utility type characterizes the tool used to convert from source code
    to executable code for a particular version of software.
    """

    buildUtilityName: str | None = None
    cpeid: str | None = None
    swid: str | None = None


class CompilerType(core.UcoInherentCharacterizationThing):
    """
    A compiler type is a grouping of characteristics unique to a specific
    program that translates computer code written in one programming language
    (the source language) into another language (the target language). Typically
    a program that translates source code from a high-level programming language
    to a lower-level language (e.g., assembly language, object code, or machine
    code) to create an executable program. [based on
    https://en.wikipedia.org/wiki/Compiler]
    """

    compilerInformalDescription: str | None = None
    cpeid: str | None = None
    swid: str | None = None


class LibraryType(core.UcoInherentCharacterizationThing):
    """
    A library type is a grouping of characteristics unique to a collection of
    resources incorporated into the build of a software.
    """

    libraryName: str | None = None
    libraryVersion: str | None = None


class Tool(core.UcoObject):
    """
    A tool is an element of hardware and/or software utilized to carry out a
    particular function.
    """

    creator: identity.Identity | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    references: XMLSchema.xsd_anyURI | list[XMLSchema.xsd_anyURI] | None = []
    servicePack: str | None = None
    toolType: str | None = None
    version: str | None = None


class BuildInformationType(core.UcoInherentCharacterizationThing):
    """
    A build information type is a grouping of characteristics that describe how
    a particular version of software was converted from source code to
    executable code.
    """

    buildConfiguration: configuration.Configuration | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    buildUtility: BuildUtilityType | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    compilers: CompilerType | list[CompilerType] | None = []
    libraries: LibraryType | list[LibraryType] | None = []
    compilationDate: AwareDatetime | None = None
    buildID: str | None = None
    buildLabel: str | None = None
    buildOutputLog: str | None = None
    buildProject: str | None = None
    buildScript: str | None = None
    buildVersion: str | None = None


class AnalyticTool(Tool):
    """
    An analytic tool is an artifact of hardware and/or software utilized to
    accomplish a task or purpose of explanation, interpretation or logical
    reasoning.
    """


class ConfiguredTool(Tool):
    """
    A ConfiguredTool is a Tool that is known to be configured to run in a more
    specified manner than some unconfigured or less-configured Tool.
    """

    usesConfiguration: configuration.Configuration | None = None
    isConfigurationOf: Tool | None = None


class DefensiveTool(Tool):
    """
    A defensive tool is an artifact of hardware and/or software utilized to
    accomplish a task or purpose of guarding.
    """


class MaliciousTool(Tool):
    """
    A malicious tool is an artifact of hardware and/or software utilized to
    accomplish a malevolent task or purpose.
    """


class BuildFacet(core.Facet):
    """
    A build facet is a grouping of characteristics unique to a particular
    version of a software.
    """

    buildInformation: BuildInformationType | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
