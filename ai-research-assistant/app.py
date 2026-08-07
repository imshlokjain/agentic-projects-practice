from langchain_core.messages import HumanMessage

from graph.builder import graph


config = {
    "configurable": {
        "thread_id": "research-session"
    }
}


print("=" * 50)
print("AI Research Assistant")
print("Type 'exit' to quit.")
print("=" * 50)


while True:

    query = input("\nYou: ")

    if query.lower() in ["exit", "quit", "bye"]:
        print("\nAssistant: Goodbye!")
        break

    response = graph.invoke(
        {
            "messages": [
                HumanMessage(content=query)
            ]
        },
        config=config
    )

    print("\nAssistant:")

    print(response["messages"][-1].content)