from task import Task  # Import Task class
from storage import load_tasks, save_tasks  # Import file I/O functions
from datetime import datetime
import constants

# Manages a list of Task objects
class TaskManager:
    def __init__(self):
        # Load tasks from file and convert each dictionary to a Task object
        self.tasks = [Task.from_dict(t) for t in load_tasks()]
    
    def add_task(self, title, priority, due_date, status=False):
        # Create a new Task and add it to the list
        task = Task(title, priority, due_date, status)
        self.tasks.append(task)
        self.save()  # Save updated list to file
    
    def view_tasks(self):
        # Display all tasks in a readable format
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")  # Uses Task.__str__()
    
    def delete_task(self, index):
        # Remove a task by its index
        try:
            removed = self.tasks.pop(index - 1)
            self.save()
            print(f"Task removed: {removed.title}")
        except IndexError:
            print("Invalid task number.")
    
    def toggle_status(self, index):
        try:
            task = self.tasks[index]
            task.status = not task.status
            self.save()
        except IndexError:
            print("Invalid task number.")
    
    def save(self):
        # Save all tasks to file as dictionaries
        save_tasks([task.to_dict() for task in self.tasks])
    
    # Sort tasks by priority: Low < Medium < High
    def sort_by_priority(self):
        priority_order = {"Low": 1, "Med": 2, "High": 3}
        self.tasks.sort(key=lambda task: priority_order.get(task.priority, 0))
        self.view_tasks()
    
    # Sort tasks by due date (earliest first)
    def sort_by_due_date(self):
        self.tasks.sort(key=lambda task: datetime.strptime(task.due_date, constants.DATE_TIME_FORMAT))
        self.view_tasks()
    
    # Filter tasks by keyword in title
    def filter_by_keyword(self, keyword):
        filtered = [task for task in self.tasks if keyword.lower() in task.title.lower()]
        if not filtered:
            print(f"No tasks found with keyword: {keyword}")
        else:
            print(f"Tasks matching '{keyword}':")
            for i, task in enumerate(filtered, 1):
                print(f"{i}. {task}")
    
    # Notification
    def check_due_tasks(self):
        now = datetime.now().strftime(constants.DATE_TIME_FORMAT)
        return [task for task in self.tasks if task.due_date == now]