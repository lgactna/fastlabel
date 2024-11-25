"""
Auto-generated classes from the SHACL graph in action.ttl.

This file was generated using the `case_models.py` script.
"""

from typing import Union

from pydantic import AwareDatetime, Field

from fastlabel.uco import core, location, vocabulary


class Action(core.UcoObject):
    """
    An action is something that may be done or performed.
    """

    subaction: Union["Action", list["Action"], None] = []
    environment: core.UcoObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    performer: core.UcoObject | None = Field(
        default=None, json_schema_extra={"IRI": True}
    )
    error: core.UcoObject | list[core.UcoObject] | None = []
    instrument: core.UcoObject | list[core.UcoObject] | None = []
    object: core.UcoObject | list[core.UcoObject] | None = []
    participant: core.UcoObject | list[core.UcoObject] | None = []
    result: core.UcoObject | list[core.UcoObject] | None = []
    location_: location.Location | list[location.Location] | None = []
    endTime: AwareDatetime | None = None
    startTime: AwareDatetime | None = None
    actionCount: int | None = None
    actionStatus: (
        vocabulary.ActionStatusTypeVocab | list[vocabulary.ActionStatusTypeVocab] | None
    ) = []


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

    estimatedCost: str | None = None
    estimatedEfficacy: str | None = None
    estimatedImpact: str | None = None
    objective: str | None = None


class ActionFrequencyFacet(core.Facet):
    """
    An action frequency facet is a grouping of characteristics unique to the
    frequency of occurrence for an action.
    """

    rate: float
    scale: str
    units: str
    trend: vocabulary.TrendVocab | list[vocabulary.TrendVocab] | None = []


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

    action_: Action | list[Action] = []


class ActionLifecycle(ActionPattern):
    """
    An action lifecycle is an action pattern consisting of an ordered set of
    multiple actions or subordinate action lifecycles.
    """

    phase: ArrayOfAction = Field(json_schema_extra={"IRI": True})
    error: core.UcoObject | None = Field(default=None, json_schema_extra={"IRI": True})
    endTime: AwareDatetime | None = None
    startTime: AwareDatetime | None = None
    actionCount: int | None = None
