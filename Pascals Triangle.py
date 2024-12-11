#function for hamming distance 
def hamming_distance(str1, str2): 
    hamming = 0
    if len(str1) > len(str2): 
        str2 = str2 + " "
    else: 
        str1 = str1 + " "
        
    for i in range(len(str1)) : #since str1 and str2 have the same length so it doesnt matter 
        if str1[i] != str2 : 
            hamming = hamming + 1
    return hamming
    
#main program 
str1 = str(input("enter the first string: "))
str2 = str(input("enter the second string: "))
print(hamming_distance(str1, str2))

#function square of number
#base : how to calculate square of number 
num = int(input("enter a number: "))
square = num*num
print(square)

#function square of number
def square(num): 
    square = num*num
    return square
    
#main program 
num = int(input("enter a number: "))
print("square of",num,"is",square(num))

#base how to change string to list of float 
num = "1 2 4 5.5 6.789"
print(num[:1]) #read the first char in str

#function string to vector
greeting = "Hello! How are you?"
print(greeting.lower())
print("I am well.".upper())
print(greeting.split())
print("1 3 5.5".split())

# main program
i = []
nstring = str(input("enter a list of number: "))
nsplit = nstring.split()
print(nsplit) #mmg dlm list [] 
i.append(nsplit) 
print(i) #dia dlm [[]]

#Change a space separated list of numbers to a list of floats
def string_to_vector_1(string):
    """
    Change a space separated list of
    numbers to a list of floats
    """
    string_list = string.split()
    float_list = []
    for s in string_list:
        float_list.append(float(s))
    return float_list

string = "1234"
print(string_to_vector_1(string))

#homework
#recap
#end = "" prevents moving to a new line, so next print statement output on the same line
def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product = product * i
    return product

#######try using factorial function here (wikipedia)#############
def binomial(n, k):
    if k > n:
        return 0
    if k > n - k: #symmetry in the binomial coefficient (n,k) = (n, n-k)
        k = n - k
    total = 1
    for i in range(k):
        total = total * (n - i) // (i + 1)
    return total

def pascals_triangle(num):
    triangle = []
    for n in range(num):
        row = [] #row by row
        for k in range(n + 1):
            coefficient = binomial(n, k)
            row.append(coefficient)
        triangle.append(row)
    maxwidth = len(str(triangle[-1][len(triangle[-1]) // 2])) + 2 #width of largest number + padding
    for n in range(num):
        spaces = (maxwidth * (num - n - 1)) // 2
        print(" " * spaces, end="") #print alignment
        for coefficient in triangle[n]:
            print(str(coefficient).center(maxwidth), end="")
        print()

#Main program
num = int(input("enter a number of rows of Pascal's triangle: "))
while num <= 0:
    num = int(input("bro enter a valid number pls"))
pascals_triangle(num)
