import sys
from pathlib import Path


def postgres_server_config() -> dict:
    return {
        "command": sys.executable,
        "args": [str(Path(__file__).with_name("postgres_server.py"))],
        "transport": "stdio",
    }
