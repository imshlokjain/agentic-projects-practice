from loader import load_pdf
from splitter import split_documents
from embeddings import create_embedding_model
from vector_store import create_vector_store


if __name__ == "__main__":

    print("Loading PDF...")

    docs = load_pdf("sample.pdf")

    print(f"Pages loaded: {len(docs)}")

    print("Splitting PDF...")

    chunks = split_documents(docs)

    print(f"Chunks created: {len(chunks)}")

    print("Creating embeddings...")

    embeddings = create_embedding_model()

    print("Creating vector store...")

    create_vector_store(
        chunks,
        embeddings
    )

    print("Vector store created successfully.")