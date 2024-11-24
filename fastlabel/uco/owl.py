"""
Manually-created file that centralizes all the logic for UCO/CASE by hijacking
`owl.Thing`.
"""

from pydantic import BaseModel


class Thing(BaseModel):
    """
    The effective top-level class of the entire thing.
    """
