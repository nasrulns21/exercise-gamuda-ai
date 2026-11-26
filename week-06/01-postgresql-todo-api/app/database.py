from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
from .settings import DATABASE_URL


def database_config() -> dict[str, str]:
    return {"url": DATABASE_URL, "runtime": "PostgreSQL"}

_engine = None
_session_factory = None


def get_engine():
    global _engine
    if _engine is None:
        _engine = create_engine(DATABASE_URL, pool_pre_ping=True)
    return _engine


def get_session_factory():
    global _session_factory
    if _session_factory is None:
        _session_factory = sessionmaker(bind=get_engine(), expire_on_commit=False)
    return _session_factory


def create_schema():
    Base.metadata.create_all(get_engine())

def get_db():
    session = get_session_factory()()
    try: yield session
    finally: session.close()
