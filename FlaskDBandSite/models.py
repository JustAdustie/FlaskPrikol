from flask_login import UserMixin
from __init__ import db


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    login = db.Column(db.String(100))
    password = db.Column(db.String(100))
    priority = db.Column(db.Integer)


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    card = db.Column(db.String(100))
