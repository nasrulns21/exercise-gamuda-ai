import os

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from sqlalchemy import create_engine, text

from query_guard import validate_read_only_sql


load_dotenv()
engine = create_engine(os.environ["DATABASE_URL"], pool_pre_ping=True)
mcp = FastMCP("Postgres Books")


@mcp.tool()
def list_tables() -> list[str]:
    """List tables in the public PostgreSQL schema."""
    statement = text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_name")
    with engine.connect() as connection:
        return [row[0] for row in connection.execute(statement)]


@mcp.tool()
def run_query(sql: str) -> list[dict]:
    """Run one read-only SELECT query and return at most 50 rows."""
    statement = validate_read_only_sql(sql)
    with engine.connect() as connection:
        connection.execute(text("SET TRANSACTION READ ONLY"))
        rows = connection.exec_driver_sql(statement).mappings().fetchmany(50)
        return [dict(row) for row in rows]


if __name__ == "__main__":
    mcp.run(transport="stdio")
