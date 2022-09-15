from flask import render_template, redirect, url_for, request
from app import app, db
from app.models import Story, Task, Developer, TaskActualTimes
from app.developer_service import add_developer
from app.developer_summary import summarize_developers
from app.story_service import get_story_values
from app.task_service import get_task_values


@app.route('/', methods=['POST','GET'])
@app.route('/story', methods=['POST', 'GET'])
def story():
    """
    This is the method to show stories.

    Query models of Story, Task & TaskActualTimes in query_result and
    returns a list (stories) after they are filtered.

    return:
        render_template (str) for getting template
    """
    if request.method == 'GET':
        query_result = db.session.query(Story, Task, TaskActualTimes).join(
            Task, Story.id == Task.story_id, isouter=True).join(
            TaskActualTimes, Task.task_id == TaskActualTimes.task_id, isouter=True).all()
        stories = get_story_values(query_result)
        return render_template('story.html', title='Stories', stories=stories)


@app.route('/story/<id>', methods=['POST', 'GET'])
def story_id(id):
    """
    This is the method for looking at specific story.

    Query models of Task & TaskActualTimes in query_result and
    Story, Task & TaskActualTimes in query_result2 while
    returning lists (tasks & stories) after they are filtered.

    args:
        id (str) for retrieving story id

    return:
        render_template (str) for getting template
    """
    if request.method == 'GET':
        story = Story.query.filter_by(id=id).first()
        query_result = db.session.query(Task, TaskActualTimes).filter(
            Task.story_id == id).filter(
            Task.task_id == TaskActualTimes.task_id).all()
        query_result_2 = db.session.query(Story, Task, TaskActualTimes).join(
            Task, Story.id == Task.story_id, isouter=True).join(
            TaskActualTimes, Task.task_id == TaskActualTimes.task_id, isouter=True).all()
        tasks = get_task_values(query_result)
        stories = get_story_values(query_result_2)
        return render_template('task.html', title='Tracker', id=id, story=story, tasks=tasks, stories=stories)


@app.route('/create_story', methods=['POST', 'GET'])
def create_story():
    if request.method == 'POST':
        """
        This is the method for creating a story.
        
        If request is GET then template is rendered while for POST request
        it takes the values from frond end, assigns them to Story variables
        and saves to database.
        
        
        returns:
            if GET:
                render_template (str) for getting template
            elif POST: 
                redirect (werkzeug.wrappers.response.Response)
        """
        story = request.form
        add_story = Story(story_name=story['story_name'],
                          status='check' in story,
                          description=story['story_description'],
                          estimated_points=story['estimated_points'])
        db.session.add(add_story)
        db.session.commit()
        return redirect(url_for('story'))

    return render_template('create_story.html', title='Tracker')


@app.route('/story/<id>/update_story', methods=['POST', 'GET'])
def update_story(id):
    """
    This is the method for updating story.

    If request is GET then template is rendered while for POST request
    it updates the values from frond end, assigns them to Story variables
    and saves to database.

    args:
        id (str) for retrieving story id

    returns:
        if GET:
            render_template (str) for getting template
        elif POST:
            redirect (werkzeug.wrappers.response.Response)
    """
    if request.method == 'GET':
        story = Story.query.get(id)
        return render_template('update_story.html', title='Tracker', story=story)

    elif request.method == 'POST':
        item = Story.query.get(id)
        item.story_name = request.form['story_name']
        item.status = 'check' in request.form
        item.description = request.form['story_description']
        item.estimated_points = request.form['estimated_points']
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('story'))


@app.route('/story/<id>/create_task', methods=['POST', 'GET'])
def create_task(id):
    """
    This the method for creating task.

    If request is GET then template is rendered while for POST request
    it takes the values from frond end, assigns them to Task variables
    and saves to database.

    args:
        id (str) for retrieving task id

    returns:
        if GET:
            render_template (str) for getting template
        elif POST:
            redirect (werkzeug.wrappers.response.Response)
    """
    if request.method == 'POST':
        task = request.form
        print('lala', id)
        print(task)
        # dev_id = request.form.get('comp_select')
        add_task = Task(
            task_name=task['task_name'],
            story_id=id,
            status=task['check'] == 'on',
            description=task['task_description'],
            developer_id=task['comp_select'],
            estimated_points=task['estimated_points'],
            iteration=task['iter'])
        db.session.add(add_task)
        db.session.flush()
        db.session.refresh(add_task)
        if request.form['actual_time'] != '0' and request.form['actual_time'] != '':
            time = TaskActualTimes(
                task_id=add_task.task_id,
                actual_time=task['actual_time']
            )
            db.session.add(time)
        db.session.commit()
        return redirect(url_for('story_id', id=id))

    developers = Developer.query.all()
    return render_template('create_task.html', title='Tracker', developers=developers)


@app.route('/story/<story_id>/update_task/<task_id>', methods=['POST', 'GET'])
def update_task(story_id, task_id):
    """
    This is the method for updating the task.

    If request is GET then template is rendered with specific task queried and
    all developers queried and shown as dropdown on front end while for POST request
    it updates the values from frond end, assigns them to Task, TaskActualTimes variables
    and saves to database.

    args:
        story_id (str) for retrieving story id
        task_id (str) for retrieving task id

    returns:
        if GET:
            render_template (str) for getting template
        elif POST:
            redirect (werkzeug.wrappers.response.Response)
    """
    if request.method == 'GET':
        task = Task.query.get(task_id)
        developers = Developer.query.all()
        print(type(story_id), type(task_id))
        return render_template('update_task.html', title='Tracker', task=task, developers=developers)

    elif request.method == 'POST':
        # dev_id = request.form.get('comp_select')
        item = Task.query.get(task_id)
        item.task_name = request.form['task_name']
        item.story_id = story_id
        item.developer_id = request.form['comp_select']
        item.status = 'check' in request.form
        item.description = request.form['task_description']
        item.estimated_points = request.form['estimated_points']
        item.iteration = request.form['iter']
        if request.form['actual_time'] != '0' and request.form['actual_time'] != '':
            time = TaskActualTimes(
                task_id=item.task_id,
                actual_time=request.form['actual_time']
            )
            db.session.add(time)
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('story_id', id=story_id))


@app.route('/create_developer', methods=['POST', 'GET'])
def create_developer():
    """
    This is the method for creating a developer.

    If request is GET then template is rendered while for POST request
    add_developer function is called followed by redirection.


    returns:
        if GET:
            render_template (str) for getting template
        elif POST:
            redirect (werkzeug.wrappers.response.Response)
    """
    if request.method == 'POST':
        add_developer(request.form)
        return redirect(url_for('story'))

    return render_template('create_developer.html', title='Tracker')


@app.route('/developer_summary', methods=['POST', 'GET'])
def developer_summary():
    """
    This is the method for looking at summary with developers.

    Query models of Task, TaskActualTimes & Developer in query_result,
    then gets the summary of developers (developers_list) and renders template.

    return:
            render_template (str) for getting template
    """
    if request.method == 'GET':
        query_result = db.session.query(Task, TaskActualTimes, Developer).filter(
            Task.developer_id == Developer.id).filter(
            Task.task_id == TaskActualTimes.task_id).all()
        developers_list = summarize_developers(query_result)
        return render_template('developer.html', developers=developers_list)
