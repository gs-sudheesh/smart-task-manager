import tkinter as tk
from tkinter import messagebox
from user_storage import authenticate, add_user

def show_login(callback):
    login_win = tk.Toplevel()
    login_win.title("Login")
    
    tk.Label(login_win, text="Username:").grid(row=0, column=0)
    tk.Label(login_win, text="Password:").grid(row=1, column=0)
    
    username_entry = tk.Entry(login_win)
    password_entry = tk.Entry(login_win, show="*")
    
    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)
    
    def try_login():
        username = username_entry.get()
        password = password_entry.get()
        
        if authenticate(username, password):
            messagebox.showinfo("Login", "Login successful!")
            login_win.destroy()
            # Show main app window here
            callback()
        else:
            messagebox.showerror("Login", "Invalid credentials.")
    
    tk.Button(login_win, text="Login", command=try_login).grid(row=2, column=0, columnspan=2)
    
    # Optional: Registration button
    def register():
        username = username_entry.get()
        password = password_entry.get()
        add_user(username, password)
        messagebox.showinfo("Register", "User registered!")
    
    tk.Button(login_win, text="Register", command=register).grid(row=3, column=0, columnspan=2)