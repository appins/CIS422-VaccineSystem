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
        - The users full name
        - An email address
        - A phone number
        - A score based on health factors
        - A password
        - If they've been vaccinated
        - And a date on which the user registered (auto-generated)
    All of this information is required
    '''
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(30), unique=True, nullable=False)
    score = db.Column(db.Float, unique=False, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    has_been_vaccinated = db.Column(db.Boolean, default=False)
    date_created = db.Column(db.Date, default=datetime.datetime.now)

def create_vaccinee(fullname: str, email: str, phone: str, score: float, password: str) -> bool:
    '''Create vaccinee creates a vaccinee and stores them in the database,
    note that the password will be hashed using db's hashing function.

    Returns true on success and false on failure.
    '''

    # TODO: Hash the password
    hashed_password = password

    # Creates the new vaccinee
    new_user = Vaccinee(fullname=fullname, email=email, phone=phone, score=score, password=hashed_password)

    # Push changes to database
    try:
        db.session.add(new_user)
        db.session.commit()
        return True
    except:
        db.session.rollback()
        return False

def get_user_by_email(email: str) -> Vaccinee:
    '''Select a user based on their email'''
    
    # Search for a user by their email, return only the first result
    # (should be the only result due to unique keys)
    user = Vaccinee.query.filter_by(email=email).first()

    return user

def delete_user(email: str) -> bool:
    '''Delete a user by finding them with thier email (if they exist) and
    issuing a delete query.

    Returns true on success and false on failure.
    '''

    # We start by finding the user
    user = Vaccinee.query.filter_by(email=email).first()

    if user is None:
        # In the case that there is no user by that email, we return false
        # as it was a failure
        return False
    else:
        # If we could find a user, we attempt to delete them
        try:
            # if it works we return true
            db.session.delete(user)
            db.session.commit()
            return True
        except:
            # If there was some sort of error we return false. No
            # need to completely halt the server, however, because
            # there could be a good reason (such as write-protection)
            db.session.rollback()
            return False

def generate_call_list(n: int) -> Optional[List[Vaccinee]]:
    '''Returns the n highest scoring users, marking them as being called.

    Returns None if there are any errors.
    '''

    # We select the first n users, sorted by health risk score (highest first)
    # and then by date. 
    users = Vaccinee.query.filter_by(has_been_vaccinated=False) \
            .order_by(Vaccinee.score.desc(), Vaccinee.date_created) \
            .limit(n).all()

    # Set all of the users as being vaccinated
    for user in users:
        user.has_been_vaccinated=True
    try:
        # Commit the changes (that is, store that these users have been vaccinated)
        db.session.commit()
    except:
        # If we fail to commit these changes, rollback (in order to not halt webserver
        # operation.
        db.session.rollback()
        return None

    return users

def debug_get_all_users() -> list:
    '''Get all users returns a list of all of the registered users. Useful for
    debugging.

    Don't use this in production. It queries the whole database and therefore
    could crash the server if it gets called on a huge database.
    '''

    # Search for all vaccinees, vaccinated or unvaccinated, and return them.
    # particularly useful in testing.
    return Vaccinee.query.all()

