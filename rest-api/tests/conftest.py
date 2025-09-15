"""Minimal fixtures for strict unit tests (no Flask test client)."""

import pytest
from importlib import import_module
from flask_login import LoginManager


@pytest.fixture(scope='session')
def app_instance():
    """Provide the Flask app without touching the database."""
    app_module = import_module('config.app_config')
    app = app_module.app
    app.config['TESTING'] = True
    # Initialize a minimal login manager for decorators to work
    if not hasattr(app, 'login_manager'):
        login_manager = LoginManager()
        login_manager.init_app(app)
    return app


@pytest.fixture
def request_context(app_instance):
    """Yield a basic request context for calling view functions directly."""
    with app_instance.test_request_context():
        yield
