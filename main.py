import sys
import os
import read_and_plot.charts as charts
import read_and_plot.utils as utils
import read_and_plot.read_file as readFile

def world_percentaje(data):
	continent = input("Select a continent to filter data or leave blank to plot everything -> ").capitalize()
	if (continent):
		data = list(filter(lambda item: item["Continent"] == continent, data))
		if not(data):
			print(f"The continent you indicated: '{continent}', is not in the file.")
			exit()
	labels = list(map(lambda item: item["Country/Territory"], data))
	values = list(map(lambda item: item["World Population Percentage"], data))
	charts.pie_chart(labels, values)

def country_population(data):
	selected_country = input("Input the full name of the country to plot -> ").capitalize()
	country = utils.get_population_by_country(data, selected_country)
	if country:
		labels, values = utils.format_data(country[0])
		if labels and values:
			charts.bar_chart(labels, values)
		else:
			print(f"The country you indicated: '{selected_country}', has no population data.")
	else:
		print(f"The country you indicated: '{selected_country}', is not in the file.")

def plot_data(data, input_check):
	if input_check == "world":
		world_percentaje(data)
	elif not(input_check):
		country_population(data)
	else:
		print(f"Invalid input: '{input_check}', please, run the program again.")

def run():
	if len(sys.argv) > 1:
		path = sys.argv[1]
	else:
		path = input("Indicate the path to the csv file you want to read --> ")
	if os.path.exists(path):
		data = readFile.read_csv(path)
		input_check = input("If you want to plot the World Population Percentage, input 'World' without quotes, else leave blank -> ").lower()
		plot_data(data, input_check)
	else:
		print("Invalid path, run the script again and input a valid path.")

if __name__ == "__main__":
	run()
