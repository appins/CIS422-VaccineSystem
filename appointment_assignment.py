'''
CIS 422: Project 1: Vaccination System
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This file pulls information from the database and creates spreadsheet files
marking those users as being vaccinated.
'''

# Import the database package that we need
from webserver.database import db
from flask import Flask

# Import the sys package for argv
import sys

# Import os for os.exit
import os

import csv
from io import StringIO

def write_call_list(filename, number):
    """write call list creates a csv file with the vaccinee information
    It takes the name of the file to be opened and the number of vaccines wished
    to be taken from the database.

    """

    vaccinees = db.generate_call_list(num_users)
    with open(output_filename, mode='w') as csv_file:
        fieldnames = ['Full name', 'Phone', 'Email', 'Score']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for vaccinee in vaccinees:
            writer.writerow({'Full name': vaccinee.fullname, "Phone": vaccinee.phone, "Email": vaccinee.email, "Score": vaccinee.score})



# Create and configure the flask application so that we can retrieve
# everything we need from our database
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webserver/database.db'
db.init_app(app)
db.create_all()

if __name__=='__main__':
    # Store the filename where we plan on putting this data. If there is no
    # filename specified (argv does not contain one), we write to call_list.csv
    output_filename = 'call_list.csv'

    # We overwrite that filename if one is in argv. If there are too many
    # arguments we exit the program.
    if len(sys.argv) == 2: # that is, exactly 1 argument
        #Incase the user tries to overwrite any python module.
        suffix = ".csv"
        if (sys.argv[1].endswith(suffix) != True):
            print("invalid file type (csv only)\n")
            exit(1)

        output_filename = sys.argv[1]
    elif len(sys.argv) > 2: # that is, more than 1 argument
        print("Usage: python3 appointment_assignment.py [FILE]")
        exit(1)
    else: # that is, no arugments
        # When no arguments given we print a message explaining how to change
        # the output file
        print(f"NOTE: Writting to {output_filename}, this can be overwritten by")
        print("specifying an argument to ")

    # Number of users to be queried (retrieved and updated) by the system
    num_users = -1

    print("NOTE: Running this file will overwrite the previous CSV sheets")
    

    # Try to get a number from users until they give an actual number
    while num_users < 0:
        # Do this with a try/except block
        try:
            num_users = int(input("How many vaccines did we recieve today? "))
        except:
            print("Not a valid number, please try again!")

    # Holds the vaccinees that are to be put in the call list
    # Print to the vaccine output file in csv format
    write_call_list(output_filename,num_users)


       

 
   






 


    
