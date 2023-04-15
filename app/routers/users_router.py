from fastapi import APIRouter, Body, Request, Response, HTTPException, status, Depends
from datetime import datetime
from bson.objectid import ObjectId
from serializers.userSerializers import userResponseEntity
from fastapi.encoders import jsonable_encoder
from typing import List
from models.user_models import User, UserUpdate

from database import User
from models import user_models as schemas
import oauth2

router = APIRouter()

@router.get('/me', response_model=schemas.UserResponse)
def get_me(user_id: str = Depends(oauth2.require_user)):
    user = userResponseEntity(User.find_one({'_id': ObjectId(str(user_id))}))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid user jwt")
    return {"status": "success", "user": user}


@router.put("/me", response_description="Update a user's symptoms", response_model=schemas.UserEditResponse)
def update_user(request: Request, user: UserUpdate = Body(...), user_id: str = Depends(oauth2.require_user)):
    user.updated_at = datetime.now()
    user = {k: v for k, v in user.dict().items() if v is not None}
    if len(user) >= 1:
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
    delete_result = request.app.db["users"].delete_one({"_id": ObjectId(str(user_id))})

    if delete_result.deleted_count == 1:
        response.status_code = status.HTTP_204_NO_CONTENT
        return response

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {user_id} not found")