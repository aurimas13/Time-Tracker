from flask import render_template, flash, redirect, url_for, request
from werkzeug.exceptions import BadRequestKeyError
from app import app, db
from app.models import Story, Task, Developer, TaskActualTimes


@app.route('/', methods=['POST','GET'])
@app.route('/story', methods=['POST', 'GET'])
def story():
    # story = {'STORY_NAME': 'Stories'}
    if request.method == 'GET':
        # query_result = db.session.query(Story, Task, TaskActualTimes).filter(
        #     Task.story_id == Story.id).filter(
        #     Task.task_id == TaskActualTimes.task_id).all()
        query_result = db.session.query(Story, Task, TaskActualTimes).join(
            Task, Story.id == Task.story_id, isouter=True).join(
            TaskActualTimes, Task.task_id == TaskActualTimes.task_id, isouter=True).all()
        stories = {}
        tasks = {}
        story_actual_time = 0
        for row in query_result:
            story = row[0].__dict__
            print(story)
            task = row[1].__dict__
            # print(task)
            actual_time = row[2].__dict__
            # print(actual_time)
            # key_id = task['task_id']
            # print(key_id)
            story_id = story['id']
            print(story_id)
            if story_id in stories:
                print('lala')
                if actual_time['actual_time']:
                    stories[story_id]['actual_times_sum'] += actual_time['actual_time']
                    stories[story_id]['estimated_time'] = story['estimated_time']
            else:
                print('haha')
                stories[story_id] = story
                if actual_time['actual_time']:
                    stories[story_id]['actual_times_sum'] = actual_time['actual_time']
                    stories[story_id]['estimated_time'] = story['estimated_time']
                else:
                    stories[story_id]['actual_times_sum'] = 0
                    stories[story_id]['estimated_time'] = 0

        stories = stories.values()
        print(stories)
        # 1 : {'id' : 1, 'description' : '1', 'status' : False, 'story_name' : 1, 'estimated_time' : 1, 'actual_times_sum' :  }

    return render_template('story.html', title='Stories', stories=stories, tasks=tasks)
    #     # return render_template('task.html', title='Tracker', id=id, story=story, stories=stories, tasks=tasks, story_actual_time=story_actual_time)
    # if request.method == 'GET':
    #     stories = Story.query.all()
    #     tasks = Task.query.all()
    #     try:
    #         story_actual_time = request.args['story_actual_time']
    #     except BadRequestKeyError:
    #         story_actual_time = None
    #     return render_template('story.html', title='Tracker', tasks=tasks, stories=stories, story_actual_time=story_actual_time)



@app.route('/story/<id>', methods=['POST', 'GET'])
def story_id(id):
    if request.method == 'GET':
        story = Story.query.filter_by(id=id).first()
        query_result = db.session.query(Task, TaskActualTimes).filter(
            Task.story_id == id).filter(
            Task.task_id == TaskActualTimes.task_id).all()
        tasks = {}
        story_actual_time = 0
        for row in query_result:
            task = row[0].__dict__
            actual_time = row[1].__dict__
            key_id = task['task_id']
            story_id = task['story_id']
            if key_id in tasks:
                if actual_time['actual_time']:
                    tasks[key_id]['actual_times'].append(actual_time)
                    tasks[key_id]['actual_times_sum'] += actual_time['actual_time']
                    story_actual_time += actual_time['actual_time']
            else:
                tasks[key_id] = task
                if actual_time['actual_time']:
                    tasks[key_id]['actual_times'] = [actual_time]
                    tasks[key_id]['actual_times_sum'] = actual_time['actual_time']
                    story_actual_time += actual_time['actual_time']
                else:
                    tasks[key_id]['actual_times'] = []
                    tasks[key_id]['actual_times_sum'] = 0

            # if story_id in tasks:
            print(story_actual_time)
        tasks = tasks.values()
        return render_template('task.html', title='Tracker', id=id, story=story, tasks=tasks, story_actual_time=story_actual_time)


@app.route('/create_story', methods=['POST', 'GET'])
def create_story():
    if request.method == 'POST':
        story = request.form
        add_story = Story(story_name=story['story_name'],
                          status='check' in story,
                          description=story['story_description'],
                          estimated_time=story['time'])
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
        item.story_name = request.form['story_name']
        item.status = 'check' in request.form
        item.description = request.form['story_description']
        item.estimated_time = request.form['time']
        db.session.add(item)
        db.session.commit()
        return redirect(url_for('story'))

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
        return render_template('developer.html', developers=developers)


@app.route('/story/<id>/create_task', methods=['POST', 'GET'])
def create_task(id):
    if request.method == 'POST':
        task = request.form
        dev_id = request.form.get('comp_select')
        add_task = Task(
            task_name=task['task_name'],
            story_id=id,
            status=task['check'] == 'on',
            description=task['task_description'],
            developer_id=dev_id,
            estimated_time=task['time'],
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
    if request.method == 'GET':
        task = Task.query.get(task_id)
        developers = Developer.query.all()
        return render_template('update_task.html', title='Tracker', task=task, developers=developers)

    elif request.method == 'POST':
        dev_id = request.form.get('comp_select')
        print('This is the developer id ', dev_id)
        item = Task.query.get(task_id)
        item.task_name = request.form['task_name']
        item.story_id = story_id
        item.developer_id = dev_id
        item.status = 'check' in request.form
        item.description = request.form['task_description']
        item.estimated_time = request.form['time']
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
