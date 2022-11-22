import matplotlib.pyplot as plt

def bar_chart(labels, values):
	fig, ax = plt.subplots()
	ax.bar(labels, values)
	plt.show()

def pie_chart(labels, values):
	fig, ax = plt.subplots()
	ax.pie(values, labels=labels)
	ax.axis("equal")
	plt.show()

if __name__ == "__main__":
	labels = ["a", "b", "c"]
	values = [100, 200, 300]
	bar_chart(labels, values)
	pie_chart(labels, values)
