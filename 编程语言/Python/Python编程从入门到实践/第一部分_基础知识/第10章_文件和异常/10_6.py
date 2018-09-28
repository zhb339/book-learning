while True:
	try:
		num1 = int(input("Enter first num: "))
		num2 = int(input("Enter second num: "))
		total = num1 + num2
		print("The sum of two numbers is " + str(total) + ".")
	except:
		print("Please enter number!")
