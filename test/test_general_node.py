import asyncio
from langchain_core.messages import HumanMessage

from ai.graph.states import GraphState
from ai.node.general.general_node import GeneralNode


async def main(state: GraphState):
    print(state)
    updated_state = GeneralNode(state).process()

    print(updated_state)


if __name__ == "__main__":
    asyncio.run(main(GraphState(
        messages=[HumanMessage(content="京都の金閣寺に観光に行きたい。")],
        assignee=None
    )))
