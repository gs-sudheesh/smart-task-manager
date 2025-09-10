from task_manager import TaskManager
from datetime import datetime
# Import TaskManager class
# For validating due date format

def add_new_task(manager):
    title = input("Enter task title: ")
    priority = input("Enter priority (Low/Med/High): ").capitalize()
    due_date = input("Enter due date (DD-MM-YYYY): ")
    
    # Validate date format
    try:
        datetime.strptime(due_date, "%d-%m-%Y")
        manager.add_task(title, priority, due_date)
        print("Task added.")
    except ValueError:
        print("Invalid date format.")

# Main function that runs the task manager app
def main():
    manager = TaskManager()  # Create a TaskManager instance
    
    while True:
        # Display menu options
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Sort by Priority")
        print("5. Sort by Due Date")
        print("6. Filter by Keyword")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Collect task details from user
            add_new_task(manager)
        elif choice == '2':
            manager.view_tasks()  # Show all tasks
        elif choice == '3':
            manager.view_tasks()  # Show tasks before deletion
            index = int(input("Enter task number to delete: "))
            manager.delete_task(index)
        elif choice == '4':
            manager.sort_by_priority()
        elif choice == '5':
            manager.sort_by_due_date()
        elif choice == '6':
            keyword = input("Enter keyword to search: ")
            manager.filter_by_keyword(keyword)
        elif choice == '7':
            print("Goodbye!")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Try again.")

# Ensures this file runs only when executed directly, not when imported
if __name__ == "__main__":
    main()