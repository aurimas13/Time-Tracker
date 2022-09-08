from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm
from app.models import Story, Task, Developer

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


@app.route('/story', methods=['POST', 'GET', 'PUT'])
def story():
    story = {'STORY_NAME': 'Stories'}
    if request.method == 'GET':
        stories = Story.query.all()
        # print(stories[0].story_name)
        # return "lala"
        return render_template('story.html', title='Tracker', story=story, stories=stories)
        # return redirect(url_for('index', story=story))
    elif request.method == 'POST':
        if request.form.get('Create Story') == 'Create Story':
            print('lala')
            return redirect(url_for('create_story'))
        else:
            pass  # do something else


@app.route('/create_story', methods=['POST', 'GET', 'PUT'])
def create_story():
    # found = False
    # print("lala", story)
    if request.method == 'POST':
        story = request.form
        print(type(story['check']))
        add_story = Story(story_name=story['story_name'],
                          active=story['check'] == 'on',
                          description=story['story_description'],
                          calculated_time=story['time'])
        print(add_story)
        db.session.add(add_story)
        db.session.commit()
        return redirect(url_for('story'))

    return render_template('create_story.html', title='Tracker')

    # print(request.form["story_name"])
    # stories = Story.query.all()
    #     story = request.form
    # json_story = dict(story)
    # print(json_story)

    # for story in stories:
    #     if story.story_name == story:
    #         found = True
    #
    # # add the story if not in database already
    # if not found:
    #     add_story = Story(story, True)
    #     db.session.add(add_story)
    #     db.session.commit()
    # #     stories = Story.query.all()
    # print(stories[1].story_name)
    # return "lala"
    # else:


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)
