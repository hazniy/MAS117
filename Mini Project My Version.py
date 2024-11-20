#choice() method : Returns a randomly selected element from the specified sequence.
#Example choice()
import random
mylist = ["apple", "banana", "cherry"] #list of elements
print(random.choice(mylist))

#First attempt (only with 5 vertices)
import random
from collections import Counter

#Define the number of vertices & steps for the journey
vertices = 5 #Total vertices
steps = 7 #Number of steps

def journey():
  currentposition = 0 #Start position is always vertex 0
  for i in range(steps):
    nextstep = random.choice([-1,1]) #Randomly choose the next step which -1(backward) or 1(forward)
    currentposition = currentposition + nextstep #Update the current position

#Handle cases where the position becomes negative (which looping back to positive vertices)
  if currentposition < 0:
    #Map (-) positions to the corresponding (+) vertices
    if currentposition == -1 or currentposition == -6:
      currentposition = 4
    elif currentposition == -2 or currentposition == -7:
      currentposition = 3
    elif currentposition == -3:
      currentposition = 2
    elif currentposition == -4:
      currentposition = 1
    elif currentposition == -5:
      currentposition = 0
  return currentposition #Return the final position after the journey

endvertices = [journey() for i in range(128)] #Simulate 128 journeys (128 is chosen becuase it's 2^7, cont.
vertexcounts = Counter(endvertices)           #where 7 is the num of steps and 2 choices (backward & forward)

#Calculate and print percentages
print("\nvertex\tfrequency(%)")
print("-"* 26)
for vertex in range(vertices):
    #Calculate the percentage for each vertex
    percentage = (vertexcounts[vertex] / 128) * 100
    print(vertex, f"{percentage:.3f}", sep="\t")

#Second attempt (with a flexible number of vertices)
import random
from collections import Counter

#Constants
vertices = 5 #Total number of vertices
steps = 7 #Number of steps

def journey():
    currentposition = 0  #Start at vertex 0
    for i in range(steps):
        nextstep = random.choice([-1, 1])  #Randomly choose direction
        currentposition = currentposition + nextstep
    currentposition = currentposition % vertices  #if vertices = 5: positions -1 and 5 both map to vertex 4. Always Positive
    return currentposition

endvertices = [journey() for i in range(128)]
vertexcounts = Counter(endvertices)

print("\nvertex\tfrequency (%)")
print("-" * 26)
for vertex in range(vertices):
    percentage = (vertexcounts[vertex] / 128) * 100
    print(vertex, f"{percentage:.3f}", sep="\t")

#Extending the project further
#What effect the number of steps has on the percentages
import random
from collections import Counter

#Constants
vertices = 5

def journey(steps):
    currentposition = 0
    for i in range(steps):
        nextstep = random.choice([-1, 1])
        currentposition = currentposition + nextstep
    currentposition = currentposition % vertices
    return currentposition

#Prompt the user for the number of steps
steps = int(input("Enter the number of steps: "))
endvertices = [journey(steps) for i in range(pow(2, steps))]
vertexcounts = Counter(endvertices)

print("\nvertex\tfrequency (%)")
print("-" * 26)
for vertex in range(vertices):
    percentage = (vertexcounts[vertex] / (pow(2, steps))) * 100
    print(vertex, f"{percentage:.3f}", sep="\t")

#Change the number of vertices on the polygon
import random
from collections import Counter

def journey(vertices, steps):
    currentposition = 0
    for i in range(steps):
        nextstep = random.choice([-1, 1])
        currentposition = currentposition + nextstep
    currentposition = currentposition % vertices
    return currentposition

#Prompt the user for the number of vertices and steps
vertices = int(input("Enter the number of vertices: "))
steps = int(input("Enter the number of steps: "))
endvertices = [journey(vertices, steps) for i in range(pow(2, steps))]
vertexcounts = Counter(endvertices)

print("\nvertex\trelative frequency (%)")
print("-" * 26)
for vertex in range(vertices):
    percentage = (vertexcounts[vertex] / (pow(2, steps))) * 100
    print(vertex, f"{percentage:.2f}", sep="\t")
