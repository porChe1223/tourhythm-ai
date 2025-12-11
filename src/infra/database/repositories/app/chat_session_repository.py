from infra.database.models import ChatSession
from infra.database.repositories.common._chat_session_repository import ChatSessionRepository


class AppChatSessionRepository(ChatSessionRepository):
    """
    ChatSession Repository for App Service
    --------------------------------------
    Extended from ChatSessionRepository

    Methods
    -------
    - create_chat_session: Create new chat session
    """
    def create_chat_session(self, chat_id: int) -> ChatSession:
        session = ChatSession(
            chat_id=chat_id,
            messages=[],
        )

        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)

        return session
