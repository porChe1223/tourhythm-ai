from ai.agent._shared.base_agent import BaseAgent
from ai.agent._shared.models import basic_openai
from ai.agent.general.general_prompt import GENERAL_PROMPT


class GeneralAgent(BaseAgent):
    """
    GeneralAgent
    ------------
    - Agent for General Purpose Tasks
    - Based on BaseAgent(for LangChain)
    - No Tools
    """
    def __init__(self) -> None:
        super().__init__('General',
                         basic_openai,
                         GENERAL_PROMPT,
                         tool_list=None)
