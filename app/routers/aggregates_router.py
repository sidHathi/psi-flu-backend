from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models.aggregates_model import AggregateMetrics

router = APIRouter()

# @router.post("/", response_description="Create new aggregate metrics entry", status_code=status.HTTP_201_CREATED, response_model=AggregateMetrics)
# def create_book(request: Request, book: Book = Body(...)):
#     book = jsonable_encoder(book)
#     new_book = request.app.database["books"].insert_one(book)
#     created_book = request.app.database["books"].find_one(
#         {"_id": new_book.inserted_id}
#     )

#     return created_book