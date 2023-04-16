from typing import Optional
from pydantic import BaseModel

class AbdominalSymptoms(BaseModel):
    vomitting: bool = False
    diarrhea: bool = False
    abdominal_pain: bool = False

class AbdominalSymptomsUpdate(BaseModel):
    vomitting: Optional[bool]
    diarrhea: Optional[bool]
    abdominal_pain: Optional[bool]