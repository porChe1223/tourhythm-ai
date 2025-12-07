from ai.agent._shared.base_agent import BaseAgent
from ai.agent._shared.models import basic_openai
from ai.agent.task.task_prompt import TASK_PROMPT
from ai.service import tavily_research_tool

class TaskAgent(BaseAgent):
    """
    TaskAgent
    ------------
    - Agent for Suggesting Tasks which are necessary for achieving the user's goal.
    - Based on BaseAgent(for LangChain)
    - No Tools
    """
    def __init__(self) -> None:
        super().__init__('Task',
                         basic_openai,
                         TASK_PROMPT,
                         tool_list=[tavily_research_tool])
