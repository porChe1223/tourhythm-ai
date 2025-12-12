from typing import Any
from ai.agent._shared import BaseAgent, NextAgentDecision, RetryWrapper, structured_openai
from ai.agent.supervisor.supervisor_prompt import SUPERVISOR_PROMPT


class SupervisorAgent(BaseAgent):
    """
    SupervisorAgent
    ---------------
    - Agent for Supervising and Delegating Tasks
    - Based on BaseAgent (for LangChain)
    - Uses structured output openai model to decide next agent
    """
    def __init__(self) -> None:
        super().__init__('Supervisor',
                         structured_openai(NextAgentDecision),
                         SUPERVISOR_PROMPT)
    

    def call(self, input_text: str) -> dict[str, Any]:
        try:
            # For structured output, directly use the model without create_agent
            # Call the structured model with RetryWrapper
            response = RetryWrapper(self.Model).invoke([
                {"role": "system", "content": self.SystemPrompt},
                {"role": "user", "content": input_text}
            ])

            return {
                "output": f"Supervisor assigned to {response.next_agent}",
                "assignee": self.AgentType,
                "next_agent": response.next_agent
            }

        except Exception as e:
            error_message = f"Error from {self.AgentType} Agent: {e}"
            return {
                "output": error_message,
                "assignee": self.AgentType
            }
