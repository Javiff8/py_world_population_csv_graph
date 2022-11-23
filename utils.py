def get_population_by_year(country):
	population = filter(lambda item: item[0] == "2022 Population", list(country.items()))
	print(dict(population))
	return population

def get_population_by_country(data, country, field):
	result = list(filter(lambda item: item[field] == country, data))
	return result
