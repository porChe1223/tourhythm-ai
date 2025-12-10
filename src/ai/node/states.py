from langgraph.graph import MessagesState

from ai.node._shared.states import NodeType
from ai.agent._shared.states import AgentType


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
    next_agent: AgentType = None
