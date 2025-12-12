from langgraph.graph import MessagesState
from typing import Literal


NodeType = Literal['Supervisor', 'Trip', 'Schedule', 'Task', 'General']


class GraphState(MessagesState):
    """
    GraphState(<u>Manage in Node Level!!</u>)
    -----------------------------------------
    - State for Graph
    - You should **Manage in Node Level!!**
    - If Message State get {"messages": [...]}
    - It will be <u>**Merged**</u> with Existing messages
    - This State is Extended from MessagesState Logic
    """
    assignee: NodeType = None
    next_agent: NodeType = None
