"""
Manually-created file that centralizes all the logic for UCO/CASE by hijacking
`owl.Thing`.
"""

import datetime
import uuid
from typing import Any, Type

from pydantic import BaseModel, ConfigDict, Field, computed_field, model_serializer


def get_full_qualname(type: Type[Any]) -> str:
    """
    Get the fully qualified class name of a provided class.

    From https://stackoverflow.com/questions/2020014
    """
    return ".".join([type.__module__, type.__name__])


def get_class_as_jsonld(type: Type[Any]) -> str:
    """
    Get the fully qualified class name of a provided class, but in the format
    that JSON-LD expects.
    """
    module, lib = type.__module__.split(".")[-2:]
    return f"{module}-{lib}:{type.__name__}"


def get_field_names(cls: Type[Any]) -> dict[str, str]:
    """
    Returns a mapping from field names to the equivalent json-ld name that should
    be used, based on the path to the class where they were originally defined.

    Partially written by Copilot using o1-preview
    """
    field_origins = {}
    # Traverse the MRO in reverse to start from base classes
    for base in reversed(cls.__mro__):
        if base is object:
            continue  # Skip base object class
        annotations = getattr(base, "__annotations__", {})
        for field_name in annotations:
            if field_name not in field_origins:
                try:
                    module, lib = base.__module__.split(".")[-2:]
                    field_origins[field_name] = f"{module}-{lib}:{field_name}"
                except Exception:
                    pass
    return field_origins


class Thing(BaseModel):
    """
    The effective top-level class of the entire thing.

    Technically, this should all be contained in UcoThing, but because UcoThing itself subclasses
    owl:Thing, this effectively becomes the parent.
    """

    # Raise when unrecognized fields are present.
    model_config = ConfigDict(extra="forbid")

    # Consistent with UcoThing declared at
    # https://github.com/casework/CASE-Mapping-Python/blob/main/case_mapping/base.py#L23
    prefix_iri: str = "http://example.org/kb/"
    prefix_label: str = "kb:"

    # Internal ID, used to generate @id
    internal_id: uuid.UUID = Field(default_factory=uuid.uuid4)

    # mypy does not support decorated properties
    @computed_field  # type: ignore[misc]
    @property
    def computed_id(self) -> str:
        return self.prefix_label + str(self.internal_id)

    @model_serializer()
    def serialize_model(self) -> dict[str, Any]:
        """
        Serialize the model.
        """
        result: dict[str, Any] = {}

        # Include the @id and @type fields
        result["@id"] = self.computed_id
        result["@type"] = get_class_as_jsonld(type(self))

        # Mutate all field names according to the *top* class they belong to.
        field_mapping = get_field_names(type(self))

        # Add each field to the dictionary
        for field, field_info in self.model_fields.items():
            # Get the value of the field
            value = getattr(self, field)

            # Always exclude unset fields and those considered internal
            if value is None:
                continue
            if isinstance(value, list) and len(value) == 0:
                continue
            if field in ["prefix_iri", "prefix_label", "internal_id"]:
                continue

            # Get the corresponding field name in the JSON-LD mapping
            field_name = field_mapping[field]

            # If the field is not a basic JSON type (str, int, float, bool, list, dict)
            # then it must be represented in the {"@type": "...", "@value": "..." format.}
            if isinstance(value, datetime.datetime):
                result[field_name] = {
                    "@type": "xsd:dateTime",
                    "@value": value.isoformat(timespec="milliseconds"),
                }
                continue
            elif type(value) not in (str, int, float, bool, list, dict):
                result[field_name] = {
                    "@type": get_class_as_jsonld(type(value)),
                    "@value": value,
                }
                continue

            # mypy: trust me it's not going to be a callable
            if (
                field_info.json_schema_extra
                and "IRI" in field_info.json_schema_extra.keys()  # type: ignore[union-attr]
            ):
                # This field is an IRI, so we should only include the @id and move on
                result[field_name] = {"@id": value.computed_id}
                continue

            if isinstance(value, BaseModel):
                result[field_name] = value.model_dump()
            else:
                result[field_name] = value

        return result
