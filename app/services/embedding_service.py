import os
import faiss
import numpy as np
from openai import OpenAI

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# OpenAI embedding dimension
EMBEDDING_DIM = 1536

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
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        )
        vector = response.data[0].embedding
        embeddings.append(vector)
        documents.append(chunk)

    vectors = np.array(embeddings).astype("float32")
    index.add(vectors)

    return len(chunks)
