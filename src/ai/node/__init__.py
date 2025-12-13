"""
Node Layer
----------
- Handle Node

Can Do
------
- Read User Input
- Read/Write Unit Node State(≒GraphState <= will be merged in Graph Layer)
- Call Agent
- Read Agent Output
- Call Service as Utils
- Read Service Output

Can Not Do
----------
- Read/Write Outside of System (document, webpage, etc...)
- Manage Graph Edge

Methods
-------
- DeclarativeGeneralNode: Node for General Purpose Tasks using Declarative Agent
- DeclarativeScheduleNode: Node for Suggesting Schedule Purpose using Declarative Agent
- DeclarativeTaskNode: Node for Suggesting Tasks necessary to achieve user's goal using Declarative Agent
- DeclarativeTripNode: Node for Suggesting Trip Purpose using Declarative Agent
- EvaluateNode: Node for Evaluating Agent Performance
- GeneralNode: Node for General Purpose Tasks
- SupervisorNode: Node for Supervising Tasks
- ScheduleNode: Node for Suggesting Schedule Purpose
- TaskNode: Node for Suggesting Tasks necessary to achieve user's goal
- TripNode: Node for Suggesting Trip Purpose
"""

from ai.node.evaluate import EvaluateNode
from ai.node.general import DeclarativeGeneralNode, GeneralNode
from ai.node.schedule import DeclarativeScheduleNode, ScheduleNode
from ai.node.supervisor import SupervisorNode
from ai.node.states import GraphState, NodeType
from ai.node.task import DeclarativeTaskNode, TaskNode
from ai.node.trip import DeclarativeTripNode, TripNode


__all__ = [
    'DeclarativeGeneralNode',
    'DeclarativeScheduleNode',
    'DeclarativeTaskNode',
    'DeclarativeTripNode',
    'EvaluateNode',
    'GeneralNode',
    'GraphState',
    'NodeType',
    'ScheduleNode',
    'SupervisorNode',
    'TaskNode',
    'TripNode'
]
