import tkinter as tk
from tkinter import messagebox
from task_manager import TaskManager
from datetime import datetime

# Create TaskManager instance
manager = TaskManager()

# Create main window
root = tk.Tk()
root.title("Smart Task Manager")
root.geometry("500x400")

# --- Add Task Section ---
tk.Label(root, text="Task Title").pack()
title_entry = tk.Entry(root, width=50)
title_entry.pack()

tk.Label(root, text="Priority (Low/Medium/High)").pack()
priority_entry = tk.Entry(root, width=50)
priority_entry.pack()

tk.Label(root, text="Due Date (DD/MM/YYYY)").pack()
due_date_entry = tk.Entry(root, width=50)
due_date_entry.pack()

def add_task():
    title = title_entry.get()
    priority = priority_entry.get().capitalize()
    due_date = due_date_entry.get()
    
    if not title or not priority or not due_date:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    try:
        # Validate date format
        datetime.strptime(due_date, "%d/%m/%Y")
        manager.add_task(title, priority, due_date)
        messagebox.showinfo("Success", "Task added!")
        
        # Clear entry fields
        title_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        
        refresh_tasks()
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Use DD/MM/YYYY")

def delete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No task selected.")
        return
    index = selected[0]
    manager.delete_task(index + 1)  # +1 because delete_task expects 1-based index
    refresh_tasks()

def sort_by_priority():
    manager.sort_by_priority()
    refresh_tasks()

def sort_by_due_date():
    manager.sort_by_due_date()
    refresh_tasks()

def filter_tasks():
    keyword = keyword_entry.get()
    if not keyword:
        refresh_tasks()
        return
    
    filtered = [task for task in manager.tasks if keyword.lower() in task.title.lower()]
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(filtered, 1):
        task_listbox.insert(tk.END, f"{i}. {task}")

# --- Filter Section ---
tk.Label(root, text="Filter by Keyword").pack()
keyword_entry = tk.Entry(root, width=50)
keyword_entry.pack()

# --- Buttons ---
tk.Button(root, text="Add Task", command=add_task).pack(pady=10)
tk.Button(root, text="Delete Selected Task", command=delete_task).pack(pady=5)
tk.Button(root, text="Sort by Priority", command=sort_by_priority).pack(pady=5)
tk.Button(root, text="Sort by Due Date", command=sort_by_due_date).pack(pady=5)
tk.Button(root, text="Filter Tasks", command=filter_tasks).pack(pady=5)

# --- Task List Section ---
task_listbox = tk.Listbox(root, width=70, height=10)
task_listbox.pack(pady=10)

# Updates the task list dynamically
def refresh_tasks():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(manager.tasks, 1):
        task_listbox.insert(tk.END, f"{i}. {task}")

# Initialize the task list
refresh_tasks()

# Run the GUI loop
root.mainloop()