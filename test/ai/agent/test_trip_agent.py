import asyncio

from ai.agent import TripAgent


async def main():
    agent = TripAgent()
    
    input_text = "来週京都のどこかに行きたい。どこがおすすめ？"
    
    result = agent.call(input_text)

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
