# Week 9 - RAG, AI Agents, and MCP

This week covers document retrieval, tool-calling agents, conversation memory, middleware, and Model Context Protocol servers.

## Exercises

1. `01-pdf-vector-store` - MongoDB Atlas vector index for PDF chunks.
2. `02-rag-fastapi` - FastAPI endpoint for questions about a PDF.
3. `03-rag-chatbot` - React chat interface connected to the RAG endpoint.
4. `04-currency-agent` - exchange-rate tool using the Frankfurter API.
5. `05-agent-memory` - thread-based short-term memory.
6. `06-postgres-agent-memory` - persistent agent checkpoints in PostgreSQL.
7. `07-summarisation-middleware` - compact long conversation history.
8. `08-model-fallback` - retry a request with a backup model.
9. `09-mcp-remote-search` - multi-server MCP client with Tavily search.
10. `10-mcp-postgres-readonly` - read-only PostgreSQL MCP server.

The `original-work` folder contains my earlier Week 9 Python exercises. Its local `.env` file is not included.

Tests use local examples and injected clients, so they do not spend API credits. MongoDB Atlas, PostgreSQL, Gemini, Tavily, and LangSmith checks require the relevant local account or service.
