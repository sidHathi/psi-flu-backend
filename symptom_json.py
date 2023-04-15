from pydantic import BaseModel

class HeadSymptoms(BaseModel):
    headache = False
    nausea = False
    dizziness = False

class EyeSymptoms(BaseModel):
    red_eyes = False
    watery_eyes = False
    itchy_eyes = False
    sensitivity_to_light = False

class MouthSymptoms(BaseModel):
    dry_mouth = False
    loss_of_taste = False

class NasalSymptoms(BaseModel):
    congestion = False
    runny_or_stuffy_nose = False
    loss_of_smell = False
    sneezing = False

class ChestSymptoms(BaseModel):
    cough = False
    chest_pain = False
    shortness_of_breath = False

class ThroatSymptoms(BaseModel):
    sore_throat = False
    dry_throat = False
    difficulty_swallowing = False
    swollen_lymph_nodes = False

class SkinSymptoms(BaseModel):
    rash = False

class AbdominalSymptoms(BaseModel):
    vomiting = False
    diarrhea = False
    abdominal_pain = False

class FullBodySymptoms(BaseModel):
    fever = False
    fatigue = False
    chills = False
    sweating = False
    body_aches = False
    joint_pain = False
    muscle_weakness = False
    weight_loss = False
    stiff_neck = False

class Symptoms(BaseModel):
    head_symptoms: HeadSymptoms
    eye_symptoms: EyeSymptoms
    mouth_symptoms: MouthSymptoms
    nasal_symptoms: NasalSymptoms
    chest_symptoms: ChestSymptoms
    throat_symptoms: ThroatSymptoms
    skin_symptoms: SkinSymptoms
    abdominal_symptoms: AbdominalSymptoms
    full_body_symptoms: FullBodySymptoms