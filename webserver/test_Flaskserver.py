
import unittest
import flask
from healthscore import score
from database import db
import requests

app = flask.Flask(__name__)
testapp = app.test_client()


s = requests.session()

payload = {
	'fullname': 'John Doe'
}

#default register
response = s.post("http://127.0.0.1:5000/register")
print(response.content)



"""
class Test_test(unittest.TestCase):
    def test_user_registration_bad_password_short(self):
        response = self.register(name='pat',
                                 email='me@mail.com', 
                                 password='Flask', 
                                 password2='Flask')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'password should be 8 or more characters long', 
                      response.data)

    def register(self, name, email, password, password2):
        return testapp.post(
            '/register',
            data=dict(username=name, 
                      email=email, 
                      password=password, 
                      password2=password2),
            follow_redirects=True
        )
"""
if __name__ == '__main__':
    unittest.main()