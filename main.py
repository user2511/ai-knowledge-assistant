print("MAIN APP LOADED")


from fastapi import FastAPI
from app.routes.upload import router as upload_route

app = FastAPI(title="AI Knowledge Assistant")
app.include_router(upload_route, prefix="/api")

@app.get("/")
def health():
    return {"status": "ok"}
