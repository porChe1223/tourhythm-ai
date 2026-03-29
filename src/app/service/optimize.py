import json
from typing import List, Any

from optimizer.main import self_improve

VALID_AGENT_TYPES = {"Schedule", "Task", "Trip"}


def call_optimize(messages: List[Any]):
    assignees = set()
    for message in messages:
        raw_content = getattr(message, 'content', '')
        try:
            parsed = json.loads(raw_content.strip())
            assignee = parsed.get('assignee')
            if assignee and assignee in VALID_AGENT_TYPES:
                assignees.add(assignee)
        except (json.JSONDecodeError, AttributeError):
            pass

    for agent_type in assignees:
        self_improve.delay(agent_type=agent_type)
