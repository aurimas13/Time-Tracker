from datetime import datetime
from app import db


class Story(db.Model):
    """    User Story Schema    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    story_name = db.Column(db.String(64), index=True)
    status = db.Column(db.Boolean)
    description = db.Column(db.String(140))
    calculated_time = db.Column(db.Integer, index=True)
    tasks = db.relationship('Task', backref='author', lazy='dynamic')


    def __repr__(self):
        return '<Story {} with id {}>'.format(self.story_name, self.id)


class Task(db.Model):
    """     Task Schema     """
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'))
    task_name = db.Column(db.String(64), index=True)
    status = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(140))
    task_estimated_time = db.Column(db.Numeric, index=True)
    # start_date = db.Column(db.DateTime, default=datetime.utcnow, index=True)
    # end_date = db.Column(db.DateTime, index=True)
    # time_spent = end_date - start_date
    iteration = db.Column(db.String(64), index=True)
    # developer_id = db.Column(db.Integer, db.ForeignKey('task.task_id')) # sitas turi buti assigninamas

    def __repr__(self):
        return '<Task {} of story id {} with task id {}>'.format(self.story_id, self.task_name, self.task_id)


class Developer(db.Model):
    """     Developer Schema    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    developer_name = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<Developer {} with developer id {}>'.format(self.developer_name, self.id)
