from ai.agent import DeclarativeEvaluationAgent

_evaluator = DeclarativeEvaluationAgent()


def metric(example, prediction, trace=None):
    try:
        # Get score from evaluation agent
        if isinstance(prediction, dict):
            output = prediction.get("output", "")
        else:
            output = prediction.output

        score = _evaluator(input=output)

        return float(score) / 100.0

    except Exception as e:
        print(f"Evaluation Error: {e}")
        return 0.0
