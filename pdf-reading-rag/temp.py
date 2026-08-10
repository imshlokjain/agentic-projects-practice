from loader import load_pdf
from splitter import split_documents
from embeddings import create_embedding_model


if __name__ == "__main__":
    docs = load_pdf("sample.pdf")
    chunks = split_documents(docs)

    embeddings = create_embedding_model()

    vector = embeddings.embed_query(
        chunks[0].page_content
    )

    print("Number of dimensions:", len(vector))
    print("First 10 values:", vector[:10])