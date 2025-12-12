import asyncio
from ai.agent import DeclarativeScheduleAgent


async def main():
    agent = DeclarativeScheduleAgent()
    
    input_text = "来週京都の金閣寺に観光に行きたい。どの時間帯で行けば良いか提案して。"
    
    result = agent(input=input_text)

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
