# PostgreSQL Todo API

Complete SQLAlchemy CRUD service with environment-based PostgreSQL configuration. Run with Python 3.12/3.13: `uvicorn app.main:app --reload`. Application startup creates the constrained `todos` table when it does not exist; production routes persist through the database session.

External gate: create `gamuda_todos`, copy `.env.example` to `.env`, install `fastapi uvicorn sqlalchemy psycopg`, then start Uvicorn and test `/docs`.
