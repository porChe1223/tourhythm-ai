from ai.agent.task.task_agent import TaskAgent
from ai.graph.states import AgentType, GraphState
from ai.node.shared.base_node import BaseNode


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
    def __init__(self, state: GraphState) -> None:
        super().__init__(state)
        self.node_type: AgentType = 'Task'
        self.Agent = TaskAgent()
    
    
    def process(self) -> GraphState:
        try:
            user_input = self.extract_user_input()

            agent_output = self.Agent.call(user_input)

            return self.update_state(agent_output["messages"])
            
        except Exception as e:
            error_message = f"Error in {self.node_type} Node processing: {str(e)}"
            
            return self.update_state(error_message)
