from fastapi import APIRouter
from pydantic import BaseModel
from app.services.query_service import answer_question

router = APIRouter()

class QueryRequest(BaseModel):
    context: str
    question: str

@router.post("/query")
def query_pdf(data: QueryRequest):
    answer = answer_question(data.context, data.question)
    return {"answer": answer}
