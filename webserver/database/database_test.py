import db
import unittest
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
db.create_all()

class T1_users(unittest.TestCase):

		def test_create_user(self):
				print("check user")
				v = db.Vaccinee()
				v.create_vaccinee()
				self.assertEqual(v.id,True)
				self.assertEqual(v.username, True)
				self.assertEqual(v.fullname, True)
				self.assertEqual(v.email, True)
				self.assertEqual(v.phone, True)
				self.assertEqual(v.id, True)
				self.assertEqual(v.id, True)
		def test_delete_user(self):
				pass

