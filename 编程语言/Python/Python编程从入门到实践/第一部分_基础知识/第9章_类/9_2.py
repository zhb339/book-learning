class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
	def describe_restaurant(self):
		print("Restaurant name is: " + self.name)
		print("Cuisine type is: " + self.type)
	def open_restaurant(self):
		print("The restaurant is open")
	
restaurant1 = Restaurant('shi mao', '5 star')
restaurant1.describe_restaurant()
restaurant2 = Restaurant('xianggelila', '6 star')
restaurant2.describe_restaurant()
restaurant3 = Restaurant('7 day', '1 star')
restaurant3.describe_restaurant()
