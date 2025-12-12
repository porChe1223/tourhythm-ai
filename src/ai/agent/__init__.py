"""
Agent Layer
-----------
- Handle Agent

Can Do
------
- Read Node Input
- Process Agent
- Call Service as Tools
- Read Service Output
- Write Agent Answer for Node

Can Not Do
----------
- Read/Write Outside of System (document, webpage, etc...)
- Read/Write Node
- Read/Write Graph

Methods
-------
- GeneralAgent: General Purpose Agent
- SupervisorAgent: Managing Agent for supervising
- TaskAgent: Task Suggestion Agent for suggesting necessary baggage/todo to achieve user's goal
"""

from ai.agent.general import DeclarativeGeneralAgent, GeneralAgent
from ai.agent.schedule import DeclarativeScheduleAgent, ScheduleAgent
from ai.agent.supervisor import SupervisorAgent
from ai.agent.task import DeclarativeTaskAgent, TaskAgent
from ai.agent.trip import DeclarativeTripAgent, TripAgent


__all__ = [
    'DeclarativeGeneralAgent',
    "DeclarativeScheduleAgent",
    "DeclarativeTaskAgent",
    "DeclarativeTripAgent",
    'GeneralAgent',
    'ScheduleAgent',
    'SupervisorAgent',
    'TaskAgent',
    'TripAgent',
]
