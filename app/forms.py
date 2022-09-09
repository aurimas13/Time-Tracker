from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField,DateField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class StoryForm(FlaskForm):
    story_name = StringField('Story Name', validators=[DataRequired()])
    status = BooleanField('Status', validators=[DataRequired()])
    story_description = StringField('Story Description', validators=[DataRequired()])
    calculated_time = IntegerField('Estimated Time', validators=[DataRequired()])


class TaskForm(FlaskForm):
    task_name = StringField('Story Name', validators=[DataRequired()])
    status = BooleanField('Status')
    task_description = StringField('Story Description', validators=[DataRequired()])
    task_estimated_time = IntegerField('Story Description', validators=[DataRequired()])
    iteration = StringField('Iteration description', validators=[DataRequired()])
    # start_date = DateField('Start Date', validators=[DataRequired()])
    # end_date = DateField('End Date', validators=[DataRequired()])
    # time_spent = end_date - start_date
    # developer_id = db.Column(db.Integer, db.ForeignKe