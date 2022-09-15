from app.models import Developer, Task, Story, TaskActualTimes


def get_task_taskactualtimes_by_ids(db):
    print(Task, TaskActualTimes)
    query = db.session.query(Task, TaskActualTimes).filter(
            Task.story_id == id).filter(
            Task.task_id == TaskActualTimes.task_id).all()
    return query