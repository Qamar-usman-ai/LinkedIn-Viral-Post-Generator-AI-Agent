from langchain.agents import Tool
from langchain_community.tools.tavily_search import TavilySearchResults

def get_linkedin_tools():
    search = TavilySearchResults(max_results=3)
    
    return [
        Tool(
            name="WebSearch",
            func=search.run,
            description="Useful for searching current LinkedIn trends and viral post structures."
        )
    ]
