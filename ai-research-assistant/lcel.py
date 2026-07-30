from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    timeout=30,
    max_retries=1
)

parser = StrOutputParser()

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

chain = prompt | llm | parser

topic = input("What would you like to research? ").strip()

response = chain.invoke({
    "topic": topic
})

print("\nAssistant:")
print(response)