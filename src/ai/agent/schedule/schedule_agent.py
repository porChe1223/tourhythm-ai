from ai.agent._shared.base_agent import BaseAgent
from ai.agent._shared.models import basic_openai
from ai.agent.schedule.schedule_prompt import SCHEDULE_PROMPT


class ScheduleAgent(BaseAgent):
    """
    ScheduleAgent
    -------------
    - Agent for Suggesting Schedules which are necessary for achieving the user's goal.
    """
    def __init__(self) -> None:
        super().__init__('Schedule',
                         basic_openai,
                         SCHEDULE_PROMPT)
