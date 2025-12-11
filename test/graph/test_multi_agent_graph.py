import asyncio

from ai.graph import MultiAgentGraph


async def main():
    input = "来週に京都に福岡から観光に行きたい。どの時間帯がおすすめ？"
    

    multi_agent_graph = MultiAgentGraph()

    multi_agent_graph.execute(input)


if __name__ == "__main__":
    asyncio.run(main())
