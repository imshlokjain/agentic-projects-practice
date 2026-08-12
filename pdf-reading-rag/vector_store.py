from langchain_chroma import Chroma


COLLECTION_NAME = "pdf-rag"
PERSIST_DIRECTORY = "./chroma_db"


def create_vector_store(chunks, embeddings):
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=PERSIST_DIRECTORY,
    )

    return vector_store


def load_vector_store(embeddings):
    vector_store = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=PERSIST_DIRECTORY,
    )

    return vector_store