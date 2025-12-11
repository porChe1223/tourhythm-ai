import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, Float, String, Text
from sqlalchemy.dialects.postgresql import UUID

from infra.database._database import Base


class Agent(Base):
    """
    Agent Model
    -----------
    Average Scores and Optimized Prompt per Agent

    Tables
    ------
    - agents

    Fields
    ------
    - id: Primary key
    - name: Agent name ('General', 'Trip', 'Schedule', 'Task', 'Supervisor')
    - average_score: Average score of agent messages
    - prompt: Optimized prompt for the agent
    - updated_at: Timestamp of last update
    """
    __tablename__ = "agents"
    
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(10), unique=True, nullable=False, index=True) # Agent name
    average_score = Column(Float, nullable=True) # Average score of messages
    prompt = Column(Text, nullable=True) # Optimized prompt for the agent
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
