"""Task Management API endpoints."""

from flask import request, jsonify
from flask_login import login_required, current_user
from config.db_config import db
from config.app_config import app
from domain.task import Task

# Application Task APIs
@app.route("/api/tasks", methods=['GET'])
@login_required
def api_get_tasks():
    # Get query parameters
    status = request.args.get("status")
    priority = request.args.get("priority")
    search = request.args.get("search")
    sort = request.args.get("sort")
    
    # Start with tasks for current user
    query = Task.query.filter_by(user_id=current_user.id)
    
    # Apply filters
    if status:
        query = query.filter_by(status=status)
    if priority:
        query = query.filter_by(priority=priority)
    if search:
        query = query.filter(Task.title.ilike(f"%{search}%"))
    
    # Apply Sorting
    if sort == "priority":
        query = query.order_by(Task.priority)
    elif sort == "duedate":
        query = query.order_by(Task.due_date)
    elif sort == "duedate_desc":
        query = query.order_by(Task.due_date.desc())
    
    tasks = query.all()
    return jsonify([
        {
            "id": task.id,
            "title": task.title,
            "priority": task.priority,
            "due_date": task.due_date,
            "status": task.status
        }
        for task in tasks
    ])

@app.route("/api/tasks", methods=["POST"])
@login_required
def api_add_task():
    data = request.get_json()
    new_task = Task(
        title=data["title"],
        priority=data["priority"],
        due_date=data["due_date"],
        status=data.get("status", "Pending"),
        user_id=current_user.id
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added!", "id": new_task.id}), 201

@app.route("/api/tasks/<int:task_id>", methods=["PUT"])
@login_required
def api_update_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    data = request.get_json()
    task.title = data.get("title", task.title)
    task.priority = data.get("priority", task.priority)
    task.due_date = data.get("due_date", task.due_date)
    task.status = data.get("status", task.status)
    db.session.commit()
    return jsonify({"message": "Task updated!"})

@app.route("/api/tasks/<int:task_id>", methods=["DELETE"])
@login_required
def api_delete_task(task_id):
    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404
    
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted!"})