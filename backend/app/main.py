from fastapi import FastAPI, HTTPException
from bson import ObjectId

from fastapi import FastAPI
from app.routes.routes import router

app = FastAPI()

app.include_router(router)