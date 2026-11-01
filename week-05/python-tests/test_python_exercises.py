from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

import pytest


ROOT = Path(__file__).resolve().parents[1]


def load(name: str, relative: str):
    spec = spec_from_file_location(name, ROOT / relative)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_temperature_conversion_values_and_type_validation():
    module = load("temperature", "05-python-temperature/temperature.py")
    assert module.celsius_to_fahrenheit(0) == 32
    assert module.celsius_to_fahrenheit(100) == 212
    assert module.celsius_to_fahrenheit(-40) == -40
    with pytest.raises(TypeError):
        module.celsius_to_fahrenheit("20")


def test_boolean_expression_is_true():
    module = load("boolean_values", "06-python-booleans/boolean_values.py")
    assert module.boolean_proof() == {"a": True, "b": True, "c": False, "d": True}


def test_list_todo_add_complete_move_and_counts():
    module = load("todo_list", "07-python-todo-list/todo_list.py")
    manager = module.ListTodoManager()
    manager.add("Read notes")
    manager.add("Complete exercise")
    manager.complete(1)
    assert manager.pending == ["Complete exercise"]
    assert manager.completed == ["Read notes"]
    assert manager.counts() == {"pending": 1, "completed": 1, "total": 2}
    with pytest.raises(IndexError):
        manager.complete(9)


def test_dictionary_todo_uses_stable_ids_and_status_updates():
    module = load("todo_dictionary", "08-python-todo-dictionary/todo_dictionary.py")
    manager = module.DictionaryTodoManager()
    first = manager.add("Build API")
    second = manager.add("Test API")
    manager.complete(first)
    assert manager.tasks[first] == {"title": "Build API", "completed": True}
    assert manager.tasks[second]["completed"] is False
    assert manager.counts() == {"pending": 1, "completed": 1, "total": 2}
