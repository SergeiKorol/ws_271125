import pytest
import requests
@pytest.mark.xfail(reason = 200)
def test_add():
    body = {"title":"Михаил","completed":False}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    id = response.json()["id"]
    response = requests.delete(f'https://todo-app-sky.herokuapp.com/{id}')
    response = requests.get(f"https://todo-app-sky.herokuapp.com/{id}")
    assert response.status_code == 404

