from fastapi import APIRouter

router = APIRouter()


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