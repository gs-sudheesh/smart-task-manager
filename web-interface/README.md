# Smart Task Manager - Web Interface

A modern, responsive web application for task management built with Flask and SQLAlchemy. This project provides a beautiful web interface for managing tasks with real-time updates and a clean, intuitive design.

## 🌟 Features

### Core Functionality
- **Task Management**: Create, read, update, and delete tasks
- **Priority System**: Set task priorities (Low, Medium, High) with color-coded indicators
- **Due Date Tracking**: Set and track task due dates
- **Status Management**: Mark tasks as pending or completed
- **Real-time Updates**: Instant task list updates without page refresh

### User Interface
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Clean, professional interface with gradient backgrounds and smooth animations
- **Color-coded Priorities**: Visual priority indicators for easy task identification
- **Interactive Elements**: Hover effects and smooth transitions
- **Empty State**: Helpful message when no tasks are present

### Technical Features
- **Database Integration**: SQLite database with SQLAlchemy ORM
- **RESTful API**: Clean URL structure and HTTP methods
- **Static File Serving**: Optimized CSS and asset delivery
- **Form Validation**: Client and server-side validation
- **Error Handling**: Graceful error handling and user feedback

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Navigate to the project directory:**
   ```bash
   cd web-interface
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open your browser and visit:**
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
web-interface/
├── app.py                 # Main Flask application
├── task.py               # SQLAlchemy Task model
├── requirements.txt      # Python dependencies
├── static/
│   └── style.css        # CSS styles and animations
├── templates/
│   └── index.html       # Main HTML template
└── README.md            # This file
```

## 🛠️ Dependencies

### Core Dependencies
- **Flask 2.3.3**: Web framework for Python
- **Flask-SQLAlchemy 3.0.5**: SQLAlchemy integration for Flask

### Development Dependencies
- **Python 3.8+**: Required Python version
- **pip**: Package installer

## 🎯 Usage

### Adding a Task
1. Fill in the task title
2. Select priority level (Low, Medium, High)
3. Set the due date
4. Click "Add Task"

### Managing Tasks
- **View Tasks**: All tasks are displayed in the main list
- **Mark Complete**: Click the "Mark Complete" button for completed tasks
- **Delete Tasks**: Click the "Delete" button to remove tasks
- **Priority Colors**: 
  - 🟢 Green: Low priority
  - 🟡 Yellow: Medium priority
  - 🔴 Red: High priority

### Task Status
- **Pending**: Newly created tasks
- **Completed**: Tasks marked as done

## 🎨 Customization

### Styling
The application uses a modern CSS design with:
- Gradient backgrounds
- Smooth animations
- Responsive layout
- Color-coded priorities
- Professional typography

### Database
The application uses SQLite by default. To use a different database:
1. Update the `SQLALCHEMY_DATABASE_URI` in `app.py`
2. Ensure the new database driver is installed

## 🔧 Configuration

### Environment Variables
You can customize the application using environment variables:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development  # For development mode
export FLASK_DEBUG=1         # Enable debug mode
```

### Database Configuration
The database is automatically created when you first run the application. The SQLite file will be created in the project directory.


### Docker Deployment
Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use:**
   ```bash
   # Kill process using port 5000
   lsof -ti:5000 | xargs kill -9
   ```

2. **Database errors:**
   - Delete `tasks.db` and restart the application
   - Check file permissions

3. **CSS not loading:**
   - Ensure the `static/` folder exists
   - Check Flask's static file serving configuration

4. **Import errors:**
   - Verify virtual environment is activated
   - Check all dependencies are installed

### Debug Mode
Enable debug mode for development:
```python
if __name__ == '__main__':
    app.run(debug=True)
```

## 📚 Learning Resources

### Flask Documentation
- [Flask Official Docs](https://flask.palletsprojects.com/)
- [Flask-SQLAlchemy Docs](https://flask-sqlalchemy.palletsprojects.com/)

### Web Development
- [HTML/CSS Basics](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Responsive Design](https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design)

---

**Happy Task Managing! 🎉**
