# RAG FastAPI Endpoint

`GET /ask?question=...` returns an answer and the PDF page numbers used as sources. The service accepts injected retrieval and answer functions for local tests. `live_service.py` contains the MongoDB Atlas and Gemini wiring used when account credentials are available.

Run from this folder with `uvicorn app.main:app --reload` and open `/docs`. The sample service works without accounts. Set `USE_LIVE_RAG=true` together with the Gemini and MongoDB variables to use the indexed PDF.
