from db import db
from contact import Contact

class ContactDAO:
	"""Contact data access object"""

	def __init__(self):
		"""Class constructor"""
		pass

	def create(self, contact):
		"""Validate current object state"""
		result = False

		con = db()
		query = 'INSERT INTO contact (firstname, lastname, email, address, phone) VALUES (?, ?, ?, ?, ?);'
		params = [contact.firstName, contact.lastName, contact.email, contact.address, contact.phone]
		result = con.executeSQL(query, params)

		return result