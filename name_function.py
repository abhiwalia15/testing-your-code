def get_formatted_name(first,last,middle=''):
	"""get a full name of the user"""
	if middle:
		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' ' + last
	return full_name.title()
	
	
	
	
