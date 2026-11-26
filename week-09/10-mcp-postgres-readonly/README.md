# Read-Only PostgreSQL MCP Server

Creates a small `books_db` database and exposes two MCP tools: `list_tables` and `run_query`. The server rejects non-read-only and multi-statement SQL before it reaches PostgreSQL, and the transaction is also set to read-only.

Run `books.sql`, set `DATABASE_URL`, add `postgres_server.py` to the MCP client configuration, then ask: “How many books are there, and who wrote the first one?”
