import unittest
from employee import Employee

class EmployTest(unittest.TestCase):
	def setUp(self):
		self.employee = Employee('hongbo', 'zheng', 989900)
	def test_give_default_raise(self):
		self.employee.give_raise()
		self.assertEqual(self.employee.salary, 989900 + 5000)
	def test_give_custom_raise(self):
		self.employee.give_raise(66666)
		self.assertEqual(self.employee.salary, 989900 + 66666)
unittest.main()
