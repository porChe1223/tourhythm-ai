import asyncio
from langchain_core.messages import HumanMessage

from ai.graph.states import GraphState
from ai.node.task.task_node import TaskNode


async def main(state: GraphState):
    print(state)
    node = TaskNode()
    updated_state = node.process(state)

    print(updated_state)


if __name__ == "__main__":
    asyncio.run(main(GraphState(
        messages=[HumanMessage(content="来週の午前中に京都の金閣寺に行きたい。準備すべきタスクを提案して。")],
        assignee=None
    )))
