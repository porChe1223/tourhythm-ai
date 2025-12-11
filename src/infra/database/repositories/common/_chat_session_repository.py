from sqlalchemy.orm import Session


class ChatSessionRepository:
    """
    ChatSession Repository
    ----------------------
    Handles ChatSession model.
    Extends to app and optim repositories.
    """
    def __init__(self, db: Session):
        self.db = db
