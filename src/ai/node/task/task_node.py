from langgraph.types import Command

from ai.agent import TaskAgent
from ai.node.states import GraphState
from ai.node._shared.base_node import BaseNode
from ai.node._shared.states import NodeType
from ai.service.tools.tavily_research import tavily_research_tool


class TaskNode(BaseNode):
    """
    TaskNode
    -----------
    - Node for Suggesting Task Purpose
    - Based on BaseNode
    - Call TaskAgent Process.
    
    Methods
    -------
    - process: Call TaskAgent with extracted user input and update GraphState
    """
    def __init__(self) -> None:
        self.node_type: NodeType = 'Task'
        self.Agent = TaskAgent()
    
    
    def process(self, state: GraphState) -> Command:
        try:
            user_input = self.extract_user_input(state)

            agent_output = self.Agent.call(user_input, [tavily_research_tool])

            return self.update_state(agent_output)
            
        except Exception as e:
            error_message = f"Error in {self.node_type} Node processing: {str(e)}"
            
            return self.update_state(error_message)
