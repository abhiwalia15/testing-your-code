import unittest

from survey import Survey

class TestSurvey(unittest.TestCase):
	"""test for the class survey"""
	
	def test_store_single_response(self):
		"""test that a single response is stored properly"""
		question = ("Which language did you learn first to speak?")
		my_survey = Survey(question)
		my_survey.store_response('English')
		self.assertIn('English',my_survey.responses)
		
unittest.main()
