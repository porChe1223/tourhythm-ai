from typing import Any, Callable
from langchain_core.runnables import Runnable
from langchain_core.runnables.retry import ExponentialJitterParams
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from openai import RateLimitError

from ai.agent._shared.states import AgentType


class BaseAgent:
    """
    BaseAgent
    ---------
    - All Agents based on this Agent
    - Provide RetryWrapper for handling RateLimitError
    - This Agent does not handle State directly
    - Instead, it use String input and returns in Dict which can be Merged to State

    Arguments
    ---------
    - agent_type: AgentType from states
    - model: LLM Model from models
    - system_prompt: System Prompt for the Agent

    Methods
    -------
    - call: Call the Agent with given input text and use tools with given optional tool list
    """
    def __init__(
        self,
        agent_type: AgentType,
        model: ChatOpenAI,
        system_prompt: str,
    ) -> None:
        self.AgentType = agent_type
        self.Model = model
        self.SystemPrompt = system_prompt
        
    
    def call(
        self, input_text: str,
        tool_list: list[Callable] | None = None
    ) -> dict[str, Any]:
        try:
            # Create Agent
            self.Agent = create_agent(
                name=self.AgentType,
                model=self.Model,
                system_prompt=self.SystemPrompt,
                tools=tool_list
            )

            # Call Agent with RetryWrapper
            response = RetryWrapper(self.Agent).invoke({"user_input": input_text})

            # Return Response in Dict format
            return {
                "output": response["messages"][-1].content,
                "assignee": self.AgentType
            }

        except Exception as e:
            error_message = f"Error from {self.AgentType} Agent: {e}"
            return {
                "output": error_message,
                "assignee": self.AgentType
            }


class RetryWrapper:
    """
    RetryWrapper
    ------------
    - Wrapper for Retrying for RateLimitError.

    Arguments
    ---------
    - runnable: Runnable to be wrapped

    Methods
    -------
    - ainvoke: Async invoke with retry
    - invoke: Sync invoke with retry
    """
    def __init__(self, runnable: Runnable):
        self.runnable = runnable.with_retry(
            retry_if_exception_type=(RateLimitError,),
            wait_exponential_jitter=True,
            stop_after_attempt=2,
            exponential_jitter_params=\
                ExponentialJitterParams(initial=70, max=70, exp_base=1, jitter=0)
        )
    

    async def ainvoke(self, *args, **kwargs):
        return await self.runnable.ainvoke(*args, **kwargs)
    

    def invoke(self, *args, **kwargs):
        return self.runnable.invoke(*args, **kwargs)
