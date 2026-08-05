from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain_groq import ChatGroq
from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)
from langchain_core.messages import (
    HumanMessage,
    AIMessage
)


load_dotenv()

class ResearchResponse(BaseModel):

    topic: str = Field(
        description="The research topic"
    )

    summary: str = Field(
        description="A concise summary of the research topic"
    )

    key_points: list[str] = Field(
        description="A list of the important points about the research topic"
    )

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    timeout=30,
    max_retries=2
)

structured_llm = llm.with_structured_output(
    ResearchResponse
)

prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
You are a research assistant.

Provide accurate, concise, and useful research.

For every research request:

1. Identify the research topic.
2. Provide a concise summary.
3. Provide a list of important key points.

You MUST provide all required fields:

- topic
- summary
- key_points

Never omit any required field.

Use the previous conversation when the user's current
question refers to something discussed earlier.
"""
    ),

    MessagesPlaceholder(
        variable_name="history"
    ),

    (
        "human",
        "{topic}"
    )
])

chain = prompt | structured_llm


history = []

print("Research Assistant")
print("Type 'exit', 'quit', or 'bye' to stop.")


while True:

    topic = input(
        "\nWhat would you like to research? "
    ).strip()

    if not topic:
        print("\nAssistant: Please enter a research topic.")
        continue

    if topic.lower() in ["exit", "quit", "bye"]:

        print("\nAssistant: Goodbye!")

        break

    try:

        response = chain.invoke({
            "history": history,
            "topic": topic
        })

    except Exception as e:

        print(
            "\nAssistant: "
            "I couldn't generate a valid structured response."
        )

        print("\nError:")
        print(e)

        continue



    print("\nAssistant:")

    print("\nTopic:")
    print(response.topic)

    print("\nSummary:")
    print(response.summary)

    print("\nKey Points:")

    for point in response.key_points:
        print("-", point)

    history.append(
        HumanMessage(
            content=topic
        )
    )

    assistant_text = (
        f"Topic: {response.topic}\n"
        f"Summary: {response.summary}\n"
        f"Key Points:\n"
        + "\n".join(
            f"- {point}"
            for point in response.key_points
        )
    )

    history.append(
        AIMessage(
            content=assistant_text
        )
    )