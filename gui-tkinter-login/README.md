# Secure GUI Task Manager - Tkinter with Authentication

A professional, secure task management application with user authentication, built using tkinter and bcrypt for password security. This project demonstrates advanced GUI development, security best practices, and complete application architecture.

## 🎯 Features

- ✅ **Secure Authentication**: User login and registration system
- ✅ **Password Security**: bcrypt hashing for secure password storage
- ✅ **Complete Task Management**: All features from advanced GUI version
- ✅ **User-Specific Data**: Each user has their own task storage
- ✅ **Session Management**: Secure login/logout functionality
- ✅ **Professional Interface**: Clean, organized grid layout
- ✅ **Background Notifications**: Automated due date reminders
- ✅ **Data Persistence**: Secure JSON file storage
- ✅ **Input Validation**: Comprehensive error handling

## 🛠️ Installation

### Prerequisites
- Python 3.6 or higher
- tkinter (usually included with Python)
- schedule (for background notifications)
- bcrypt (for password hashing)

### Setup
```bash
cd gui-tkinter-login
pip install -r requirements.txt
```

### Manual Installation
```bash
pip install schedule bcrypt
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

### First Time Setup
1. **Register Account**: Click "Register" button
2. **Enter Credentials**: Username and password
3. **Account Created**: User account is securely stored

### Daily Usage
1. **Login**: Enter your username and password
2. **Access Tasks**: Full task management interface
3. **Manage Tasks**: Add, edit, delete, and organize tasks
4. **Logout**: Close application to end session

### Task Management
- **Add Tasks**: Fill form and click "Add Task"
- **Delete Tasks**: Select and click "Delete Selected"
- **Toggle Status**: Mark tasks as Done/Pending
- **Sort Tasks**: Organize by priority or due date
- **Filter Tasks**: Search by keyword
- **Notifications**: Automatic due date reminders

### Security Features
- **Password Hashing**: All passwords are securely hashed with bcrypt
- **User Isolation**: Each user's data is stored separately
- **Session Security**: Login state is properly managed
- **Data Validation**: All inputs are validated and sanitized

## 📁 File Structure

```
gui-tkinter-login/
├── main.py           # Main application with login integration
├── login.py          # Login/registration interface
├── user_storage.py   # User authentication and storage
├── task_manager.py   # TaskManager class
├── task.py           # Task class definition
├── storage.py        # File I/O operations
├── constants.py      # Application constants
├── requirements.txt  # Dependencies
├── users.json        # User data storage (auto-created)
├── tasks.json        # Task data storage (auto-created)
└── README.md        # This file
```

## 🔐 Authentication System

### User Registration
```python
def add_user(username, password):
    users = load_users()
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    users[username] = hashed
    save_users(users)
```

### User Authentication
```python
def authenticate(username, password):
    users = load_users()
    hashed = users.get(username)
    if not hashed:
        return False
    return bcrypt.checkpw(password.encode(), hashed.encode())
```

### Login Interface
```python
def show_login(callback):
    login_win = tk.Toplevel()
    login_win.title("Login")
    
    # Username and password fields
    tk.Label(login_win, text="Username:").grid(row=0, column=0)
    username_entry = tk.Entry(login_win)
    username_entry.grid(row=0, column=1)
    
    tk.Label(login_win, text="Password:").grid(row=1, column=0)
    password_entry = tk.Entry(login_win, show="*")
    password_entry.grid(row=1, column=1)
```

## 🎨 GUI Architecture

### Login Flow
1. **Main Window**: Hidden until login succeeds
2. **Login Dialog**: Modal window for authentication
3. **Task Interface**: Full task management after login
4. **Session Management**: Proper window state handling

### Application Structure
```python
def main():
    root = tk.Tk()
    root.withdraw()  # Hide main window until login
    
    def on_login_success():
        launch_main_app(root)  # Show task interface
    
    show_login(on_login_success)
    root.mainloop()
```

## 🔧 Security Implementation

### Password Hashing
- **bcrypt Algorithm**: Industry-standard password hashing
- **Salt Generation**: Unique salt for each password
- **Secure Storage**: Hashed passwords stored in JSON

### Data Protection
- **User Isolation**: Separate data files per user
- **Input Validation**: All user inputs are validated
- **Error Handling**: Secure error messages without data exposure

### Session Management
- **Login State**: Proper authentication state tracking
- **Window Management**: Secure window transitions
- **Data Persistence**: User data saved securely

## 📊 Data Storage

### User Data (`users.json`)
```json
{
    "username1": "$2b$12$hashedpassword1",
    "username2": "$2b$12$hashedpassword2"
}
```

### Task Data (`tasks.json`)
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
- **Security Best Practices**: Password hashing and data protection
- **Authentication Systems**: User login and session management
- **Advanced GUI Design**: Complex interface layouts
- **Data Architecture**: Multi-user data management
- **Error Handling**: Secure error management
- **Threading**: Background processes and notifications
- **File I/O**: Secure data persistence
- **User Experience**: Intuitive authentication flows

## 🔔 Background Features

### Notification System
- **Due Date Alerts**: Automatic task reminders
- **Background Threading**: Non-blocking notifications
- **User-Specific**: Notifications for logged-in user only

### Data Synchronization
- **Real-time Updates**: Task list updates immediately
- **Persistent Storage**: Data saved automatically
- **User Context**: All operations respect user authentication

## 🚨 Security Considerations

### Password Security
- **Never store plaintext passwords**
- **Use bcrypt for password hashing**
- **Implement proper salt generation**
- **Validate password strength**

### Data Protection
- **Validate all user inputs**
- **Sanitize data before storage**
- **Implement proper error handling**
- **Use secure file permissions**

---

**Perfect for learning security and authentication! 🔐✨**
