"""
Internal, Python-specific utilities that support the UCO ontology.
"""

from typing import Annotated, Any, Generic, TypeAlias, TypeVar

from pydantic import WithJsonSchema

# Define a type variable to use with the generic IRI type
T = TypeVar("T")

# Define a type alias for the Annotated type
IRIType: TypeAlias = Annotated[T, WithJsonSchema({"IRI": True})]


class IRI(Generic[T]):
    """
    Class used to annotate a type as an IRI. This is used to indicate that on serialiation,
    only the IRI should be used, rather than the full object.

    The net result is that only the "@id" field is serialized, and nothing else.
    """

    def __class_getitem__(cls, item: T) -> IRIType[Any]:
        return Annotated[item, WithJsonSchema({"IRI": True})]
