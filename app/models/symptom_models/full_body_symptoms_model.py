from typing import Optional
from pydantic import BaseModel, Extra

class FullBodySymptoms(BaseModel):
    fever: bool = False
    fatigue: bool = False
    chills: bool = False
    sweating: bool = False
    body_aches: bool = False
    joint_pain: bool = False
    muscle_weakness: bool = False
    weight_loss: bool = False
    stiff_neck: bool = False

class FullBodySymptomsUpdate(BaseModel):
    fever: Optional[bool]
    fatigue: Optional[bool]
    chills: Optional[bool]
    sweating: Optional[bool]
    body_aches: Optional[bool]
    joint_pain: Optional[bool]
    muscle_weakness: Optional[bool]
    weight_loss: Optional[bool]
    stiff_neck: Optional[bool]