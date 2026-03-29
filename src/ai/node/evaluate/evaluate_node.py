from ai.node.states import GraphState
from ai.agent.evaluation.evaluation_agent import DeclarativeEvaluationAgent
from ai.service import get_non_scored_specific_agent_messages, update_message_score


class EvaluateNode:
    """
    Evaluate Node
    -------------
    Node for evaluating agent performance using DSPy evaluation framework.
    """
    def process(self, state: GraphState):
        """Process evaluation of non-scored chat messages"""
        messages = get_non_scored_specific_agent_messages()

        if not messages:
            return {
                "status": "No messages to evaluate",
                "num_messages_evaluated": 0
            }

        evaluator = DeclarativeEvaluationAgent()

        for message in messages:
            score = evaluator(input=message.message)
            update_message_score(message.id, score)

        return {
            "status": "Evaluation process completed",
            "num_messages_evaluated": len(messages)
        }
