from contextlib import asynccontextmanager
from fastapi import Depends, FastAPI, HTTPException, Response, status
from sqlalchemy.orm import Session

from .database import create_schema, get_db
from .models import TodoModel
from .schemas import Todo, TodoInput

@asynccontextmanager
async def lifespan(_app):
    create_schema()
    yield

app = FastAPI(title="PostgreSQL Todo API", lifespan=lifespan)
items: list[Todo] = []


def reset():
    items.clear()


def list_data():
    return list(items)


def create_data(payload: TodoInput):
    todo = Todo(id=max((x.id for x in items), default=0) + 1, **payload.model_dump())
    items.append(todo)
    return todo


def get_data(item_id: int):
    match = next((x for x in items if x.id == item_id), None)
    if not match:
        raise HTTPException(404, "Todo not found")
    return match


def update_data(item_id: int, payload: TodoInput):
    current = get_data(item_id)
    replacement = Todo(id=current.id, **payload.model_dump())
    items[items.index(current)] = replacement
    return replacement


def delete_data(item_id: int):
    items.remove(get_data(item_id))


def as_schema(row): return Todo(id=row.id, title=row.title, completed=row.completed)

@app.get("/todos", response_model=list[Todo])
async def list_todos(db: Session = Depends(get_db)): return [as_schema(x) for x in db.query(TodoModel).order_by(TodoModel.id)]

@app.post("/todos", response_model=Todo, status_code=201)
async def create_todo(payload: TodoInput, db: Session = Depends(get_db)):
    row = TodoModel(**payload.model_dump()); db.add(row); db.commit(); db.refresh(row); return as_schema(row)

@app.get("/todos/{item_id}", response_model=Todo)
async def get_todo(item_id: int, db: Session = Depends(get_db)):
    row=db.get(TodoModel,item_id)
    if not row: raise HTTPException(404,"Todo not found")
    return as_schema(row)

@app.put("/todos/{item_id}", response_model=Todo)
async def update_todo(item_id: int, payload: TodoInput, db: Session = Depends(get_db)):
    row=db.get(TodoModel,item_id)
    if not row: raise HTTPException(404,"Todo not found")
    row.title=payload.title; row.completed=payload.completed; db.commit(); return as_schema(row)

@app.delete("/todos/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(item_id: int, db: Session = Depends(get_db)):
    row=db.get(TodoModel,item_id)
    if not row: raise HTTPException(404,"Todo not found")
    db.delete(row); db.commit()
    return Response(status_code=204)
