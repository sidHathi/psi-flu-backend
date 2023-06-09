from typing import Optional
from pydantic import BaseModel, Extra

class NasalSymptoms(BaseModel):
    congestion: bool = False
    runny_nose: bool = False
    loss_of_smell: bool = False
    sneezing: bool = False

class NasalSymptomsUpdate(BaseModel):
    congestion: Optional[bool]
    runny_nose: Optional[bool]
    loss_of_smell: Optional[bool]
    sneezing: Optional[bool]