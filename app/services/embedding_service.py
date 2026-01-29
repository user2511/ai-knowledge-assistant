import os
import faiss
import numpy as np
#from openai import OpenAI
from sentence_transformers import SentenceTransformer
from app.services.vector_store import VECTOR_STORE

# OpenAI client
#client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model = SentenceTransformer("all-MiniLM-L6-v2")

EMBEDDING_DIM = model.get_sentence_embedding_dimension()

# FAISS index (in-memory)
index = faiss.IndexFlatL2(EMBEDDING_DIM)

# Store original chunks (same order as vectors)
documents: list[str] = []


def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> list[str]:
    """
    Split text into overlapping chunks
    """
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunks.append(" ".join(chunk_words))
        start += chunk_size - overlap

    return chunks


def embed_and_store(text: str) -> int:
    """
    Chunk text, generate embeddings, store in FAISS
    Returns number of chunks stored
    """
    chunks = chunk_text(text)

    if not chunks:
        return 0

    embeddings = []

    for chunk in chunks:
        embedding = model.encode(chunk)
        embeddings.append(embedding)

        VECTOR_STORE.append({
            "text": chunk,
            "embedding": embedding
        })


    # Store chunks + vectors
    for chunk, vector in zip(chunks, embeddings):
        documents.append(chunk)

        

        

    vectors_np = np.array(embeddings).astype("float32")
    index.add(vectors_np)


    

    return len(chunks)

def search_similar_chunks(query: str, top_k: int = 5):
    """
    Embed query and retrieve top-k similar chunks
    """
    if index.ntotal == 0:
        return []

    query_vector = model.encode([query]).astype("float32")

    distances, indices = index.search(query_vector, top_k)

    results = []
    for idx in indices[0]:
        if idx < len(documents):
            results.append(documents[idx])

    return results

