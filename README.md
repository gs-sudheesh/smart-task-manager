# Smart Task Manager
![Python CI](https://github.com/gs-sudheesh/smart-task-manager/workflows/Python%20CI/badge.svg)
![Python CI](https://github.com/gs-sudheesh/smart-task-manager/workflows/Python%20CI/badge.svg)

A comprehensive Python-based task management application showcasing different programming paradigms and user interfaces. This project includes multiple implementations ranging from command-line interfaces to modern GUI applications with user authentication.
A comprehensive Python-based task management application showcasing different programming paradigms and user interfaces. This project includes multiple implementations ranging from command-line interfaces to modern GUI applications with user authentication.

## 📁 Project Structure

```
smart-task-manager/
├── python_fundamentals/          # Procedural programming approach (CLI)
├── oop/                         # Object-oriented programming approach (CLI)
├── gui-tkinter/                 # Basic GUI with tkinter (Pack layout)
├── gui-tkinter-grid/            # Advanced GUI with tkinter (Grid layout)
├── gui-tkinter-login/           # GUI with user authentication system
├── web-interface/               # Modern web application with Flask
├── rest-api/                    # Flask REST API with OpenAPI docs, Docker
├── requirements.txt             # Global dependencies
└── README.md                   # This file
```

## 🚀 Project Overview

| Project | Type | Features | Complexity |
|---------|------|----------|------------|
| **python_fundamentals** | CLI | Basic CRUD operations | Beginner |
| **oop** | CLI | Advanced sorting & filtering | Intermediate |
| **gui-tkinter** | GUI | Basic GUI with pack layout | Intermediate |
| **gui-tkinter-grid** | GUI | Advanced GUI with grid layout | Advanced |
| **gui-tkinter-login** | GUI | Full authentication system | Expert |
| **web-interface** | Web | Modern responsive web app | Expert |
| **rest-api** | API | Flask REST API + Swagger UI | Expert |

---

## 📋 Project 1: Python Fundamentals (CLI)

**Location:** `python_fundamentals/`

### Features
- ✅ Add, view, and delete tasks
- ✅ Basic task management with title, priority, and due date
- ✅ JSON file storage
- ✅ Command-line interface
- ✅ Date validation

### Dependencies
- Python 3.6+ (no external packages required)

### Installation & Run
### Installation & Run
```bash
cd python_fundamentals
python task_manager.py
```

### Usage
- Follow the interactive menu prompts
- Date format: `DD/MM/YYYY` (e.g., 25/12/2024)
- Priority levels: Low, Med, High

---

## 🏗️ Project 2: Object-Oriented Programming (CLI)

**Location:** `oop/`

### Features
- ✅ All features from python_fundamentals
- ✅ Sort tasks by priority (Low < Medium < High)
- ✅ Sort tasks by due date (earliest first)
- ✅ Filter tasks by keyword search
- ✅ Clean OOP architecture with Task and TaskManager classes
- ✅ Better code organization and reusability

### Dependencies
- Python 3.6+ (no external packages required)

### Installation & Run
### Usage
- Follow the interactive menu prompts
- Date format: `DD/MM/YYYY` (e.g., 25/12/2024)
- Priority levels: Low, Med, High

---

## 🏗️ Project 2: Object-Oriented Programming (CLI)

**Location:** `oop/`

### Features
- ✅ All features from python_fundamentals
- ✅ Sort tasks by priority (Low < Medium < High)
- ✅ Sort tasks by due date (earliest first)
- ✅ Filter tasks by keyword search
- ✅ Clean OOP architecture with Task and TaskManager classes
- ✅ Better code organization and reusability

### Dependencies
- Python 3.6+ (no external packages required)

### Installation & Run
```bash
cd oop
python main.py
```

### Usage
- Interactive menu with additional sorting and filtering options
- Date format: `DD-MM-YYYY` (e.g., 25-12-2024)
- Use keyword filtering to search through task titles

---

## 🖥️ Project 3: Basic GUI (Tkinter Pack Layout)

**Location:** `gui-tkinter/`

### Features
- ✅ Modern GUI interface using tkinter
- ✅ Add, delete, view tasks with visual interface
- ✅ Sort by priority and due date
- ✅ Filter tasks by keyword
- ✅ Real-time task list updates
- ✅ Input validation with error messages
- ✅ Clean, user-friendly interface

### Dependencies
- Python 3.6+
- tkinter (usually included with Python)
- schedule (for background notifications)

### Installation & Run
```bash
cd gui-tkinter
pip install schedule
python main.py
```

### Usage
- Fill in the task form (Title, Priority, Due Date)
- Click "Add Task" to create new tasks
- Use buttons to sort, filter, or delete tasks
- Select tasks from the list to delete them

---

## 🎨 Project 4: Advanced GUI (Tkinter Grid Layout)

**Location:** `gui-tkinter-grid/`

### Features
- ✅ All features from basic GUI
- ✅ Professional grid-based layout
- ✅ Better visual organization
- ✅ Toggle task status (Done/Pending)
- ✅ Background notification system
- ✅ Scrollable task list
- ✅ Enhanced user experience

### Dependencies
- Python 3.6+
- tkinter (usually included with Python)
- schedule (for background notifications)

### Installation & Run
```bash
cd gui-tkinter-grid
pip install schedule
python main.py
```

### Usage
- More organized interface with grid layout
- Toggle task status between Done and Pending
- Background notifications for due tasks
- Enhanced filtering and sorting capabilities

---

## 🔐 Project 5: GUI with Authentication System

**Location:** `gui-tkinter-login/`

### Features
- ✅ All features from advanced GUI
- ✅ Secure user authentication with bcrypt
- ✅ User registration system
- ✅ Password hashing and verification
- ✅ Login-protected task management
- ✅ User-specific data storage
- ✅ Professional security implementation

### Dependencies
- Python 3.6+
- tkinter (usually included with Python)
- schedule (for background notifications)
- bcrypt (for password hashing)

### Installation & Run
```bash
cd gui-tkinter-login
pip install -r requirements.txt
python main.py
```

### Usage
1. **First Time**: Register a new account
2. **Login**: Enter your credentials
3. **Task Management**: Full task management after authentication
4. **Security**: All passwords are securely hashed

---

## 🌐 Project 6: Modern Web Interface (Flask)

**Location:** `web-interface/`

### Features
- ✅ All features from GUI versions
- ✅ Modern responsive web design
- ✅ Real-time task management
- ✅ SQLite database with SQLAlchemy ORM
- ✅ RESTful API endpoints
- ✅ Beautiful CSS styling with animations
- ✅ Mobile-responsive design
- ✅ Static file serving optimization
- ✅ Professional web application architecture

### Dependencies
- Python 3.8+
- Flask 2.3.3 (web framework)
- Flask-SQLAlchemy 3.0.5 (database ORM)

### Installation & Run
```bash
cd web-interface
pip install -r requirements.txt
python app.py
```

### Usage
1. **Start the server**: Run `python app.py`
2. **Open browser**: Visit `http://localhost:5000`
3. **Add tasks**: Use the web form to create tasks
4. **Manage tasks**: Mark complete, delete, or view all tasks
5. **Responsive design**: Works on desktop, tablet, and mobile

### Web Features
- **Modern UI**: Gradient backgrounds, smooth animations
- **Color-coded priorities**: Visual priority indicators
- **Real-time updates**: Instant task list refresh
- **Database integration**: Persistent SQLite storage
- **Professional styling**: Clean, modern CSS design

---

## 🧩 Project 7: REST API (Flask)

**Location:** `rest-api/`

### Features
- ✅ Flask-based REST API with session auth
- ✅ OpenAPI 3 spec at `/api/docs/openapi.yaml`
- ✅ Swagger UI at `/api/docs`
- ✅ SQLite via SQLAlchemy (Docker volume at `/app/data`)
- ✅ Dockerfile and docker-compose ready (port 8500)
- ✅ Unit tests (strict, mocked) with pytest

### Dependencies
- Python 3.13+
- See `rest-api/requirements.txt`

### Run (local)
```bash
cd rest-api
pip install -r requirements.txt
python app.py
# Open: http://localhost:8500/api/docs
```

### Run with Docker
```bash
cd rest-api
docker-compose up --build
# Open: http://localhost:8500/api/docs
```

### Tests
```bash
cd rest-api
pytest -q
```

### Notes
- App binds to `0.0.0.0:8500`
- DB file stored under `rest-api/data/tasks.db` (mounted to `/app/data` in Docker)

---

## 🛠️ Global Installation

### Install All Dependencies
```bash
# Navigate to project root
cd smart-task-manager

# Install all dependencies
pip install schedule bcrypt

# Or install from requirements.txt (if available)
pip install -r requirements.txt
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

---

## 📊 Feature Comparison

| Feature | CLI Basic | CLI OOP | GUI Basic | GUI Grid | GUI Login | Web Interface |
|---------|-----------|---------|-----------|----------|-----------|---------------|
| Add Tasks | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Delete Tasks | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| View Tasks | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Sort by Priority | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Sort by Due Date | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Filter by Keyword | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| GUI Interface | ❌ | ❌ | ✅ | ✅ | ✅ | ❌ |
| Web Interface | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Task Status Toggle | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Background Notifications | ❌ | ❌ | ❌ | ✅ | ✅ | ❌ |
| User Authentication | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Password Security | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Database Integration | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Responsive Design | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| RESTful API | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

---

## 🎯 Learning Path

### Beginner → Expert
1. **Start with `python_fundamentals`** - Learn basic Python concepts
2. **Move to `oop`** - Understand object-oriented programming
3. **Try `gui-tkinter`** - Introduction to GUI development
4. **Explore `gui-tkinter-grid`** - Advanced GUI layouts and features
5. **Master `gui-tkinter-login`** - Complete application with security
6. **Build `web-interface`** - Modern web development with Flask

### Key Learning Objectives

#### Python Fundamentals
- Functions and modules
- File I/O operations
- JSON data handling
- Error handling
- Error handling
- User input validation

#### Object-Oriented Programming
#### Object-Oriented Programming
- Class definition and instantiation
- Encapsulation and data hiding
- Method chaining and composition
- Static methods and inheritance

#### GUI Development
- tkinter widgets and layouts
- Event handling and callbacks
- Grid vs Pack layout managers
- User interface design principles

#### Security & Authentication
- Password hashing with bcrypt
- User session management
- Secure data storage
- Authentication workflows

#### Web Development
- Flask framework and routing
- SQLAlchemy ORM and database models
- HTML templating with Jinja2
- CSS styling and responsive design
- RESTful API design principles

---

## 🔧 Technical Details

### Data Storage
- **Tasks**: Stored in `tasks.json` files (CLI/GUI versions)
- **Users**: Stored in `users.json` files (login version)
- **Web Database**: SQLite database with SQLAlchemy ORM (web-interface)
- **Format**: Human-readable JSON with proper indentation (CLI/GUI), SQLite (web)

### Date Formats
- **CLI Basic**: `DD/MM/YYYY`
- **CLI OOP**: `DD-MM-YYYY`
- **GUI Versions**: `DD/MM/YYYY` (input) → `DD/MM/YYYY HH:MM` (storage)
- **Web Interface**: `YYYY-MM-DD` (HTML date input) → SQLite datetime

### Priority Levels
- `Low`: Low priority tasks
- `Med`: Medium priority tasks
- `High`: High priority tasks

---

## 🚨 Troubleshooting

### Common Issues

1. **tkinter not found**
   - Install system tkinter package (see system dependencies above)

2. **schedule module not found**
   - Run: `pip install schedule`

3. **bcrypt installation fails**
   - Run: `pip install bcrypt`

4. **Import errors**
   - Ensure you're in the correct project directory
   - Check that all required files are present

### Getting Help
- Check the individual project README files
- Verify all dependencies are installed
- Ensure Python version is 3.6 or higher

---

**Happy Task Managing! 📋✨**
