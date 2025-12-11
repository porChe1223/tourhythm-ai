from typing import Optional, Any

from infra.database.models import Agent
from infra.database._database import DBSession, close_db


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
    def __init__(self):
        self.db = DBSession()


    def update_field(self, agent_name: str, field_name: str, value: Any) -> Optional[Agent]:
        """Update specific field of agent"""
        agent = self.db.query(Agent).filter(Agent.name == agent_name)

        if agent:
            setattr(agent, field_name, value)
            self.db.commit()

            close_db(self.db)

            return agent
        
        close_db(self.db)
        return None
    

    def get_field(self, agent_name: str, field_name: str) -> Any:
        """Get specific field value of agent"""
        agent = self.db.query(Agent).filter(Agent.name == agent_name)

        if agent:
            field = getattr(agent, field_name, None)
            close_db(self.db)
            
            return field
        
        close_db(self.db)
        return None
