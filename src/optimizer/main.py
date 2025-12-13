from optimizer._celery import celery


@celery.task(bind=False)
def self_improve():
    from ai import SelfImproveGraph
    
    
    graph = SelfImproveGraph()
    result = graph.execute()

    return result
