from sqlalchemy.orm import Session
from typing import Optional, Any

from infra.database.models import Agent


class AgentRepository:
    """
    Agent Repository
    ----------------
    Repository for agent data handling
    
    Methods
    -------
    - update_field: Update specific field of agent
    - get_field: Get specific field value of agent
    """
    def __init__(self, db: Session):
        self.db = db


    def update_field(self, agent_name: str, field_name: str, value: Any) -> Optional[Agent]:
        """Update specific field of agent"""
        agent = self.db.query(Agent).filter(Agent.name == agent_name)

        if agent:
            setattr(agent, field_name, value)
            self.db.commit()

            return agent
        
        return None
    

    def get_field(self, agent_name: str, field_name: str) -> Any:
        """Get specific field value of agent"""
        agent = self.db.query(Agent).filter(Agent.name == agent_name)

        if agent:
            return getattr(agent, field_name, None)
        
        return None
