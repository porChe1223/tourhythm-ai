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
- DeclarativeGeneralAgent: General Purpose Agent using Declarative Approach
- DeclarativeScheduleAgent: Schedule Suggestion Agent using Declarative Approach
- DeclarativeTaskAgent: Task Suggestion Agent using Declarative Approach
- DeclarativeTripAgent: Trip Suggestion Agent using Declarative Approach
- GeneralAgent: General Purpose Agent
- ScheduleAgent: Schedule Suggestion Agent for suggesting schedule based on user's trip plan
- SupervisorAgent: Managing Agent for supervising
- TaskAgent: Task Suggestion Agent for suggesting necessary baggage/todo to achieve user's goal
- TripAgent: Trip Suggestion Agent for suggesting trip plan based on user's preferences
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
