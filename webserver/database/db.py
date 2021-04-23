'''
CIS 422 Project 1: Vaccination System
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This file allows interfacing with the raw SQLite data via a Python import
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from typing import List, Optional
import datetime

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    app.app_context().push()

def create_all():
    db.create_all()

def setup_headless():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    init_app(app)

if __name__=='__main__':
    setup_headless() 

class Vaccinee(db.Model):
    '''Vaccinee is a person who wishes to be vaccinated.

    They have some simple information about them, namely
        - A simple incrementing id
        - A username
        - The users full name
        - An email address
        - A phone number
        - A score based on health factors
        - A password
        - If they've been vaccinated
    All of this information is required
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    fullname = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(30), unique=True, nullable=False)
    score = db.Column(db.Float, unique=False, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    has_been_vaccinated = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.Date, default=datetime.datetime.now)

def create_vaccinee(username: str, fullname: str, email: str, phone: str, score: float, password: str) -> bool:
    '''Create vaccinee creates a vaccinee and stores them in the database,
    note that the password will be hashed using db's hashing function.

    Returns true on success and false on failure.
    '''

    # TODO: Hash the password
    hashed_password = password

    # Creates the new vaccinee
    new_user = Vaccinee(username=username, fullname=fullname, email=email, phone=phone, score=score, password=hashed_password)

    # Push changes to database
    try:
        db.session.add(new_user)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def get_user_by_username(username: str) -> Vaccinee:
    '''Select a user based on their username'''
    user = Vaccinee.query.filter_by(username=username).first()
    return user

def delete_user(username: str) -> bool:
    '''Delete a user by finding them with thier username (if they exist) and
    issuing a delete query.

    Returns true on success and false on failure.
    '''
    user = Vaccinee.query.filter_by(username=username).first()
    if user is None:
        return False
    else:
        try:
            db.session.delete(user)
            db.session.commit()
            return True
        except:
            db.session.rollback()
            return False

def generate_call_list(n: int) -> Optional[List[Vaccinee]]:
    '''Returns the n highest scoring users, marking them as being called.

    Returns None if there are any errors.
    '''
    users = Vaccinee.query.filter_by(has_been_vaccinated=False
            ).order_by(Vaccinee.score.desc(), Vaccinee.date_created
            ).limit(n).all()

    for user in users:
        user.has_been_vaccinated=True

    try:
        db.session.commit()
    except:
        return None

    return users


def debug_get_all_users() -> list:
    '''Get all users returns a list of all of the registered users. Useful for
    debugging.

    Don't use this in production.
    '''
    return Vaccinee.query.all()

