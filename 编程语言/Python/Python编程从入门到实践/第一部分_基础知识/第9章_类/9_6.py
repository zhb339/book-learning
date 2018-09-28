class Restaurant():
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
	def describe_restaurant(self):
		print("Restaurant name is: " + self.name)
		print("Cuisine type is: " + self.type)
	def open_restaurant(self):
		print("The restaurant is open")
		
class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type, flavors = 'chocolate'):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors
	def show_icecreams(self):
		print(self.flavors)
	
restaurant = IceCreamStand('shi mao', '5 star')
restaurant.show_icecreams()
