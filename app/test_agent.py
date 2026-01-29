import pytest
from src.tools import get_linkedin_tools

def test_tools_list():
    tools = get_linkedin_tools()
    assert len(tools) > 0
    assert tools[0].name == "WebSearch"
