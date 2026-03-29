from typing import List, Tuple

from infra.database import ChatMessage, ChatRepository


def get_message_pairs_by_assignee(assignee: str) -> List[Tuple[ChatMessage, ChatMessage]]:
    """
    Get message pairs for training data by assignee
    Returns list of tuples: (first_human_message, agent_message)
    """
    repository = ChatRepository()
    
    return repository.get_message_pairs_by_assignee(assignee)
