class ThreadMemory:
    def __init__(self):
        self._threads: dict[str, list[dict[str, str]]] = {}

    def add(self, thread_id: str, role: str, content: str) -> None:
        if not thread_id.strip() or not content.strip():
            raise ValueError("Thread ID and content are required")
        self._threads.setdefault(thread_id, []).append({"role": role, "content": content})

    def messages(self, thread_id: str) -> list[dict[str, str]]:
        return list(self._threads.get(thread_id, []))

    def clear(self, thread_id: str) -> None:
        self._threads.pop(thread_id, None)
