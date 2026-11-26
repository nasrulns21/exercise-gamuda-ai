import os
import sys
from pathlib import Path


ROOT = Path(__file__).parent


def build_servers() -> dict:
    tavily_key = os.getenv("TAVILY_API_KEY", "").strip()
    servers = {
        "random_number": {
            "command": sys.executable,
            "args": [str(ROOT / "server" / "stdio" / "random_number.py")],
            "transport": "stdio",
        },
        "roll_dice": {
            "url": "http://localhost:8000/mcp",
            "transport": "streamable_http",
        },
        "tavily": {
            "url": "https://mcp.tavily.com/mcp/",
            "transport": "streamable_http",
            "headers": {"Authorization": f"Bearer {tavily_key}"},
        },
    }
    if os.getenv("DATABASE_URL"):
        servers["postgres"] = {
            "command": sys.executable,
            "args": [str(ROOT.parent / "10-mcp-postgres-readonly" / "postgres_server.py")],
            "transport": "stdio",
        }
    return servers
