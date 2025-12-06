from langgraph.graph.state import CompiledStateGraph
from langgraph.graph import StateGraph, START, END

from ai.graph.states import GraphState
from ai.node.supervisor.supervisor_node import SupervisorNode
from ai.node.general.general_node import GeneralNode
from ai.node.task.task_node import TaskNode


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
        try:
            # Build
            compiled_graph = self.build_graph()
            
            # Execute
            result = compiled_graph.invoke(input)
            
            return result
            
        except Exception as e:
            raise e
