from langgraph.types import Command

from ai.agent import DeclarativeScheduleAgent, ScheduleAgent
from ai.node.states import GraphState, NodeType
from ai.node._shared import BaseNode


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
            user_input = self.extract_messages(state)

            agent_output = self.Agent.call(user_input)

            return self.update_state(agent_output)
            
        except Exception as e:
            error_message = f"Error in {self.node_type} Node processing: {str(e)}"
            
            return self.update_state(error_message)


class DeclarativeScheduleNode(BaseNode):
    """
    DeclarativeScheduleNode
    -----------------------
    - Node for Schedule Purpose Tasks using Declarative Agent
    - Based on ScheduleNode
    - Call Declarative Schedule Agent
    """
    def __init__(self) -> None:
        self.node_type: NodeType = 'Schedule'
        self.Agent = DeclarativeScheduleAgent()


    def process(self, state: GraphState) -> Command:
        try:
            user_input = self.extract_messages(state)

            agent_output = self.Agent(input=user_input)

            return self.update_state(agent_output)
            
        except Exception as e:
            error_message = f"Error in {self.node_type} Node processing: {str(e)}"
            
            return self.update_state(error_message)
