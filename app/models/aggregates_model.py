# from models.aggregate_sympton_models.aggregate_symptoms_model import AggregateSymptoms, AggregateSymptomsUpdate
# from typing import Optional
from pydantic import BaseModel
from datetime import datetime

default_list = ["vomitting", "diarrhea", "abdominal_pain", "cough", "chest_pain", "shortness_of_breath",
    "red_eyes", "watery_eyes", "itchy_eyes", "sensitivity_to_light", "fever", "fatigue", "chills",
    "sweating", "body_aches", "joint_pain", "muscle_weakness", "weight_loss", "stiff_neck",
    "headache", "nausea", "dizziness", "dry_mouth", "loss_of_taste", "congestion", "runny_nose",
    "loss_of_smell", "sneezing", "rash", "sore_throat", "dry_throat", "difficulty_swallowing",
    "swollen_lymph_nodes"]

class AggregateSymptomCounts(BaseModel):
    vomitting: int = 0
    diarrhea: int = 0
    abdominal_pain: int = 0
    cough: int = 0
    chest_pain: int = 0
    shortness_of_breath: int = 0
    red_eyes: int = 0
    watery_eyes: int = 0
    itchy_eyes: int = 0
    sensitivity_to_light: int = 0
    fever: int = 0
    fatigue: int = 0
    chills: int = 0
    sweating: int = 0
    body_aches: int = 0
    joint_pain: int = 0
    muscle_weakness: int = 0
    weight_loss: int = 0
    stiff_neck: int = 0
    headache: int = 0
    nausea: int = 0
    dizziness: int = 0
    dry_mouth: int = 0
    loss_of_taste: int = 0
    congestion: int = 0
    runny_nose: int = 0
    loss_of_smell: int = 0
    sneezing: int = 0
    rash: int = 0
    sore_throat: int = 0
    dry_throat: int = 0
    difficulty_swallowing: int = 0
    swollen_lymph_nodes: int = 0

class AggregateMetrics(BaseModel):
    timestamp: datetime | None = datetime.now()
    symptoms_sorted_by_count_desc: list = default_list
    current_number_of_infections: int = 0
    number_of_users: int = 0
    new_infections_in_last_week: int = 0
    symptom_counts: AggregateSymptomCounts = AggregateSymptomCounts()