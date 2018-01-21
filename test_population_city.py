import unittest

from population import population

class cityTestCase(unittest.TestCase):
	'''your class should inherit from the class" unittest.TestCase " '''
	
	def test_city_country(self):
		
		name = population('city','country')
		self.assertEqual(name,"Ddn,India")
		
	def test_city_country_population(self):
	
		name = population('city','country','population')
		self.assertEqual(name,'Ddn,India-population 1551') 
		
unittest.main()

