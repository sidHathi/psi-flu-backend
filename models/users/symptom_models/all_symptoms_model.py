from typing import Optional
from pydantic import BaseModel, Extra
from models.users.symptom_models.abdominal_symptoms_model import AbdominalSymptoms, AbdominalSymptomsUpdate
from models.users.symptom_models.chest_symptoms_model import ChestSymptoms, ChestSymptomsUpdate
from models.users.symptom_models.eye_symptoms_model import EyeSymptoms, EyeSymptomsUpdate
from models.users.symptom_models.full_body_symptoms_model import FullBodySymptoms, FullBodySymptomsUpdate
from models.users.symptom_models.head_symptoms_model import HeadSymptoms, HeadSymptomsUpdate
from models.users.symptom_models.mouth_symptoms_model import MouthSymptoms, MouthSymptomsUpdate
from models.users.symptom_models.nasal_symptoms_model import NasalSymptoms, NasalSymptomsUpdate
from models.users.symptom_models.skin_symptoms_model import SkinSymptoms, SkinSymptomsUpdate
from models.users.symptom_models.throat_symptoms_model import ThroatSymptoms, ThroatSymptomsUpdate

class Symptoms(BaseModel):
    abdominal_symptoms: AbdominalSymptoms
    chest_symptoms: ChestSymptoms
    eye_symptoms: EyeSymptoms
    full_body_symptoms: FullBodySymptoms
    head_symptoms: HeadSymptoms
    mouth_symptoms: MouthSymptoms
    nasal_symptoms: NasalSymptoms
    skin_symptoms: SkinSymptoms
    throat_symptoms: ThroatSymptoms

class SymptomsUpdate(BaseModel):
    abdominal_symptoms: Optional[AbdominalSymptomsUpdate]
    chest_symptoms: Optional[ChestSymptomsUpdate]
    eye_symptoms: Optional[EyeSymptomsUpdate]
    full_body_symptoms: Optional[FullBodySymptomsUpdate]
    head_symptoms: Optional[HeadSymptomsUpdate]
    mouth_symptoms: Optional[MouthSymptomsUpdate]
    nasal_symptoms: Optional[NasalSymptomsUpdate]
    skin_symptoms: Optional[SkinSymptomsUpdate]
    throat_symptoms: Optional[ThroatSymptomsUpdate]