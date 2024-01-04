class ToDoListManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"description": task, "completed": False})

    def list_tasks(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['description']} - {status}")

    def mark_task_completed(self, task_description):
        description_ = self.tasks[int(task_description)-1]['description']
        for task in self.tasks:
            if task["description"] == description_:
                task["completed"] = True
                status = "Completed" if task["completed"] else "Pending"
                print(f"{task['description']} - {status}")
                break
            
    def remove_task(self, task_description):
        description_ = self.tasks[int(task_description)-1]['description']
        self.tasks = [task for task in self.tasks if task["description"] != description_]

    def clear_tasks(self):
        self.tasks = []

if __name__ == "__main__":
    todo_manager = ToDoListManager()
    while True:
        print("ToDo List Manager")
        print("Insert an option:")
        print("1. Add a new task to the to-do list.")
        print("2. List all the tasks in the to-do list")
        print("3. Mark a task as completed")
        print("4. Clear the entire to-do list")
        print("5. Remove task")
        print("6. Exit")
        print("------------------------------------------")

        option = input("Select an option: ")

        if option == "1":
            task = input("Enter task description: ")
            todo_manager.add_task(task)
        elif option == "2":
            todo_manager.list_tasks()
        elif option == "3":
            task_description = input("Enter task description to mark as completed: ")
            todo_manager.mark_task_completed(task_description)
        elif option == "4":
            todo_manager.clear_tasks()
        elif option == "5":
            todo_manager.remove_task()
        elif option == "6":
            break
        else:
            print("Invalid option. Try again.")