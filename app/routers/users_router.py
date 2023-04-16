from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends
from datetime import datetime
from bson.objectid import ObjectId
from serializers.userSerializers import userResponseEntity
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import List
from models.user_models import User, UserUpdate
from database import User
from models import user_models as schemas
import oauth2
from config import settings
from aggregate_metrics_functions import decrement_user_count, increment_number_of_infections, decrement_number_of_infections
from aggregate_metrics_functions import increment_symptom_count, decrement_symptom_count, increment_new_infections_in_last_week
from pymongo import MongoClient
import json

router = APIRouter()

@router.get('/me', response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid user jwt")
    return {"status": "success", "user": user}

@router.get('/similar', response_description="For each sympton you have, give the number of OTHER people who have this symptom")
def get_similar_symptom_counts(user_id: str = Depends(oauth2.require_user)):
    user_symptoms = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))["symptoms"]
    if user_symptoms is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid user jwt")
    
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.DB_NAME]
    similar_symptoms = dict()

    for symptom_type in user_symptoms:
        for symptom in user_symptoms[symptom_type]:
            if user_symptoms[symptom_type][symptom]:
                similar_symptoms[symptom] = db["current_aggregates"].find_one({})["symptom_counts"][symptom] - 1

    return JSONResponse(content=jsonable_encoder(similar_symptoms))


@router.put("/me", response_description="Update a user's symptoms", response_model=schemas.UserEditResponse)
def update_user(request: Request, user: UserUpdate = Body(...), user_id: str = Depends(oauth2.require_user)):
    user.updated_at = datetime.now()
    user = {k: v for k, v in user.dict().items() if v is not None}
    if len(user) >= 1:
        # update data in current_aggregates collection
        client = MongoClient(settings.MONGO_URI)
        db = client[settings.DB_NAME]

        was_infected = False
        is_infected = False
        old_user_data = db["users"].find_one({"_id": ObjectId(str(user_id))})
        for symptom_type in old_user_data["symptoms"]:
            for symptom in old_user_data["symptoms"][symptom_type]:
                # see if user was infected
                if old_user_data["symptoms"][symptom_type][symptom]:
                    was_infected = True
                    # see if symptom has gone away
                    if not user["symptoms"][symptom_type][symptom]:
                        decrement_symptom_count(settings.MONGO_URI, settings.DB_NAME, symptom)
                    
                # see if user is infected
                if user["symptoms"][symptom_type][symptom]:
                    is_infected = True
                    # see if symptom is new
                    if not old_user_data["symptoms"][symptom_type][symptom]:
                        increment_symptom_count(settings.MONGO_URI, settings.DB_NAME, symptom) 

        if was_infected and not is_infected:
            decrement_number_of_infections(settings.MONGO_URI, settings.DB_NAME)
        elif not was_infected and is_infected:
            increment_number_of_infections(settings.MONGO_URI, settings.DB_NAME)
            increment_new_infections_in_last_week(settings.MONGO_URI, settings.DB_NAME)

        
        # update data in user collection
        update_result = request.app.db["users"].update_one(
            {"_id": ObjectId(str(user_id))}, {"$set": user}
        )

        if update_result.modified_count == 0:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")

    if (
        existing_user := request.app.db["users"].find_one({"_id": ObjectId(str(user_id))})
    ) is not None:
        return {"status": "success", "user": existing_user}

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")


@router.delete("/me", response_description="Delete a user")
def delete_user(request: Request, response: Response, user_id: str = Depends(oauth2.require_user)):
    # get data on user before attempting to remove
    client = MongoClient(settings.MONGO_URI)
    db = client[settings.DB_NAME]
    user_symptoms = []
    was_infected = False
    for symptom_type in db["users"].find_one({"_id": ObjectId(str(user_id))})["symptoms"]:
        for symptom in db["users"].find_one({"_id": ObjectId(str(user_id))})["symptoms"][symptom_type]:
            if db["users"].find_one({"_id": ObjectId(str(user_id))})["symptoms"][symptom_type][symptom]:
                was_infected = True
                user_symptoms.append(symptom)
    
    delete_result = request.app.db["users"].delete_one({"_id": ObjectId(str(user_id))})
    
    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT

        # update data in current_aggregates collection
        decrement_user_count(settings.MONGO_URI, settings.DB_NAME)
        if was_infected:
            decrement_number_of_infections(settings.MONGO_URI, settings.DB_NAME)
        for symptom in user_symptoms:
            decrement_symptom_count(settings.MONGO_URI, settings.DB_NAME, symptom)
        
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")