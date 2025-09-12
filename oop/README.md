# Object-Oriented Programming - Task Manager

An advanced command-line task management application built using object-oriented programming principles. This project demonstrates classes, encapsulation, and advanced data manipulation techniques.

## 🎯 Features

- ✅ **All Basic Features**: Add, view, and delete tasks
- ✅ **Sort by Priority**: Organize tasks (Low < Medium < High)
- ✅ **Sort by Due Date**: Arrange tasks chronologically
- ✅ **Filter by Keyword**: Search tasks by title content
- ✅ **Clean Architecture**: Object-oriented design with proper separation
- ✅ **Data Persistence**: JSON file storage
- ✅ **Enhanced CLI**: More interactive and feature-rich interface

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Setup
```bash
cd oop
# No additional installation needed
```

## 🚀 Running the Application

```bash
python main.py
```

## 📖 Usage

### Menu Options
1. **Add Task** - Create a new task
2. **View Tasks** - Display all tasks
3. **Delete Task** - Remove a task by number
4. **Sort by Priority** - Organize by priority level
5. **Sort by Due Date** - Arrange chronologically
6. **Filter by Keyword** - Search task titles
7. **Exit** - Close the application

### Input Format
- **Date**: `DD-MM-YYYY` (e.g., 25-12-2024)
- **Priority**: Low, Med, High
- **Title**: Any descriptive text

### Example Session
```
=== Advanced Task Manager ===
1. Add Task
2. View Tasks
3. Delete Task
4. Sort by Priority
5. Sort by Due Date
6. Filter by Keyword
7. Exit
Choose an option: 4

Tasks sorted by priority:
1. Buy groceries | Priority: Low | Due: 20-12-2024
2. Team meeting | Priority: Med | Due: 22-12-2024
3. Project deadline | Priority: High | Due: 25-12-2024
```

## 📁 File Structure

```
oop/
├── main.py           # Application entry point
├── task.py           # Task class definition
├── task_manager.py   # TaskManager class
├── storage.py        # File I/O operations
├── tasks.json        # Data storage (auto-created)
└── README.md        # This file
```

## 🏗️ Architecture

### Task Class (`task.py`)
```python
class Task:
    def __init__(self, title, priority, due_date)
    def __str__(self)                    # String representation
    def to_dict(self)                    # Convert to dictionary
    @staticmethod
    def from_dict(data)                  # Create from dictionary
```

### TaskManager Class (`task_manager.py`)
```python
class TaskManager:
    def __init__(self)                   # Load existing tasks
    def add_task(self, title, priority, due_date)
    def view_tasks(self)                 # Display all tasks
    def delete_task(self, index)         # Remove task
    def sort_by_priority(self)           # Sort by priority
    def sort_by_due_date(self)           # Sort by date
    def filter_by_keyword(self, keyword) # Search tasks
    def save(self)                       # Persist to file
```

## 🔧 Key Methods

### Sorting
- **Priority Sorting**: Low (1) < Med (2) < High (3)
- **Date Sorting**: Chronological order (earliest first)

### Filtering
- **Case-insensitive** keyword search
- **Partial matching** in task titles
- **Real-time results** display

## 📊 Data Format

Tasks are stored in `tasks.json`:
```json
[
    {
        "title": "Complete project report",
        "priority": "High",
        "due_date": "25-12-2024"
    }
]
```

## 🎓 Learning Objectives

This project teaches:
- **Classes and Objects**: Creating and using classes
- **Encapsulation**: Data hiding and method organization
- **Constructor**: `__init__` method for object initialization
- **String Representation**: `__str__` method for display
- **Static Methods**: `@staticmethod` decorator
- **Data Serialization**: Converting objects to/from JSON
- **Method Chaining**: Combining multiple operations
- **Error Handling**: Robust exception management

## 🔍 Advanced Features

### Priority Sorting Algorithm
```python
priority_order = {"Low": 1, "Med": 2, "High": 3}
self.tasks.sort(key=lambda task: priority_order.get(task.priority, 0))
```

### Date Sorting
```python
self.tasks.sort(key=lambda task: datetime.strptime(task.due_date, "%d-%m-%Y"))
```

### Keyword Filtering
```python
filtered = [task for task in self.tasks if keyword.lower() in task.title.lower()]
```

## 🚨 Error Handling

The application handles:
- Invalid date formats
- File I/O errors
- Invalid task indices
- Missing or corrupted data files
- Empty search results

---

**Perfect for learning OOP concepts! 🏗️✨**
