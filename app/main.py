from fastapi import FastAPI
from app.api.v1 import api

app = FastAPI(title="User Management Microservice")

@app.get("/health")
def health_check():
    return {"status": "ok", "service": "User Management Microservice"}

app.include_router(api.router, prefix="/v1", tags=["api"])
