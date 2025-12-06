import json
from langgraph.types import Command

from ai.agent.general.general_agent import GeneralAgent
from ai.graph.states import AgentType, GraphState
from ai.node.shared.base_node import BaseNode


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
        self.node_type: AgentType = 'General'
        self.Agent = GeneralAgent()
    
    
    def process(self, state: GraphState) -> Command:
        try:
            user_input = self.extract_user_input(state)

            agent_output = self.Agent.call(user_input)

            return self.update_state(agent_output)
            
        except Exception as e:
            error_message = f"Error in {self.node_type} Node processing: {str(e)}"
            
            return self.update_state(error_message)
