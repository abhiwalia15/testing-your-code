import unittest

from city_functions import *

class cityTestCase(unittest.TestCase):
	'''your class should inherit from the class" unittest.TestCase " '''
	
	def test_city_country(self):
		
		name = city_function('city','country')
		self.assertEqual(name,"Bangalore,India")
		
unittest.main()
