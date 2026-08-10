import os

from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings


load_dotenv()


def create_embedding_model():
    embeddings = CohereEmbeddings(
        model="embed-v4.0",
        cohere_api_key=os.getenv("COHERE_API_KEY"),
    )

    return embeddings