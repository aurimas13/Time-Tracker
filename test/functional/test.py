from app.models import Story, Task, TaskActualTimes, Developer
import app


def test_create_story_post(test_client):
    value = {
            'story_name': 'Story 1',
            'status': True,
            'story_description': 'Great one',
            'estimated_points': 5
    }
    response = test_client.post("/create_story", data=value, follow_redirects=True)
    print(response.get_data(as_text=True))
    assert response.status_code == 200
    assert len(response.history) == 1
    assert response.request.path == "/story"
    assert response.get_data(as_text=True).count("<div><p>Total time to complete the story <b>Story 1</b>") == 1


def test_create_developer_post(test_client):
    value = {'developer_name': 'Alex'}
    response = test_client.post("/create_developer", data=value, follow_redirects=True)
    print(response.get_data(as_text=True))
    assert response.status_code == 200
    assert len(response.history) == 1
    assert response.request.path == "/story"


def test_update_story_post(test_client):
    value = {
        'estimated_points': 10,
        'story_name': 'Task Zero',
        'status': False,
        'story_description': 'Let\'s go',
    }
    response = test_client.post("/story/1/update_story", data=value, follow_redirects=True)
    print(response.get_data(as_text=True))
    assert response.status_code == 200
    assert len(response.history) == 1
    assert response.request.path == "/story"
    assert response.get_data(as_text=True).count("<div><p>Total time to complete the story <b>Task Zero</b>") == 1


def test_create_task_post(test_client):
    value = {
        'story_id': 1,
        'task_name': 'Task 1',
        'status': True,
        'task_description': 'Great one',
        'estimated_points': 5,
        'comp_select': 1,
        'iter': 'From Story 1'
    }
    response = test_client.post("/story/1/create_task", data=value, follow_redirects=True)
    # print(response.get_data(as_text=True))
    print(response)
    assert response.status_code == 200
    # assert len(response.history) == 1
    # assert response.request.path == "/story_id"
    # assert response.get_data(as_text=True).count("<div><p>The estimated points for the user story") == 1

