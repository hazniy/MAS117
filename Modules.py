import random 
print(random.random())
print("random number between 0 and 10:",10*random.random())
dice_score = random.randrange(1,7)
print(dice_score)

import random #imports random module we will use to stimulate the dice roll
random.seed() #randomizes the randomizer
NO_OF_TRIALS = 100 #sets num of times that we will roll the dice
frequency = [0]*13 #initializes each element in the list of frequencies = 0 

for i in range(NO_OF_TRIALS):
    dice_score = random.randrange(1,7) + random.randrange(1,7) 
    frequency[dice_score] = frequency[dice_score] + 1
    #print("dice score =", dice_score, end="; ")
    #print("frequency list =", frequency)
print("\nscore\trelative frequency") 
print("-"* 26)
for i in range(1,13): 
    #print(i, frequency[i]/NO_OF_TRIALS, sep ="\t") #prints out each line in the table, w the entries separated by tab
    print(i, int(100*frequency[i]/NO_OF_TRIALS), sep="\t") #want to make it graphical just add "*"* before int(100...)

#exercise 6.1 rolling 2 dice and taking their sums 
#line thats change here
#frequency = [0, 0, 0, 0, 0, 0, 0] ====> frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ====> frequency = [0]*13
#dice_score = random.randrange(1,7) ====> dice_score = random.randrange(1,7) + random.randrange(1,7) 
#for i in range(1,7): ====> for i in range(1,13): 
    
import math 
print(math.pi)
print(math.e)
print(math.log(10))
print(math.sin(1))
print(math.radians(180))
print(math.degrees(math.pi))
#command like trigo hyperbolic https://docs.python.org/3.6/library/math.html.
print(math.sin(math.pi))
print(1.455e6, "\t", 1.455e-4)

import math 
NO_OF_INTERVALS = 40
HORIZONTAL_LINE = "-" * 48 

print(HORIZONTAL_LINE)
print("x\t\t\tsin(x)")
print(HORIZONTAL_LINE)
for i in range(NO_OF_INTERVALS + 1): 
    x = 2 * math.pi * i / NO_OF_INTERVALS
    #print(x, math.sin(x), sep="\t")
    print("{0:f}\t{1: f}".format(x, math.sin(x))) #more organize
print(HORIZONTAL_LINE)

#exercise 6.2 plot graph sin(x)
#NO_OF_INTERVALS = 16 ===> NO_OF_INTERVALS = 40
import math
NO_OF_INTERVALS = 40
for i in range(NO_OF_INTERVALS + 1):
    x = 2 * math.pi * i / NO_OF_INTERVALS
    print(" " * int(30 * (1 + math.sin(x))) + "*")

#random shit
import math
NO_OF_INTERVALS = 40
for i in range(NO_OF_INTERVALS + 1):
    x = 4 * (i / NO_OF_INTERVALS - 1/2)
    y = math.exp(-x**2)
    print("{0:f}".format(x), "*"*int(40*(y)), sep="\t")

