from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

from config import llm
from tools.search import search_web


agent = create_react_agent(
    model=llm,
    tools=[search_web]
)


if __name__ == "__main__":

    response = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="What are today's biggest AI news stories?"
                )
            ]
        }
    )

    print(response["messages"][-1].content)