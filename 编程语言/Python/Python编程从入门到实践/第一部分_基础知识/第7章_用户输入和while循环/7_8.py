sandwich_orders = ['aa', 'bb', 'cc']
finished_sandwiches = []
while sandwich_orders:
	sandwich = sandwich_orders.pop()
	finished_sandwiches.append(sandwich)
	print("I made your " + sandwich + " sandwich")
print("Finished all sandwiches: " + str(finished_sandwiches))
