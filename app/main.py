from fastapi import FastAPI
from config import settings
from routers import auth_router, users_router, aggregates_router
from fastapi.middleware.cors import CORSMiddleware

import pymongo
from pymongo import mongo_client, MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

app = FastAPI()

origins = [
    settings.CLIENT_ORIGIN,
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = mongo_client.MongoClient(
    settings.MONGO_URI, 
    serverSelectionTimeoutMS=5000
)

def check_env():
    assert settings.MONGO_URI is not None
    assert settings.DB_NAME is not None
    assert settings.USERS_COL is not None

@app.on_event('startup')
def startup_db_client():
    check_env()

    app.mongodb_client: MongoClient = mongo_client.MongoClient(
        settings.MONGO_URI, 
        serverSelectionTimeoutMS=5000
    )
    app.db: Database = app.mongodb_client[settings.DB_NAME]


@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()
    

app.include_router(auth_router.router, tags=['Auth'], prefix='/api/auth')
app.include_router(users_router.router, tags=['Users'], prefix='/api/users')
app.include_router(aggregates_router.router, tags=['Aggregates'], prefix='/api/aggregates')

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8765,
        log_level="debug",
        reload=True,
    )