# Agent Short-Term Memory

The exercise compares conversations with and without a checkpointer. `memory.py` demonstrates thread separation locally; `langgraph_example.py` shows the LangGraph `InMemorySaver` setup.

Using a different `thread_id` starts a separate conversation. Without a checkpointer, earlier messages are not available to later calls.
