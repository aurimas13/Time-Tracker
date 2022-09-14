from app import db


class Story(db.Model):
    """    User Story Schema    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    story_name = db.Column(db.String(64))
    status = db.Column(db.Boolean)
    description = db.Column(db.String(140))
    estimated_points = db.Column(db.Integer)

    def __repr__(self):
        return '<Story {} with id {}>'.format(self.story_name, self.id)


class Task(db.Model):
    """     Task Schema     """
    task_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    story_id = db.Column(db.Integer, db.ForeignKey('story.id'))
    task_name = db.Column(db.String(64))
    status = db.Column(db.Boolean, default=False)
    description = db.Column(db.String(140))
    estimated_points = db.Column(db.Integer)
    developer_id = db.Column(db.Integer, db.ForeignKey('developer.id')) # sitas turi buti assigninamas
    iteration = db.Column(db.String(64))

    def __repr__(self):
        return '<Task {} of story id {} with task id {}>'.format(self.task_id, self.story_id, self.task_id)


class TaskActualTimes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.task_id'))
    actual_time = db.Column(db.Integer)

    def __repr__(self):
        return '<Actual task id - {} with time {}>'.format(self.task_id, self.actual_time)


class Developer(db.Model):
    """     Developer Schema    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True)
    # Jei yra du jonai reikia sukurti emailus kurie yra unique ir leidzia atskirti developerius Jonus ar panasiai, tada email unique o developer name'ai nebe

    def __repr__(self):
        return '<Developer {} with developer id {}>'.format(self.name, self.id)
