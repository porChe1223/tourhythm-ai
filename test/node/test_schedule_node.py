import asyncio
from langchain_core.messages import HumanMessage

from ai.node import GraphState, ScheduleNode


async def main(state: GraphState):
    print(state)
    node = ScheduleNode()
    updated_state = node.process(state)

    print(updated_state)


if __name__ == "__main__":
    asyncio.run(main(GraphState(
        messages=[HumanMessage(content="来週京都の金閣寺に観光に行きたい。どの時間帯で行けば良いか提案して。")],
        assignee=None
    )))
