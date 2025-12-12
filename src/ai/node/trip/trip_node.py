from langgraph.types import Command

from ai.agent import DeclarativeTripAgent, TripAgent
from ai.node.states import GraphState, NodeType
from ai.node._shared import BaseNode
from ai.service.tools import tavily_research_tool


class TripNode(BaseNode):
    """
    TripNode
    --------
    - Node for Suggesting Trip Purpose
    - Based on BaseNode
    - Call TripAgent Process.
    
    Methods
    -------
    - process: Call TripAgent with extracted user input and update GraphState
    """
    def __init__(self) -> None:
        self.node_type: NodeType = 'Trip'
        self.Agent = TripAgent()
    
    
    def process(self, state: GraphState) -> Command:
        try:
            user_input = self.extract_user_input(state)

            agent_output = self.Agent.call(user_input, [tavily_research_tool])

            return self.update_state(agent_output)
            
        except Exception as e:
            error_message = f"Error in {self.node_type} Node processing: {str(e)}"
            
            return self.update_state(error_message)


class DeclarativeTripNode(TripNode):
    """
    DeclarativeTripNode
    -------------------
    - Node for Suggesting Trip Purpose using Declarative Agent
    - Based on TripNode
    - Call Declarative Trip Agent
    """
    def __init__(self) -> None:
        self.node_type: NodeType = 'Trip'
        self.Agent = DeclarativeTripAgent()


    def process(self, state: GraphState) -> Command:
        try:
            user_input = self.extract_user_input(state)

            agent_output = self.Agent(input=user_input)

            return self.update_state(agent_output)
            
        except Exception as e:
            error_message = f"Error in {self.node_type} Node processing: {str(e)}"
            
            return self.update_state(error_message)
