"""
Auto-generated classes from the SHACL graph in action.ttl.

This file was generated using the `case_models.py` script.
"""

from typing import Any, Optional

from fastlabel.case import core, location


class ActionEstimationFacet(core.Facet):
    """
    An action estimation facet is a grouping of characteristics unique to
    decision-focused approximation aspects for an action that may potentially be
    performed.
    """

    estimatedCost: Optional[str] = None
    estimatedEfficacy: Optional[str] = None
    estimatedImpact: Optional[str] = None
    objective: Optional[str] = None


class ActionArgumentFacet(core.Facet):
    """
    An action argument facet is a grouping of characteristics unique to a single
    parameter of an action.
    """

    argumentName: str
    value: str


class ActionFrequencyFacet(core.Facet):
    """
    An action frequency facet is a grouping of characteristics unique to the
    frequency of occurrence for an action.
    """

    rate: float
    scale: str
    units: str
    trend: Optional[str] = None
    trend: Any
    trend: Optional[Any] = None


class Action(core.UcoObject):
    """
    An action is something that may be done or performed.
    """

    subaction: Optional["Action"] = None
    environment: Optional[core.UcoObject] = None
    performer: Optional[core.UcoObject] = None
    error: Optional[core.UcoObject] = None
    instrument: Optional[core.UcoObject] = None
    object: Optional[core.UcoObject] = None
    participant: Optional[core.UcoObject] = None
    result: Optional[core.UcoObject] = None
    location: Optional[location.Location] = None
    endTime: Optional[str] = None
    startTime: Optional[str] = None
    actionCount: Optional[int] = None
    actionStatus: Optional[str] = None
    actionStatus: Optional[Any] = None
    actionStatus: Optional[Any] = None


class ActionPattern(Action):
    """
    An action pattern is a grouping of characteristics unique to a combination
    of actions forming a consistent or characteristic arrangement.
    """

    pass


class ArrayOfAction(core.UcoInherentCharacterizationThing):
    """
    An array of action is an ordered list of references to things that may be
    done or performed.
    """

    action: Action


class ActionLifecycle(Action):
    """
    An action lifecycle is an action pattern consisting of an ordered set of
    multiple actions or subordinate action lifecycles.
    """

    phase: ArrayOfAction
    error: Optional[core.UcoObject] = None
    endTime: Optional[str] = None
    startTime: Optional[str] = None
    actionCount: Optional[int] = None
    actionStatus: Optional[Any] = None
