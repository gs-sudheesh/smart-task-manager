#task_manager.py - Comments in Python
from storage import save_tasks, load_tasks
from datetime import datetime

#tasks = [] - List declaration
tasks = load_tasks()

#Add task with String (as task) input
# def add_task(task):
#   tasks.append(task)
#   save_tasks(tasks)
#   print(f"Task added: {task}")

def add_task():
    title = input("Enter task title: ")
    priority = input("Enter priority (Low/Med/High): ").capitalize()
    due_date = input("Enter due date (DD/MM/YYYY): ")
    
    # Validate date format
    try:
        datetime.strptime(due_date, "%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Task not added.")
        return
    
    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {title}")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['title']} | Priority: {task['priority']} | Due: {task['due_date']}")

def delete_task(index):
    try:
        removed = tasks.pop(index-1)
        save_tasks(tasks)
        print(f"Task removed: {removed['title']}")
    except IndexError:
        print("Invalid task number.")

def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            index = int(input("Enter task number to delete: "))
            delete_task(index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()