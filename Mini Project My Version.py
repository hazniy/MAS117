#choice() method : Returns a randomly selected element from the specified sequence.
#Example choice()
import random
mylist = ["apple", "banana", "cherry"] #list of elements
print(random.choice(mylist))

###############First attempt (only with 5 vertices)###############
import random
from collections import Counter

#Define the number of vertices & steps for the journey
totvertices = 5 #Total vertices
totsteps = 7 #Number of steps

def randomwalk():
  position = 0 #Start position is always vertex 0
  for step in range(totsteps):
    move = random.choice([-1,1]) #Randomly choose the next step which -1(backward) or 1(forward)
    position = position + move #Update the current position

#Handle cases where the position becomes negative (which looping back to positive vertices)
  if position < 0:
    #Map (-) positions to the corresponding (+) vertices
    if position == -1 or position == -6:
      position = 4
    elif position == -2 or position == -7:
      position = 3
    elif position == -3:
      position = 2
    elif position == -4:
      position = 1
    elif position == -5:
      position = 0
  return position #Return the final position after the journey

finalpositions = [randomwalk() for i in range(128)] #Simulate 128 journeys (128 is chosen becuase it's 2^7, cont.
positioncounts = Counter(finalpositions)           #where 7 is the num of steps and 2 choices (backward & forward)

#Calculate and print percentages
print("\nvertex\tfrequency(%)")
print("-"* 26)
for vertex in range(totvertices):
    #Calculate the percentage for each vertex
    frequency = (positioncounts[vertex] / 128) * 100
    print(vertex, f"{frequency:.3f}", sep="\t")

###############Second attempt (with a flexible number of vertices)###############
import random
from collections import Counter

#Constants
totvertices = 5 #Total number of vertices
totsteps = 7 #Number of steps

def randomwalk():
    position = 0  #Start at vertex 0
    for i in range(totsteps):
        move = random.choice([-1, 1])  #Randomly choose direction
        position = position + move
    position = position % totvertices  #if vertices = 5: positions -1 and 5 both map to vertex 4. Always Positive
    return position

finalpositions = [randomwalk() for i in range(128)]
positioncounts = Counter(finalpositions)

print("\nvertex\tfrequency (%)")
print("-" * 26)
for vertex in range(totvertices):
    frequency = (positioncounts[vertex] / 128) * 100
    print(vertex, f"{frequency:.3f}", sep="\t")

###############Extending the project further###############
#What effect the number of steps has on the percentages
import random
from collections import Counter

#Constants
totvertices = 5

def randomwalk(steps):
    position = 0
    for i in range(steps):
        move = random.choice([-1, 1])
        position = position + move
    position = position % totvertices
    return position

#Prompt the user for the number of steps
steps = int(input("Enter the number of steps: "))
finalpositions = [randomwalk(steps) for i in range(pow(2, steps))]
positioncounts = Counter(finalpositions)

print("\nvertex\tfrequency (%)")
print("-" * 26)
for vertex in range(totvertices):
    frequency = (positioncounts[vertex] / (pow(2, steps))) * 100
    print(vertex, f"{frequency:.3f}", sep="\t")

###############Change the number of vertices on the polygon################
import random
from collections import Counter

def randomwalk(vertices, steps):
    position = 0
    for i in range(steps):
        move = random.choice([-1, 1])
        position = position + move
    position = position % vertices
    return position

#Prompt the user for the number of steps
steps = int(input("Enter the number of steps: "))
vertices = int(input("Enter the number of vertices: "))
finalpositions = [randomwalk(vertices, steps) for i in range(pow(2, steps))]
positioncounts = Counter(finalpositions)

print("\nvertex\tfrequency (%)")
print("-" * 26)
for vertex in range(vertices):
    frequency = (positioncounts[vertex] / (pow(2, steps))) * 100
    print(vertex, f"{frequency:.3f}", sep="\t")
