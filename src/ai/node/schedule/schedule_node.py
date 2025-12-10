from langgraph.types import Command

from ai.agent import ScheduleAgent
from ai.node.states import GraphState
from ai.node._shared.base_node import BaseNode
from ai.node._shared.states import NodeType


class ScheduleNode(BaseNode):
    """
    ScheduleNode
    ------------
    - Node for Schedule Purpose Tasks
    - Based on BaseNode
    - Call ScheduleAgent Process.
    
    Methods
    -------
    - process: Call ScheduleAgent with extracted user input and update GraphState
    """
    def __init__(self) -> None:
        self.node_type: NodeType = 'Schedule'
        self.Agent = ScheduleAgent()
    
    
    def process(self, state: GraphState) -> Command:
        try:
            user_input = self.extract_user_input(state)

            agent_output = self.Agent.call(user_input)

            return self.update_state(agent_output)
            
        except Exception as e:
            error_message = f"Error in {self.node_type} Node processing: {str(e)}"
            
            return self.update_state(error_message)
