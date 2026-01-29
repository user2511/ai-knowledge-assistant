import numpy as np
from sentence_transformers import SentenceTransformer
from app.services.vector_store import VECTOR_STORE

model = SentenceTransformer("all-MiniLM-L6-v2")

def retrieve_similar_chunks(query: str, top_k: int = 3):
    if len(VECTOR_STORE) == 0:
        return []

    query_embedding = model.encode(query)

    similarities = []

    for item in VECTOR_STORE:
        chunk_embedding = item["embedding"]
        similarity = np.dot(query_embedding, chunk_embedding) / (
            np.linalg.norm(query_embedding) * np.linalg.norm(chunk_embedding)
        )
        similarities.append((similarity, item["text"]))

    similarities.sort(reverse=True, key=lambda x: x[0])

    return [text for _, text in similarities[:top_k]]
