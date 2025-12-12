from ai.agent._shared import BaseAgent, basic_openai
from ai.agent.general.general_prompt import GENERAL_PROMPT


class GeneralAgent(BaseAgent):
    """
    GeneralAgent
    ------------
    - Agent for General Purpose Tasks
    - Based on BaseAgent(for LangChain)
    """
    def __init__(self) -> None:
        super().__init__('General',
                         basic_openai,
                         GENERAL_PROMPT)
