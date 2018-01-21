import unittest

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
	"""test for name_function.py"""
	"""this class inherit from class unittest.TestCase"""
	
	def test_first_last_name(self):
		"""test names like Mrinal Walia"""
		
		formatted_name = get_formatted_name('mrinal','walia')
		self.assertEqual(formatted_name,'Mrinal Walia')
		
	def test_first_last_middle_name(self):
		"""test names like MRinalSinghWalia"""
		
		f_name = get_formatted_name('mrinal','walia','singh')
		self.assertEqual(f_name,'Mrinal Singh Walia')
		
unittest.main()
