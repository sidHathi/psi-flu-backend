from models.symptom_models.all_symptoms_model import Symptoms, SymptomsUpdate
from pydantic import BaseModel, Extra, Field, EmailStr, constr
from datetime import datetime
from typing import Optional

class User(BaseModel):
    email: str
    role: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
    symptoms: Symptoms = Symptoms()

    class Config:
        orm_mode = True

class UserUpdate(BaseModel):
    symptoms: Optional[SymptomsUpdate]
    updated_at: datetime | None = None


class CreateUserSchema(User):
    password: constr(min_length=8)
    passwordConfirm: str


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponseSchema(User):
    id: str
    pass

class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema

class UserEditResponse(BaseModel):
    status:str
    user: User