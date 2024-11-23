"""
Generate models from the GRR library.
"""

from pydantic import BaseModel

class GRRModel(BaseModel):
    """
    Generic representation of a GRR artifact.
    
    The artifact may be written out as a separate Pydantic model with class 
    variables declared, at which point it is up to you to declare any 
    """
    pass