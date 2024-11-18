#choice() method returns a randomly selected element fro. the specified sequence 
#example choice() 
import random 
mylist = ["apple", "banana", "cherry"] #element 
print(random.choice(mylist)) 

#second attempt 
import random
from collections import Counter
vertices = 5 
steps = 7 

def journey(): 
  currentposition = 0 #always starts with 0 
  for i in range(steps): 
    nextstep = random.choice([-1,1])
    currentposition = currentposition + nextstep
  if currentposition < 0: 
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
  return currentposition 

endvertices = [journey() for i in range(128)] #why 128 ifs 2^7 which have 2 choice clockwise anti and 7 steps
vertexcounts = Counter(endvertices)

# Calculate and print percentages
print("\nvertex\trelative frequency(%)") 
print("-"* 26)
for vertex in range(vertices):
    percentage = (vertex_counts[vertex] / 128) * 100
    print(vertex, f"{percentage:.2f}", sep="\t") 

import random
from collections import Counter

# Constants
vertices = 5
steps = 7

def journey():
    """
    Simulates a random journey on a circular graph with `vertices` nodes.
    """
    currentposition = 0  # Start at position 0
    for _ in range(steps):
        nextstep = random.choice([-1, 1])  # Randomly choose direction
        currentposition += nextstep
    # Use modular arithmetic to wrap position within the vertex range
    currentposition %= vertices
    return currentposition

# Perform 128 random journeys
endvertices = [journey() for _ in range(128)]

# Count occurrences of each vertex
vertexcounts = Counter(endvertices)

# Calculate and print percentages
print("\nvertex\trelative frequency (%)")
print("-" * 26)
for vertex in range(vertices):
    percentage = (vertexcounts[vertex] / 128) * 100
    print(vertex, f"{percentage:.2f}", sep="\t")

#steps 
import random
from collections import Counter

# Constants
vertices = 5

def journey(steps):
    """
    Simulates a random journey on a circular graph with `vertices` nodes.
    The number of steps is passed as an argument.
    """
    currentposition = 0  # Start at position 0
    for _ in range(steps):
        nextstep = random.choice([-1, 1])  # Randomly choose direction
        currentposition += nextstep
    # Use modular arithmetic to wrap position within the vertex range
    currentposition %= vertices
    return currentposition

# Prompt the user for the number of steps
steps = int(input("Enter the number of steps: "))

# Perform 128 random journeys with the user-defined number of steps
endvertices = [journey(steps) for _ in range(128)]

# Count occurrences of each vertex
vertexcounts = Counter(endvertices)

# Calculate and print percentages
print("\nvertex\trelative frequency (%)")
print("-" * 26)
for vertex in range(vertices):
    percentage = (vertexcounts[vertex] / 128) * 100
    print(vertex, f"{percentage:.2f}", sep="\t")

#vertices 
import random
from collections import Counter

def journey(vertices, steps):
    """
    Simulates a random journey on a circular graph with `vertices` nodes.
    The number of steps is passed as an argument.
    """
    currentposition = 0  # Start at position 0
    for _ in range(steps):
        nextstep = random.choice([-1, 1])  # Randomly choose direction
        currentposition += nextstep
    # Use modular arithmetic to wrap position within the vertex range
    currentposition %= vertices
    return currentposition

# Prompt the user for the number of vertices and steps
vertices = int(input("Enter the number of vertices: "))
steps = int(input("Enter the number of steps: "))

# Perform 128 random journeys with the user-defined number of vertices and steps
endvertices = [journey(vertices, steps) for _ in range(128)]

# Count occurrences of each vertex
vertexcounts = Counter(endvertices)

# Calculate and print percentages
print("\nvertex\trelative frequency (%)")
print("-" * 26)
for vertex in range(vertices):
    percentage = (vertexcounts[vertex] / 128) * 100
    print(vertex, f"{percentage:.2f}", sep="\t")

