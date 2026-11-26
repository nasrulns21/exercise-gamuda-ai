# MCP Remote Search

Connects one agent to three MCP servers, or four when the PostgreSQL exercise is configured:

- Local random-number server over `stdio`.
- Local dice server over streamable HTTP.
- Tavily search server over streamable HTTP.
- Read-only PostgreSQL books server over `stdio` when `DATABASE_URL` is set.

The Tavily key is sent in an `Authorization` header and is never placed in the URL. Start `server/http/roll_dice.py`, then run `main.py`. The tracing variables in the Week 9 `.env.example` are optional.
