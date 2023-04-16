from typing import Optional
from pydantic import BaseModel
from models.symptom_models.abdominal_symptoms_model import AbdominalSymptoms, AbdominalSymptomsUpdate
from models.symptom_models.chest_symptoms_model import ChestSymptoms, ChestSymptomsUpdate
from models.symptom_models.eye_symptoms_model import EyeSymptoms, EyeSymptomsUpdate
from models.symptom_models.full_body_symptoms_model import FullBodySymptoms, FullBodySymptomsUpdate
from models.symptom_models.head_symptoms_model import HeadSymptoms, HeadSymptomsUpdate
from models.symptom_models.mouth_symptoms_model import MouthSymptoms, MouthSymptomsUpdate
from models.symptom_models.nasal_symptoms_model import NasalSymptoms, NasalSymptomsUpdate
from models.symptom_models.skin_symptoms_model import SkinSymptoms, SkinSymptomsUpdate
from models.symptom_models.throat_symptoms_model import ThroatSymptoms, ThroatSymptomsUpdate

class Symptoms(BaseModel):
    abdominal_symptoms: AbdominalSymptoms = AbdominalSymptoms()
    chest_symptoms: ChestSymptoms = ChestSymptoms()
    eye_symptoms: EyeSymptoms = EyeSymptoms()
    full_body_symptoms: FullBodySymptoms = FullBodySymptoms()
    head_symptoms: HeadSymptoms = HeadSymptoms()
    mouth_symptoms: MouthSymptoms = MouthSymptoms()
    nasal_symptoms: NasalSymptoms = NasalSymptoms()
    skin_symptoms: SkinSymptoms = SkinSymptoms()
    throat_symptoms: ThroatSymptoms = ThroatSymptoms()

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