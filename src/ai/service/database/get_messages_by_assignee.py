from typing import List

from infra.database import ChatMessage, ChatRepository


def get_messages_by_assignee(assignee: str) -> List[ChatMessage]:
    """Get all messages by specific assignee"""
    repository = ChatRepository()
    
    return repository.get_messages_by_assignee(assignee)
