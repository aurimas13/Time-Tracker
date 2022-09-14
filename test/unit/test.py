import pytest
from app.models import Task, TaskActualTimes, Developer
from app.developer_service import add_developer
from app.database_utils import save_changes
from app.developer_summary import summarize_developers

# def test_add_developer():
#     test_dev = {'developer_name': 'Alex'}
#     assert add_developer(test_dev) is True


def test_developers_summary():
    query = [
        (
            Task(
                story_id=1,
                task_name='Two',
                status=True,
                description='Something is happening again',
                estimated_time=121,
                developer_id=1,
                iteration='Story 1'
            ),
            TaskActualTimes(
                task_id=2,
                actual_time=121
            ),
            Developer(id=1, name='Alex')
        )
    ]
    print(summarize_developers(query))
    assert summarize_developers(query) == dict_values([{'id': 1, 'name': 'Alex', 'actual_times_sum': 121, 'estimated_time': 121}])
