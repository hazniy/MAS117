#choice() method returns a randomly selected element fro. the specified sequence 
#example choice() 
import random 
mylist = ["apple", "banana", "cherry"] #element 
print(random.choice(mylist)) 

import random 
#define parameters 
vertices = 5 #theres 5 vertices 
steps = 7 #there are 7 steps to complete 1 cycle 

def journey(): 
  currentvertex = 0 
  for i in range (steps): 
    step = random.choice([-1,1]) #anticlockwise & clockwise 
    currentvertex = (currentvertex + step) % vertices
  return currentvertex

#main 
endvertices = []
endvertices = endvertices + journey() for i in range(10000) 
vertexcount = len(endvertices) 

for vertex in range(vertices): 
  percentage = (vertexcount/10000)*100 
  print(f"Vertex {vertex: {percentage:.2f}%"}


  
