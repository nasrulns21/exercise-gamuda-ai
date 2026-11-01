import pytest
from pathlib import Path
import sys
from fastapi import HTTPException
from pydantic import ValidationError

sys.path.insert(0, str(Path(__file__).parents[1]))
from app.main import (
    BookInput,
    app,
    book_by_id_data,
    book_by_title_data,
    create_book_data,
    delete_book_data,
    list_books_data,
    reset_books,
    update_book_data,
)


def setup_function():
    reset_books()


def test_openapi_exposes_every_required_route_and_method():
    paths = app.openapi()["paths"]
    assert set(paths["/books"]) >= {"get", "post"}
    assert set(paths["/books/{book_id}"]) >= {"get", "put", "delete"}
    assert "get" in paths["/books/title/{title}"]


def test_list_lookup_and_filters():
    assert len(list_books_data()) >= 3
    assert book_by_title_data("Clean Code").author == "Robert C. Martin"
    assert all(book.author == "George Orwell" for book in list_books_data(author="George Orwell"))
    assert all(book.year == 2008 for book in list_books_data(year=2008))


def test_create_update_delete_and_not_found_logic():
    created = create_book_data(BookInput(title="New Book", author="A. Writer", year=2026))
    updated = update_book_data(created.id, BookInput(title="Updated Book", author="A. Writer", year=2025))
    assert updated.title == "Updated Book"
    delete_book_data(created.id)
    with pytest.raises(HTTPException) as error:
        book_by_id_data(created.id)
    assert error.value.status_code == 404


def test_validation_and_missing_title():
    with pytest.raises(ValidationError):
        BookInput(title="", author="A", year=2026)
    with pytest.raises(ValidationError):
        BookInput(title="Future", author="A", year=3000)
    with pytest.raises(HTTPException) as error:
        book_by_title_data("Unknown")
    assert error.value.status_code == 404
