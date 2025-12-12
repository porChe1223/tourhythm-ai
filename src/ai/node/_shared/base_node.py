import json
from langchain_core.messages import AIMessage
from langgraph.types import Command

from ai.node.states import GraphState


class BaseNode():
    """
    BaseNode
    --------
    - Provides GraphState handling.
    - You can Extend this BaseNode for specific Agent Nodes.
    - at Extension, you should Update process Method.
    
    Methods
    -------
    - extract_messages: Extract messages from GraphState
    - update_state: Update State with Agent output
    - process: you should Update process Method in Extended Node
    """
    def extract_messages(self, state: GraphState) -> str:
        return str([message.content for message in state["messages"]])
    

    def update_state(self, output: str) -> Command:
        return Command(
            update={
                "messages": [AIMessage(content=json.dumps(output, ensure_ascii=False))]
            }
        )
    
    
    def process(self, state: GraphState) -> GraphState:
        pass
