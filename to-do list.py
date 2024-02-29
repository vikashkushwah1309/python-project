class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        # Add task to the list
        pass

    def delete_task(self, task_index):
        # Delete task from the list
        pass

    def list_tasks(self):
        # List all tasks
        pass

    def mark_task_completed(self, task_index):
        # Mark task as completed
        pass

def main():
    todo_list = TodoList()

    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. List Tasks")
        print("4. Mark Task as Completed")
        print("5. Exit")
        choice = input("Enter your choice:")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "3":
            todo_list.list_tasks()
        elif choice == "4":
            task_index = int(input("Enter task index to mark as completed: "))
            todo_list.mark_task_completed(task_index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
