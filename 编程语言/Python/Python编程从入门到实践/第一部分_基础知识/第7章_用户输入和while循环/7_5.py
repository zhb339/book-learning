exit_flag = False

while (exit_flag == False):
	age = input("Enter you age (enter 0 to exit): ")
	age = int(age)
	if (age <= 0):
		break;
	elif (age < 3):
		print("The price is free")
	elif (age <= 12):
		print("The price is 10 dollars")
	else:
		print("The price is 15 dollars")	
