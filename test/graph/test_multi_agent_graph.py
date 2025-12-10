import asyncio
from langchain_core.messages import HumanMessage

from ai.node import GraphState
from ai.graph import MultiAgentGraph


async def main():
    input = "来週に京都に福岡から観光に行きたい。どの時間帯がおすすめ？"
    

    multi_agent_graph = MultiAgentGraph()

    multi_agent_graph.execute(GraphState(
        messages=[HumanMessage(content=input)]
    ))


if __name__ == "__main__":
    asyncio.run(main())
