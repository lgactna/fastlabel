
"""
Auto-generated classes from the SHACL graph in core.ttl.

This file was generated using the `case_models.py` script.
"""

from fastlabel.case import (owl, types)
from typing import Any, Optional
from enum import Enum

class ObjectStatusVocab(str, Enum):
    DRAFT = 'Draft'
    FINAL = 'Final'
    DEPRECATED = 'Deprecated'


class UcoThing(owl.Thing):
    """
    UcoThing is the top-level class within UCO.
    """

    pass

class UcoInherentCharacterizationThing(UcoThing):
    """
    A UCO inherent characterization thing is a grouping of characteristics
    unique to a particular inherent aspect of a UCO domain object.
    """

    pass

class ExternalReference(UcoInherentCharacterizationThing):
    """
    Characteristics of a reference to a resource outside of the UCO.
    """

    referenceURL: Optional[str] = None
    definingContext: Optional[str] = None
    externalIdentifier: Optional[str] = None

class Facet(UcoInherentCharacterizationThing):
    """
    A facet is a grouping of characteristics singularly unique to a particular
    inherent aspect of a UCO domain object.
    """

    pass

class UcoObject(UcoThing):
    """
    A UCO object is a representation of a fundamental concept either directly
    inherent to the cyber domain or indirectly related to the cyber domain and
    necessary for contextually characterizing cyber domain concepts and
    relationships. Within the Unified Cyber Ontology (UCO) structure this is the
    base class acting as a consistent, unifying and interoperable foundation for
    all explicit and inter-relatable content objects.
    """

    externalReference: Optional[ExternalReference] = None
    hasFacet: Optional[Facet] = None
    objectCreatedTime: Optional[str] = None
    modifiedTime: Optional[str] = None
    name: Optional[str] = None
    specVersion: Optional[str] = None
    description: Optional[str] = None
    tag: Optional[str] = None
    objectStatus: Optional[str] = None

class ConfidenceFacet(Facet):
    """
    A confidence is a grouping of characteristics unique to an asserted level of
    certainty in the accuracy of some information.
    """

    confidence: int

class Item(UcoObject):
    """
    An item is a distinct article or unit.
    """

    pass

class AttributedName(UcoObject):
    """
    An attributed name is a name of an entity issued by some attributed naming
    authority.
    """

    namingAuthority: Optional[str] = None

class Relationship(UcoObject):
    """
    A relationship is a grouping of characteristics unique to an assertion that
    one or more objects are related to another object in some way.
    """

    target: UcoObject
    source: UcoObject
    isDirectional: bool
    endTime: Optional[str] = None
    startTime: Optional[str] = None
    kindOfRelationship: Optional[str] = None

class ModusOperandi(UcoObject):
    """
    A modus operandi is a particular method of operation (how a particular
    entity behaves or the resources they use).
    """

    pass

class Assertion(UcoObject):
    """
    An assertion is a statement declared to be true.
    """

    statement: Optional[str] = None

class ControlledVocabulary(UcoObject):
    """
    A controlled vocabulary is an explicitly constrained set of string values.
    """

    constrainingVocabularyReference: Optional[str] = None
    value: str
    constrainingVocabularyName: Optional[str] = None

class Compilation(UcoObject):
    """
    A compilation is a grouping of things.
    """

    pass

class IdentityAbstraction(UcoObject):
    """
    An identity abstraction is a grouping of identifying characteristics unique
    to an individual or organization. This class is an ontological structural
    abstraction for this concept. Implementations of this concept should utilize
    the identity:Identity class.
    """

    pass

class Event(UcoObject):
    """
    An Event is a noteworthy occurrence (something that happens or might
    happen).
    """

    eventContext: Optional[UcoObject] = None
    eventAttribute: Optional[types.Dictionary] = None
    endTime: Optional[str] = None
    startTime: Optional[str] = None
    eventType: Optional[str] = None

class MarkingDefinitionAbstraction(UcoObject):
    """
    A marking definition abstraction is a grouping of characteristics unique to
    the expression of a specific data marking conveying restrictions,
    permissions, and other guidance for how marked data can be used and shared.
    This class is an ontological structural abstraction for this concept.
    Implementations of this concept should utilize the marking:MarkingDefinition
    class.
    """

    pass

class Annotation(Assertion):
    """
    An annotation is an assertion made in relation to one or more objects.
    """

    object: UcoObject

class ContextualCompilation(Compilation):
    """
    A contextual compilation is a grouping of things sharing some context (e.g.,
    a set of network connections observed on a given day, all accounts
    associated with a given person).
    """

    object: Optional[UcoObject] = None

class EnclosingCompilation(Compilation):
    """
    An enclosing compilation is a container for a grouping of things.
    """

    object: UcoObject

class Grouping(ContextualCompilation):
    """
    A grouping is a compilation of referenced UCO content with a shared context.
    """

    context: Optional[str] = None

class Bundle(EnclosingCompilation):
    """
    A bundle is a container for a grouping of UCO content with no presumption of
    shared context.
    """

    pass

