from ai.graph.self_improve_graph import SelfImproveGraph
from ai.node.evaluate.evaluate_node import EvaluateNode
from optimizer._celery import celery


@celery.task(bind=True)
def self_improve(self, agent_type: str):
    # Evaluate non-scored messages before optimization
    EvaluateNode().process(state={})

    graph = SelfImproveGraph()
    result = graph.execute(agent_type)

    return result
