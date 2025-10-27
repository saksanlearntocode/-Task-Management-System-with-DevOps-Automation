import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test if the index page loads correctly"""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'To-Do App' in rv.data

def test_add_task(client):
    """Test adding a new task"""
    rv = client.post('/add', data={
        'title': 'Test Task',
        'description': 'This is a test task'
    }, follow_redirects=True)
    assert rv.status_code == 200
    assert b'Test Task' in rv.data

def test_complete_task(client):
    """Test marking a task as complete"""
    # First add a task
    client.post('/add', data={
        'title': 'Complete Test Task',
        'description': 'This task will be completed'
    })
    
    # Then mark it as complete (assuming it's the first task with id=1)
    rv = client.get('/complete/1', follow_redirects=True)
    assert rv.status_code == 200
