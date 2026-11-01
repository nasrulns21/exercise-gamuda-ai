class DictionaryTodoManager:
    def __init__(self) -> None:
        self.tasks: dict[int, dict[str, object]] = {}
        self._next_id = 1

    def add(self, title: str) -> int:
        title = title.strip()
        if not title:
            raise ValueError("Task title is required")
        task_id = self._next_id
        self.tasks[task_id] = {"title": title, "completed": False}
        self._next_id += 1
        return task_id

    def complete(self, task_id: int) -> None:
        if task_id not in self.tasks:
            raise KeyError("Task ID was not found")
        self.tasks[task_id]["completed"] = True

    def counts(self) -> dict[str, int]:
        completed = sum(bool(task["completed"]) for task in self.tasks.values())
        return {"pending": len(self.tasks) - completed, "completed": completed, "total": len(self.tasks)}


if __name__ == "__main__":
    manager = DictionaryTodoManager()
    manager.add("Try the dictionary task manager")
    print(manager.tasks)
