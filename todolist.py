tasks = []

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task(index):
    if 1 <= index <= len(tasks):
        deleted_task = tasks.pop(index - 1)
        print(f"Task '{deleted_task}' deleted.")
    else:
        print("Invalid task index.")

def todo_list():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            new_task = input("Enter the task: ")
            add_task(new_task)
        elif choice == '3':
            show_tasks()
            index_to_delete = int(input("Enter the index of the task to delete: "))
            delete_task(index_to_delete)
        elif choice == '4':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

todo_list()