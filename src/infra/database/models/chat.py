import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from infra.database._database import Base


class ChatSession(Base):
    """
    ChatSession Model
    -----------------
    Chat session data with individual message tracking

    Tables
    ------
    - chat_sessions

    Fields
    ------
    - id: Primary key
    - created_at: Timestamp of creation

    Relationships
    -------------
    - messages: One-to-Many relationship with ChatMessage
    """
    __tablename__ = "chat_sessions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationship
    messages = relationship("ChatMessage", back_populates="session", order_by="ChatMessage.order_index")


class ChatMessage(Base):
    """
    ChatMessage Model
    -----------------
    Individual chat messages with assignee tracking and scoring

    Tables
    ------
    - chat_messages

    Fields
    ------
    - id: Primary key. this is used from AI system message ID
    - session_id: Foreign key to ChatSession
    - message: Message content
    - assignee: Agent assignee ('General', 'Trip', 'Schedule', 'Task', 'Supervisor') or NULL for human
    - order_index: Order within session for restoration
    - score: Message quality score (0-10) .this score not must be 0-10 because AI evaluated
    - score_reason: Reason for the score
    - created_at: Timestamp of creation

    Relationships
    -------------
    - session: Many-to-one relationship with ChatSession
    """
    __tablename__ = "chat_messages"
    
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)  # UUID primary key
    session_id = Column(UUID(as_uuid=True), ForeignKey("chat_sessions.id"), nullable=False, index=True)
    message = Column(Text, nullable=False)
    assignee = Column(String(10), nullable=True, index=True)  # NULL for human messages
    order_index = Column(Integer, nullable=False)  # For maintaining message order
    score = Column(Integer, nullable=True)  # 0-10 score (Not must be 0-10 because AI evaluated)
    score_reason = Column(Text, nullable=True)  # Reason for the score
    created_at = Column(DateTime, default=datetime.now)
    
    # Relationship
    session = relationship("ChatSession", back_populates="messages")
