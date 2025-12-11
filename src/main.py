from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from ai import MultiAgentGraph


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


app = FastAPI(title="tourist-ai", version="1.0.0")


multi_agent_graph = MultiAgentGraph()


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        result = multi_agent_graph.execute(request.message)
        
        if result and "messages" in result and result["messages"]:
            last_message = result["messages"][-1]
            response_content = last_message.content
        else:
            raise HTTPException(status_code=500, detail="No response from agents.")
            
        return ChatResponse(response=response_content)
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
