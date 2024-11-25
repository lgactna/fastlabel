"""
Manually-created file that centralizes all the logic for UCO/CASE by hijacking
`owl.Thing`.
"""

import datetime
import uuid
from enum import Enum
from typing import Any, Type, TypeVar

from pydantic import BaseModel, ConfigDict, Field, computed_field, model_serializer

# Used to denote that Thing.ref() returns the same type.
T = TypeVar("T", bound="Thing")


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

    # If this is a member of the uco.XMLSchema library, we perform special handling
    if module == "uco" and lib == "XMLSchema":
        return f"xsd:{type.__name__.replace('xsd_', '')}"

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


def dump_scalar(value: Any) -> Any:
    # If the field is an enum, get the underlying value and work form there
    if isinstance(value, Enum):
        value = value.value

    # If the field is a scalar...
    if isinstance(value, Thing):
        # If the field is itself a Thing, we must recursively dump it,
        # unless it is a reference.
        if value._is_reference:
            return {"@id": value.computed_id}
        return value.model_dump()

    if type(value) in (str, int, float, bool, dict):
        # If the field is a basic type, we can just dump it.
        return value

    if isinstance(value, datetime.datetime):
        # Dates must be handled specially.
        return {
            "@type": "xsd:dateTime",
            "@value": value.isoformat(timespec="milliseconds"),
        }

    # If the field is not a basic type, it must be represented in the
    # `{"@type": "...", "@value": "..."}` format.
    return {
        "@type": get_class_as_jsonld(type(value)),
        "@value": str(value),
    }


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
    _prefix_iri: str = "http://example.org/kb/"
    _prefix_label: str = "kb:"

    # Internal ID, used to generate @id
    internal_id: uuid.UUID = Field(default_factory=uuid.uuid4)

    # Whether this object should be serialized as a reference, i.e. only its @id
    # should be printed out. When attaching this object as a reference elsewhere,
    # you should use the `ref()` method to get a copy of this object marked as a
    # reference.
    _is_reference: bool = False

    # mypy does not support decorated properties
    @computed_field  # type: ignore[misc]
    @property
    def computed_id(self) -> str:
        return self._prefix_label + str(self.internal_id)

    @model_serializer()
    def serialize_model(self) -> dict[str, Any]:
        """
        Serialize the model.
        """
        # If this object is a reference, only print out the @id and move on.
        if self._is_reference:
            return {"@id": self.computed_id}

        result: dict[str, Any] = {}

        # Include the @id and @type fields
        result["@id"] = self.computed_id
        result["@type"] = get_class_as_jsonld(type(self))

        # If the context is specified, attach it
        if hasattr(self, "_context"):
            result["@context"] = self._context

        # Mutate all field names according to the *top* class they belong to.
        field_mapping = get_field_names(type(self))

        # Add each field to the dictionary
        for field, _field_info in self.model_fields.items():
            # Get the value of the field
            value = getattr(self, field)

            # Always exclude unset fields and those considered internal
            if value is None:
                continue
            if isinstance(value, list) and len(value) == 0:
                continue
            if field.startswith("_") or field in ["model_config", "internal_id"]:
                continue

            # Get the corresponding field name in the JSON-LD mapping
            field_name = field_mapping[field]

            # If the value is a list, we must dump each value individually.
            # Otherwise, just the sole value can be dumped.
            if isinstance(value, list):
                result[field_name] = [dump_scalar(v) for v in value]
                continue
            else:
                result[field_name] = dump_scalar(value)

        return result

    def ref(self: T) -> T:
        """
        Return a copy of this object marked as a "reference". The object
        will be printed out as a reference when serialized.

        Note that this is NOT a deep copy. You can think of this as just attaching
        the @id of the object to something else.
        """
        return self.model_copy(update={"_is_reference": True})
