import uuid
from datetime import datetime
from sqlalchemy import Column, DateTime, Float, INTEGER, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

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

    Relationships
    -------------
    - prompts: One-to-Many relationship with Prompt
    """
    __tablename__ = "agents"
    
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(10), unique=True, nullable=False, index=True) # Agent name
    average_score = Column(Float, nullable=True) # Average score of messages
    prompt = Column(Text, nullable=True) # Optimized prompt for the agent
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    # Relationships
    prompts = relationship("Prompt", back_populates="agent", order_by="Prompt.id")


class Prompt(Base):
    """
    Prompt Model
    ------------
    Stores optimized prompts for different agents.

    Tables
    ------
    - prompts

    Fields
    ------
    - id: Primary key
    - agent_name: Name of the agent ('General', 'Trip', 'Schedule', 'Task', 'Supervisor')
    - prompt: The optimized prompt text
    - updated_at: Timestamp of last update

    Relationships
    -------------
    - agent: Many-to-One relationship with Agent
    """
    __tablename__ = "prompts"
    
    id = Column(INTEGER, primary_key=True, index=True, autoincrement=True)
    agent_name = Column(String(10), ForeignKey("agents.name"), nullable=False, index=True) # Agent name
    prompt = Column(Text, nullable=False) # Optimized prompt text
    created_at = Column(DateTime, default=datetime.now) # Creation timestamp

    # Relations
    agent = relationship("Agent", back_populates="prompts")
