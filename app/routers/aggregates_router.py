from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List
from config import settings
from pymongo import MongoClient
from models.aggregates_model import AggregateMetrics
import json

router = APIRouter()

# class AggregateMetrics(BaseModel):
#     timestamp: datetime | None = datetime.now()
#     symptoms_sorted_by_count_desc: list = default_list
#     current_number_of_infections: int = 0
#     number_of_users: int = 0
#     new_infections_in_last_week: int = 0
#     symptom_counts: AggregateSymptomCounts = AggregateSymptomCounts()


@router.get("/four_trending_symptoms", response_description="Get list of symptoms sorting by frequency in decreasing order")
def get_symptoms_sorted_by_count_desc(request: Request, response: Response):
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.DB_NAME]
    
    if (symptoms := db["current_aggregates"].find_one({})["symptoms_sorted_by_count_desc"]) is not None:
        res = []
        res.append({"symptom": symptoms[0], "count": db["current_aggregates"].find_one({})["symptom_counts"][symptoms[0]]})
        res.append({"symptom": symptoms[1], "count": db["current_aggregates"].find_one({})["symptom_counts"][symptoms[1]]})
        res.append({"symptom": symptoms[2], "count": db["current_aggregates"].find_one({})["symptom_counts"][symptoms[2]]})
        res.append({"symptom": symptoms[3], "count": db["current_aggregates"].find_one({})["symptom_counts"][symptoms[3]]})

        print(res)

        return json.dumps(res)

    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot find trending symptoms")


@router.get("/infected", response_description="Get current number of infected users", response_model=int)
def get_infected_user_count(request: Request, response: Response):
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.DB_NAME]
    if (count := db["current_aggregates"].find_one({})["current_number_of_infections"]) >= 0:
        return count
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot find number of infected users")


@router.get("/num_users", response_description="Get the total number of users on the platform", response_model=int)
def get_total_user_count(request: Request, response: Response):
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.DB_NAME]
    if (count := db["current_aggregates"].find_one({})["number_of_users"]) >= 0:
        return count
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot find total number of users")


@router.get("/new_infections", response_description="Get the number of new infections in the last week", response_model=int)
def get_number_of_new_infections(request: Request, response: Response):
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.DB_NAME]
    collection = db["aggregates_by_week"]
    id = collection.count_documents({})
    if (count := collection.find_one({"_id": id})["new_infections_in_last_week"]) >= 0:
        return count
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot find number of new infections in last week")


@router.get("/infected_last_4_weeks", response_description="Get an array of length 4 containing the total number of infected users \
            from 3 weeks ago, 2 weeks ago, 1 week ago, and this week, respectively", response_model=list)
def get_infected_last_4_weeks(request: Request, response: Response):
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.DB_NAME]
    collection = db["aggregates_by_week"]
    id = collection.count_documents()

    infection_counts = []

    if (count := collection.find_one({"_id": id-3})["current_number_of_infections"]) >= 0:
        infection_counts.append(collection.find_one({"_id": id-3})["current_number_of_infections"])
    
    if (count := collection.find_one({"_id": id-2})["current_number_of_infections"]) >= 0:
        infection_counts.append(collection.find_one({"_id": id-2})["current_number_of_infections"])
    
    if (count := collection.find_one({"_id": id-1})["current_number_of_infections"]) >= 0:
        infection_counts.append(collection.find_one({"_id": id-1})["current_number_of_infections"])
    
    if (count := collection.find_one({"_id": id})["current_number_of_infections"]) >= 0:
        infection_counts.append(collection.find_one({"_id": id})["current_number_of_infections"])
    
    if (len(infection_counts) == 4):
        return infection_counts

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Cannot find infection counts from last 4 weeks")