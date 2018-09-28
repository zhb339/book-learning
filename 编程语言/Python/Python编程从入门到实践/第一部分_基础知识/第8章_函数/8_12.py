def make_sandwich(*toppings):
	print("The sandwich contains:")
	for topping in toppings:
		print(topping)
	print()
	
make_sandwich('meat')

make_sandwich('egg', 'fish')

make_sandwich('straw berry', 'orange', 'apple')
