import csv

def read_csv(path):
	with open(path, 'r') as csvfile:
		reader = csv.reader(csvfile)
		header = next(reader)
		data = []
		for row in reader:
			iterable = zip(header, row)
			new_dict = dict(iterable)
			data.append(new_dict)
		return data
