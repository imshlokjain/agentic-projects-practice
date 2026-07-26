from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    timeout=30,
    max_retries=1
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a research assistant. Keep answers concise."
    ),
    (
        "human",
        "Explain {topic}."
    )
])

topic = input("What would you like to research? ").strip()

formatted_prompt = prompt.invoke({
    "topic": topic
})

response = llm.invoke(formatted_prompt)

print("\nAssistant:")
print(response.content)