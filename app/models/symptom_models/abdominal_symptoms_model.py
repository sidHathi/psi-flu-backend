from typing import Optional
from pydantic import BaseModel

class AbdominalSymptoms(BaseModel):
    vomiting: bool = False
    diarrhea: bool = False
    abdominal_pain: bool = False

class AbdominalSymptomsUpdate(BaseModel):
    vomiting: Optional[bool]
    diarrhea: Optional[bool]
    abdominal_pain: Optional[bool]