import csv
import sys
import os

def read_csv(path):
	with open(path, 'r') as csvfile:
		reader = csv.reader(csvfile)
		header = next(reader)
		data = []
		for row in reader:
			iterable = zip(header, row)
			new_dict = {key: value for key, value in iterable}
			data.append(new_dict)
		return data

if __name__ == "__main__":
	path = sys.argv[1]
	if (not(path)):
		path = input("Indicate the path to the csv file you want to read --> ")
	if os.path.exists(path):
		data = read_csv(path)
		print(data)
	else:
		print("Invalid path, run the script again and input a valid path")
