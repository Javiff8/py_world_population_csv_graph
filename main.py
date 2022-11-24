import sys
import os
import read_and_plot.charts as charts
import read_and_plot.utils as utils
import read_and_plot.read_file as readFile

def run():
	if len(sys.argv) > 1:
		path = sys.argv[1]
	else:
		path = input("Indicate the path to the csv file you want to read --> ")
	if os.path.exists(path):
		data = readFile.read_csv(path)
		if len(sys.argv) > 2:
			selected_country = sys.argv[2]
		else:
			selected_country = input("Input the full name of the country to plot -> ")
		country = utils.get_population_by_country(data, selected_country)
		if country:
			labels, values = utils.format_data(country[0])
			if labels and values:
				charts.bar_chart(labels, values)
			else:
				print(f"The country you indicated: {selected_country}, has no population data.")
		else:
			print(f"The country you indicated: {selected_country}, is not in the file.")
	else:
		print("Invalid path, run the script again and input a valid path.")

if __name__ == "__main__":
	run()
