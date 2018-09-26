toppings = []

exit_flag = False
while (exit_flag == False):
	topping = input("Please enter what you want add to you pizza(enter quit to exit): ")
	if (topping != 'quit'):
		print("We will add " + topping + " to your pizza!")
		toppings.append(topping)
	else:
		print("Now you pizza contains: " + str(toppings) + "!")
		exit_flag = True
