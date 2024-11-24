"""
Auto-generated classes from the SHACL graph in investigation.ttl.

This file was generated using the `case_models.py` script.
"""

from typing import Optional

from pydantic import AwareDatetime

from fastlabel.case import vocabulary
from fastlabel.uco import action, core, role


class Attorney(role.Role):
    """
    Attorney is a role involved in preparing, interpreting, and applying law.
    """


class Examiner(role.Role):
    """
    Examiner is a role involved in providing scientific evaluations of evidence
    that are used to aid law enforcement investigations and court cases.
    """


class Investigator(role.Role):
    """
    Investigator is a role involved in coordinating an investigation.
    """


class Subject(role.Role):
    """
    Subject is a role whose conduct is within the scope of an investigation.
    """


class Authorization(core.UcoObject):
    """
    An authorization is a grouping of characteristics unique to some form of
    authoritative permission identified for investigative action.
    """

    endTime: Optional[AwareDatetime] = None
    startTime: Optional[AwareDatetime] = None
    authorizationType: Optional[str] = None
    authorizationIdentifier: Optional[str] = None


class ExaminerActionLifecycle(action.ActionLifecycle):
    """
    An examiner action lifecycle is an action pattern consisting of an ordered
    set of actions or subordinate action-lifecycles performed by an entity
    acting in a role involved in providing scientific evaluations of evidence
    that is used to aid law enforcement investigations and court cases.
    """


class SubjectActionLifecycle(action.ActionLifecycle):
    """
    A subject action lifecycle is an action pattern consisting of an ordered set
    of multiple actions or subordinate action-lifecycles performed by an entity
    acting in a role whose conduct may be within the scope of an investigation.
    """


class VictimActionLifecycle(action.ActionLifecycle):
    """
    A victim action lifecycle is an action pattern consisting of an ordered set
    of multiple actions or subordinate action-lifecycles performed by an entity
    acting in a role characterized by its potential to be harmed as a result of
    a crime, accident, or other event or action.
    """


class ProvenanceRecord(core.ContextualCompilation):
    """
    A provenance record is a grouping of characteristics unique to the
    provenantial (chronology of the ownership, custody or location) connection
    between an investigative action and a set of observations (items and/or
    actions) or interpretations that result from it.
    """

    exhibitNumber: Optional[str] = None
    rootExhibitNumber: Optional[str] = None


class InvestigativeAction(action.Action):
    """
    An investigative action is something that may be done or performed within
    the context of an investigation, typically to examine or analyze evidence or
    other data.
    """

    wasInformedBy: Optional["InvestigativeAction"] = None


class Investigation(core.ContextualCompilation):
    """
    An investigation is a grouping of characteristics unique to an exploration
    of the facts involved in a cyber-relevant set of suspicious activity.
    """

    relevantAuthorization: Optional[Authorization] = None
    endTime: Optional[AwareDatetime] = None
    startTime: Optional[AwareDatetime] = None
    investigationStatus: Optional[str] = None
    focus: Optional[str] = None
    investigationForm: Optional[vocabulary.InvestigationFormVocab] = None
