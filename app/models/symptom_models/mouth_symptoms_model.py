from typing import Optional
from pydantic import BaseModel

class MouthSymptoms(BaseModel):
    dry_mouth: bool = False
    loss_of_taste: bool = False

class MouthSymptomsUpdate(BaseModel):
    dry_mouth: Optional[bool]
    loss_of_taste: Optional[bool]