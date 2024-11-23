
"""
Auto-generated classes from the SHACL graph in tool.ttl.

This file was generated using the `case_models.py` script.
"""

class BuildInformationType(core.UcoInherentCharacterizationThing):
    """
    A build information type is a grouping of characteristics that describe how
    a particular version of software was converted from source code to
    executable code.
    """

    buildConfiguration: Optional[Configuration] = None
    buildUtility: Optional[BuildUtilityType] = None
    compilers: Optional[CompilerType] = None
    libraries: Optional[LibraryType] = None
    compilationDate: Optional[str] = None
    buildID: Optional[str] = None
    buildLabel: Optional[str] = None
    buildOutputLog: Optional[str] = None
    buildProject: Optional[str] = None
    buildScript: Optional[str] = None
    buildVersion: Optional[str] = None

class AnalyticTool(tool.Tool):
    """
    An analytic tool is an artifact of hardware and/or software utilized to
    accomplish a task or purpose of explanation, interpretation or logical
    reasoning.
    """


class LibraryType(core.UcoInherentCharacterizationThing):
    """
    A library type is a grouping of characteristics unique to a collection of
    resources incorporated into the build of a software.
    """

    libraryName: Optional[str] = None
    libraryVersion: Optional[str] = None

class ConfiguredTool(tool.Tool):
    """
    A ConfiguredTool is a Tool that is known to be configured to run in a more
    specified manner than some unconfigured or less-configured Tool.
    """

    usesConfiguration: Optional[Configuration] = None
    isConfigurationOf: Optional[Tool] = None

class BuildUtilityType(core.UcoInherentCharacterizationThing):
    """
    A build utility type characterizes the tool used to convert from source code
    to executable code for a particular version of software.
    """

    buildUtilityName: Optional[str] = None
    cpeid: Optional[str] = None
    swid: Optional[str] = None

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

    compilerInformalDescription: Optional[str] = None
    cpeid: Optional[str] = None
    swid: Optional[str] = None

class Tool(core.UcoObject):
    """
    A tool is an element of hardware and/or software utilized to carry out a
    particular function.
    """

    creator: Optional[Identity] = None
    references: Optional[str] = None
    servicePack: Optional[str] = None
    toolType: Optional[str] = None
    version: Optional[str] = None

class DefensiveTool(tool.Tool):
    """
    A defensive tool is an artifact of hardware and/or software utilized to
    accomplish a task or purpose of guarding.
    """


class MaliciousTool(tool.Tool):
    """
    A malicious tool is an artifact of hardware and/or software utilized to
    accomplish a malevolent task or purpose.
    """


class BuildFacet(core.Facet):
    """
    A build facet is a grouping of characteristics unique to a particular
    version of a software.
    """

    buildInformation: Optional[BuildInformationType] = None

