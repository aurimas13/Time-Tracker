from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm, StoryForm, TaskForm
from app.models import Story, Task, Developer, TaskActualTimes
from sqlalchemy import update

@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    story = {'STORY_NAME': 'Home'}
    stories = [
        {
            'name': {'story_name': 'Story X'},
            'story_id': 1,
            'description': 'Finish the first endpoint!',
            'active': True,
            'estimated_time': 7
        },
        {
            'name': {'story_name': 'Story Y'},
            'story_id': 2,
            'description': 'Conclude with the first story endpoint!',
            'active': False,
            'estimated_time': 33
        }
    ]
    if request.method == 'POST':
        return 'Hello'
    else:
        return render_template('index.html', title='Home', story=story, stories=stories)


@app.route('/story', methods=['POST', 'GET'])
def story():
    story = {'STORY_NAME': 'Stories'}
    if request.method == 'GET':
        stories = Story.query.all()
        return render_template('story.html', title='Tracker', story=story, stories=stories)
        # return redirect(url_for('index', story=story))
    # elif request.method == 'POST':
    #     if request.form.get('Create Story') == 'Create Story':
    #         return redirect(url_for('create_story'))
    #     else:
    #         pass  # do something else


@app.route('/story/<id>', methods=['POST', 'GET'])
def story_id(id):
    task = {'TASK_NAME': 'Tasks'}
    if request.method == 'GET':
        tasks = Task.query.filter_by(story_id=id).join(TaskActualTimes).all()
        print(tasks.keys())
        return render_template('task.html', title='Tracker', id=id, task=task, tasks=tasks)
    # elif request.method == 'POST':
    #     if request.form.get('Create Task') == 'Create Task':
    #         return 'lala'
    #         # return redirect(url_for('/story/<id>/create_task'))
    #     else:
    #         pass  # do something else


@app.route('/create_story', methods=['POST', 'GET'])
def create_story():
    if request.method == 'POST':
        story = request.form
        print(story, 'check' in story)
        add_story = Story(story_name=story['story_name'],
                          status='check' in story,
                          description=story['story_description'],
                          estimated_time=story['time'])
        print(add_story)
        db.session.add(add_story)
        db.session.commit()
        return redirect(url_for('story'))

    return render_template('create_story.html', title='Tracker')


@app.route('/story/<id>/update_story', methods=['POST', 'GET'])
def update_story(id):
    if request.method == 'GET':
        stories = Story.query.filter_by(id=id)
        story = Story.query.get(id)
        return render_template('update_story.html', title='Tracker', story=story, stories=stories)

    elif request.method == 'POST':
        # return 'jaa'
        item = Story.query.get(id)
        print(item)
        item.story_name = request.form['story_name']
        item.status = 'check' in request.form
        item.description = request.form['story_description']
        item.estimated_time = request.form['time']
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('story'))
    #
    # return render_template('create_story.html', form=form)


@app.route('/story/<id>/create_task', methods=['POST', 'GET'])
def create_task(id):
    if request.method == 'POST':
        task = request.form
        task_actual = request.form
        add_task = Task(
            task_name=task['task_name'],
            story_id=id,
            status=task['check'] == 'on',
            description=task['task_description'],
            estimated_time=task['time'],
            iteration=task['iter'])
        print(add_task)
        db.session.add(add_task)
        db.session.flush()
        db.session.refresh(add_task)
        time = TaskActualTimes(
            task_id=add_task.task_id,
            actual_time=task['actual_time']
        )
        db.session.add(time)
        db.session.commit()
        return redirect(url_for('story_id', id=id))
#
    return render_template('create_task.html', title='Tracker')


@app.route('/story/<story_id>/update_task/<task_id>', methods=['POST', 'GET'])
def update_task(story_id, task_id):
    if request.method == 'GET':
        # tasks = Task.query.filter_by(id=task_id)
        task = Task.query.get(task_id)
        return render_template('update_task.html', title='Tracker', task=task)

    elif request.method == 'POST':
        # return 'kasdkask'
        item = Task.query.get(task_id)
        print(item)
        item.task_name = request.form['task_name']
        item.story_id = story_id
        item.status = 'check' in request.form
        item.description = request.form['task_description']
        item.estimated_time = request.form['time']
        item.actual_time = request.form['actual_time'] # MAKE SURE TIMES ARE ADDED not overwritten
        item.iteration = request.form['iter']
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('story_id', id=story_id))


#     if request.method == 'POST':
#
#         task = db.session.query(Task).get(Task.id)
#         form = AddItem()
#         update_task = Task(
#             task_name=task['task_name'],
#             story_id=id,
#             status=task['check'] == 'on',
#             description=task['task_description'],
#             task_estimated_time=task['time'],
#             iteration=task['iter'])
#         print(update_task)
#         db.session.add(update_task)
#         db.session.commit()
#         return redirect(url_for('story_id', id=id))
# #
#     return render_template('create_task.html', title='Tracker')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         flash('Login requested for user {}, remember_me={}'.format(
#             form.username.data, form.remember_me.data))
#         return redirect(url_for('index'))
#     return render_template('login.html',  title='Sign In', form=form)
