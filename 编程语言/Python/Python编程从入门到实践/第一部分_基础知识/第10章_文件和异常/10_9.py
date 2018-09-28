def read_txt(filename):
	try:
		with open(filename) as txtobj:
			for line in txtobj:
				print(line.strip())
	except FileNotFoundError:
		#print(filename + " not found!")
		pass
		

read_txt("dog1s.txt")
print()
read_txt("cats.txt")
