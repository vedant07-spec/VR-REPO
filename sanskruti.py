todo_list = []

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def view_tasks():
    if not todo_list:
        print("No tasks yet!")
    else:
        print("Your Tasks:")
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print("Task added!")

def remove_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(todo_list):
            removed = todo_list.pop(task_num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    if choice == '1':
        view_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
