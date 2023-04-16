from typing import Optional
from pydantic import BaseModel

class EyeSymptoms(BaseModel):
    red_eyes: bool = False
    watery_eyes: bool = False
    itchy_eyes: bool = False
    sensitivity_to_light: bool = False

class EyeSymptomsUpdate(BaseModel):
    red_eyes: Optional[bool]
    watery_eyes: Optional[bool]
    itchy_eyes: Optional[bool]
    sensitivity_to_light: Optional[bool]