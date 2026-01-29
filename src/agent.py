from langchain.agents import create_react_agent, AgentExecutor
from langchain_groq import ChatGroq
from langchain import hub
from .tools import get_linkedin_tools

def initialize_agent(api_key):
    llm = ChatGroq(api_key=api_key, model_name="llama-3.3-70b-versatile")
    tools = get_linkedin_tools()
    
    # We pull a standard ReAct prompt but can also use our src/prompts.py
    prompt = hub.pull("hwchase17/react")
    
    agent = create_react_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
