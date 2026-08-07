from langgraph.prebuilt import ToolNode

from tools.search import search_web
from config import llm
from graph.state import ResearchState

tools = [search_web]

llm = llm.bind_tools(tools)


def assistant_node(state: ResearchState):
    response = llm.invoke(state["messages"])

    return {
        "messages": [response]
    }


tool_node = ToolNode(tools)