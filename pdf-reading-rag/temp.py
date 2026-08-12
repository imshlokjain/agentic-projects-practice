from loader import load_pdf
from splitter import split_documents
from embeddings import create_embedding_model
from vector_store import create_vector_store
from retriever import create_retriever


if __name__ == "__main__":
    # 1. Load PDF
    docs = load_pdf("sample.pdf")

    # 2. Split into chunks
    chunks = split_documents(docs)

    # 3. Create embedding model
    embeddings = create_embedding_model()

    # 4. Create vector store
    vector_store = create_vector_store(
        chunks,
        embeddings
    )

    # 5. Create retriever
    retriever = create_retriever(vector_store)

    # 6. Ask a question
    question = "What is this document about?"

    # 7. Retrieve relevant chunks
    results = retriever.invoke(question)

    print(f"Retrieved {len(results)} chunks\n")

    for i, doc in enumerate(results):
        print(f"--- Result {i + 1} ---")
        print(doc.page_content)
        print("\nMetadata:")
        print(doc.metadata)
        print()