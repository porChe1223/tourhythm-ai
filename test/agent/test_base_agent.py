import asyncio

from ai.agent.shared.base_agent import BaseAgent
from ai.agent.shared.models import basic_openai


async def main():
    agent = BaseAgent(
        'Trip',
        basic_openai,
        "Act as a general-purpose AI agent. You can assist with a variety of tasks including answering questions, providing recommendations, and generating content.",
        tool_list=None)
    
    input_text = "京都の金閣寺に観光に行きたい。"
    
    result = agent.call(input_text)

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
