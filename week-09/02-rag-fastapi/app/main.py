from pathlib import Path
import sys
import os

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

sys.path.insert(0, str(Path(__file__).parents[1]))
from rag_service import RagService, sample_service


app = FastAPI(title="Diabetes RAG API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["GET"],
    allow_headers=["*"],
)
if os.getenv("USE_LIVE_RAG", "false").lower() == "true":
    from live_service import build_live_service
    service: RagService = build_live_service()
else:
    service = sample_service()


@app.get("/ask")
async def ask(question: str = Query(min_length=3, max_length=500)):
    result = service.ask(question)
    return {"question": question, "answer": result.answer, "sources": result.sources}


@app.get("/health")
async def health():
    return {"status": "ok"}
