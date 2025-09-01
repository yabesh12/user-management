from fastapi import FastAPI
from app.api.v1 import api

app = FastAPI(title="FastAPI Microservice")

app.include_router(api.router, prefix="/v1", tags=["api"])
