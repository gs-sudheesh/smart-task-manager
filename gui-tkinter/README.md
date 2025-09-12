# GUI Task Manager - Tkinter (Pack Layout)

A modern graphical user interface for task management built with Python's tkinter library. This project demonstrates GUI development using the pack layout manager and provides an intuitive visual interface for task management.

## 🎯 Features

- ✅ **Modern GUI Interface**: Clean, user-friendly visual interface
- ✅ **Add Tasks**: Create tasks with form-based input
- ✅ **Delete Tasks**: Select and remove tasks from a list
- ✅ **Sort by Priority**: Organize tasks by priority level
- ✅ **Sort by Due Date**: Arrange tasks chronologically
- ✅ **Filter by Keyword**: Search tasks by title content
- ✅ **Real-time Updates**: Task list updates immediately
- ✅ **Input Validation**: Error messages for invalid input
- ✅ **Background Notifications**: Due date reminders (with schedule)

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- tkinter (usually included with Python)
- schedule (for background notifications)

### Setup
```bash
cd gui-tkinter
pip install schedule
```

### System Dependencies (if tkinter not available)

#### macOS (Homebrew Python)
```bash
brew install python-tk
```

#### Ubuntu/Debian
```bash
sudo apt-get install python3-tk
```

#### Windows
- tkinter is usually included with Python installation

## 🚀 Running the Application

```bash
python main.py
```

## 📖 Usage

### Interface Overview
- **Top Section**: Task input form (Title, Priority, Due Date)
- **Middle Section**: Action buttons (Add, Delete, Sort, Filter)
- **Bottom Section**: Scrollable task list

### Adding Tasks
1. Fill in the task form:
   - **Title**: Enter task description
   - **Priority**: Enter Low, Medium, or High
   - **Due Date**: Enter in DD/MM/YYYY format
2. Click "Add Task" button
3. Task appears in the list below

### Managing Tasks
- **Delete**: Select a task from the list and click "Delete Selected"
- **Sort by Priority**: Click "Sort by Priority" to organize by importance
- **Sort by Due Date**: Click "Sort by Due Date" to arrange chronologically
- **Filter**: Enter a keyword and click "Filter Tasks"

### Input Format
- **Date**: `DD/MM/YYYY` (e.g., 25/12/2024)
- **Priority**: Low, Medium, High (case-insensitive)
- **Title**: Any descriptive text

## 📁 File Structure

```
gui-tkinter/
├── main.py           # Main GUI application
├── task_manager.py   # TaskManager class
├── task.py           # Task class definition
├── storage.py        # File I/O operations
├── constants.py      # Date format constants
├── tasks.json        # Data storage (auto-created)
└── README.md        # This file
```

## 🎨 GUI Layout

### Pack Layout Manager
The interface uses tkinter's pack layout manager for organizing widgets:

```python
# Top frame for input
top_frame.pack(fill="x")

# Middle frame for buttons
middle_frame.pack(fill="x")

# Bottom frame for task list
bottom_frame.pack(fill="both", expand=True)
```

### Widget Organization
- **Labels and Entries**: Organized in a grid within the top frame
- **Buttons**: Arranged horizontally in the middle frame
- **Listbox**: Scrollable list in the bottom frame with scrollbar

## 🔧 Key Components

### Task Input Form
```python
# Title input
tk.Label(top_frame, text="Task Title").pack()
title_entry = tk.Entry(top_frame, width=50)
title_entry.pack()

# Priority input
tk.Label(top_frame, text="Priority (Low/Medium/High)").pack()
priority_entry = tk.Entry(top_frame, width=50)
priority_entry.pack()

# Due date input
tk.Label(top_frame, text="Due Date (DD/MM/YYYY)").pack()
due_date_entry = tk.Entry(top_frame, width=50)
due_date_entry.pack()
```

### Action Buttons
```python
# Add task button
tk.Button(top_frame, text="Add Task", command=add_task).pack(pady=10)

# Action buttons
tk.Button(middle_frame, text="Delete Selected Task", command=delete_task).pack(pady=5)
tk.Button(middle_frame, text="Sort by Priority", command=sort_by_priority).pack(pady=5)
tk.Button(middle_frame, text="Sort by Due Date", command=sort_by_due_date).pack(pady=5)
tk.Button(middle_frame, text="Filter Tasks", command=filter_tasks).pack(pady=5)
```

### Task List Display
```python
# Scrollable task list
task_listbox = tk.Listbox(bottom_frame, width=70)
task_listbox.pack(side="left", fill="both", expand=True)

# Scrollbar
scrollbar = tk.Scrollbar(bottom_frame)
scrollbar.pack(side="right", fill="y")
```

## 🔔 Background Notifications

The application includes a background notification system:
- Checks for due tasks every minute
- Shows popup alerts for tasks due today
- Runs in a separate thread to avoid blocking the GUI

## 📊 Data Format

Tasks are stored in `tasks.json`:
```json
[
    {
        "title": "Complete project report",
        "priority": "High",
        "due_date": "25/12/2024 14:30"
    }
]
```

## 🎓 Learning Objectives

This project teaches:
- **GUI Development**: Creating user interfaces with tkinter
- **Layout Management**: Using pack layout manager
- **Event Handling**: Button clicks and user interactions
- **Widget Management**: Labels, entries, buttons, listboxes
- **Threading**: Background processes for notifications
- **Input Validation**: User input checking and error messages
- **Data Binding**: Connecting GUI to data models

## 🚨 Error Handling

The application handles:
- Invalid date formats with user-friendly error messages
- Empty form fields with validation prompts
- File I/O errors gracefully
- Invalid task selections
- Missing or corrupted data files

---

**Perfect for learning GUI development! 🖥️✨**
