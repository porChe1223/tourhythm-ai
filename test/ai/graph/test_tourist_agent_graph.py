import asyncio
import json
from langchain_core.messages import HumanMessage

from ai.graph import TouristAgentGraph


async def main():
    input = json.dumps(HumanMessage({"output": "来週に京都に福岡から観光に行きたい。どの時間帯がおすすめ？", "assignee": "Human"}), ensure_ascii=False)
    

    multi_agent_graph = TouristAgentGraph()

    multi_agent_graph.execute(input)


if __name__ == "__main__":
    asyncio.run(main())
