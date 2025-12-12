from ai.agent._shared import BaseAgent, basic_openai
from ai.agent.task.task_prompt import TASK_PROMPT


class TaskAgent(BaseAgent):
    """
    TaskAgent
    ------------
    - Agent for Suggesting Tasks which are necessary for achieving the user's goal.
    - Based on BaseAgent(for LangChain)
    """
    def __init__(self) -> None:
        super().__init__('Task',
                         basic_openai,
                         TASK_PROMPT)
