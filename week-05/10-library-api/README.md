# FastAPI Library API

**Source:** Trainer Notes, Week 5 FastAPI exercise. **Original work:** expands the retained `week-05/fastapi-introduction` starter.

Supports list, title lookup, author/year filters, create, update and delete with validation and not-found responses.

```powershell
python -m pip install -r requirements.txt
python -m pytest tests -v
python -m uvicorn app.main:app --reload
```

The automated suite verifies service logic, validation, not-found behaviour, and the generated OpenAPI route/method contract. On this workstation, Python 3.14 hangs even on empty `asyncio` and Trio event loops, so an HTTP runtime smoke test remains **External verification required**. On a normal Python 3.12/3.13 environment, start Uvicorn and run `curl http://127.0.0.1:8000/books`.
