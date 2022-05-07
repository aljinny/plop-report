from mainpage import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    colors = db.Column(db.Text(), nullable=False)
    colors_code = db.Column(db.Text(), nullable=False)
    img_url = db.Column(db.Text(), nullable=False)
    #playlist
    create_date = db.Column(db.DateTime(), nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    #user = db.relationship('User', backref=db.backref('question_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False,)
    #user = db.relationship('User', backref=db.backref('answer_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)

class bugs_pl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pl_id = db.Column(db.Integer, nullable=False)
    s_title = db.Column(db.Text, nullable=False)
    s_artist = db.Column(db.Text, nullable=False)
    plop_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    question = db.relationship('Question', backref=db.backref('bugs_pl_set'))

"""
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
"""
