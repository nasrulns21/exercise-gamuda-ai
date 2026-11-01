from fastapi import APIRouter, FastAPI

todos = APIRouter(prefix="/todos", tags=["todos"])
books = APIRouter(prefix="/books", tags=["books"])

@todos.get("")
async def list_todos(): return [{"id": 1, "title": "Review routers", "completed": True}]

@books.get("")
async def list_books(): return [{"id": 1, "title": "FastAPI", "category": "technology"}]

app = FastAPI(title="Todos and Books API")
app.include_router(todos)
app.include_router(books)
