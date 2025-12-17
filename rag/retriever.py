import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
import google.genai as genai

load_dotenv()

# Qdrant
client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

COLLECTION = os.getenv("COLLECTION_NAME")

# Gemini for embeddings (lightweight, no torch)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def embed_query(text: str):
    res = genai.embed_content(
        model="models/embedding-001",
        content=text
    )
    return res["embedding"]


def retrieve(query: str, top_k: int = 5, score_threshold: float = 0.3):
    query_vector = embed_query(query)

    results = client.query_points(
        collection_name=COLLECTION,
        query=query_vector,
        limit=top_k,
    ).points

    semantic_hits = [r for r in results if r.score >= score_threshold]
    if semantic_hits:
        return semantic_hits

    # Title fallback
    fallback = client.query_points(
        collection_name=COLLECTION,
        query=query_vector,
        limit=20,
    ).points

    query_lower = query.lower()
    return [
        r for r in fallback
        if query_lower in r.payload.get("section_title", "").lower()
    ]
