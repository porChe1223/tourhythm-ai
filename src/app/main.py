from fastapi import FastAPI, HTTPException, BackgroundTasks

from app.service import AIChatService, save_chat_data, call_optimize
from app.schemas import ChatRequest, ChatResponse


# Application
app = FastAPI(title="tourhythm-ai", version="1.0.0")


# Services
ai_chat_service = AIChatService()


# API Endpoints
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest, background_tasks: BackgroundTasks):
    try:
        # Get AI chat response
        response_content, full_result = ai_chat_service.chat(request.message)
        
        # Save Messages in Background
        background_tasks.add_task(save_chat_data, full_result)
        background_tasks.add_task(call_optimize, full_result)
        
        return ChatResponse(response=response_content)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
