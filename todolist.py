todo_list = []

def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Complete")
    print("5. Exit")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(todo_list, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{i}. {task['task']} [{status}]")

def add_task():
    task = input("Enter the task: ")
    todo_list.append({"task": task, "completed": False})
    print(f"'{task}' has been added to your to-do list.")

def remove_task():
    view_tasks()
    try:
        task_number = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_number < len(todo_list):
            removed_task = todo_list.pop(task_number)
            print(f"'{removed_task['task']}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_task_complete():
    view_tasks()
    try:
        task_number = int(input("Enter the number of the task to mark as complete: ")) - 1
        if 0 <= task_number < len(todo_list):
            todo_list[task_number]["completed"] = True
            print(f"'{todo_list[task_number]['task']}' has been marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_task_complete()
        elif choice == "5":
            print("Exiting the to-do list program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
