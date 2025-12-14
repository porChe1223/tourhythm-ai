from typing import List

from infra.database.models import ChatSession, ChatMessage
from infra.database._database import DBSession, close_db


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
    - get_non_scored_specific_agent_messages: Get non-scored messages from specific agent type
    - update_field: Update a single field of a message
    - update_fields: Update multiple fields of a message at once
    """
    def __init__(self):
        self.db = DBSession()

        
    def create_session(self, session: ChatSession) -> ChatSession:
        """Create a new chat session"""
        try:
            self.db.add(session)
            self.db.commit()
            
            self.db.refresh(session)

            if True:
                from optimizer import self_improve


                self_improve.delay()
            
            close_db(self.db)
            
            return session
        except Exception as e:
            self.db.rollback()
            close_db(self.db)

            raise e
    
    
    def add_messages(self, messages: List[ChatMessage]) -> List[ChatMessage]:
        """
        Add multiple messages to chat session in batch.  
        Batch size would not be bigger than 26, so splitting is not necessary
        """
        try:
            self.db.add_all(messages)
            self.db.commit()
            
            close_db(self.db)
            
            return messages
        except Exception as e:
            self.db.rollback()
            close_db(self.db)

            raise e
    

    def get_non_scored_specific_agent_messages(self, agent_type: str = None) -> List[ChatMessage]:
        """Get non-scored messages from specific agent type"""
        try:
            query = (
                self.db.query(ChatMessage)
                .filter(
                    ChatMessage.score == None,
                    ChatMessage.assignee != None
                )
            )
            
            if agent_type:
                query = query.filter(ChatMessage.assignee == agent_type)
            
            messages = query.order_by(ChatMessage.created_at.desc()).all()
            
            close_db(self.db)
            
            return messages
        except Exception as e:
            close_db(self.db)

            raise e
    

    def get_messages_by_assignee(self, assignee: str) -> List[ChatMessage]:
        """Get all messages by specific assignee"""
        try:
            messages = (
                self.db.query(ChatMessage)
                .filter(ChatMessage.assignee == assignee)
                .all()
            )
            
            close_db(self.db)
            
            return messages
        except Exception as e:
            close_db(self.db)

            raise e
    

    def update_field(self, message_id: str, field_name: str, value) -> ChatMessage:
        """Update specific field of message"""
        try:
            message = (
                self.db.query(ChatMessage)
                .filter(ChatMessage.id == message_id)
                .first()
            )
            
            if message:
                setattr(message, field_name, value)
                self.db.commit()
                self.db.refresh(message)
            
            close_db(self.db)
            
            return message
        except Exception as e:
            self.db.rollback()
            close_db(self.db)

            raise e


    def update_fields(self, message_id: str, fields: dict) -> ChatMessage:
        """Update multiple fields of message at once"""
        try:
            message = (
                self.db.query(ChatMessage)
                .filter(ChatMessage.id == message_id)
                .first()
            )
            
            if message:
                for field_name, value in fields.items():
                    setattr(message, field_name, value)
                
                self.db.commit()
                self.db.refresh(message)
            
            close_db(self.db)
            
            return message
        except Exception as e:
            self.db.rollback()
            close_db(self.db)

            raise e
