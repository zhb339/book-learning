class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
		self.number_served = 0
	def describe_restaurant(self):
		print("Restaurant name is: " + self.name)
		print("Cuisine type is: " + self.type)
	def open_restaurant(self):
		print("The restaurant is open")
	def increment_number_served(self, num):
		self.number_served += num
	
restaurant = Restaurant('shi mao', '5 star')
print(restaurant.number_served)

restaurant.increment_number_served(8)
print(restaurant.number_served)
