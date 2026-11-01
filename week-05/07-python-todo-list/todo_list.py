class ListTodoManager:
    def __init__(self) -> None:
        self.pending: list[str] = []
        self.completed: list[str] = []

    def add(self, title: str) -> None:
        title = title.strip()
        if not title:
            raise ValueError("Task title is required")
        self.pending.append(title)

    def complete(self, number: int) -> str:
        if number < 1 or number > len(self.pending):
            raise IndexError("Task number is out of range")
        task = self.pending.pop(number - 1)
        self.completed.append(task)
        return task

    def counts(self) -> dict[str, int]:
        return {"pending": len(self.pending), "completed": len(self.completed), "total": len(self.pending) + len(self.completed)}

    def numbered(self) -> list[str]:
        return [f"{index}. {title}" for index, title in enumerate(self.pending, 1)]


def main() -> None:
    manager = ListTodoManager()
    while True:
        print("\n1 Add  2 Complete  3 List  4 Counts  5 Exit")
        choice = input("Choose: ").strip()
        try:
            if choice == "1": manager.add(input("Task: "))
            elif choice == "2": manager.complete(int(input("Task number: ")))
            elif choice == "3": print("\n".join(manager.numbered()) or "No pending tasks.")
            elif choice == "4": print(manager.counts())
            elif choice == "5": break
            else: print("Invalid menu choice.")
        except (ValueError, IndexError) as error:
            print(error)


if __name__ == "__main__":
    main()
