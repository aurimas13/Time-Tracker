from datetime import datetime
from app import db


class Story(db.Model):
    """    User Story Schema    """
    story_id = db.Column(db.Integer, primary_key=True)
    story_name = db.Column(db.String(64), index=True, unique=True)
    active = db.Column(db.Boolean)
    description = db.Column(db.String(140))
    calculated_time = db.Column(db.Integer, index=True, unique=True)
    # Setup the relationship to the User table
    # tasks = db.relationship('Task')

    def __repr__(self):
        return '<Story {} with id {}>'.format(self.story_name, self.story_id)


class Task(db.Model):
    """     Task Schema     """
    task_id = db.Column(db.Integer, primary_key=True)
    story_id = db.Column(db.Integer, db.ForeignKey('story.story_id'))
    task = db.Column(db.String(64), index=True, unique=True)
    status = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(140))
    task_estimated_time = db.Column(db.Numeric, index=True, unique=True)
    start_date = db.Column(db.DateTime, default=datetime.utcnow, index=True, unique=True)
    end_date = db.Column(db.DateTime, index=True, unique=True)
    time_spent = end_date - start_date
    task_name = db.Column(db.String(64), index=True, unique=True)
    iteration = db.Column(db.Integer, index=True, unique=True)
    # developer_id = db.Column(db.Integer, db.ForeignKey('task.task_id')) # sitas turi buti assigninamas

    def __repr__(self):
        return '<Task {} of story id {} with task id {}>'.format(self.story_id, self.task_name, self.task_id)


class Developer(db.Model):
    """     Developer Schema    """
    developer_id = db.Column(db.Integer, primary_key=True)
    developer_name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Developer {} with developer id {}>'.format(self.developer_name, self.developer_id)
