import importlib
from pathlib import Path
import sys
import pytest
from pydantic import ValidationError

ROOT = Path(__file__).parents[1]


def load(name, relative):
    package_root = ROOT / relative
    for key in [key for key in sys.modules if key == "app" or key.startswith("app.")]:
        del sys.modules[key]
    sys.path.insert(0, str(package_root))
    module = importlib.import_module("app.main")
    sys.path.pop(0)
    return module


def test_postgresql_todo_crud_and_schema():
    module = load("todo_main", "01-postgresql-todo-api")
    module.reset()
    with pytest.raises(ValidationError): module.TodoInput(title="")
    item = module.create_data(module.TodoInput(title="Test database"))
    assert module.get_data(item.id).title == "Test database"
    assert module.update_data(item.id, module.TodoInput(title="Done", completed=True)).completed
    module.delete_data(item.id)
    with pytest.raises(Exception): module.get_data(item.id)


def test_window_and_combined_router_contracts():
    windows = load("window_main", "02-window-routers").app.openapi()["paths"]
    combined = load("combined_main", "03-todos-books-api").app.openapi()["paths"]
    assert {"/left-window", "/right-window"} <= set(windows)
    assert {"/todos", "/books"} <= set(combined)


def test_enhanced_books_have_category_and_cors():
    module = load("enhanced_main", "04-react-fastapi/backend")
    created = module.create_data(module.BookInput(title="API", author="Trainer", category="learning"))
    assert created.category == "learning"
    assert module.list_data("learning") == [created]
    assert any(m.cls.__name__ == "CORSMiddleware" for m in module.app.user_middleware)
