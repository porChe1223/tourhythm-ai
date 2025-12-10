import asyncio

from ai.agent import ScheduleAgent


async def main():
    agent = ScheduleAgent()
    
    input_text = "来週京都の金閣寺に観光に行きたい。どの時間帯で行けば良いか提案して。"
    
    result = agent.call(input_text)

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
