import time
from langgraph.graph.state import CompiledStateGraph
from langgraph.graph import StateGraph, START, END

from ai.node import GeneralNode, GraphState, SupervisorNode, TaskNode
from log import AgentGraphLogger


class MultiAgentGraph:
    """
    MultiAgentGraph
    ---------------
    """

    def __init__(self) -> None:
        self.State = GraphState


    def build_graph(self) -> CompiledStateGraph:
        # --- Init Graph ---
        graph = StateGraph(self.State)

        # --- Nodes ---
        graph.add_node('Supervisor', SupervisorNode().process)
        graph.add_node('General', GeneralNode().process)
        # graph.add_node('Trip', self.Node.trip_node)
        # graph.add_node('Scheduler', self.Node.scheduler_node)
        graph.add_node('Task', TaskNode().process)

        # --- Edges ---
        # from START to Supervisor
        graph.add_edge(START, "Supervisor")

        graph.add_edge("Supervisor", 'Task')  #TODO: This is For test, should be Conditional Edges
        
        # from Agents to END
        graph.add_edge("General", END)
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
