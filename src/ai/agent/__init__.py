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

from ai.agent.general.general_agent import GeneralAgent
from ai.agent.supervisor.supervisor_agent import SupervisorAgent
from ai.agent.task.task_agent import TaskAgent


__all__ = [
    'GeneralAgent',
    'SupervisorAgent',
    'TaskAgent',
]
