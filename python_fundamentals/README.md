# Python Fundamentals - Task Manager

A command-line task management application built using procedural programming principles. This project demonstrates basic Python concepts including functions, file I/O, and user input handling.

## 🎯 Features

- ✅ **Add Tasks**: Create new tasks with title, priority, and due date
- ✅ **View Tasks**: Display all tasks in a formatted list
- ✅ **Delete Tasks**: Remove tasks by selecting their index
- ✅ **Data Persistence**: Save tasks to JSON file
- ✅ **Date Validation**: Ensure proper date format
- ✅ **Interactive CLI**: User-friendly command-line interface

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Setup
```bash
cd python_fundamentals
# No additional installation needed
```

## 🚀 Running the Application

```bash
python task_manager.py
```

## 📖 Usage

### Menu Options
1. **Add Task** - Create a new task
2. **View Tasks** - Display all tasks
3. **Delete Task** - Remove a task by number
4. **Exit** - Close the application

### Input Format
- **Date**: `DD/MM/YYYY` (e.g., 25/12/2024)
- **Priority**: Low, Med, High
- **Title**: Any descriptive text

### Example Session
```
=== Task Manager ===
1. Add Task
2. View Tasks
3. Delete Task
4. Exit
Choose an option: 1

Enter task title: Complete project report
Enter priority (Low/Med/High): High
Enter due date (DD/MM/YYYY): 25/12/2024
Task added successfully!
```

## 📁 File Structure

```
python_fundamentals/
├── task_manager.py    # Main application logic
├── storage.py         # File I/O operations
├── tasks.json         # Data storage (auto-created)
└── README.md         # This file
```

## 🔧 Code Structure

### task_manager.py
- `main()` - Application entry point and menu loop
- `add_task()` - Add new task to the list
- `view_tasks()` - Display all tasks
- `delete_task()` - Remove task by index
- `get_user_input()` - Handle user input with validation

### storage.py
- `load_tasks()` - Load tasks from JSON file
- `save_tasks()` - Save tasks to JSON file
- `create_file_if_not_exists()` - Ensure data file exists

## 📊 Data Format

Tasks are stored in `tasks.json`:
```json
[
    {
        "title": "Complete project report",
        "priority": "High",
        "due_date": "25/12/2024"
    }
]
```

## 🎓 Learning Objectives

This project teaches:
- **Functions**: Breaking code into reusable blocks
- **File I/O**: Reading and writing JSON files
- **User Input**: Handling and validating user input
- **Error Handling**: Using try/except blocks
- **Data Structures**: Working with lists and dictionaries
- **Control Flow**: Loops and conditional statements

## 🚨 Error Handling

The application handles:
- Invalid date formats
- File I/O errors
- Invalid menu selections
- Missing or corrupted data files

---

**Perfect for Python beginners! 🐍✨**
