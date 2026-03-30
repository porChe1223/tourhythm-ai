from ai.graph.self_improve_graph import SelfImproveGraph
from ai.node.evaluate.evaluate_node import EvaluateNode
from infra.database.repositories.agent_repository import AgentRepository
from optimizer._celery import celery

SCORE_THRESHOLD = 80.0


@celery.task(bind=True)
def self_improve(self, agent_type: str):
    # Evaluate non-scored messages before optimization
    EvaluateNode().process(state={})

    # Feedback Loop (check Average Score is below threshold)
    average_score = AgentRepository().get_field(agent_type, "average_score")
    if average_score is None or average_score < SCORE_THRESHOLD:
        # Run self-improvement graph
        graph = SelfImproveGraph()
        return graph.execute(agent_type)

    return {"status": "skipped", "reason": f"average_score={average_score:.1f} >= {SCORE_THRESHOLD}"}
