import unittest
from city_functions import get_location

class CityTest(unittest.TestCase):
	def test_city_country(self):
		location = get_location("hangzhou", "china")
		self.assertEqual(location, "hangzhou, china")
		
unittest.main()
