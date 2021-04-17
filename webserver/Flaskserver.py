"""
CIS 422 Project 1: Vaccination System
Group 1: Alex Anderson, Hans Prieto, Vince Qiu, Colton Trebbien, Michael Wiltshire

This file Supports the Server Framework
"""

import flask

app = flask.Flask(__name__)

@app.route("/")
def Home():
	return flask.render_template("Reg.html")

@app.route("/", methods = ["POST", "GET"])
def RegistrationPage():
	#Registration page
	
	#Get the required Fields From the html file 
	first = flask.request.form["First_Name"]
	last = flask.request.form["Last_Name"]
	email = flask.request.form["Email"]
	phone = flask.request.form["Phone"]
	other = flask.request.form["OTHER"]

	print(f"{first},{last},{email},{phone},{other}")  #debug



	#with check boxes if there are multiple, we need to get the list
	checklist = flask.request.form.getlist("Checkboxes")
	radios = flask.request.form.getlist("Radios")
	color = flask.request.form.getlist("Color")

	#More Debug
	print(f"Checklist: {checklist}")
	print(f"Radios {radios}")
	print(f"Color:  {color}") 

	#calculate socre here
	#
	#


	return flask.render_template("success.html",
		First = first, Last = last, Email = email, Phone = phone, OTHER = other,
		Checklist = checklist, Radios = radios, Color = color)


	#calcut;ate socre here
	


if __name__ == "__main__":
	app.run()
