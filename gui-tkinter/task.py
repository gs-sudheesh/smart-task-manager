from datetime import datetime
# Used for date validation if needed later

# Represents a single task with title, priority, and due date
class Task:
    def __init__(self, title, priority, due_date):
        # Constructor initializes task attributes
        self.title = title
        self.priority = priority
        self.due_date = due_date
    
    def __str__(self):
        # Defines how the task is printed (e.g., in view_tasks)
        return f"{self.title} | Priority: {self.priority} | Due: {self.due_date}"
    
    def to_dict(self):
        # Converts the Task object to a dictionary for saving to JSON
        return {
            "title": self.title,
            "priority": self.priority,
            "due_date": self.due_date
        }
    
    @staticmethod
    def from_dict(data):
        # Creates a Task object from a dictionary (used when loading from JSON)
        return Task(data["title"], data["priority"], data["due_date"])