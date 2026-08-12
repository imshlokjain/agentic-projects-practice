from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful PDF question-answering assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context, say:
"I don't have enough information in the provided document."

Do not invent information that is not present in the context."""
    ),
    (
        "human",
        """Context:
{context}

Question:
{question}"""
    )
])