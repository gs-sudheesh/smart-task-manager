# Advanced GUI Task Manager - Tkinter (Grid Layout)

A professional-grade task management application with a sophisticated GUI built using tkinter's grid layout manager. This project demonstrates advanced GUI development techniques and provides a comprehensive task management solution.

## 🎯 Features

- ✅ **Professional Grid Layout**: Organized, responsive interface design
- ✅ **Complete Task Management**: Add, delete, view, and manage tasks
- ✅ **Task Status Toggle**: Mark tasks as Done or Pending
- ✅ **Advanced Sorting**: Sort by priority and due date
- ✅ **Smart Filtering**: Search tasks by keyword with real-time results
- ✅ **Background Notifications**: Automated due date reminders
- ✅ **Scrollable Interface**: Handle large numbers of tasks efficiently
- ✅ **Input Validation**: Comprehensive error handling and user feedback
- ✅ **Status Indicators**: Visual task completion status

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- tkinter (usually included with Python)
- schedule (for background notifications)

### Setup
```bash
cd gui-tkinter-grid
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

### Interface Layout
- **Top Row**: Task input form with labels and entry fields
- **Middle Row**: Action buttons and filter controls
- **Bottom Section**: Scrollable task list with status indicators

### Adding Tasks
1. Fill in the input form:
   - **Title**: Task description (30 characters)
   - **Priority**: Low, Medium, or High (15 characters)
   - **Due Date**: DD/MM/YYYY format (15 characters)
2. Click "Add Task" button
3. Task appears in the list with status indicator

### Managing Tasks
- **Delete**: Select task and click "Delete Selected"
- **Toggle Status**: Select task and click "Toggle Task Status"
- **Sort by Priority**: Click "Sort by Priority"
- **Sort by Due Date**: Click "Sort by Due Date"
- **Filter**: Enter keyword and click "Filter"

### Task Status
- **✓ Done**: Completed tasks (green checkmark)
- **✗ Pending**: Incomplete tasks (red X)

### Input Format
- **Date**: `DD/MM/YYYY` (e.g., 25/12/2024)
- **Priority**: Low, Medium, High (case-insensitive)
- **Title**: Any descriptive text

## 📁 File Structure

```
gui-tkinter-grid/
├── main.py           # Main GUI application
├── task_manager.py   # TaskManager class with advanced features
├── task.py           # Task class with status support
├── storage.py        # File I/O operations
├── constants.py      # Date format constants
├── tasks.json        # Data storage (auto-created)
└── README.md        # This file
```

## 🎨 Advanced Grid Layout

### Grid Organization
The interface uses tkinter's grid layout manager for precise widget positioning:

```python
# Top frame - Input form
tk.Label(top_frame, text="Title").grid(row=0, column=0, sticky="w")
title_entry = tk.Entry(top_frame, width=30)
title_entry.grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="Priority").grid(row=0, column=2, sticky="w")
priority_entry = tk.Entry(top_frame, width=15)
priority_entry.grid(row=0, column=3, padx=5)

tk.Label(top_frame, text="Due Date (DD/MM/YYYY)").grid(row=0, column=4, sticky="w")
due_date_entry = tk.Entry(top_frame, width=15)
due_date_entry.grid(row=0, column=5, padx=5)

tk.Button(top_frame, text="Add Task", command=add_task).grid(row=0, column=6, padx=10)
```

### Responsive Design
- **Sticky Parameters**: Widgets stick to edges for proper alignment
- **Padding**: Consistent spacing between elements
- **Column Spanning**: Buttons span multiple columns when needed
- **Row Organization**: Logical grouping of related elements

## 🔧 Key Features

### Task Status Management
```python
def toggle_task_status():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No task selected.")
        return
    index = selected[0]
    manager.toggle_status(index)
    refresh_tasks()
```

### Advanced Filtering
```python
def filter_tasks():
    keyword = keyword_entry.get()
    if not keyword:
        refresh_tasks()
        return
    
    filtered = [task for task in manager.tasks if keyword.lower() in task.title.lower()]
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(filtered, 1):
        task_listbox.insert(tk.END, f"{i}. {task}")
```

### Background Notifications
```python
def check_due_tasks():
    current_time = datetime.now()
    due_tasks = []
    
    for task in manager.tasks:
        try:
            task_due = datetime.strptime(task.due_date, constants.DATE_TIME_FORMAT)
            if task_due.date() == current_time.date():
                due_tasks.append(task)
        except ValueError:
            continue
    
    if due_tasks:
        for task in due_tasks:
            messagebox.showinfo("Task Due", f"{task.title} is due today!")
```

## 📊 Data Format

Tasks are stored in `tasks.json` with status information:
```json
[
    {
        "title": "Complete project report",
        "priority": "High",
        "due_date": "25/12/2024 14:30",
        "status": false
    }
]
```

## 🎓 Learning Objectives

This project teaches:
- **Advanced GUI Design**: Professional interface layout
- **Grid Layout Management**: Precise widget positioning
- **Event Handling**: Complex user interactions
- **State Management**: Task status tracking
- **Background Processing**: Threading for notifications
- **Data Visualization**: Status indicators and formatting
- **User Experience**: Intuitive interface design
- **Error Handling**: Comprehensive validation

## 🔔 Notification System

### Background Scheduler
- Runs every minute in a separate thread
- Checks for tasks due today
- Shows popup alerts for due tasks
- Non-blocking operation

### Due Date Detection
- Compares task due dates with current date
- Handles different date formats gracefully
- Provides user-friendly notifications

## 🚨 Error Handling

The application handles:
- Invalid date formats with specific error messages
- Empty form fields with validation
- Invalid task selections
- File I/O errors
- Threading exceptions
- Data corruption issues

---

**Perfect for advanced GUI development! 🎨✨**
