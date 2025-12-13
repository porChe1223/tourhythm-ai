"""
Service Layer
-------------
- Handle Service

Can Do
------
- Read/Write Outside of System (document, webpage, etc...)
- Answer to Agent Call
- Answer to Node Call

Can Not Do
----------
- Call Agent
- Call Node
- Manage Graph Edge

Methods
-------
- tavily_research_tool: Tool for Researching via Tavily API
"""

from ai.service.database import get_non_scored_messages
from ai.service.tools import tavily_research_tool


__all__ = [
    'get_non_scored_messages',
    'tavily_research_tool',
    ]
