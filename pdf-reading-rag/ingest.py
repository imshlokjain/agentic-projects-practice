from pathlib import Path

from loader import load_pdf
from splitter import split_documents
from embeddings import create_embedding_model
from vector_store import create_vector_store


BASE_DIR = Path(__file__).resolve().parent
PDF_PATH = BASE_DIR / "sample.pdf"


if __name__ == "__main__":

    print("Loading PDF...")
    print(f"PDF: {PDF_PATH}")

    docs = load_pdf(str(PDF_PATH))

    print(f"Pages loaded: {len(docs)}")

    for i, doc in enumerate(docs):
        print(f"\n--- PAGE {i + 1} ---")
        print(doc.page_content[:1000])

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