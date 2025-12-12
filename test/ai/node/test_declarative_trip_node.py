import asyncio
from langchain_core.messages import HumanMessage

from ai.node import DeclarativeTripNode, GraphState


async def main(state: GraphState):
    print(state)
    node = DeclarativeTripNode()
    updated_state = node.process(state)

    print(updated_state)


if __name__ == "__main__":
    asyncio.run(main(GraphState(
        messages=[HumanMessage(content="京都の金閣寺に観光に行きたい。")],
        assignee=None
    )))
