import importlib.util
from pathlib import Path

import pytest


ROOT = Path(__file__).parents[1]


def load(folder: str, filename: str):
    path = ROOT / folder / filename
    spec = importlib.util.spec_from_file_location(folder.replace("-", "_"), path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_pdf_vector_store_uses_trainer_configuration():
    module = load("01-pdf-vector-store", "settings.py")
    assert module.DB_NAME == "test_db"
    assert module.COLLECTION_NAME == "test_collection_pdf"
    assert module.INDEX_NAME == "test-index-pdf"
    assert module.EMBEDDING_DIMENSIONS == 768


def test_rag_service_returns_grounded_answer_and_sources():
    module = load("02-rag-fastapi", "rag_service.py")
    retriever = lambda question: [
        module.Chunk(text="Insulin helps control blood glucose.", page=3),
        module.Chunk(text="Exercise can improve insulin sensitivity.", page=7),
    ]
    service = module.RagService(retriever, lambda question, context: f"Based on the document: {context[0].text}")
    result = service.ask("What does insulin do?")
    assert "document" in result.answer
    assert result.sources == [3, 7]


def test_rag_api_exposes_question_endpoint():
    module = load("02-rag-fastapi", "app/main.py")
    paths = module.app.openapi()["paths"]
    assert "get" in paths["/ask"]
    question = paths["/ask"]["get"]["parameters"][0]
    assert question["name"] == "question" and question["in"] == "query"


def test_currency_tool_parses_usd_to_myr_rate():
    module = load("04-currency-agent", "currency_tool.py")
    client = lambda url: {"base": "USD", "rates": {"MYR": 4.42}, "date": "2026-11-26"}
    result = module.fetch_exchange_rate("USD", "MYR", client)
    assert result.rate == 4.42
    assert result.base == "USD" and result.quote == "MYR"


def test_memory_keeps_threads_separate():
    module = load("05-agent-memory", "memory.py")
    memory = module.ThreadMemory()
    memory.add("thread-a", "user", "My name is Nasrul")
    memory.add("thread-b", "user", "My name is Amir")
    assert memory.messages("thread-a")[0]["content"] == "My name is Nasrul"
    assert memory.messages("thread-b")[0]["content"] == "My name is Amir"


def test_postgres_saver_config_requires_database_uri(monkeypatch):
    module = load("06-postgres-agent-memory", "settings.py")
    monkeypatch.delenv("DB_URI", raising=False)
    with pytest.raises(RuntimeError, match="DB_URI"):
        module.database_uri()
    monkeypatch.setenv("DB_URI", "postgresql://postgres:secret@localhost:5432/agentdb")
    assert module.database_uri().endswith("/agentdb")


def test_summarisation_and_model_fallback():
    summary = load("07-summarisation-middleware", "summarisation.py")
    fallback = load("08-model-fallback", "fallback.py")
    messages = [{"role": "user", "content": f"Message {i}"} for i in range(8)]
    compacted = summary.compact_history(messages, keep_recent=3)
    assert compacted[0]["role"] == "system"
    assert len(compacted) == 4

    calls = []
    models = [
        lambda prompt: (_ for _ in ()).throw(RuntimeError("unavailable")),
        lambda prompt: calls.append(prompt) or "fallback response",
    ]
    assert fallback.generate_with_fallback("hello", models) == "fallback response"
    assert calls == ["hello"]


def test_mcp_remote_search_keeps_key_in_header(monkeypatch):
    module = load("09-mcp-remote-search", "servers.py")
    monkeypatch.setenv("TAVILY_API_KEY", "test-key")
    config = module.build_servers()
    assert config["tavily"]["headers"]["Authorization"] == "Bearer test-key"
    assert "test-key" not in config["tavily"]["url"]
    assert config["random_number"]["transport"] == "stdio"
    assert config["roll_dice"]["transport"] == "streamable_http"
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg://localhost/books_db")
    assert module.build_servers()["postgres"]["transport"] == "stdio"


def test_postgres_mcp_rejects_write_queries():
    module = load("10-mcp-postgres-readonly", "query_guard.py")
    assert module.validate_read_only_sql("SELECT * FROM books") == "SELECT * FROM books"
    with pytest.raises(ValueError, match="read-only"):
        module.validate_read_only_sql("DELETE FROM books")
    with pytest.raises(ValueError, match="single"):
        module.validate_read_only_sql("SELECT 1; SELECT 2")
