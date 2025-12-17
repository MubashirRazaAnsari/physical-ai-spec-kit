import os
from pathlib import Path
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

from chunker import chunk_markdown
from embed import embed_texts

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_URL"),
    api_key=os.getenv("QDRANT_API_KEY")
)

COLLECTION = os.getenv("COLLECTION_NAME")

# Create collection (idempotent)
client.recreate_collection(
    collection_name=COLLECTION,
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

paper_dir = Path("../paper")
chunks = []

for md in paper_dir.glob("*.md"):
    text = md.read_text(encoding="utf-8")
    chunks.extend(chunk_markdown(text, md.name))

vectors = embed_texts([c["text"] for c in chunks])

points = [
    PointStruct(
        id=i,
        vector=vectors[i],
        payload={
            **chunks[i]["metadata"],
            "text": chunks[i]["text"]
        }
    )
    for i in range(len(chunks))
]


client.upsert(collection_name=COLLECTION, points=points)

print(f"Ingested {len(points)} chunks into Qdrant.")
