import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
	
	def test_give_default_raise(self):
		man = Employee('abhi','walia',5000)
		man.give_raise(5000)
		self.assertIn(5000,self.salary)
		
unittest.main()
		
