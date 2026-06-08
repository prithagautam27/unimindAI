from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chatbot_service import get_chatbot_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/api/chat")
def chat(request: ChatRequest):

    response = get_chatbot_response(request.message)

    return {
        "success": True,
        "response": response
    }