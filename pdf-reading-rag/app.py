from embeddings import create_embedding_model
from vector_store import load_vector_store
from retriever import create_retriever
from llm import llm
from prompt import prompt


if __name__ == "__main__":

    # -------------------------
    # LOAD EXISTING RAG INDEX
    # -------------------------

    embeddings = create_embedding_model()

    vector_store = load_vector_store(
        embeddings
    )

    retriever = create_retriever(
        vector_store
    )

    print("=" * 50)
    print("PDF RAG Assistant")
    print("Type 'exit' to quit.")
    print("=" * 50)

    # -------------------------
    # CHAT LOOP
    # -------------------------

    while True:

        question = input("\nYou: ")

        if question.lower() in ["exit", "quit", "bye"]:
            print("\nAssistant: Goodbye!")
            break

        # Retrieve relevant PDF chunks
        documents = retriever.invoke(question)

        # Convert Documents → context
        context = "\n\n".join(
            doc.page_content
            for doc in documents
        )

        # Build prompt
        messages = prompt.invoke({
            "context": context,
            "question": question
        })

        # Generate answer using Project 1's LLM
        response = llm.invoke(messages)

        print("\nAssistant:")
        print(response.content)