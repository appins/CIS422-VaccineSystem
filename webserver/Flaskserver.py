"""
PUT THE DOC STUFF HERE
"""
import flask

app = flask.Flask(__name__)

@app.route("/")
def Home():
	return "Hello This is a test page <h1>HELLO<h1>"

if __name__ == "__main__":
	app.run()
