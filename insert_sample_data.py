'''
CIS 422: Project 1: Vaccination System
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This file inserts an arbitrary number of random records into the database.
Very useful for manual (non-automated) testing
'''

# Import the database package that we need
from webserver.database import db
from flask import Flask

# For random strings. We want to select a random character from
# the ascii characters
import random, string

# Create and configure the flask application so that we can retrieve
# everything we need from our database
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webserver/database.db'
db.init_app(app)
db.create_all()


def insert_sample_user() -> bool:
    #
    # first goal: generate a random name, something like "Alvne Lenclsake"
    #

    # Begin by setting name to a single uppercase character
    name = random.choice(string.ascii_uppercase)

    # Add somewhere between 3 and 5 lowercase characters afterwards
    for _ in range(random.randrange(3, 6)):
        name += random.choice(string.ascii_lowercase)

    # Then add a space and another uppercase character
    name += ' ' + random.choice(string.ascii_uppercase)

    # Add somewhere between 3 and 8 lowercase characters afterwards
    for _ in range(random.randrange(3, 9)):
        name += random.choice(string.ascii_lowercase)

    #
    # second goal: generate a random email, somethign like "alsdkjflkaj@asdkasd.com"
    #

    # Begin with an empty string 
    email = ''

    # Add somewhere between 5 and 15 lowercase characters afterwards
    for _ in range(random.randrange(5, 16)):
        email += random.choice(string.ascii_lowercase)

    # Add an @ symbol
    email += '@'

    # Add somewhere between 3 and 10 lowercase characters afterwards
    for _ in range(random.randrange(3, 11)):
        email += random.choice(string.ascii_lowercase)

    # Add a .com
    email += '.com'

    #
    # third goal: generate a random phone number, something like "546-345-2311"
    #
    
    # Begin with an empty string
    phone = ''

    # Add 3 numbers followed by a dash, twice
    for _ in range(2):
        for _ in range(3):
            phone += random.choice(string.digits)
        phone += '-'
    
    # Add 4 numbers to the end of the phone number
    for _ in range(4):
        phone += random.choice(string.digits)

    #
    # fourth (and final) goal: generate a random score, something in the range of 0 to 50
    #

    # Pick a number from 0 to 50 to an accuracy of .01
    # Hans, who did the score module, told me that this is the range of the score function
    score = random.randrange(5000) / 100

    # Finally, add this to the database, return the result of the operation. Note that password
    # gets left blank 
    return db.create_vaccinee(name, email, phone, score, "")


if __name__=='__main__':
    # n is the number of sample records we wish to insert into our database
    n = -1

    # Get user input. Needs to be an integer >= 0.
    while n < 0:
        try:
            n = int(input("Please enter the number of sample records you wish to insert into the database: "))
        except:
            print("Invalid number! Please enter an integer greater than or equal to 0")

    # Insert n sample users
    count = 0
    for _ in range(n):
        if insert_sample_user():
            count += 1

    print(count, "out of", n, "users inserted successfully")

