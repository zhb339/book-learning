import json

try:
	with open('num.txt') as fobj:
		print("I know your favorite number! It's " + str(json.load(fobj)))
except FileNotFoundError:
	num = int(input("Enter your favorite num: "))
	with open("num.txt", 'w') as fobj:
		json.dump(num, fobj)
