print("MAIN APP LOADED")

from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI
from app.routes.upload import router as upload_route
from app.routes.search import router as search_route
from app.routes.query import router as query_route
from app.routes.qa import router as qa_router

app = FastAPI(title="AI Knowledge Assistant")
app.include_router(upload_route, prefix="/api")
app.include_router(search_route, prefix="/api")
app.include_router(query_route, prefix="/api")
app.include_router(qa_router, prefix="/api")

@app.get("/")
def health():
    return {"status": "ok"}
