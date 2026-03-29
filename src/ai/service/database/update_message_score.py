from infra.database import ChatRepository


def update_message_score(message_id: str, score: int) -> None:
    """Update message score using the generic update_field method"""
    chat_repo = ChatRepository()
    
    chat_repo.update_field(
        message_id=message_id,
        field_name="score",
        value=score
    )
    