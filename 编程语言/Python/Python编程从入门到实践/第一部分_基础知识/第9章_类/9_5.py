class User():
	def __init__(self, first_name, last_name):
		self.first = first_name
		self.last = last_name
		self.login_attempts = 0
	def describe_user(self):
		print("First name: " + self.first)
		print("Last name: " + self.last)
	def greet_user(self):
		print("Welcome " + self.first + " " + self.last + "!")
	def increment_login_attempts(self):
		self.login_attempts += 1
	def reset_login_attempts(self):
		self.login_attempts = 0 

user = User("zheng", "hongbo")
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.increment_login_attempts()
print(user.login_attempts)
user.reset_login_attempts()
print(user.login_attempts)
