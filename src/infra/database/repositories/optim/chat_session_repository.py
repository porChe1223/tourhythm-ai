from infra.database.models import ChatSession
from infra.database.repositories.common._chat_session_repository import ChatSessionRepository


class OptimChatSessionRepository(ChatSessionRepository):
    """
    ChatSession Repository for Optimization Service
    -----------------------------------------------
    Extended from ChatSessionRepository

    Methods
    -------
    - get_chat_session: Get chat session by ID
    """
    def get_chat_session(self, session_id: int) -> ChatSession:
        return self.db.query(ChatSession).filter(ChatSession.id == session_id).first()
