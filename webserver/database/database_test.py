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

	def test_create_delete_user(self):
		print("check user")
		#checks create user
		self.assertEqual(db.create_vaccinee("hi", "Hi Hello", "hello@hi.hey",
												1234567890, 7777, "password123"),True)
		#checks if you can create user with same full name
		self.assertEqual(db.create_vaccinee("hey", "Hi Hello", "hey@hi.hey",
						   				1234567891, 1111, "password123"), True)

		#check delete user
		db.create_vaccinee("hey", "Hey Hello", "hey@hi.hey",
						   1234567891, 1111, "password123")
		self.assertTrue(db.delete_user("hi"))
		self.assertTrue(db.delete_user("hey"))
		self.assertEqual(len(db.debug_get_all_users()), 0)

	def test_get_user(self):
		#checks get user
		db.create_vaccinee("hi", "Hi Hello", "hello@hi.hey",
						   1234567890, 7777, "password123")
		db.create_vaccinee("hey", "Hey Hello", "hey@hi.hey",
						   1234567891, 1111, "password123")

		self.assertEqual(str(db.get_user_by_username("hi")),"<Vaccinee 1>")
		self.assertEqual(str(db.get_user_by_username("hey")),"<Vaccinee 2>")
		self.assertEqual(len(db.debug_get_all_users()), 2)
		print("here:",db.debug_get_all_users())
		self.assertTrue(db.delete_user("hi"))
		self.assertEqual(str(db.get_user_by_username("hi")), "None")
		self.assertTrue(db.delete_user("hey"))
		self.assertEqual(str(db.get_user_by_username("hey")), "None")
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
		self.assertTrue(db.delete_user("hi"))
		self.assertEqual(len(db.debug_get_all_users()), 0)

	def test_scores(self):
		#checks to see if you can create users with different scores,
		#and checks highest score is returned first
		db.create_vaccinee("hi", "Hi Hello", "hello@hi.hey",
						   1234567890, 2222, "password123")
		db.create_vaccinee("hey", "Hey Hello", "hey@hi.hey",
						   1234567891, 1111, "password123")
		db.create_vaccinee("hola", "Hola Hello", "hola@hi.hey",
						   1234567892, 9999, "password123")

		self.assertEqual(str(db.generate_call_list(1)),"[<Vaccinee 3>]")
		self.assertTrue(db.delete_user("hola"))
		self.assertEqual(str(db.generate_call_list(1)),"[<Vaccinee 1>]")
		self.assertTrue(db.delete_user("hi"))
		self.assertTrue(db.delete_user("hey"))
		self.assertEqual(len(db.debug_get_all_users()), 0)
if __name__ == '__main__':
    unittest.main()