import asyncio
from langchain_core.messages import HumanMessage

from ai.graph.states import GraphState
from ai.node.supervisor.supervisor_node import SupervisorNode


async def main(state: GraphState):
    print(state)
    updated_state = SupervisorNode(state).process()

    print(updated_state)


if __name__ == "__main__":
    asyncio.run(main(GraphState(
        messages=[HumanMessage(content="京都の金閣寺に観光に行きたい。")],
        assignee=None
    )))
