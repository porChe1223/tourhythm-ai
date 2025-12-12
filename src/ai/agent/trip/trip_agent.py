import dspy
from typing import Dict

from ai.agent._shared import AgentType, BaseAgent, basic_openai, dspy_openai
from ai.agent.trip.trip_prompt import TRIP_PROMPT


class TripAgent(BaseAgent):
    """
    TripAgent
    -------------
    - Agent for Suggesting Trips which are necessary for achieving the user's goal.
    """
    def __init__(self) -> None:
        super().__init__('Trip',
                         basic_openai,
                         TRIP_PROMPT)


class TripSignature(dspy.Signature):
    """
    Trip Signature
    --------------
    - Defines Signature for Trip AI Agent using DSPy
    """

    input = dspy.InputField(
        type=str
    )

    response = dspy.OutputField(
        desc=TRIP_PROMPT,
        type=str,
    )


class DeclarativeTripAgent(dspy.Module):
    """
    Declarative Trip Agent
    ----------------------
    - Agent for Suggesting Trips which are necessary for achieving the user's goal
    - Using DSPy framework
    - Using Chain of Thought
    - Returns structured JSON format with output and assignee fields
    """
    def __init__(self):
        super().__init__()
        self.lm = dspy_openai()
        self.agent = dspy.ChainOfThought(TripSignature)

    def forward(self, input: str) -> Dict[str, AgentType]:
        with dspy.context(lm=self.lm):
            result = self.agent(input=input)

        return {
            "output": result.response,
            "assignee": 'Trip'
        }
