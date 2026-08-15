from embeddings import create_embedding_model
from vector_store import load_vector_store
from retriever import create_retriever
from llm import llm
from prompt import prompt
from sources import format_sources
from question_rewriter import rewrite_question

from langchain_core.messages import HumanMessage, AIMessage


if __name__ == "__main__":

    # ==================================================
    # 1. LOAD EMBEDDING MODEL
    # ==================================================

    embeddings = create_embedding_model()


    # ==================================================
    # 2. LOAD EXISTING VECTOR STORE
    # ==================================================

    vector_store = load_vector_store(
        embeddings
    )


    # ==================================================
    # 3. CREATE RETRIEVER
    # ==================================================

    retriever = create_retriever(
        vector_store
    )


    # ==================================================
    # 4. CREATE CONVERSATION HISTORY
    # ==================================================

    chat_history = []


    # ==================================================
    # 5. START APPLICATION
    # ==================================================

    print("=" * 50)
    print("PDF RAG Assistant")
    print("Type 'exit' to quit.")
    print("=" * 50)


    # ==================================================
    # 6. CHAT LOOP
    # ==================================================

    while True:

        question = input("\nYou: ")


        # ------------------------------------------------
        # EXIT CONDITION
        # ------------------------------------------------

        if question.lower() in ["exit", "quit", "bye"]:

            print("\nAssistant: Goodbye!")

            break


        # ==================================================
        # 7. CREATE RETRIEVAL QUESTION
        # ==================================================

        if chat_history:

            retrieval_question = rewrite_question(
                question,
                chat_history
            )

            print(
                f"\n[Retrieval Question]: "
                f"{retrieval_question}"
            )

        else:

            retrieval_question = question


        # ==================================================
        # 8. RETRIEVE RELEVANT DOCUMENTS
        # ==================================================

        documents = retriever.invoke(
            retrieval_question
        )


        # ==================================================
        # 9. DEBUG: DISPLAY RETRIEVED DOCUMENTS
        # ==================================================

        print("\n[Retrieved Documents]")
        print(
            f"Number of chunks: {len(documents)}"
        )

        for i, doc in enumerate(documents):

            print(
                f"\n--- Chunk {i + 1} ---"
            )

            print(
                "Metadata:",
                doc.metadata
            )

            print("Content:")

            print(
                doc.page_content
            )


        # ==================================================
        # 10. BUILD CONTEXT FOR LLM
        # ==================================================

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


        # ==================================================
        # 11. BUILD ANSWERING PROMPT
        # ==================================================

        messages = prompt.invoke(
        {
            "chat_history": chat_history,
            "context": context,
            "question": question
        }
)


        # ==================================================
        # 12. GENERATE ANSWER
        # ==================================================

        response = llm.invoke(
            messages
        )


        # ==================================================
        # 13. DISPLAY ANSWER
        # ==================================================

        print("\nAssistant:")

        print(
            response.content
        )


        # ==================================================
        # 14. DISPLAY SOURCES
        # ==================================================

        sources = format_sources(
            documents
        )

        print("\nSources:")

        for source in sources:

            print(
                f"- {source}"
            )


        # ==================================================
        # 15. UPDATE CONVERSATION HISTORY
        # ==================================================

        chat_history.append(
            HumanMessage(
                content=question
            )
        )

        chat_history.append(
            AIMessage(
                content=response.content
            )
        )