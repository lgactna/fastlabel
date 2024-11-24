"""
Auto-generated classes from the SHACL graph in victim.ttl.

This file was generated using the `case_models.py` script.
"""

from enum import Enum
from typing import Any, Optional

from fastlabel.case import role


class Victim(role.NeutralRole):
    """
    A victim is a role played by a person or organization that is/was the target
    of some malicious action.
    """

    pass


class VictimTargeting(Victim):
    """
    A victim targeting is a grouping of characteristics unique to people or
    organizations that are the target of some malicious activity.
    """

    pass
