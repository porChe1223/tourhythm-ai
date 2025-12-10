import json
from langgraph.types import Command
from langchain_core.messages import AIMessage

from ai.agent import SupervisorAgent
from ai.node.states import GraphState
from ai.node._shared.base_node import BaseNode
from ai.node._shared.states import NodeType


class SupervisorNode(BaseNode):
    """
    SupervisorNode
    --------------
    - Node for Supervising and Delegating Tasks
    - Based on BaseNode
    - Call SupervisorAgent Process.
    
    Methods
    -------
    - process: Call SupervisorAgent with extracted user input and update GraphState
    """
    def __init__(self) -> None:
        self.node_type: NodeType = 'Supervisor'
        self.Agent = SupervisorAgent()
    
    
    def process(self, state: GraphState) -> Command:
        try:
            user_input = self.extract_user_input(state)

            agent_output = self.Agent.call(user_input)

            

            return Command(
                update={
                    "messages": [AIMessage(content=json.dumps(agent_output))],
                }
            )
            
        except Exception as e:
            error_message = f"Error in {self.node_type} Node processing: {str(e)}"
            
            return self.update_state(error_message)
