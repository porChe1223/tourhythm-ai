from typing import List, Optional

from infra.database import  ChatMessage, ChatRepository


def get_non_scored_specific_agent_messages(agent_type: Optional[str] = None) -> List[ChatMessage]:
    """Get non-scored messages from specific agent type"""
    repository = ChatRepository()
    
    return repository.get_non_scored_specific_agent_messages(agent_type)
