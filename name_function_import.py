from name_function import get_formatted_name

print('Enter "q" to exit the program at anytime')

while True:
	
	first = input('Enter your first name:')
	if first == 'q':
		break
		
	middle = input('Enter your middle name:')
	if middle == 'q':
		break	
		
	last = input('Enter your last name:')
	if last == 'q':
		break

	print(get_formatted_name(first,last,middle))
