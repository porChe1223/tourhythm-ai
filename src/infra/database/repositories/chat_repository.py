from sqlalchemy.orm import Session
from typing import List

from infra.database.models import ChatSession, ChatMessage


class ChatRepository:
    """
    Chat Repository
    ---------------
    Repository for sessions and chat messages data handling
    
    Methods
    -------
    - create_session: Create a new chat session
    - add_messages: Add multiple messages to chat session in batch
    - get_messages_by_assignee: Get all messages by specific assignee
    """
    def __init__(self, db: Session):
        self.db = db

        
    def create_session(self, session: ChatSession) -> ChatSession:
        """Create a new chat session"""
        self.db.add(session)
        self.db.commit()
        return session
    
    
    def add_messages(self, messages: List[ChatMessage]) -> List[ChatMessage]:
        """
        Add multiple messages to chat session in batch.  
        Batch size would not be bigger than 26, so splitting is not necessary
        """
        self.db.add_all(messages)
        self.db.commit()
        return messages
    

    def get_messages_by_assignee(self, assignee: str) -> List[ChatMessage]:
        """Get all messages by specific assignee"""
        return (
            self.db.query(ChatMessage)
            .filter(ChatMessage.assignee == assignee)
            .all()
        )
