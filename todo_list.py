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
        #print(self.tasks[task_description])
        for task in self.tasks:
            #print(task["description"])
            if task["description"] == task_description:
                task["completed"] = True
                status = "Completed" if task["completed"] else "Pending"
                print(f"{task['description']} - {status}")
                break
            

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
        print("5. Exit")
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
            break
        else:
            print("Invalid option. Try again.")