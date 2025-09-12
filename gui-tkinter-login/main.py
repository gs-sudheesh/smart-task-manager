import tkinter as tk
from tkinter import messagebox
from login import show_login
from datetime import datetime
import schedule
import threading
import time
import constants
from task_manager import TaskManager

# Create TaskManager instance
manager = TaskManager()

def launch_main_app(root):
    # Use existing hidden root instead of creating a second Tk instance
    root.title("Smart Task Manager")
    root.geometry("650x500")
    root.deiconify()
    
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
    
    # Add task, validation, event
    def add_task():
        title = title_entry.get()
        priority = priority_entry.get().capitalize()
        due_date = due_date_entry.get()
        
        if not title or not priority or not due_date:
            messagebox.showerror("Error", "Please fill in all fields.")
            return
        
        try:
            # Validate date format
            due_datetime = datetime.strptime(due_date, "%d/%m/%Y")
            # Convert to the format expected by TaskManager
            formatted_date = due_datetime.strftime(constants.DATE_TIME_FORMAT)
            manager.add_task(title, priority, formatted_date, False)
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
    
    # Delete task, validation, event
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
    
    tk.Button(middle_frame, text="Toggle Status", command=toggle_task_status).grid(row=0, column=6, padx=5)
    
    tk.Label(middle_frame, text="Keyword").grid(row=0, column=3, padx=5)
    keyword_entry = tk.Entry(middle_frame, width=15)
    keyword_entry.grid(row=0, column=4, padx=5)
    
    def filter_tasks():
        keyword = keyword_entry.get()
        if not keyword:
            refresh_tasks()
            return
        
        filtered = [task for task in manager.tasks if keyword.lower() in task.title.lower()]
        task_listbox.delete(0, tk.END)
        for i, task in enumerate(filtered, 1):
            task_listbox.insert(tk.END, f"{i}. {task}")
    
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
    
    refresh_tasks()
    
    def check_due_tasks():
        due_tasks = manager.check_due_tasks()
        if due_tasks:
            for t in due_tasks:
                messagebox.showinfo("Task Due!", f"{t.title} is due now!")
        else:
            print("No task due!")
    
    def run_scheduler():
        schedule.every(1).minutes.do(check_due_tasks)
        while True:
            schedule.run_pending()
            time.sleep(1)
    
    def start_scheduler():
        t = threading.Thread(target=run_scheduler, daemon=True)
        t.start()
    
    # Start the notification scheduler
    start_scheduler()

def main():
    root = tk.Tk()
    root.withdraw()  # Hide main window until Login succeeds
    
    def on_login_success():
        # Populate and show the single root window
        launch_main_app(root)
    
    # Modify show_login to accept a callback for successful login
    show_login(on_login_success)
    
    # Run the GUI Loop
    root.mainloop()

if __name__ == "__main__":
    main()