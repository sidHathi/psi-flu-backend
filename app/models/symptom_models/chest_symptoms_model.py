from typing import Optional
from pydantic import BaseModel

class ChestSymptoms(BaseModel):
    cough: bool = False
    chest_pain: bool = False
    shortness_of_breath: bool = False

class ChestSymptomsUpdate(BaseModel):
    cough: Optional[bool]
    chest_pain: Optional[bool]
    shortness_of_breath: Optional[bool]