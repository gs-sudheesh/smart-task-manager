"""Task Manager REST API application entry point."""

from config.db_config import db
from config.app_config import app

# Imports to register APIs
import security.login_sec
import api.task_manager
import docs

if __name__ == "__main__":
    # Initialize database
    with app.app_context():
        db.create_all()
    
    # Run the application
    app.run(host='0.0.0.0', port=8500, debug=True)