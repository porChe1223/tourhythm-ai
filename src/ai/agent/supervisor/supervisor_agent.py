from typing import Callable

from ai.agent.shared.base_agent import BaseAgent
from ai.agent.shared.models import basic_openai
from ai.agent.supervisor.supervisor_prompt import SUPERVISOR_PROMPT


class SupervisorAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__('Supervisor',
                         basic_openai,
                         SUPERVISOR_PROMPT,
                         tool_list=None)
