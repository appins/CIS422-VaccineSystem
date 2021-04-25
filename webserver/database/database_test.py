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
		self.assertEqual(db.create_vaccinee("Hi Hello", "hello@hi.hey",
												1234567890, 7777, "password123"),True)
		#checks if you can create user with same full name
		self.assertEqual(db.create_vaccinee("Hi Hello", "hey@hi.hey",
						   				1234567891, 1111, "password123"), True)

		#check delete user
		db.create_vaccinee("Hey Hello", "hey@hi.hey",
						   1234567891, 1111, "password123")
		self.assertTrue(db.delete_user("hey@hi.hey"))
		self.assertTrue(db.delete_user("hello@hi.hey"))
		self.assertEqual(len(db.debug_get_all_users()), 0)

	def test_get_user(self):
		#checks get user
		db.create_vaccinee("Hi Hello", "hello@hi.hey",
						   1234567890, 7777, "password123")
		db.create_vaccinee("Hey Hello", "hey@hi.hey",
						   1234567891, 1111, "password123")

		self.assertEqual(str(db.get_user_by_email("hello@hi.hey")),"<Vaccinee 1>")
		self.assertEqual(str(db.get_user_by_email("hey@hi.hey")),"<Vaccinee 2>")
		self.assertEqual(len(db.debug_get_all_users()), 2)
		print("here:",db.debug_get_all_users())
		self.assertTrue(db.delete_user("hey@hi.hey"))
		self.assertEqual(str(db.get_user_by_email("hey@hi.hey")), "None")
		self.assertTrue(db.delete_user("hello@hi.hey"))
		self.assertEqual(str(db.get_user_by_email("hello@hi.hey")), "None")
		self.assertEqual(len(db.debug_get_all_users()), 0)
	def test_duplicates(self):
		db.create_vaccinee("Hi Hello", "hello@hi.hey",
							1234567891, 7777, "password123")

		#check duplicate email
		self.assertFalse(db.create_vaccinee("Henlo Hoi", "hello@hi.hey",
											1234567892, 7777, "password123"))

        # Check duplicate phone number
		self.assertFalse(db.create_vaccinee("Henlo Hoi", "heyo@hi.hey",
											1234567891, 7777, "password123"))

		self.assertEqual(len(db.debug_get_all_users()), 1)
		self.assertTrue(db.delete_user("hello@hi.hey"))
		self.assertEqual(len(db.debug_get_all_users()), 0)

	def test_scores(self):
		#checks to see if you can create users with different scores,
		#and checks highest score is returned first
		db.create_vaccinee("Hi Hello", "hello@hi.hey",
						   1234567890, 2222, "password123")
		db.create_vaccinee("Hey Hello", "hey@hi.hey",
						   1234567891, 1111, "password123")
		db.create_vaccinee("Hola Hello", "hola@hi.hey",
						   1234567892, 9999, "password123")

		self.assertEqual(str(db.generate_call_list(1)),"[<Vaccinee 3>]")
		self.assertTrue(db.delete_user("hola@hi.hey"))
		self.assertEqual(str(db.generate_call_list(1)),"[<Vaccinee 1>]")
		self.assertTrue(db.delete_user("hello@hi.hey"))
		self.assertTrue(db.delete_user("hey@hi.hey"))
		self.assertEqual(len(db.debug_get_all_users()), 0)

if __name__ == '__main__':
	unittest.main()
