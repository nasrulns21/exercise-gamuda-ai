from sqlalchemy import Boolean, CheckConstraint, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase): pass

class TodoModel(Base):
    __tablename__ = "todos"
    __table_args__ = (CheckConstraint("length(trim(title)) > 0", name="todo_title_not_blank"),)
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(120), nullable=False)
    completed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
