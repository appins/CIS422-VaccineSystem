'''
CIS 422 Project 1: Vaccination System
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This file does all migrations needed to create the datbase
'''

import db

# If an app exists, we use it to work with the database, otherwise, we
# create one and use that one instead
if 'app' in locals():
    db.init_app(app)
else:
    db.setup_headless()

def hard_reset():
    '''Hard reset completely resets the database.'''

    # Ask the user and make sure they know what they're doing
    # ans = input("Deleting all information from the database. Continue? ([no]/yes): ")

    # If they say yes, completely reset the database
    # if ans == "yes":
    if "yes" == "yes":
        db.db.drop_all()
        db.db.create_all()

def create_all():
    '''Create all updates and creates the database tables'''
    db.db.create_all()

def drop_all(confirm: str):
    '''Drops all database tables. Must be passed the string yes to proceed'''
    if confirm == "yes":
        db.db.drop_all()

# Whenever this file is run, we create all of the tables needed
if __name__=='__main__':
    db.db.create_all()

