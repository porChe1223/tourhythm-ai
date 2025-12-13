from langgraph.graph import StateGraph, START, END
from langgraph.graph.state import CompiledStateGraph

from ai.node import EvaluateNode, GraphState


class SelfImproveGraph:
    """
    SelfImproveGraph
    ----------------
    Graph for evaluating agents using EvaluateNode  
    this graph is single-direction
    """
    def __init__(self) -> None:
        self.State = GraphState
    

    def build_graph(self) -> CompiledStateGraph:
        # --- Init Graph ---
        graph = StateGraph(self.State)

        # --- Nodes ---
        graph.add_node('Evaluate', EvaluateNode().process)

        # --- Edges ---
        graph.add_edge(START, "Evaluate")
        graph.add_edge("Evaluate", END)

        # --- Compile Graph ---
        compiled_graph = graph.compile()

        return compiled_graph
    

    def execute(self):
        try:
            # Build
            compiled_graph = self.build_graph()
            
            # Execute
            result = compiled_graph.invoke(self.State())
            
            return result
            
        except Exception as e:
            
            raise e
