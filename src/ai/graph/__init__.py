"""
Graph Layer
-----------
- Handle Graph
- Made by **Edge(Command/Branching Logic)** and **Node(Node Layer=Business Logic)**

Can Do
------
- Read All Node States(=GraphState)
- Merge/Split All Node States(=GraphState)
- Call Node
- Manage Graph Edge

Can Not Do
----------
- Read/Write Outside of System (document, webpage, etc...)
- Call Agent
- Write Unit Node State

Methods
-------
- TouristAgentGraph: Graph for Multi-Agent Collaboration
"""

from ai.graph.self_improve_graph import SelfImproveGraph
from ai.graph.tourist_agent_graph import TouristAgentGraph


__all__ = [
    'SelfImproveGraph',
    'TouristAgentGraph',
]
