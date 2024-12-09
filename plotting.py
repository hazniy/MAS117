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

#parametric equation of a curve
import numpy as np 
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 200)
for k in range(2, 7): 
    plt.plot(1.2*np.cos(theta) - np.cos(k*theta),
             1.5*np.sin(theta) - np.sin(k*theta))
plt.gca().set_aspect("equal")
plt.axis([-3, 3, -3, 3])
plt.show()

#lots of spokes in a wheel 
import numpy as np 
import matplotlib.pyplot as plt

NO_OF_SPOKES = 17 
for i in range(NO_OF_SPOKES):
    phi = i * 2 * np.pi / NO_OF_SPOKES
    plt.plot([0, np.cos(phi)], [0, np.sin(phi)], color='pink')

plt.gca().set_aspect("equal") #make sure the scaling on x & y axes is the same
plt.axis([-1.1, 1.1, -1.1, 1.1]) #[2,x,x,x] starts of x axis #[x,2,x,x] ends of x axis etc
plt.show()

#exercise 11.2 draw outline of a chess board
import numpy as np 
import matplotlib.pyplot as plt

NO_OF_SPOKES = 18 
for i in range(NO_OF_SPOKES): 
    plt.plot([i, i], [0, 8], color='blue')
    plt.plot([0, 8], [i, i], color='blue')

plt.gca().set_aspect("equal")
plt.axis([-1, 9, -1, 9])
plt.show()

#circle with another circle inside
import numpy as np
import matplotlib.pyplot as plt
def draw_circle(centre, radius):
    """Draw a black circle with specified centre and radius."""
    theta = np.linspace(0, 2*np.pi, 100)
    plt.plot(radius*np.cos(theta) + centre[0],
            radius*np.sin(theta) + centre[1],
            color="black")

draw_circle([0, 0], 5)
draw_circle([0, 0], 1)
draw_circle([3, 0], 2)
draw_circle([-3, 0], 2)
draw_circle([0, 3], 2)
draw_circle([0, -3], 2)
plt.gca().set_aspect("equal")
plt.show()

#exercise 11.3 spider web
import numpy as np
import matplotlib.pyplot as plt

def draw_circle(centre, radius):
    """Draw a black circle with specified centre and radius."""
    theta = np.linspace(0, 2 * np.pi, 100)
    plt.plot(
        radius * np.cos(theta) + centre[0],
        radius * np.sin(theta) + centre[1],
        color="black"
    )

# Parameters
NO_OF_SPOKES = 17  # Number of spokes
NO_OF_CIRCLES = 9  # Number of concentric circles
MAX_RADIUS = 1.0   # Maximum radius of the outermost circle

# Draw concentric circles
for i in range(1, NO_OF_CIRCLES + 1):
    radius = MAX_RADIUS * i / NO_OF_CIRCLES
    draw_circle([0, 0], radius)

# Draw spokes
for i in range(NO_OF_SPOKES):
    phi = i * 2 * np.pi / NO_OF_SPOKES
    x = MAX_RADIUS * np.cos(phi)
    y = MAX_RADIUS * np.sin(phi)
    plt.plot([0, x], [0, y], color="pink")

# Adjust plot settings
plt.axis("equal")  # Ensure equal aspect ratio
plt.axis([-1.1, 1.1, -1.1, 1.1])  # Extend axis limits slightly for visibility
plt.show()

#save picture png
plt.savefig("picture.png")
