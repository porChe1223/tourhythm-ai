from langchain_tavily import TavilySearch
from langchain_core.tools import tool
from tenacity import retry, stop_after_attempt, wait_fixed


@tool
def tavily_research_tool(query: str) -> str:
    """
    TavilyResearch Tool
    --------------------
    - Perform web searches using Tavily and return summarized results.
    - Provides Several Retries on Failure.

    Attributes
    ----------
    query : The search query string
    """
    search = TavilySearch(max_results = 3)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def research_with_retry(query: str) -> str:
        return search.invoke(query)
    
    return research_with_retry(query)
