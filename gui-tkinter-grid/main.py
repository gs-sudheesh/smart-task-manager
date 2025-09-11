import tkinter as tk
from tkinter import messagebox
from task_manager import TaskManager
from datetime import datetime
import schedule
import threading
import time
import constants

# Create TaskManager instance
manager = TaskManager()

# Create main window
root = tk.Tk()
root.title("Smart Task Manager")
root.geometry("650x500")

# --- Top Frame: Task Input ---
top_frame = tk.Frame(root, padx=10, pady=10)
top_frame.pack(fill="x")

# --- Add Task Section ---
tk.Label(top_frame, text="Title").grid(row=0, column=0, sticky="w")
title_entry = tk.Entry(top_frame, width=30)
title_entry.grid(row=0, column=1, padx=5)

tk.Label(top_frame, text="Priority").grid(row=0, column=2, sticky="w")
priority_entry = tk.Entry(top_frame, width=15)
priority_entry.grid(row=0, column=3, padx=5)

tk.Label(top_frame, text="Due Date (DD/MM/YYYY)").grid(row=0, column=4, sticky="w")
due_date_entry = tk.Entry(top_frame, width=15)
due_date_entry.grid(row=0, column=5, padx=5)

def add_task():
    title = title_entry.get()
    priority = priority_entry.get().capitalize()
    due_date = due_date_entry.get()
    
    if not title or not priority or not due_date:
        messagebox.showerror("Error", "Please fill in all fields.")
        return
    
    try:
        # Validate date format - convert to full datetime format
        due_datetime = datetime.strptime(due_date, constants.DATE_TIME_FORMAT)
        # Convert to the format expected by TaskManager
        formatted_date = due_datetime.strftime(constants.DATE_TIME_FORMAT)
        manager.add_task(title, priority, formatted_date)
        messagebox.showinfo("Success", "Task added!")
        
        # Clear entry fields
        title_entry.delete(0, tk.END)
        priority_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        
        refresh_tasks()
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Use DD/MM/YYYY")

tk.Button(top_frame, text="Add Task", command=add_task).grid(row=0, column=6, padx=10)

# --- Middle Frame: Actions ---
middle_frame = tk.Frame(root, padx=10, pady=10)
middle_frame.pack(fill="x")

def delete_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No task selected.")
        return
    index = selected[0]
    manager.delete_task(index + 1)  # +1 because delete_task expects 1-based index
    refresh_tasks()

tk.Button(middle_frame, text="Delete Selected", command=delete_task).grid(row=0, column=0, padx=5)

def sort_by_priority():
    manager.sort_by_priority()
    refresh_tasks()

tk.Button(middle_frame, text="Sort by Priority", command=sort_by_priority).grid(row=0, column=1, padx=5)

def sort_by_due_date():
    manager.sort_by_due_date()
    refresh_tasks()

tk.Button(middle_frame, text="Sort by Due Date", command=sort_by_due_date).grid(row=0, column=2, padx=5)

def toggle_task_status():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No task selected.")
        return
    index = selected[0]
    manager.toggle_status(index)
    refresh_tasks()

tk.Button(middle_frame, text="Toggle Task Status", command=toggle_task_status).grid(row=0, column=6, padx=5)

def filter_tasks():
    keyword = keyword_entry.get()
    if not keyword:
        refresh_tasks()
        return
    
    filtered = [task for task in manager.tasks if keyword.lower() in task.title.lower()]
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(filtered, 1):
        task_listbox.insert(tk.END, f"{i}. {task}")

tk.Label(middle_frame, text="Keyword").grid(row=0, column=3, padx=5)
keyword_entry = tk.Entry(middle_frame, width=15)
keyword_entry.grid(row=0, column=4, padx=5)
tk.Button(middle_frame, text="Filter", command=filter_tasks).grid(row=0, column=5, padx=5)

# --- Bottom Frame: Task List ---
bottom_frame = tk.Frame(root, padx=10, pady=10)
bottom_frame.pack(fill="both", expand=True)

task_listbox = tk.Listbox(bottom_frame, width=80, height=15)
task_listbox.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(bottom_frame)
scrollbar.pack(side="right", fill="y")
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Updates the task list dynamically
def refresh_tasks():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(manager.tasks, 1):
        task_listbox.insert(tk.END, f"{i}. {task}")

def check_due_tasks():
    #Check for tasks that are due and show notifications
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
    else:
        print("No tasks due today!")

def run_scheduler():
    #Run the scheduler in a separate thread
    schedule.every(1).minutes.do(check_due_tasks)
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_scheduler():
    #Start the notification scheduler in a background thread
    t = threading.Thread(target=run_scheduler, daemon=True)
    t.start()

# Initialize the task list
refresh_tasks()

# Start the notification scheduler
start_scheduler()

# Run the GUI loop
root.mainloop()