import os


def database_uri() -> str:
    value = os.getenv("DB_URI", "").strip()
    if not value:
        raise RuntimeError("DB_URI is required")
    if not value.startswith(("postgresql://", "postgres://")):
        raise RuntimeError("DB_URI must be a PostgreSQL connection string")
    return value
