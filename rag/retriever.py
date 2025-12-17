import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from google import genai

load_dotenv()

# -----------------------------
# Clients
# -----------------------------
qdrant = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

COLLECTION = os.getenv("COLLECTION_NAME")

genai_client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# -----------------------------
# Embedding
# -----------------------------
def embed_query(text: str):
    response = genai_client.models.embed_content(
        model="models/embedding-001",
        contents=text
    )
    return response.embeddings[0].values

# -----------------------------
# Retrieval
# -----------------------------
def retrieve(query: str, top_k: int = 5, score_threshold: float = 0.3):
    query_vector = embed_query(query)

    results = qdrant.query_points(
        collection_name=COLLECTION,
        query=query_vector,
        limit=top_k,
    ).points

    semantic_hits = [r for r in results if r.score >= score_threshold]
    if semantic_hits:
        return semantic_hits

    # Fallback: title match
    fallback = qdrant.query_points(
        collection_name=COLLECTION,
        query=query_vector,
        limit=20,
    ).points

    q = query.lower()
    return [
        r for r in fallback
        if q in r.payload.get("section_title", "").lower()
    ]
