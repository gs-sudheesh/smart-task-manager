"""Strict unit tests for API view functions (no Flask test client)."""

import json
from types import SimpleNamespace
import pytest
from werkzeug.exceptions import Unauthorized

from api import task_manager as views


def _fake_user(user_id=1, authenticated=True):
    return SimpleNamespace(id=user_id, is_authenticated=authenticated)


class _FakeQuery:
    def __init__(self, items):
        self._items = items

    def filter_by(self, **kwargs):
        filtered = [i for i in self._items if all(getattr(i, k) == v for k, v in kwargs.items())]
        return _FakeQuery(filtered)

    def filter(self, predicate):
        # Very lightweight title ilike support
        try:
            term = predicate.right.value.strip('%').lower()
            filtered = [i for i in self._items if term in getattr(i, 'title', '').lower()]
        except Exception:
            filtered = self._items
        return _FakeQuery(filtered)

    def order_by(self, key):
        # Support sorting by priority or due_date / due_date.desc()
        if hasattr(key, 'desc'):
            return _FakeQuery(sorted(self._items, key=lambda x: getattr(x, 'due_date'), reverse=True))
        attr = getattr(key, 'key', None) or getattr(key, 'name', None) or key
        return _FakeQuery(sorted(self._items, key=lambda x: getattr(x, attr) if isinstance(attr, str) else getattr(x, 'priority')))

    def all(self):
        return self._items

    def get(self, pk):
        for i in self._items:
            if getattr(i, 'id', None) == pk:
                return i
        return None


class _FakeSession:
    def __init__(self):
        self.added = []
        self.deleted = []
        self._id_counter = 1

    def add(self, obj):
        if getattr(obj, 'id', None) is None:
            obj.id = self._id_counter
            self._id_counter += 1
        self.added.append(obj)

    def add_all(self, objs):
        for o in objs:
            self.add(o)

    def delete(self, obj):
        self.deleted.append(obj)

    def commit(self):
        return None

    def remove(self):
        # Flask-SQLAlchemy teardown calls session.remove(); make it a no-op
        return None


@pytest.fixture
def mock_auth(monkeypatch):
    # Force login_required to see an authenticated user
    from flask_login import utils as login_utils
    monkeypatch.setattr(login_utils, '_get_user', lambda: _fake_user(1, True))


@pytest.fixture
def mock_unauth(monkeypatch):
    from flask_login import utils as login_utils
    monkeypatch.setattr(login_utils, '_get_user', lambda: _fake_user(1, False))


@pytest.fixture
def fake_session(monkeypatch):
    from config import db_config
    sess = _FakeSession()
    monkeypatch.setattr(db_config.db, 'session', sess)
    return sess


@pytest.fixture
def fake_tasks(monkeypatch):
    class _Task(SimpleNamespace):
        pass

    items = [
        _Task(id=1, title='A task', priority='High', due_date='2024-12-31', status='Pending', user_id=1),
        _Task(id=2, title='B task', priority='Low', due_date='2024-12-25', status='Completed', user_id=1),
    ]

    from domain import task as task_domain
    monkeypatch.setattr(task_domain.Task, 'query', _FakeQuery(items))
    return items


def test_get_tasks_unauthorized(request_context, mock_unauth):
    with pytest.raises(Unauthorized):
        views.api_get_tasks()


def test_get_tasks_returns_items(request_context, mock_auth, fake_tasks):
    rv = views.api_get_tasks()
    status = getattr(rv, 'status_code', None) or (rv[1] if isinstance(rv, tuple) and len(rv) > 1 else 200)
    assert status == 200
    resp = rv[0] if isinstance(rv, tuple) else rv
    data = json.loads(resp.get_data(as_text=True))
    assert len(data) == 2
    assert {d['title'] for d in data} == {'A task', 'B task'}


def test_create_task_success(monkeypatch, request_context, mock_auth, fake_session):
    # Monkeypatch request.get_json
    from flask.wrappers import Request
    monkeypatch.setattr(Request, 'get_json', lambda self, *a, **k: {
        'title': 'New Task', 'priority': 'Medium', 'due_date': '2024-12-31'
    })

    class _Task(SimpleNamespace):
        pass

    monkeypatch.setattr(views, 'Task', _Task)
    rv = views.api_add_task()
    status = getattr(rv, 'status_code', None) or (rv[1] if isinstance(rv, tuple) and len(rv) > 1 else None)
    assert status == 201
    resp = rv[0] if isinstance(rv, tuple) else rv
    data = json.loads(resp.get_data(as_text=True))
    assert data['message'] == 'Task added!'
    assert data['id'] == 1


def test_update_task_not_found(request_context, mock_auth, monkeypatch):
    class _Query:
        def get(self, _):
            return None
    class _Task:
        query = _Query()
    monkeypatch.setattr(views, 'Task', _Task)

    rv = views.api_update_task(999)
    status = getattr(rv, 'status_code', None) or (rv[1] if isinstance(rv, tuple) and len(rv) > 1 else None)
    assert status == 404


def test_delete_task_success(request_context, mock_auth, monkeypatch, fake_session):
    class _T(SimpleNamespace):
        pass
    existing = _T(id=5)

    class _Query:
        def get(self, _):
            return existing
    class _Task:
        query = _Query()
    monkeypatch.setattr(views, 'Task', _Task)

    rv = views.api_delete_task(5)
    status = getattr(rv, 'status_code', None) or (rv[1] if isinstance(rv, tuple) and len(rv) > 1 else 200)
    assert status == 200
    resp = rv[0] if isinstance(rv, tuple) else rv
    data = json.loads(resp.get_data(as_text=True))
    assert data['message'] == 'Task deleted!'

 