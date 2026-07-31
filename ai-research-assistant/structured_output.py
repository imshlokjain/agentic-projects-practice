from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import MessagesPlaceholder

load_dotenv()


class ResearchResponse(BaseModel):

    topic: str = Field(
        description="The research topic"
    )

    summary: str = Field(
        description="A concise summary of the topic"
    )

    key_points: list[str] = Field(
        description="The important points about the topic"
    )


llm = ChatGroq(
    model="openai/gpt-oss-20b",
    timeout=30,
    max_retries=1
)


structured_llm = llm.with_structured_output(
    ResearchResponse
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a research assistant. "
        "Provide accurate and concise research."
    ),
    (
        "human",
        "Research and explain {topic}."
    )
])


chain = prompt | structured_llm


while True:

    topic = input(
        "\nWhat would you like to research? "
    ).strip()

    if topic.lower() in ["exit", "quit", "bye"]:
        print("Assistant: Goodbye!")
        break

    response = chain.invoke({
        "topic": topic
    })

    print("\nTopic:")
    print(response.topic)

    print("\nSummary:")
    print(response.summary)

    print("\nKey Points:")

    for point in response.key_points:
        print("-", point)