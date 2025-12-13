from ai.node.states import GraphState
from ai.service import get_non_scored_messages


class EvaluateNode:
    """
    Evaluate Node
    -------------
    
    Node for evaluating agent performance using DSPy evaluation framework.
    """
    def process(self, state: GraphState):
        """Process evaluation of non-scored chat messages"""
        messages = get_non_scored_messages()
        
        # Handle edge case where messages might be None or empty
        if not messages:
            return {
                "status": "No messages to evaluate",
                "num_messages_evaluated": 0
            }
        
        for message in messages:
            print(message)
        
        return {
            "status": "Evaluation process completed",
            "num_messages_evaluated": len(messages)
        }
