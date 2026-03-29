import asyncio

from ai.node import GraphState, OptimizeNode


async def main(state: GraphState):
    print(state)
    node = OptimizeNode()
    updated_state = node.process(state, agent_type="Trip")

    print(updated_state)


if __name__ == "__main__":
    asyncio.run(main(GraphState(
        messages=[],
        assignee=None
    )))
