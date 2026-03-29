import asyncio

from ai.graph import SelfImproveGraph


async def main():
    graph = SelfImproveGraph()

    result = graph.execute(agent_type="Trip")

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
