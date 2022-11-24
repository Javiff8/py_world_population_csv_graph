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
