from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/")
async def root():
    return {"message": "Welcome to Axiomind API v1"}
