from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes.user_routes import users_router

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(users_router, tags=["users"], prefix="/users")
# app.include_router(aggregates_router, tags=["aggregates"], prefix="/aggregates")