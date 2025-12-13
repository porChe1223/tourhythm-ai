from ai import TouristAgentGraph


class AIChatService:
    """
    AIChatService
    -------------
    AI chat service
    Use multi-agent-graph from ai/
    """
    def __init__(self):
        self.ai_agent = TouristAgentGraph()
    
    
    def chat(self, message: str) -> tuple[str, list]:
        """
        Chat with AI agents and return last message and full messages.

        Returns:
            tuple: (response_content, full_result)
        """
        result = self.ai_agent.execute(message)
        
        if result and "messages" in result and result["messages"]:
            last_message = result["messages"][-1]

            return last_message.content, result["messages"]
        else:
            raise Exception("No response from agents.")
