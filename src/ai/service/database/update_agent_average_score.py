from infra.database.repositories import ChatRepository, AgentRepository


def update_agent_average_score(assignee: str) -> None:
    """Calculate average score of scored messages for assignee and update agent record"""
    avg = ChatRepository().get_average_score_by_assignee(assignee)
    if avg is not None:
        AgentRepository().update_field(assignee, "average_score", avg)
