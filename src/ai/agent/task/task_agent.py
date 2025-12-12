import dspy
from typing import Dict

from ai.agent._shared import AgentType, BaseAgent, basic_openai, dspy_openai
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


class TaskSignature(dspy.Signature):
    """
    Task Signature
    --------------
    - Defines Signature for Task AI Agent using DSPy
    """

    input = dspy.InputField(
        type=str
    )

    response = dspy.OutputField(
        desc=TASK_PROMPT,
        type=str,
    )


class DeclarativeTaskAgent(dspy.Module):
    """
    Declarative Task Agent
    ----------------------
    - Agent for Suggesting Tasks which are necessary for achieving the user's goal
    - Using DSPy framework
    - Using Chain of Thought
    - Returns structured JSON format with output and assignee fields
    """
    def __init__(self):
        super().__init__()
        self.lm = dspy_openai()
        self.agent = dspy.ChainOfThought(TaskSignature)

    def forward(self, input: str) -> Dict[str, AgentType]:
        with dspy.context(lm=self.lm):
            result = self.agent(input=input)

        return {
            "output": result.response,
            "assignee": 'Task'
        }
