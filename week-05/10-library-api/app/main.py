from datetime import date

from fastapi import FastAPI, HTTPException, Query, Response, status
from pydantic import BaseModel, Field


class BookInput(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    author: str = Field(min_length=1, max_length=120)
    year: int = Field(ge=1000, le=date.today().year + 1)


class Book(BookInput):
    id: int


SEED = [
    Book(id=1, title="Clean Code", author="Robert C. Martin", year=2008),
    Book(id=2, title="1984", author="George Orwell", year=1949),
    Book(id=3, title="Animal Farm", author="George Orwell", year=1945),
]
books: list[Book] = []


def reset_books() -> None:
    books.clear()
    books.extend(book.model_copy() for book in SEED)


reset_books()
app = FastAPI(title="Training Library API")


@app.get("/books", response_model=list[Book])
async def list_books(author: str | None = None, year: int | None = Query(default=None, ge=1000)):
    return list_books_data(author, year)


def list_books_data(author: str | None = None, year: int | None = None):
    return [book for book in books if (author is None or book.author == author) and (year is None or book.year == year)]


@app.get("/books/title/{title}", response_model=Book)
async def book_by_title(title: str):
    return book_by_title_data(title)


def book_by_title_data(title: str):
    match = next((book for book in books if book.title.casefold() == title.casefold()), None)
    if match is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return match


@app.get("/books/{book_id}", response_model=Book)
async def book_by_id(book_id: int):
    return book_by_id_data(book_id)


def book_by_id_data(book_id: int):
    match = next((book for book in books if book.id == book_id), None)
    if match is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return match


@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
async def create_book(payload: BookInput):
    return create_book_data(payload)


def create_book_data(payload: BookInput):
    book = Book(id=max((item.id for item in books), default=0) + 1, **payload.model_dump())
    books.append(book)
    return book


@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: int, payload: BookInput):
    return update_book_data(book_id, payload)


def update_book_data(book_id: int, payload: BookInput):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = Book(id=book_id, **payload.model_dump())
            return books[index]
    raise HTTPException(status_code=404, detail="Book not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    delete_book_data(book_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def delete_book_data(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return
    raise HTTPException(status_code=404, detail="Book not found")
