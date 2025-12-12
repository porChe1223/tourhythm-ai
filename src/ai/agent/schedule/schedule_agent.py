import dspy
from typing import Dict

from ai.agent._shared import AgentType, BaseAgent, basic_openai, dspy_openai
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


class ScheduleSignature(dspy.Signature):
    """
    Schedule Signature
    ------------------
    - Defines Signature for Schedule AI Agent using DSPy
    """

    input = dspy.InputField(
        type=str
    )

    response = dspy.OutputField(
        desc=SCHEDULE_PROMPT,
        type=str,
    )


class DeclarativeScheduleAgent(dspy.Module):
    """
    Declarative Schedule Agent
    ----------------------
    - Agent for Schedule Tasks
    - Using DSPy framework
    - Using Chain of Thought reasoning for complex tasks
    - Returns structured JSON format with output and assignee fields
    """
    def __init__(self):
        super().__init__()
        dspy_openai()
        self.agent = dspy.ChainOfThought(ScheduleSignature)

    def forward(self, input: str) -> Dict[str, AgentType]:
        result = self.agent(input=input)

        return {
            "output": result.response,
            "assignee": 'Schedule'
        }
