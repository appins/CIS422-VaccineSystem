'''
CIS 422 Project 1: Vaccination System
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This file does all migrations needed to create the datbase
'''

from db import db

def hard_reset():
    '''Hard reset completely resets the database.'''

    # Ask the user and make sure they know what they're doing
    ans = input("Deleting all information from the database. Continue? ([no]/yes): ")

    # If they say yes, completely reset the database
    if ans == "yes":
        db.drop_all()
        db.create_all()

# Whenever this file is run, we create all of the tables needed
if __name__=='__main__':
    db.create_all()


