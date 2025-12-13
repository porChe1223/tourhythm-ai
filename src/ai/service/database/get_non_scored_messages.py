from typing import List
from infra.database import ChatMessage, ChatRepository


def get_non_scored_messages() -> List[ChatMessage]:
    """Pick non-scored chat messages from the database"""
    chat_repo = ChatRepository()
    messages = chat_repo.get_non_scored_messages()

    # Print each message for debugging
    for message in messages:
        print(message)
    
    return messages
