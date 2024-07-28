import pickle

class Task:
    def __init__(self, title, description="", completed=False):
        self.title = title
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Title: {self.title}, Description: {self.description}, Status: {status}"

class ArpitTaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description=""):
        new_task = Task(title, description)
        self.tasks.append(new_task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

    def update_task(self, index, title=None, description=None, completed=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            if completed is not None:
                task.completed = completed
        else:
            print("Task not found.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Task not found.")

    def save_tasks(self, filename="data.pkl"):
        with open(filename, 'wb') as f:
            pickle.dump(self.tasks, f)

    def load_tasks(self, filename="data.pkl"):
        try:
            with open(filename, 'rb') as f:
                self.tasks = pickle.load(f)
        except FileNotFoundError:
            self.tasks = []

def main():
    manager = ArpitTaskManager()
    manager.load_tasks()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Save and Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description (optional): ")
            manager.add_task(title, description)

        elif choice == "2":
            manager.view_tasks()

        elif choice == "3":
            manager.view_tasks()
            index = int(input("Enter task number to update: ")) - 1
            title = input("Enter new title (leave blank to keep unchanged): ")
            description = input("Enter new description (leave blank to keep unchanged): ")
            completed = input("Mark as completed? (yes/no): ").strip().lower() == "yes"
            manager.update_task(index, title or None, description or None, completed)

        elif choice == "4":
            manager.view_tasks()
            index = int(input("Enter task number to delete: ")) - 1
            manager.delete_task(index)

        elif choice == "5":
            manager.save_tasks()
            print("Tasks saved. Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
