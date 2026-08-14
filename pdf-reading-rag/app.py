from embeddings import create_embedding_model
from vector_store import load_vector_store
from retriever import create_retriever
from llm import llm
from prompt import prompt
from sources import format_sources


if __name__ == "__main__":

    # -------------------------
    # LOAD EXISTING VECTOR DB
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

    while True:

        question = input("\nYou: ")

        if question.lower() in ["exit", "quit", "bye"]:
            print("\nAssistant: Goodbye!")
            break

        # -------------------------
        # RETRIEVAL
        # -------------------------

        documents = retriever.invoke(question)

        print("\n[Retrieved Documents]")
        print(f"Number of chunks: {len(documents)}")

        for i, doc in enumerate(documents):

            print(f"\n--- Chunk {i + 1} ---")
            print("Metadata:", doc.metadata)
            print("Content:")
            print(doc.page_content)

        # -------------------------
        # BUILD CONTEXT
        # -------------------------

        context_parts = []

        for doc in documents:

            source = doc.metadata.get(
                "source",
                "Unknown"
            )

            page = doc.metadata.get(
                "page",
                "Unknown"
            )

            context_parts.append(
                f"""Source: {source}
Page: {page}

{doc.page_content}"""
            )

        context = "\n\n---\n\n".join(
            context_parts
        )

        # -------------------------
        # BUILD PROMPT
        # -------------------------

        messages = prompt.invoke({
            "context": context,
            "question": question
        })

        # -------------------------
        # GENERATE ANSWER
        # -------------------------

        response = llm.invoke(
            messages
        )

        # -------------------------
        # DISPLAY ANSWER
        # -------------------------

        print("\nAssistant:")
        print(response.content)

        # -------------------------
        # DISPLAY SOURCES
        # -------------------------

        sources = format_sources(
            documents
        )

        print("\nSources:")

        for source in sources:
            print(f"- {source}")