"""
Manually-created file that centralizes all the logic for UCO/CASE by hijacking
`owl.Thing`.
"""

from typing import Type

from pydantic import BaseModel, model_serializer, ConfigDict

def get_full_qualname(type: Type) -> str:
    """
    Get the fully qualified class name of a provided class.

    From https://stackoverflow.com/questions/2020014
    """
    return ".".join([type.__module__, type.__name__])

def get_field_names(cls: Type) -> dict[str, str]:
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
        annotations = getattr(base, '__annotations__', {})
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
    model_config = ConfigDict(extra='forbid') 
    
    # Consistent with UcoThing declared at 
    # https://github.com/casework/CASE-Mapping-Python/blob/main/case_mapping/base.py#L23
    prefix_iri: str = "http://example.org/kb/"
    prefix_label: str = "kb:"

    @model_serializer()
    def serialize_model(self):
        """
        Serialize the model.
        """
        result = {}
        
        # Mutate all field names according to the *top* class they belong to.
        field_mapping = get_field_names(type(self))
        
        # Add each field to the dictionary
        for field in self.model_fields:
            # Get the value of the field
            value = getattr(self, field)
            
            # Always exclude unset fields and those related to the model configuration
            if value is None:
                continue
            if field in ["prefix_iri", "prefix_label"]:
                continue
            
            # If the field is not a basic JSON type (str, int, float, bool, list, dict)
            # then it must be represented in the {"@type": "...", "@value": "..." format.}
            # TODO: the above
            
            # Get the corresponding field name in the JSON-LD mapping
            field_name = field_mapping[field]
            
            if isinstance(value, BaseModel):
                result[field_name] = value.model_dump()
            else:
                result[field_name] = value
        
        return result
    