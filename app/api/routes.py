from fastapi import APIRouter
from pydantic import BaseModel

from services.llm_service import LLMService

router = APIRouter()

class PromptRequest(BaseModel):
    query: str

@router.get("/")
def home():
    return {
        "message": "Welcome to the AI Travel Planner"
    }
    
@router.get("/health")
def health_check():
    return {
        "status": "Running"
    }
    
@router.post("/chat")
def chat(request: PromptRequest):
    response = LLMService.ask(request.query)
    return {
        "response": response
    }