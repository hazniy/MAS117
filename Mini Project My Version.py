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

#print graphical 
print("\nscore\trelative frequency") 
print("-"* 26)
for i in range(1,13): 
    #print(i, frequency[i]/NO_OF_TRIALS, sep ="\t") #prints out each line in the table, w the entries separated by tab
    print(i, int(100*frequency[i]/NO_OF_TRIALS), sep="\t") #want to make it graphical just add "*"* before int(100...)

#second attempt 
vertices = 5 
steps = 7 

def jorney(): 
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

#main 
endvertices = []
endvertices = endvertices + journey() for i in range(10000) 
vertexcount = len(endvertices) 
