def get_population_by_year(country):
	country_pop = list(filter(lambda item: item.keys() == "/^\d{4} Population/", country))
	return country_pop

def get_population_by_country(data, country, field):
	result = list(filter(lambda item: item[field] == country, data))
	return result
