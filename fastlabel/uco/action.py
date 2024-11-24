"""
Auto-generated classes from the SHACL graph in action.ttl.

This file was generated using the `case_models.py` script.
"""

from typing import Optional

from pydantic import AwareDatetime

from fastlabel.uco import core, location, vocabulary


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
    location_: Optional[location.Location] = None
    endTime: Optional[AwareDatetime] = None
    startTime: Optional[AwareDatetime] = None
    actionCount: Optional[int] = None
    actionStatus: Optional[vocabulary.ActionStatusTypeVocab] = None


class ActionArgumentFacet(core.Facet):
    """
    An action argument facet is a grouping of characteristics unique to a single
    parameter of an action.
    """

    argumentName: str
    value: str


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


class ActionFrequencyFacet(core.Facet):
    """
    An action frequency facet is a grouping of characteristics unique to the
    frequency of occurrence for an action.
    """

    rate: float
    scale: str
    units: str
    trend: Optional[vocabulary.TrendVocab] = None


class ActionPattern(Action):
    """
    An action pattern is a grouping of characteristics unique to a combination
    of actions forming a consistent or characteristic arrangement.
    """


class ArrayOfAction(core.UcoInherentCharacterizationThing):
    """
    An array of action is an ordered list of references to things that may be
    done or performed.
    """

    action_: Action


class ActionLifecycle(ActionPattern):
    """
    An action lifecycle is an action pattern consisting of an ordered set of
    multiple actions or subordinate action lifecycles.
    """

    phase: ArrayOfAction
    error: Optional[core.UcoObject] = None
    endTime: Optional[AwareDatetime] = None
    startTime: Optional[AwareDatetime] = None
    actionCount: Optional[int] = None
