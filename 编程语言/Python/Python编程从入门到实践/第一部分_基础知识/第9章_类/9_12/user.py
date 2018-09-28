class User():
	def __init__(self, first_name, last_name):
		self.first = first_name
		self.last = last_name
	def describe_user(self):
		print("First name: " + self.first)
		print("Last name: " + self.last)
	def greet_user(self):
		print("Welcome " + self.first + " " + self.last + "!")

