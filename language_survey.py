from survey import Survey

#define a question and make a survey.

questions = "Which language did you learn first?"

my_survey = Survey(questions)

#show the question.
my_survey.show_question()

#store the responses in the list 
print("Enter 'q' to quit.\n")

while True:
	responses = input('Language:')
	if responses == 'q':
		break
		
	my_survey.store_response(responses)
	
#show the survey result.
print('Thank you every one who participiated in the survey.\n')

my_survey.show_result()

