"""
Auto-generated classes from the SHACL graph in victim.ttl.

This file was generated using the `case_models.py` script.
"""

from fastlabel.uco import role


class Victim(role.NeutralRole):
    """
    A victim is a role played by a person or organization that is/was the target
    of some malicious action.
    """


class VictimTargeting(Victim):
    """
    A victim targeting is a grouping of characteristics unique to people or
    organizations that are the target of some malicious activity.
    """
