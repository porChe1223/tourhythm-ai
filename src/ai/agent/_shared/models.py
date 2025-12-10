from langchain_openai import ChatOpenAI

from config import Setting


"""
Models for Agents
"""

basic_openai = ChatOpenAI(model="gpt-4o-mini",
                          temperature=0,
                          api_key=Setting().OPENAI_API_KEY.get_secret_value())


def structured_openai(structure):
    """
    Create a ChatOpenAI instance with structured output based on a Pydantic model
    """
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=Setting().OPENAI_API_KEY.get_secret_value()
    )
    
    return llm.with_structured_output(structure)
