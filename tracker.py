from app import app, db
from app.models import Story, Task, Developer


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Story': Story, 'Task': Task, 'Developer': Developer}