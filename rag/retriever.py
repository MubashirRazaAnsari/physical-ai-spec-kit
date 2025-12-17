import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

load_dotenv()

# -------------------------------
# Qdrant client
# -------------------------------
client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY"),
)

COLLECTION = os.getenv("COLLECTION_NAME")

# -------------------------------
# Embedding model (local, CPU)
# -------------------------------
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def retrieve(query: str, top_k: int = 5, score_threshold: float = 0.3):
    """
    Retrieve relevant chunks from Qdrant.

    Strategy:
    1. Primary: semantic similarity search with threshold
    2. Fallback: section-title match (for heading-based queries)

    Returns:
        List of Qdrant points (may be empty)
    """

    # ---- semantic search ----
    query_vector = model.encode(query).tolist()

    results = client.query_points(
        collection_name=COLLECTION,
        query=query_vector,
        limit=top_k,
    ).points

    semantic_hits = [r for r in results if r.score >= score_threshold]

    if semantic_hits:
        return semantic_hits

    # ---- fallback: title-aware retrieval ----
    # This handles queries like:
    # "What is Opening: Synthesis of Insights"
    # without relaxing hallucination guardrails.
    fallback_results = client.query_points(
        collection_name=COLLECTION,
        query=query_vector,
        limit=20,
    ).points

    query_lower = query.lower()

    title_hits = []
    for r in fallback_results:
        title = r.payload.get("section_title", "").lower()
        if query_lower in title:
            title_hits.append(r)

    return title_hits
