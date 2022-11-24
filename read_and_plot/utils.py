import re

def format_data(country):
	population = {key[0:4]:int(country[key]) for key in country if re.match("\d{4} Population", key)}
	population = dict(sorted(population.items()))
	return population.keys(), population.values()

def get_population_by_country(data, country):
	result = list(filter(lambda item: item["Country/Territory"] == country, data))
	return result
