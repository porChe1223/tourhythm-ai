from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph

from ai.node import GraphState, OptimizeNode


class SelfImproveGraph:
    """
    SelfImproveGraph
    ----------------
    Graph for Self-Improvement of Agents using Optimization Node
    """
    def __init__(self) -> None:
        self.State = GraphState
    

    def build_graph(self, agent_type: str) -> CompiledStateGraph:
        # --- Init Graph ---
        graph = StateGraph(self.State)

        # --- Nodes ---
        # Create wrapper function to bind agent_type parameter
        optimize_node = OptimizeNode()
        def optimize_with_agent_type(state: GraphState):
            return optimize_node.process(state, agent_type)
        
        graph.add_node('Optimize', optimize_with_agent_type)

        # --- Edges ---
        graph.add_edge(START, "Optimize")
        graph.add_edge("Optimize", END)

        # --- Compile Graph ---
        compiled_graph = graph.compile()

        return compiled_graph
    

    def execute(self, agent_type: str):
        try:
            # Build
            compiled_graph = self.build_graph(agent_type=agent_type)
            
            # Execute
            result = compiled_graph.invoke(self.State())
            
            return result
            
        except Exception as e:
            
            raise e
