from fastapi import FastAPI, HTTPException

from app.service import AIChatService
from app.schemas import ChatRequest, ChatResponse


# Application
app = FastAPI(title="tourist-ai", version="1.0.0")


# Services
ai_chat_service = AIChatService()


# API Endpoints
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response_content = ai_chat_service.chat(request.message)
        
        return ChatResponse(response=response_content)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
