import json

try:
	with open('remberme.txt') as fobj:
		name = input("Enter your name: ")
		user = str(json.load(fobj))
		if user != name:
			print("user error!")
		else:
			print("Welcome back " + user)
except FileNotFoundError:
	name = input("Enter your name: ")
	with open('remberme.txt', 'w') as fobj:
		json.dump(name, fobj)
