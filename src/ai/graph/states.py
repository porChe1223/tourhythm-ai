from typing import Literal
from langgraph.graph import MessagesState


AgentType = Literal['Supervisor', 'Trip', 'Schedule', 'Task', 'General', 'Finisher'] | None


class GraphState(MessagesState):
    """
    GraphState
    ----------
    - State for Graph
    - This State is Extended from MessagesState
    - If Node returns {"messages": [...]}, it will be Merged with Existing messages in GraphState
    """
    next_agent: AgentType = None
