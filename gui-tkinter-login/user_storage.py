import json
import bcrypt

USER_FILE = "users.json"

def load_users():
    try:
        with open(USER_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

def add_user(username, password):
    users = load_users()
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    users[username] = hashed
    save_users(users)

def authenticate(username, password):
    users = load_users()
    hashed = users.get(username)
    if not hashed:
        return False
    return bcrypt.checkpw(password.encode(), hashed.encode())