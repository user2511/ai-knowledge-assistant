from fastapi import APIRouter
from pydantic import BaseModel

from app.services.embedding_service import search_similar_chunks

router = APIRouter()


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5


@router.post("/search")
def search_docs(request: SearchRequest):
    results = search_similar_chunks(
        query=request.query,
        top_k=request.top_k
    )

    return {
        "query": request.query,
        "results": results
    }
