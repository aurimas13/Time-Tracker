from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm

in_memory_datastore = {
    "COBOL": {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
    "ALGOL": {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
    "APL": {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
}


@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST','GET'])
def index():
    story = {'STORY_NAME': 'Let\'s go'}
    stories = [
        {
            'name': {'story_name': 'Story One'},
            'story_id': 1,
            'description': 'Finish the first endpoint!',
            'active': True,
            'estimated_time': 7
        },
        {
            'name': {'story_name': 'Story Two'},
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
    story = {'STORY_NAME': 'Let\'s go'}
    stories = [
        {
            'name': {'story_name': 'Story One'},
            'story_id': 1,
            'description': 'Finish the first endpoint!',
            'active': True,
            'estimated_time': 7
        },
        {
            'name': {'story_name': 'Story Two'},
            'story_id': 2,
            'description': 'Conclude with the first story endpoint!',
            'active': False,
            'estimated_time': 33
        }
    ]
    if request.method == 'GET':
        story = request.args.get('Story One')
        # print(request.args)
        # return (f'{story}')
        return redirect(url_for('index', story=story))
    # in_memory_datastore = {
    #     "COBOL": {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
    #     "ALGOL": {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
    #     "APL": {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
    #     "BASIC": {"name": "BASIC", "publication_year": 1964, "contribution": "runtime interpretation, office tooling"},
    #     "PL": {"name": "PL", "publication_year": 1966, "contribution": "constants, function overloading, pointers"},
    #     "SIMULA67": {"name": "SIMULA67", "publication_year": 1967,
    #                  "contribution": "class/object split, subclassing, protected attributes"},
    #     "Pascal": {"name": "Pascal", "publication_year": 1970,
    #                "contribution": "modern unary, binary, and assignment operator syntax expectations"},
    #     "CLU": {"name": "CLU", "publication_year": 1975,
    #             "contribution": "iterators, abstract data types, generics, checked exceptions"},
    # }
    # return {"story": list(in_memory_datastore.values())}


@app.route('/story/<programming_language_name>')
def get_programming_language(programming_language_name):
    return in_memory_datastore[programming_language_name]


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)
