"""
CIS 422 Project 1: Vaccination System
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This file Supports the Server Framework
"""

import flask
from healthscore import score
from database import db

app = flask.Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db.init_app(app)
db.create_all()

@app.route("/", methods= ["POST", "GET"])
def ServeWebpage():
	if flask.request.method == "POST":
		#if flask.request.form.get()
		return flask.redirect("/register")
	return flask.render_template("Index1.html")


@app.route("/register", methods = ["POST", "GET"])
def RegistrationUser():
	"""Once the button is pressed and the user wants to submit their data
		we request the form data

		Send data to the user score module. 
		current score module numbers mapped to meanings
			0: Heart problems
			1: diabetes
			2: lung problems
			3: liver problems
			4: cancer
			5: positive test
			6: close contact
			7: Any current symptoms
			8: feet
			9: inches
			10: weight
			11: age
		The Database List contains the info that is not needed in the calculating
		the user score
			0: Full Name
			1: Email
			2: Phone
			3: score

		These Items should be put into a list format to calculate the users score.
		"""
	if flask.request.method == "POST": #Server Recieves POST request
		try:

			ScoreList = [] #create initial list
			DatabaseList = [] #create initial database list
			ScoreList.append(flask.request.form["heart_prblms"])	#Grab Heart Problems
			ScoreList.append(flask.request.form["diabetes"])		#Grab Diabetes
			ScoreList.append(flask.request.form["lung_prblms"])		#Grab Lung Problems
			ScoreList.append(flask.request.form["liver_prblms"])	#Grab Liver Problems
			ScoreList.append(flask.request.form["cancer"])			#Grab Cancer
			ScoreList.append(flask.request.form["pos_test"])		#Grab Pre-exposed
			ScoreList.append(flask.request.form["close_contact"])	#Grab closecontact
			ScoreList.append(flask.request.form["symptoms"])		#Grab Symptoms
			ScoreList.append(flask.request.form["heightft"])		#Grab Height in feet
			ScoreList.append(flask.request.form["heightin"])		#Grab Height in inches
			ScoreList.append(flask.request.form["weight"])			#Grab Weight
			ScoreList.append(flask.request.form["age"])				#Grab the Age
			#For the Database List
			DatabaseList.append(flask.request.form["fname"])		#Grab The Full Name
			DatabaseList.append(flask.request.form["email"])		#Grab the Email
			DatabaseList.append(flask.request.form["phone"])		#Grab Phone Number
			
			#Uncomment these out for debug
			print(f"THE SCORE LIST: {ScoreList}")
			print(f"THE DATABASE LIST {DatabaseList}")
			
			#Calculate the score
			UserScore = score.calculate_score(ScoreList) #Calculate the Score
			print(f"User_Score:{UserScore}")			 #Uncomment For Debug

			#Create user in database
			Password = "dummy_password"

			#send vaccinee data to the database, If it fails redirect to /failure.
			if(db.create_vaccinee(DatabaseList[0], DatabaseList[1], DatabaseList[2], UserScore, Password) == False):
				print("Database creation Failed")
				return flask.redirect("/failure")


			print("looking at the database list:\n")
			print(db.debug_get_all_users())

			print("redirecting to success\n")
			return flask.redirect("/success")
				#First = first, Last = last, Email = email, Phone = phone, OTHER = other,
				#Checklist = checklist, Radios = radios, Color = color)
		except:
			return flask.redirect("/notfilled")
	return flask.render_template("Index2.html")

@app.route("/success", methods = ["POST", "GET"])
def Success():
	#print("I got HeRE\n")
	return flask.render_template("Index3.html")

@app.route("/failure", methods = ["POST", "GET"])
def Failure():
	return flask.render_template("Index5.html")

@app.route("/notfilled", methods = ["POST", "GET"])
def notfilled():
	return flask.render_template("Index6.html")

if __name__ == "__main__":
	app.run()
