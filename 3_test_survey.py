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
		
	def test_store_three_response(self):
		"""test that three responses is stored """
		question = "waht language did you learn ?"
		my_survey = Survey(question)
		#store the responses in a list
		responses = ['English','Hindi','Punjabi']
		
		for response in responses:
			my_survey.store_response(response)
			
		for response in responses:
			self.assertIn(response,my_survey.responses)
		
unittest.main()

