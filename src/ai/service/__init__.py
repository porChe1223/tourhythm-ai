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

from ai.service.tools.tavily_research import tavily_research_tool


__all__ = [
    'tavily_research_tool',
    ]
