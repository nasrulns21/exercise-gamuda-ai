import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg://postgres:password@localhost:5432/gamuda_todos")


def is_postgresql_url(value: str = DATABASE_URL) -> bool:
    return value.startswith(("postgresql://", "postgresql+psycopg://"))
