from user import User

class Privileges():
	def __init__(self, privileges = "boss"):
		self.privileges = privileges
	def show_privileges(self):
		print(self.privileges)	
class Admin(User):
	def __init__(self, first_name, last_name, privileges = 'master'):
		super().__init__(first_name, last_name)
		self.privileges = Privileges(privileges)
		

