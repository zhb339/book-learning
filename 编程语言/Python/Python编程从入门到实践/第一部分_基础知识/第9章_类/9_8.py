class User():
	def __init__(self, first_name, last_name):
		self.first = first_name
		self.last = last_name
	def describe_user(self):
		print("First name: " + self.first)
		print("Last name: " + self.last)
	def greet_user(self):
		print("Welcome " + self.first + " " + self.last + "!")
class Privileges():
	def __init__(self, privileges = "boss"):
		self.privileges = privileges
	def show_privileges(self):
		print(self.privileges)	
class Admin(User):
	def __init__(self, first_name, last_name, privileges = 'master'):
		super().__init__(first_name, last_name)
		self.privileges = Privileges(privileges)
		
admin = Admin('zheng', 'hongbo')
admin.privileges.show_privileges()
