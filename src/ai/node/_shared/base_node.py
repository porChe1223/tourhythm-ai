import json
from langchain_core.messages import AIMessage
from langgraph.types import Command

from ai.graph.states import GraphState


class BaseNode():
    """
    BaseNode
    --------
    - Provides GraphState handling.
    - You can Extend this BaseNode for specific Agent Nodes.
    - at Extension, you should Update process Method.
    
    Methods
    -------
    - extract_user_input: Extract user input from GraphState
    - update_state: Update State with Agent output
    - process: you should Update process Method in Extended Node
    """
    def extract_user_input(self, state: GraphState) -> str:
        return state["messages"][-1].content
    

    def update_state(self, output: str) -> Command:
        return Command(
            update={
                "messages": [AIMessage(content=json.dumps(output))]
            }
        )
    
    
    def process(self, state: GraphState) -> GraphState:
        pass
