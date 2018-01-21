def population(city,country,population=' '):
	"""input a city and the country you are living in"""
	
	if population:
		
		pops = city + ',' + country + '- population ' + str(population)
	
	else:
	
		pops = city + ',' + country 
			
	return pops.title()
	
name = population('ddn','india',1551)
print(name)

