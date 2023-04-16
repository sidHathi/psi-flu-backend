from typing import Optional
from pydantic import BaseModel

class ThroatSymptoms(BaseModel):
    sore_throat: bool = False
    dry_throat: bool = False
    difficulty_swallowing: bool = False
    swollen_lymph_nodes: bool = False

class ThroatSymptomsUpdate(BaseModel):
    sore_throat: Optional[bool]
    dry_throat: Optional[bool]
    difficulty_swallowing: Optional[bool]
    swollen_lymph_nodes: Optional[bool]