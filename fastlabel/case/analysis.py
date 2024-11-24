"""
Auto-generated classes from the SHACL graph in analysis.ttl.

This file was generated using the `case_models.py` script.
"""

from enum import Enum
from typing import Any, Optional

from fastlabel.case import action, core


class Analysis(action.Action):
    """
    An analysis is an action of detailed examination of something in order to
    understand its nature, context or essential features.
    """

    pass


class AnalyticResultFacet(core.Facet):
    """
    An analytic result facet is a grouping of characteristics unique to the
    results of an analysis action.
    """

    pass


class ArtifactClassification(core.UcoInherentCharacterizationThing):
    """
    An artifact classification is a single specific assertion that a particular
    class of a classification taxonomy applies to something.
    """

    classificationConfidence: Optional[float] = None
    class_: str


class AnalyticResult(core.Assertion):
    """
    An analytic result is a characterization of the understanding resulting from
    an analysis action.
    """

    originatingAnalysis: Optional[Analysis] = None
    resultContent: Optional[core.UcoObject] = None


class ArtifactClassificationResultFacet(AnalyticResultFacet):
    """
    An artifact classification result facet is a grouping of characteristics
    unique to the results of an artifact classification analysis action.
    """

    classification: Optional[ArtifactClassification] = None
