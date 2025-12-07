from langgraph.types import Command

from ai.agent import GeneralAgent
from ai.node.states import GraphState
from ai.node._shared.base_node import BaseNode
from ai.node._shared.states import NodeType


class GeneralNode(BaseNode):
    """
    GeneralNode
    -----------
    - Node for General Purpose Tasks
    - Based on BaseNode
    - Call GeneralAgent Process.
    
    Methods
    -------
    - process: Call GeneralAgent with extracted user input and update GraphState
    """
    def __init__(self) -> None:
        self.node_type: NodeType = 'General'
        self.Agent = GeneralAgent()
    
    
    def process(self, state: GraphState) -> Command:
        try:
            user_input = self.extract_user_input(state)

            agent_output = self.Agent.call(user_input)

            return self.update_state(agent_output)
            
        except Exception as e:
            error_message = f"Error in {self.node_type} Node processing: {str(e)}"
            
            return self.update_state(error_message)
