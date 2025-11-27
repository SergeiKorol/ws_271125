import pytest
import requests

@pytest.mark.smoke
def completed_task_test():
    """ Тест на созданее задачи, которая сразу отмечена как выполненная"""
    body = {"title": "Already completed task", "completed": True}
    response = requests.post("https://todo-app-sky.herokuapp.com/", json=body)
    completed_task_json = response.json()

    completed_task_text = completed_task_json["completed"]

    assert response.status_code == 200
