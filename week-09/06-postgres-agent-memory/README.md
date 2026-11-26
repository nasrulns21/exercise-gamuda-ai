# PostgreSQL Agent Memory

Uses `PostgresSaver` to keep agent checkpoints beyond one process. Create the `agentdb` database, set `DB_URI`, then run `postgres_agent.py`.

The first run calls `checkpointer.setup()` to create the required tables. Change `thread_id` to verify that each conversation stays separate.
