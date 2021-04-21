import db
import unittest
from flask import Flask
import migrate
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate.hard_reset()

class T1_users(unittest.TestCase):

		def test_create__get_delete_user(self):
				print("check user")
				#checks create user
				self.assertEqual(db.create_vaccinee("hi", "Hi Hello", "hello@hi.hey",
														1234567890, 7777, "password123"),True)
				#checks get user
				self.assertIsNotNone(db.get_user_by_username("hi"))
				self.assertEqual(len(db.debug_get_all_users()), 1)

				#check delete user
				self.assertTrue(db.delete_user("hi"))
				self.assertEqual(len(db.debug_get_all_users()), 0)

		def test_duplicates(self):
			db.create_vaccinee("hi", "Hi Hello", "hello@hi.hey",
									1234567890, 7777, "password123")

			#check duplicate username
			self.assertFalse(db.create_vaccinee("hi", "Hello", "Hola@hi.hey",
									1234567891, 7777, "password123"))

			#check duplicate email
			self.assertFalse(db.create_vaccinee("Hoi", "Henlo Hoi", "hello@hi.hey",
												1234567892, 7777, "password123"))

			self.assertFalse(db.create_vaccinee("eyyy", "Henlo Hoi", "heyo@hi.hey",
												1234567890, 7777, "password123"))

			self.assertEqual(len(db.debug_get_all_users()), 1)




if __name__ == '__main__':
    unittest.main()