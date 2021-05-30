from flask_sqlalchemy import SQLAlchemy

from src import app

db = SQLAlchemy(app)


class Game(db.Model):
    __tablename__ = 'Game'

    gid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    platform = db.Column(db.String(255))
    score = db.Column(db.Integer)
    genre = db.Column(db.String(255))
    editors_choice = db.Column(db.String(1))

class User(db.Model):

    __tablename__ = 'user'

    email = db.Column(db.String(255), primary_key=True, index=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    password = db.Column(db.String(255))
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False