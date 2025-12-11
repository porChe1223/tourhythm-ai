# Tourist data models
from sqlalchemy import Column, Integer, DateTime, JSON
from datetime import datetime
from infra.database._database import Base


class ChatSession(Base):
    """
    ChatSession Model
    -----------------
    chat session data

    Tables
    ------
    - chat_sessions

    Fields
    ------
    - id: Primary key
    - chat_id: Optional link to trip
    - messages: Chat message history
    - created_at: Timestamp of creation
    - updated_at: Timestamp of last update
    """
    __tablename__ = "chat_sessions"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    chat_id = Column(Integer, nullable=True)  # Optional link to trip
    messages = Column(JSON)  # Chat message history
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
