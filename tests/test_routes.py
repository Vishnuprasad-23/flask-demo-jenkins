import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

def test_add():
    app = create_app()
    client = app.test_client()
    response = client.post('/add', json={'a': 2, 'b': 3})
    assert response.status_code == 200
    assert response.json['result'] == 5
