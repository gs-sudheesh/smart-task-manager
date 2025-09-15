# Testing Guide for Task Manager REST API

## Overview

This document provides testing guidelines for the Task Manager REST API. The project now uses strict unit tests only (no Flask test client, no database).

## Test Structure

```
tests/
├── __init__.py
├── conftest.py      # Minimal app and request context fixtures
└── test_api.py      # Strict unit tests for API views with mocks
```

## Test Categories

### Unit Tests (`test_api.py`)
Purpose: Validate view logic directly with mocked dependencies.

Coverage:
- Task CRUD logic
- Query parameter handling (filter/search/sort)
- Authentication guard behavior
- Response payloads and status codes

## Running Tests

### Prerequisites
```bash
pip install -r requirements.txt
```

### Run All Tests
```bash
pytest
```

### Run Specific Test Files
```bash
pytest tests/test_api.py
```

### Run Tests with Coverage
```bash
pytest --cov=. --cov-report=html
```

### Run Tests Verbosely
```bash
pytest -v
```

### Run Specific Test Cases
```bash
# Run specific test class
pytest tests/test_auth.py::TestUserLogin

# Run specific test method
pytest tests/test_auth.py::TestUserLogin::test_login_success
```

## Test Configuration

### Fixtures (`conftest.py`)
- `app_instance`: Flask application instance (TESTING=True)
- `request_context`: Request context for calling views directly

No database is used in tests; `db.session`, `Task.query`, and `flask_login` are mocked.

## Test Data Management

### Sample Data
Tests construct lightweight objects (e.g., `SimpleNamespace`) inline.

### Data Isolation
- Each test function gets a fresh database
- No test data persists between tests
- Tests can safely modify data without affecting others

## Assertion Patterns

### View Logic Testing
```python
def test_create_task_success(monkeypatch, request_context, mock_auth, fake_session):
    # monkeypatch request.get_json and call the view directly
    rv = api_add_task()
    resp = rv[0] if isinstance(rv, tuple) else rv
    assert resp.status_code == 201 or rv[1] == 201
```

### Database State Testing
```python
def test_task_creation(app_context):
    task = Task(title='Test', priority='High', due_date='2024-12-31', status='Pending', user_id=1)
    db.session.add(task)
    db.session.commit()
    assert task.id is not None
```

### Authentication Testing
Authentication is mocked by patching `flask_login.utils._get_user()`.

## Common Test Patterns

### 1. Happy Path Testing
Test successful execution of normal operations:
```python
def test_create_task_success(client, sample_user):
    # Setup, execute, assert success
```

### 2. Error Handling Testing
Test error conditions and edge cases:
```python
def test_create_task_unauthorized(client):
    # Test without authentication
    assert response.status_code == 401
```

### 3. Input Validation Testing
Test various input validation scenarios:
```python
def test_create_task_missing_fields(client, sample_user):
    # Test with missing required fields
    assert response.status_code == 400
```

### 4. Security Testing
Test user isolation and access control:
```python
def test_user_cannot_access_other_user_tasks(client, app_context):
    # Test user isolation
    assert len(user1_tasks) == 0
```

## Coverage Goals

### Target Coverage Areas
- **Models**: 100% - All model methods and validations
- **API Endpoints**: 100% - All endpoints and status codes
- **Authentication**: 100% - All auth flows and edge cases
- **Integration**: 90% - Major workflows and scenarios

### Coverage Reports
- HTML coverage report: `htmlcov/index.html`
- Terminal coverage summary with missing lines
- Excludes test files and virtual environments

## Continuous Integration

### Pre-commit Hooks
```bash
# Run tests before commit
pytest --cov=. --cov-fail-under=90
```

### CI/CD Pipeline
```yaml
test:
  script:
    - pip install -r requirements.txt
    - pytest --cov=. --cov-report=xml
    - pytest --cov=. --cov-fail-under=90
```

## Debugging Tests

### Verbose Output
```bash
pytest -v -s
```

### Debug Specific Test
```bash
pytest tests/test_auth.py::test_login_success -v -s
```

### Print Statements
```python
def test_debug_example(client):
    response = client.post('/api/tasks', json=data)
    print(f"Response: {response.data}")
    assert response.status_code == 201
```

## Best Practices

### Test Organization
- One test class per module/endpoint
- Descriptive test method names
- Clear setup, execution, and assertion phases
- Use fixtures for common setup

### Test Data
- Use realistic test data
- Test both valid and invalid inputs
- Cover edge cases and boundary conditions
- Maintain test data consistency

### Assertions
- Use specific assertions (`assert response.status_code == 201`)
- Test both positive and negative cases
- Verify data integrity and relationships
- Check error messages and status codes

### Performance
- No database dependency; tests run fast and are isolated

## Troubleshooting

### Common Issues
1. **Request context errors**: Ensure `request_context` fixture wraps view calls
2. **Unauthorized errors**: Mock user via `flask_login.utils._get_user()`
3. **Import errors**: Verify test directory structure and imports

### Debug Commands
```bash
# Check test discovery
pytest --collect-only

# Run with maximum verbosity
pytest -vvv

# Run single test with debugging
pytest tests/test_auth.py::test_login_success --pdb
```

This comprehensive test suite ensures the Task Manager REST API is robust, secure, and reliable across all use cases and edge conditions.
