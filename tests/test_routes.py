import json
from app import create_app

def test_add():
    app = create_app()
    client = app.test_client()
    response = client.post('/add', json={'a': 2, 'b': 3})
    assert response.status_code == 200
    assert response.json['result'] == 5
