import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    category: str = Field(min_length=1)


class Book(BookInput):
    id: int


items = [Book(id=1, title="Clean Code", author="Robert C. Martin", category="technology")]
app = FastAPI(title="Enhanced Books API")
origins = [x.strip() for x in os.getenv("ALLOWED_ORIGINS", "http://localhost:5173").split(",")]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_methods=["*"], allow_headers=["*"])


def list_data(category: str | None = None):
    return [x for x in items if category is None or x.category == category]


def create_data(payload: BookInput):
    item = Book(id=max(x.id for x in items) + 1, **payload.model_dump())
    items.append(item)
    return item


@app.get("/books", response_model=list[Book])
async def list_books(category: str | None = None): return list_data(category)

@app.post("/books", response_model=Book, status_code=201)
async def create_book(payload: BookInput): return create_data(payload)

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    match = next((x for x in items if x.id == book_id), None)
    if not match: raise HTTPException(404, "Book not found")
    return match
