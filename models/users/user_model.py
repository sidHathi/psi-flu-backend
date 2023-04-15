from models.users.symptom_models.all_symptoms_model import Symptoms, SymptomsUpdate
from pydantic import BaseModel, Extra, Field, EmailStr, constr
import uuid
from datetime import datetime
from typing import Optional

class User(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    email: str
    role: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    symptoms: Symptoms

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    symptoms: Optional[SymptomsUpdate]
    updated_at: datetime | None = None