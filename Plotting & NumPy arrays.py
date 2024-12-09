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

#plot sin(x) for x from 0 to 2pi, using 8 intervals 
import math 
import matplotlib.pyplot as plt

x_min = 0
x_max = 2*math.pi 
NO_OF_INTERVALS = 100 #more num intervals, smoother the line of the graph

x_values, y_values = [], []

for i in range(NO_OF_INTERVALS + 1): 
    x = x_min + i * (x_max - x_min)/ NO_OF_INTERVALS
    x_values.append(x)
    y_values.append(math.sin(x))

#print("\nx:", x_values, "\n\ny:", y_values, "\n") #to see value of x and y 

plt.plot(x_values, y_values, color='red')
#plt.gca().set_aspect("equal") #equal = same scale !important if want squares and circles to look correct
plt.title("sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()

#exercise 10.1
#plot cos(x) for x from 0 to 2pi, using 8 intervals 
import math 
import matplotlib.pyplot as plt

x_min = 0
x_max = 2*math.pi 
NO_OF_INTERVALS = 100 #more num intervals, smoother the line of the graph

x_values, y_values = [], []

for i in range(NO_OF_INTERVALS + 1): 
    x = x_min + i * (x_max - x_min)/ NO_OF_INTERVALS
    x_values.append(x)
    y_values.append(math.cos(x))

#print("\nx:", x_values, "\n\ny:", y_values, "\n") #to see value of x and y 

plt.plot(x_values, y_values, color='pink')

plt.title("Cos(x)")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.show()

#combine the sin(x) and cos(x) in one graph
#plot sin(x) for x from 0 to 2pi, using 8 intervals 
import math 
import matplotlib.pyplot as plt

x_min = 0
x_max = 2*math.pi 
NO_OF_INTERVALS = 100 #more num intervals, smoother the line of the graph

x_values, y_values, y2_values = [], [], []

for i in range(NO_OF_INTERVALS + 1): 
    x = x_min + i * (x_max - x_min)/ NO_OF_INTERVALS
    x_values.append(x)
    y_values.append(math.sin(x))
    y2_values.append(math.cos(x))

#print("\nx:", x_values, "\n\ny:", y_values, "\n") #to see value of x and y 

plt.plot(x_values, y_values, color='red')
plt.plot(x_values, y2_values, color='pink')
#plt.gca().set_aspect("equal") #equal = same scale !important if want squares and circles to look correct
plt.show()
###############################################NUMPY###################################################
import numpy as np #numpy array more like a vector than a list
array_1 = np.array([1.1, 2.2, 3.3]) #theres no comma here if using np
print(array_1)
type(array_1)
list_1 = [1.1, 2.2, 3.3]
print(list_1) 

print(list_1 + list_1) #[1.1, 2.2, 3.3, 1.1, 2.2, 3.3]
print(list_1 * 5) #[1.1, 2.2, 3.3, 1.1, 2.2, 3.3, 1.1, 2.2, 3.3, 1.1, 2.2, 3.3, 1.1, 2.2, 3.3]

#pointwise
print(array_1 + array_1) #[2.2 4.4 6.6] its added!
print(array_1 * 5) #[ 5.5 11.  16.5] 

print(np.exp(array_1), "\n", np.log(array_1)) 
#np.exp(array_1) for exponential
#np.log(array_1) for logarithm

#np.linspace(x_min, x_max, N) #create a NumPy array of N equally spaced points from x_min to x_max, which includes both endpoints.

print(np.linspace(0, 1, 11))
print(np.linspace(1, 3, 5))

import numpy as np 
import matplotlib.pyplot as plt 

x_values = np.linspace(0, 2*np.pi, 100)
plt.plot(x_values, np.sin(x_values), color='pink')
plt.plot(x_values, np.cos(x_values), color='red') #exercise 10.2 plot for cos(x)
plt.show()

#http://www.labri.fr/perso/nrougier/teaching/matplotlib/ #github of matplotlib
#homework 
import numpy as np
import matplotlib.pyplot as plt

x_e = np.linspace(-4, 2, 100)  # Range for exponential function
x_ln = np.linspace(0.01, 7.4, 100)  # Range for logarithmic function
#why stop at 7.5, e^2 = 7.39 so reasonable to stop at 7.4

x_straight = np.linspace(-4, 7.4, 100)
plt.plot(x_straight, x_straight, linestyle='None')

plt.plot(x_exp, np.exp(x_e), color='red')
plt.plot(x_log,  np.log(x_ln), color='pink')

# Add title
plt.title('Exponential and Logarithmic Functions')
plt.xlabel('x')
plt.ylabel('e^x // ln(x)')
plt.show()

#another way if dont know about the log range 
import numpy as np
import matplotlib.pyplot as plt

#rules of log and e
#y = e^x --> x = ln(y)

#x and y values of exponential
x_e = np.linspace(-4, 2, 100)
y_e = np.exp(x_e)

#x and y values of log
x_ln = y_e
y_ln = np.log(x_ln)

#a line
x_straight = np.linspace(-4, 7.4, 100)
plt.plot(x_straight, x_straight, linestyle='-')

plt.plot(x_e, y_e, color='red')
plt.plot(x_ln, y_ln, color='pink')

plt.title('Exponential and Logarithmic Functions')
plt.xlabel('x')
plt.ylabel('$e^x$ $\ln(x)$')
plt.show()
