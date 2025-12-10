from typing import Literal
from pydantic import BaseModel


AgentType = Literal['Supervisor', 'Trip', 'Schedule', 'Task', 'General']


class NextAgentDecision(BaseModel):
    """
    NextAgent
    ---------
    - Next Agent with structured output
    - this is for Supervisor Agent to decide the next agent
    """
    next_agent: AgentType
