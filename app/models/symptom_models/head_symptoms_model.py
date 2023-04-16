from typing import Optional
from pydantic import BaseModel

class HeadSymptoms(BaseModel):
    headache: bool = False
    nausea: bool = False
    dizziness: bool = False

class HeadSymptomsUpdate(BaseModel):
    headache: Optional[bool]
    nausea: Optional[bool]
    dizziness: Optional[bool]