from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from .settings import DATABASE_URL


def database_config() -> dict[str, str]:
    return {"url": DATABASE_URL, "runtime": "PostgreSQL"}

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

def create_schema(): Base.metadata.create_all(engine)

def get_db():
    session = SessionLocal()
    try: yield session
    finally: session.close()
