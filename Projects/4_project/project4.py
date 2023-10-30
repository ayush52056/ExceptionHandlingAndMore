import os
import pickle


class Task:
    def __init__(self, id, title, description, due_date, done=False):
        self.id = id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.done = done


class TaskList:
    def __init__(self):
        self.tasks = []
        self.filename = "task_list.pkl"

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        for task in self.tasks:
            status = "Done" if task.done else "Not Done"
            print(f"Task ID: {task.id}, Title: {task.title}, Status: {status}")

    def mark_task_as_done(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.done = True

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self.tasks, file)

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "rb") as file:
                self.tasks = pickle.load(file)


if __name__ == "__main__":
    task_list = TaskList()
    task_list.load_from_file()

    while True:
        print("\nTask List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            task_id = len(task_list.tasks) + 1
            task = Task(task_id, title, description, due_date)
            task_list.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            task_list.view_tasks()

        elif choice == "3":
            task_id = int(input("Enter task ID to mark as done: "))
            task_list.mark_task_as_done(task_id)
            print("Task marked as done!")

        elif choice == "4":
            task_list.save_to_file()
            print("Exiting the program.")
            break
