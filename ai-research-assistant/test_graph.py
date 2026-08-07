print("Step 1")

from graph.builder import graph

print("Step 2")

from langchain_core.messages import HumanMessage

print("Step 3")

response = graph.invoke(
    {
        "messages": [
            HumanMessage(
                content="Explain LangGraph."
            )
        ]
    }
)

print("Step 4")

print(response)

print("Step 5")