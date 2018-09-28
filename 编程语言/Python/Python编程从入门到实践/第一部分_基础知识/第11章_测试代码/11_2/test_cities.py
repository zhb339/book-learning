import unittest
from city_functions import get_location

class CityTest(unittest.TestCase):
	def test_city_country(self):
		location = get_location("hangzhou", "china")
		self.assertEqual(location, "hangzhou, china - population " + str(999))
	def test_city_country_population(self):
		location = get_location("hangzhou", "china", 666)
		self.assertEqual(location, "hangzhou, china - population 666")	
unittest.main()
