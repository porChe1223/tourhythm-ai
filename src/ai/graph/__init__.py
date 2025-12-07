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
- MultiAgentGraph: Graph for Multi-Agent Collaboration
"""

from ai.graph.multi_agent_graph import MultiAgentGraph


__all__ = [
    'MultiAgentGraph',
]
