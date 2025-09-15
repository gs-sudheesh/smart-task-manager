"""Authentication and security endpoints."""

from flask import request, jsonify
from flask_login import LoginManager, login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from config.app_config import app
from config.db_config import db
from domain.user import User

# Flask-Login configuration
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({"error": "Unauthorized"}), 401

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data["username"]
    password = generate_password_hash(data["password"])
    
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already exists"}), 400
    
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered!"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    
    if user and check_password_hash(user.password, data["password"]):
        login_user(user)
        return jsonify({"message": "Login successful!"})
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out!"})