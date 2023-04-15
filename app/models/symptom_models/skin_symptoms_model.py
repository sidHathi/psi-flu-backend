from typing import Optional
from pydantic import BaseModel, Extra

class SkinSymptoms(BaseModel):
    rash: bool = False

class SkinSymptomsUpdate(BaseModel):
    rash: Optional[bool]