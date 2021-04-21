'''
CIS 422: Project 1: Vaccination System
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This file pulls information from the database and creates spreadsheet files
marking those users as being vaccinated.
'''

# Import the database package that we need
from webserver.database import db
from flask import Flask

# Create and configure the flask application so that we can retrieve
# everything we need from our database
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webserver/database.db'
db.init_app(app)
db.create_all()

if __name__=='__main__':
    # Number of users to be queried (retrieved and updated) by the system
    num_users = -1

    while num_users < 0:
        try:
            num_users = int(input("How many vaccines did we recieve today? "))
        except:
            print("Not a valid number, please try again!")

    print(num_users)
