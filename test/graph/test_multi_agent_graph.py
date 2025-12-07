import asyncio
from langchain_core.messages import HumanMessage

from ai.node import GraphState
from ai.graph import MultiAgentGraph


async def main():
    input = "来週水曜日の昼に京都の金閣寺に福岡から観光に行きたい。何をすればいい？"
    

    multi_agent_graph = MultiAgentGraph()

    multi_agent_graph.execute(GraphState(
        messages=[HumanMessage(content=input)],
        assignee=None
    ))


if __name__ == "__main__":
    asyncio.run(main())
