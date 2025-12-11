from ai import MultiAgentGraph


class AIChatService:
    """
    AIChatService
    -------------
    AI chat service
    Use multi-agent-graph from ai/
    """
    def __init__(self):
        self.ai_agent = MultiAgentGraph()
    
    
    def chat(self, message: str) -> str:
        result = self.ai_agent.execute(message)
        
        if result and "messages" in result and result["messages"]:
            last_message = result["messages"][-1]

            return last_message.content
        else:
            raise Exception("No response from agents.")
