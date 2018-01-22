class Survey():
	'''collect anonymous answers to a question'''
	
	def __init__(self,question):
		'''Store a question and also prepare to store the responses'''
		
		self.question = question
		self.responses = []
		
	def show_question(self):
		'''show the survey question'''
		print(self.question)
		
	def store_response(self,new_response):
		'''store a single response to the esurvey'''
		self.responses.append(new_response)
		
	def show_result(self):
		'''show all the responses that have been given'''
		print('SURVEY RESULTS : ')
		
		for self.response in self.responses:
			'''print the responses that have been given'''
			print('-' + self.response)
