from ai.agent._shared import BaseAgent, basic_openai
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
