class Car():
	def __init__(self, car_type):
		self.car_type = car_type
		
class Battery():
	def __init__(self, vol = 75):
		self.battery = vol	
	def get_range(self):
		if (self.battery <= 75):
			print("The range is 233")
		else:
			print("The range is 999")
	def upgrade_battery(self):
		self.battery = 85	
		
class Eleccar(Car):
	def __init__(self, car_type, battery_level = 75):
		super().__init__(car_type)
		self.battery = Battery(battery_level)
eleccar = Eleccar('Fox')
eleccar.battery.get_range()
eleccar.battery.upgrade_battery()
eleccar.battery.get_range()
