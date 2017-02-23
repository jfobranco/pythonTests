class Contact:
	"""Contact class"""

	lastName = ''
	firstName = ''
	phone = ''
	address = ''
	email = ''
	errors = None

	def __init__(self, firstName='', lastName='', phone='', address='', email=''):
		"""Class constructor"""

		self.lastName = lastName
		self.firstName = firstName
		self.phone = phone
		self.address = address
		self.email = email
		self.errors = { firstName:'', lastName:'', phone:'', address:'', email:''}

	@property
	def errors(self):
		return self.errors

	@errors.setter
	def errors(self, v):
		self.errors  =  v

	@property
	def lastName(self):
		return self.lastName

	@lastName.setter
	def lastName(self, v):
		self.lastName  =  v

	@property
	def firstName(self):
		return self.firstName

	@firstName.setter
	def firstName(self, v):
		self.firstName  =  v

	@property
	def phone(self):
		return self.phone

	@phone.setter
	def phone(self, v):
		self.phone  =  v

	@property
	def address(self):
		return self.address

	@address.setter
	def address(self, v):
		self.address  =  v

	@property
	def email(self):
		return self.email

	@email.setter
	def email(self, v):
		self.email  =  v

	def validate(self):
		"""Validate current object state"""
		error = False
		if (not self.firstName):
			self.errors["firstName"] = "First name is required"
			error = True
		else:
			self.firstName = self.test_input(self.firstName)

		if (not self.lastName):
			self.errors["lastName"] = "Last name is required"
			error = True
		else:
			self.lastName = self.test_input(self.lastName)

		if (not self.email):
			self.errors["email"] = "Mail is required"
			error = True
		elif self.validateMail(self.email) == False:
			self.errors["email"] = "Wrong mail format for " . self.email
			error = True
		else:
			self.email = self.test_input(self.email)

		if (self.address and len(self.address) < 5):
			self.errors["address"] = "Address must be at least 5 characters"
			error = True
		else:
			self.address = self.test_input(self.address);

		if (self.phone and len(self.phone) < 5):
			self.errors["phone"] = "Phone must be at least 5 characters"
			error = True
		else:
			self.phone = self.test_input(self.phone)

		return error

	def validateMail(self, mail):
		return True

	def test_input(self, data):
		#data = trim(data)
		#data = stripslashes(data)
		#data = htmlspecialchars(data)

		return data