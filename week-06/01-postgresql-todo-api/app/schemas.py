from pydantic import BaseModel, Field


class TodoInput(BaseModel):
    title: str = Field(min_length=1, max_length=120)
    completed: bool = False


class Todo(TodoInput):
    id: int
