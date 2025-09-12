from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    priority = db.Column(db.String(10), nullable=False)
    due_date = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(10), nullable=False, default="Pending")
    
    def __init__(self, title, priority, due_date, status="Pending"):
        self.title = title
        self.priority = priority
        self.due_date = due_date
        self.status = status