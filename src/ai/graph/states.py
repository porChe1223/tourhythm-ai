from langgraph.graph import MessagesState


class GraphState(MessagesState):
    """
    GraphState
    ----------
    - State for Graph
    - This State is Extended from MessagesState
    - If Node returns {"messages": [...]}, it will be Merged with Existing messages in GraphState
    """
    assignee: str = None
