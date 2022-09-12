from flask import render_template, flash, redirect, url_for, request
from werkzeug.exceptions import BadRequestKeyError

from app import app, db
from app.forms import LoginForm, StoryForm, TaskForm
from app.models import Story, Task, Developer, TaskActualTimes
from sqlalchemy import update
from itertools import groupby
from operator import itemgetter


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


@app.route('/', methods=['POST','GET'])
@app.route('/story', methods=['POST', 'GET'])
def story():
    story = {'STORY_NAME': 'Stories'}
    if request.method == 'GET':
        try:
            story_actual_time = request.args['story_actual_time']
        except BadRequestKeyError:
            story_actual_time = None
        task = Task.query.all()
        stories = Story.query.all()
        return render_template('story.html', title='Tracker', task=task, story=story, stories=stories, story_actual_time=story_actual_time)
        # return redirect(url_for('index', story=story))
    # elif request.method == 'POST':
    #     if request.form.get('Create Story') == 'Create Story':
    #         return redirect(url_for('create_story'))
    #     else:
    #         pass  # do something else


@app.route('/story/<id>', methods=['POST', 'GET'])
def story_id(id):
    if request.method == 'GET':
        story = Story.query.filter_by(id=id).first()
        # print(story)
        query_result = db.session.query(Task, TaskActualTimes).filter(
            Task.story_id == id).filter(
            Task.task_id == TaskActualTimes.task_id).all()
        tasks = {}
        story_actual_time = 0
        for row in query_result:
            task = row[0].__dict__
            actual_time = row[1].__dict__
            key_id = task['task_id']  # pvz, 1, 2, 3
            story_id = task['story_id']
            if key_id in tasks:  # pvz, if 1 in tasks
                if actual_time['actual_time']:
                    # print(actual_time['actual_time'])
                    tasks[key_id]['actual_times'].append(actual_time)  # pvz, tasks[1]['actual_times'].append({'actual_time': 10})\
                    tasks[key_id]['actual_times_sum'] += actual_time['actual_time']
            else:
                tasks[key_id] = task  # pvz, tasks[1] = {'task_id': 1}
                if actual_time['actual_time']:
                    tasks[key_id]['actual_times'] = [actual_time]  # # pvz, tasks[1]['actual_times'] = {'actual_time': 10}
                    tasks[key_id]['actual_times_sum'] = actual_time['actual_time']
                else:
                    tasks[key_id]['actual_times'] = []
                    tasks[key_id]['actual_times_sum'] = 0

            if story_id in tasks:
                story_actual_time += tasks[key_id]['actual_times_sum']

        print(story_actual_time)
        tasks = tasks.values()
        return render_template('task.html', title='Tracker', id=id, story=story, tasks=tasks, story_actual_time=story_actual_time)

    # elif request.method == 'POST':
    #     story = Story.query.all()
    #     return render_template('story.html', story=story)
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
        # print(story, 'check' in story)
        add_story = Story(story_name=story['story_name'],
                          status='check' in story,
                          description=story['story_description'],
                          estimated_time=story['time'])
        # print(add_story)
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
        item = Story.query.get(id)
        # print(item)
        item.story_name = request.form['story_name']
        item.status = 'check' in request.form
        item.description = request.form['story_description']
        item.estimated_time = request.form['time']
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('story'))
    #
    # return render_template('create_story.html', form=form)

@app.route('/create_developer', methods=['POST', 'GET'])
def create_developer():
    if request.method == 'POST':
        developer = request.form
        add_developer = Developer(name=developer['developer_name'])
        db.session.add(add_developer)
        db.session.commit()
        return redirect(url_for('story'))

    return render_template('create_developer.html', title='Tracker')

@app.route('/developer_summary', methods=['POST', 'GET'])
def developer_summary():
    if request.method == 'GET':
        query_result = db.session.query(Task, TaskActualTimes, Developer).filter(Task.developer_id == Developer.id).filter(
            Task.task_id == TaskActualTimes.task_id).all()
        print(query_result)
        developers = {}
        for row in query_result:
            task = row[0].__dict__
            actual_time = row[1].__dict__
            developer = row[2].__dict__
            story_id = task['story_id']
            dev_id = developer['id']
            if dev_id in developers:
                if actual_time['actual_time']:
                    developers[dev_id]['actual_times_sum'] += actual_time['actual_time']
                    developers[dev_id]['estimated_time'] = task['estimated_time']
            else:
                developers[dev_id] = developer  # pvz, tasks[1] = {'task_id': 1}
                if actual_time['actual_time']:
                    developers[dev_id]['actual_times_sum'] = actual_time['actual_time']
                    developers[dev_id]['estimated_time'] = task['estimated_time']
                else:
                    developers[dev_id]['actual_times_sum'] = 0
                    developers[dev_id]['estimated_time'] = 0

        developers = developers.values()
        print(developers)
        # print(developers[dev_id]['actual_times_sum'])
        # print(developers[dev_id]['estimated_time'])
        # print(developers)
        # print(developers[dev_id]["name"])
        # print(f'Developer {developer["name"]} estimates {task["estimated_time"]} hours to complete the task while it took {actual_time["actual_time"]} hours to finish the task.')\
        return render_template('developer.html', developers=developers)


@app.route('/story/<id>/create_task', methods=['POST', 'GET'])
def create_task(id):
    if request.method == 'POST':
        task = request.form
        dev_id = request.form.get('comp_select')
        task_actual = request.form
        add_task = Task(
            task_name=task['task_name'],
            story_id=id,
            status=task['check'] == 'on',
            description=task['task_description'],
            developer_id=dev_id,
            estimated_time=task['time'],
            iteration=task['iter'])
        # print(add_task)
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
    if request.method == 'GET':
        # tasks = Task.query.filter_by(id=task_id)
        task = Task.query.get(task_id)
        developers = Developer.query.all()
        return render_template('update_task.html', title='Tracker', task=task, developers=developers)

    elif request.method == 'POST':
        # developers = Developer.query.all()
        dev_id = request.form.get('comp_select')
        print('This is the developer id ', dev_id)
        item = Task.query.get(task_id)
        item.task_name = request.form['task_name']
        item.story_id = story_id
        item.developer_id = dev_id
        item.status = 'check' in request.form
        item.description = request.form['task_description']
        item.estimated_time = request.form['time']
        # item.actual_time = request.form['actual_time'] # MAKE SURE TIMES ARE ADDED not overwritten
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
