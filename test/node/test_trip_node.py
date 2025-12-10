import asyncio
from langchain_core.messages import HumanMessage

from ai.node import GraphState, TripNode


async def main(state: GraphState):
    print(state)
    node = TripNode()
    updated_state = node.process(state)

    print(updated_state)


if __name__ == "__main__":
    asyncio.run(main(GraphState(
        messages=[HumanMessage(content="来週京都のどこかに行きたい。どこがおすすめ？")],
        assignee=None
    )))
