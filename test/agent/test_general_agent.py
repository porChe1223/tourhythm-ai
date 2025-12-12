import asyncio

from ai.agent import GeneralAgent


async def main():
    agent = GeneralAgent()
    
    input_text = "来週の午前中に京都の金閣寺に観光に行きたい。準備すべきタスクを提案して。"
    
    result = agent.call(input_text)

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
