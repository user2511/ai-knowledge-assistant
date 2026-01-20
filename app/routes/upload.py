print("UPLOAD ROUTE LOADED")


import os
import uuid
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.pdf_service import extract_text_from_pdf
from app.services.embedding_service import embed_and_store

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    file_id = f"{uuid.uuid4()}.pdf"
    file_path = os.path.join(UPLOAD_DIR, file_id)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    text = extract_text_from_pdf(file_path)

    if not text.strip():
        return {
            "status": "error",
            "message": "No text extracted from PDF"
        }

    # 🔥 LAYER 2 CALL
    chunk_count = embed_and_store(text)

    return {
        "status": "success",
        "filename": file.filename,
        "chunks_created": chunk_count
    }