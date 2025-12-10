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
- GeneralNode: Node for General Purpose Tasks
- SupervisorNode: Node for Supervising Tasks
- TaskNode: Node for Suggesting Tasks necessary to achieve user's goal
"""

from ai.node.general.general_node import GeneralNode
from ai.node.schedule.schedule_node import ScheduleNode
from ai.node.supervisor.supervisor_node import SupervisorNode
from ai.node.states import GraphState
from ai.node.task.task_node import TaskNode
from ai.node.trip.trip_node import TripNode


__all__ = [
    'GeneralNode',
    'GraphState',
    'ScheduleNode',
    'SupervisorNode',
    'TaskNode',
    'TripNode'
]
