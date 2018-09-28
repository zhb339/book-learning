class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
	def describe_restaurant(self):
		print("Restaurant name is: " + self.name)
		print("Cuisine type is: " + self.type)
	def open_restaurant(self):
		print("The restaurant is open")
	
restaurant = Restaurant('shi mao', '5 star')
print(restaurant.name)
print(restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
