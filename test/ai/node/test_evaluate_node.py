import asyncio

from ai.node import GraphState, EvaluateNode


async def main(state: GraphState):
    print(state)
    node = EvaluateNode()
    updated_state = node.process(state)

    print(updated_state)


if __name__ == "__main__":
    asyncio.run(main(GraphState(
        messages=[],
        assignee=None
    )))
