from fastapi import APIRouter
from pydantic import BaseModel
import subprocess
from app.services.retrieval_service import retrieve_similar_chunks

router = APIRouter( tags=["QA"])

class QuestionRequest(BaseModel):
    question: str

@router.post("/ask")
def ask_question(req: QuestionRequest):
    chunks = retrieve_similar_chunks(req.question)

    if not chunks:
        return {"answer": "No documents available to answer this question."}

    context = "\n\n".join(chunks)

    prompt = f"""
You are a helpful AI assistant.
Answer the question ONLY using the context below.

Context:
{context}

Question:
{req.question}

Answer:
"""

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        text=True,
        encoding="utf-8",
        capture_output=True
    )

    return {"answer": result.stdout.strip()}
