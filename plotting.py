import numpy as np 
import matplotlib.pyplot as plt

#for circle graph
theta = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(theta), np.sin(theta)) #x val and y val 
plt.gca().set_aspect("equal") #make sure the scaling on x & y axes is the same
plt.axis([-1.1, 1.1, -1.1, 1.1]) #[2,x,x,x] starts of x axis #[x,2,x,x] ends of x axis etc
plt.show()

#exercise 11.1
#ellipse
import numpy as np 
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 100)
plt.plot(np.cos(theta)*0.3, np.sin(theta)*0.5) #x val and y val 
plt.gca().set_aspect("equal") #make sure the scaling on x & y axes is the same
plt.axis([-1.1, 1.1, -1.1, 1.1]) #[2,x,x,x] starts of x axis #[x,2,x,x] ends of x axis etc
plt.show()

#archimedean spiral 
theta = np.linspace(0, 4*np.pi, 100)
plt.plot(theta*np.cos(theta), theta*np.sin(theta)) #x val and y val 
plt.gca().set_aspect("equal") #make sure the scaling on x & y axes is the same
plt.show()
