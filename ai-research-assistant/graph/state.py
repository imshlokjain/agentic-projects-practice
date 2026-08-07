from langgraph.graph import MessagesState


class ResearchState(MessagesState):
    """
    State shared across every node in the graph.

    Currently inherits the default LangGraph messages state.
    Additional fields can be added later as the project grows.
    """
    pass