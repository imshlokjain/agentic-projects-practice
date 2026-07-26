from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    timeout=30,
    max_retries=1
)

messages = [
    SystemMessage(
        content="You are a research assistant. Keep answers concise."
    )
]

exit_phrases = [
    "exit",
    "quit",
    "bye",
    "goodbye",
    "ok bye",
    "okay bye"
]

while True:
    question = input("\nYou: ").strip()

    if question.lower() in exit_phrases:
        print("Research assistant stopped.")
        break

    messages.append(
        HumanMessage(content=question)
    )

    response = llm.invoke(messages)

    messages.append(response)

    print("\nAssistant:")
    print(response.content)