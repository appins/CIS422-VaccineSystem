'''
CIS 422 Project 1: Vaccination System
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This file allows interfacing with the raw SQLite data via a Python import
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://database.db'
db = SQLAlchemy(app)

class Vaccinee(db.Model):
    '''Vaccinee is a person who wishes to be vaccinated.

    They have some simple information about them, namely
        - A simple incrementing id
        - A username
        - An email address
        - A phone number
        - A score based on health factors
        - A password
    All of this information is required
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(30), unique=True, nullable=False)
    score = db.Column(db.Float, unique=False, nullable=False)
    password = db.Column(db.String(100), nullable=False)



