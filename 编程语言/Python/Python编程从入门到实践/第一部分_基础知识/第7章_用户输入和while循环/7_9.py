sandwich_orders = ['aa', 'bb', 'pastrami', 'cc', 'pastrami', 'pastrami']
finished_sandwiches = []
print("pastrami is sold out")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	finished_sandwiches.append(sandwich)
	print("I made your " + sandwich + " sandwich")
print("Finished all sandwiches: " + str(finished_sandwiches))
