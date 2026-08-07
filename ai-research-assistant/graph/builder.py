from langgraph.graph import StateGraph
from langgraph.graph import START, END

from graph.state import ResearchState
from graph.nodes import assistant_node, tool_node
from graph.edges import tools_condition

builder = StateGraph(ResearchState)

builder.add_node("assistant", assistant_node)
builder.add_node("tools", tool_node)

builder.add_edge(START, "assistant")

builder.add_conditional_edges(
    "assistant",
    tools_condition,
)

builder.add_edge("tools", "assistant")

graph = builder.compile()