"""
Auto-generated classes from the SHACL graph in pattern.ttl.

This file was generated using the `case_models.py` script.
"""

from fastlabel.uco import core


class Pattern(core.UcoObject):
    """
    A pattern is a combination of properties, acts, tendencies, etc., forming a
    consistent or characteristic arrangement.
    """


class PatternExpression(core.UcoInherentCharacterizationThing):
    """
    A pattern expression is a grouping of characteristics unique to an explicit
    logical expression defining a pattern (e.g., regular expression, SQL Select
    expression, etc.).
    """


class LogicalPattern(Pattern):
    """
    A logical pattern is a grouping of characteristics unique to an
    informational pattern expressed via a structured pattern expression
    following the rules of logic.
    """

    patternExpression: str | None = None
