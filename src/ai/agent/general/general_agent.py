import dspy
from typing import Dict

from ai.agent._shared import AgentType, BaseAgent, basic_openai, dspy_openai
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


class GeneralPurposeSignature(dspy.Signature):
    """
    General Purpose Signature
    -------------------------
    - Defines Signature for General Purpose AI Agent using DSPy
    """

    input = dspy.InputField(
        type=str
    )

    response = dspy.OutputField(
        desc=GENERAL_PROMPT,
        type=str,
    )


class DeclarativeGeneralAgent(dspy.Module):
    """
    Declarative General Agent
    ----------------------
    - Agent for General Purpose Tasks
    - Using DSPy framework
    - Using Chain of Thought reasoning for complex tasks
    - Returns structured JSON format with output and assignee fields
    """
    def __init__(self):
        super().__init__()
        dspy_openai()
        self.agent = dspy.ChainOfThought(GeneralPurposeSignature)

    def forward(self, input: str) -> Dict[str, AgentType]:
        result = self.agent(input=input)

        return {
            "output": result.response,
            "assignee": 'General'
        }
