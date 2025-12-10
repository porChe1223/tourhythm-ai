import json
import time
from langgraph.graph.state import CompiledStateGraph
from langgraph.graph import StateGraph, START, END

from ai.node import GeneralNode, GraphState, ScheduleNode, SupervisorNode, TaskNode, TripNode
from log import AgentGraphLogger


class MultiAgentGraph:
    """
    MultiAgentGraph
    ---------------
    """

    def __init__(self) -> None:
        self.State = GraphState
    

    def assign_node_types(self, state: GraphState) -> str:
        messages = state.get("messages", None)
        if not messages:
            return 'General'
        
        next_agent = json.loads(messages[-1].content).get("next_agent", None)
        if not next_agent:
            return 'General'

        if next_agent == 'Trip':
            return 'Trip'
        elif next_agent == 'Schedule':
            return 'Schedule'
        elif next_agent == 'Task':
            return 'Task'
        
        return 'General'


    def build_graph(self) -> CompiledStateGraph:
        # --- Init Graph ---
        graph = StateGraph(self.State)

        # --- Nodes ---
        graph.add_node('Supervisor', SupervisorNode().process)
        graph.add_node('General', GeneralNode().process)
        graph.add_node('Trip', TripNode().process)
        graph.add_node('Schedule', ScheduleNode().process)
        graph.add_node('Task', TaskNode().process)

        # --- Edges ---
        # from START to Supervisor
        graph.add_edge(START, "Supervisor")

        # from Supervisor to General / Task
        graph.add_conditional_edges(
            "Supervisor",
            self.assign_node_types,
            {
                "General": 'General',
                "Trip": 'Trip',
                "Schedule": 'Schedule',
                "Task": 'Task'
            }
        )
        
        # from Agents to END
        graph.add_edge("General", END)
        graph.add_edge("Trip", END)
        graph.add_edge("Schedule", END)
        graph.add_edge("Task", END)

        # --- Compile Graph ---
        compiled_graph = graph.compile()

        return compiled_graph
    

    def execute(self, input: dict):
        self.agent_graph_logger = AgentGraphLogger()
        start_time = time.time()
        
        try:
            # Build
            compiled_graph = self.build_graph()
            
            # Execute
            result = compiled_graph.invoke(input)
            
            # Logging Graph
            self.agent_graph_logger.log_graph(
                input_data=input,
                output_data=result,
                execution_time=(time.time() - start_time)
            )
            
            return result
            
        except Exception as e:
            execution_time = time.time() - start_time
            
            # Logging error
            self.agent_graph_logger.log_graph(
                input_data=input,
                error=e,
                execution_time=execution_time
            )
            
            raise e
