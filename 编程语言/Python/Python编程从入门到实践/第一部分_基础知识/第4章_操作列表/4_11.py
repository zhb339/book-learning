pizzas = ['pazza hut', 'magrita', 'sabel']
for pizza in pizzas:
	print("I like " + pizza)

print("I very like pizza, the most is " + pizzas[0])

friend_pizzas = pizzas[:]
pizzas.append('my_pizza')
friend_pizzas.append('feiend')

print("My favorate pizza:")
for pizza in pizzas:
	print(pizza)
	
print("Friend favorate pizza:")	
for pizza in friend_pizzas:	
	print(pizza)
