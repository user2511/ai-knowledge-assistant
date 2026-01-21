from app.services.llm_service import ask_llm

def answer_question(context: str, question: str) -> str:
    prompt = f"""
You are an AI assistant.
Answer the question using ONLY the context below.

Context:
{context}

Question:
{question}

Answer:
"""
    return ask_llm(prompt)
