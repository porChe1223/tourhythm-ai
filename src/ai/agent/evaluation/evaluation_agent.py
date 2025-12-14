import dspy
from typing import Dict

from ai.agent._shared import dspy_openai
from ai.agent.evaluation.evaluation_prompt import EVALUATION_PROMPT


class EvaluationSignature(dspy.Signature):
    """
    Evaluation Signature
    --------------------
    - Defines Signature for Evaluation AI Agent using DSPy
    """

    input = dspy.InputField(
        desc="Evaluation context including answer",
        type=str
    )

    score = dspy.OutputField(
        desc=EVALUATION_PROMPT,
        type=float,
    )


class DeclarativeEvaluationAgent(dspy.Module):
    """
    Declarative Evaluation Agent
    ----------------------------
    - Agent for evaluating agent outputs
    - Using DSPy framework
    - Returns structured JSON format with score field
    """
    def __init__(self):
        super().__init__()
        self.lm = dspy_openai()
        self.agent = dspy.Predict(EvaluationSignature)

    def forward(self, input: str) -> Dict[str, float]:
        with dspy.context(lm=self.lm):
            result = self.agent(input=input)

        return {
            "score": result.score
        }
