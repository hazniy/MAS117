import matplotlib.pyplot as plt #call plt instead of writing full matplotlib

x_values = [0, 1, 2, 3, 4]
y_values = [0, 4, 3, 4, 3.5]

plt.plot(x_values, y_values, color='red')
plt.plot(x_values, y_values, color='red', marker='o')
plt.plot(x_values, y_values, color='red', marker='o', linestyle='None')
plt.plot(x_values, y_values, 'r')
plt.plot(x_values, y_values, 'ro-')
plt.plot(x_values, y_values, 'ro')

#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html

y_values_2 = [2, 0, -1, 4, 2.5]
plt.plot(x_values, y_values_2, color='pink')

plt.title("A very basic plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
