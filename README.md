# Smart Task Manager

A Python-based task management application with two different implementations: procedural programming and object-oriented programming (OOP). This project demonstrates different programming paradigms while providing a functional task management system.

## 📁 Project Structure

```
smart-task-manager/
├── python_fundamentals/          # Procedural programming approach
│   ├── task_manager.py          # Main application logic
│   └── storage.py               # File I/O operations
├── oop/                         # Object-oriented programming approach
│   ├── main.py                  # Application entry point
│   ├── task.py                  # Task class definition
│   ├── task_manager.py          # TaskManager class
│   └── storage.py               # File I/O operations
└── README.md                    # This file
```

## 🚀 Features

### Core Features (Both Versions)
- ✅ Add new tasks with title, priority, and due date
- ✅ View all tasks in a formatted list
- ✅ Delete tasks by index
- ✅ Persistent storage using JSON files
- ✅ Date validation for due dates
- ✅ Interactive command-line interface

### Advanced Features (OOP Version Only)
- 🔄 Sort tasks by priority (Low < Medium < High)
- 🔄 Sort tasks by due date (earliest first)
- 🔍 Filter tasks by keyword search
- 🏗️ Clean object-oriented architecture

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.6 or higher
- No external dependencies required (uses only standard library)

### Running the Applications

#### Procedural Version (Python Fundamentals)
```bash
cd python_fundamentals
python task_manager.py
```

#### Object-Oriented Version (OOP)
```bash
cd oop
python main.py
```

## 📖 Usage

### Basic Operations

1. **Add Task**: Create a new task with title, priority, and due date
2. **View Tasks**: Display all tasks in a numbered list
3. **Delete Task**: Remove a task by selecting its number
4. **Exit**: Close the application

### Advanced Operations (OOP Version)

5. **Sort by Priority**: Organize tasks by priority level
6. **Sort by Due Date**: Arrange tasks chronologically
7. **Filter by Keyword**: Search for tasks containing specific text

### Date Format
- **Procedural Version**: `DD/MM/YYYY` (e.g., 25/12/2024)
- **OOP Version**: `DD-MM-YYYY` (e.g., 25-12-2024)

### Priority Levels
- `Low`: Low priority tasks
- `Med`: Medium priority tasks  
- `High`: High priority tasks

## 🏗️ Architecture

### Procedural Approach (`python_fundamentals/`)
- Functions-based design
- Global variables for task storage
- Direct file operations
- Simpler structure, easier for beginners

### Object-Oriented Approach (`oop/`)
- Class-based design with encapsulation
- `Task` class for individual task objects
- `TaskManager` class for task operations
- Better code organization and reusability

## 📁 Data Storage

Tasks are stored in `tasks.json` files in each respective directory:
- Human-readable JSON format
- Automatic file creation if not exists
- Pretty-printed with indentation for readability

### Example JSON Structure
```json
[
    {
        "title": "Complete project report",
        "priority": "High",
        "due_date": "25-12-2024"
    },
    {
        "title": "Buy groceries",
        "priority": "Low", 
        "due_date": "20-12-2024"
    }
]
```

## 🔧 Code Structure

### Procedural Version
- `task_manager.py`: Contains all functions and main loop
- `storage.py`: Handles JSON file operations
- Global `tasks` list for data storage

### OOP Version
- `main.py`: Application entry point and user interface
- `task.py`: `Task` class with `__init__`, `__str__`, `to_dict()`, `from_dict()`
- `task_manager.py`: `TaskManager` class with CRUD operations and sorting
- `storage.py`: File I/O utilities (shared with procedural version)

## 🎯 Learning Objectives

This project demonstrates:

### Python Fundamentals
- Functions and modules
- File I/O operations
- JSON data handling
- Error handling with try/except
- User input validation
- List operations and iteration

### Object-Oriented Programming
- Class definition and instantiation
- Constructor (`__init__`) and methods
- String representation (`__str__`)
- Static methods
- Encapsulation and data hiding
- Method chaining and composition

### Software Engineering
- Code organization and structure
- Separation of concerns
- Error handling and validation
- User interface design
- Data persistence

## 🚨 Error Handling

Both versions include robust error handling for:
- Invalid date formats
- File I/O errors
- Invalid task indices
- Missing or corrupted data files

## 🔮 Future Enhancements

Potential improvements could include:
- Task categories or tags
- Due date reminders
- Task completion status
- Export/import functionality
- GUI interface
- Database integration
- Task dependencies
- Recurring tasks

---

**Happy Task Managing! 📋✨**
