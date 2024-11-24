"""
Auto-generated classes from the SHACL graph in role.ttl.

This file was generated using the `case_models.py` script.
"""

from typing import Any, Optional

from fastlabel.case import core


class Role(core.UcoObject):
    """
    A role is a usual or customary function based on contextual perspective.
    """

    pass


class BenevolentRole(Role):
    """
    A benevolent role is a role with positive and/or beneficial intent.
    """

    pass


class MaliciousRole(Role):
    """
    A malicious role is a role with malevolent intent.
    """

    pass


class NeutralRole(Role):
    """
    A neutral role is a role with impartial intent.
    """

    pass
