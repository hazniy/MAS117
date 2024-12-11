#format(): taken first argument, and inserted where the {0} was. 
function =  "sin"
derivative = "cos"
template = "The derivative of {0} is {1}."
print(template.format(function,derivative))
#The derivative of sin is cos.
template = "An integral of {1} is {0}."
print(template.format(function, derivative))

#format specification : putting a colon after index 
print("={0}=".format("parrot"))
print("={0:20}=".format("parrot"))
print("={0:6}=".format("parrot")) #if the specified wisth is less than the str length, then no spaces are added
print("={0:5}=".format("parrot"))

import math 
print("Approximately, pi is {0}.".format(math.pi)) #3.141592653589793.
print("Approximately, pi is {0:.5f}.".format(math.pi)) #3.14159.
print("Approximately, pi is {0:.1f}.".format(math.pi)) #3.1.

#exercise 8.1 use format() with math.pi and math.e
#Output: Roughly, pi is 3.14 and e is 2.72.
print("Roughly, pi is {0:.2f}.".format(math.pi), "and e is {0:.2f}".format(math.e))

#width specification with floats as well 
print("Approximately, pi is {0:10.2f}.".format(math.pi))

#limit function
import math 

#f(a + 10^-i) for i = 1,...,n. For large n you can often get a sense of wether lim x-->a f(x) exists
def limit_table(f, a, n): #this function take another function as parameter
    """
    Print out a table of n values of the function f(x) 
    close to x = a. 
    """
    horizontal_line = "-" * 31
    
    print(horizontal_line)
    print("  {0:14}  {1:14}".format("x", "f(x)"))
    print(horizontal_line)
    
    for i in range(1, n+1): 
        print("{0:14.10f}  {1:14.10f}".format
              (a + 10**(-i), f(a + 10**(-i))))
    
    print(horizontal_line)

def f_1(x):
    """Calculate a simple rational function of x."""
    return (x**4 - x**3 + x**2 - 1)/(x - 1)

def f_2(x):
    """Calculate the function sin(7x)/x"""
    return math.sin(7*x)/x

#main
print("\nf(x) = (x**4 - x**3 + x**2 - 1)/(x - 1)")
limit_table(f_1, 1, 10)

print("\n\nf(x) = sin(7x)/x")
limit_table(f_2, 0, 10)

#exercise 8.2
#prints out the values just below x = a ✓
#tabulates f(a-10^-i) for i = 1,...,n ✓
import math 

def limit_table(f, a, n): 
    """
    Print out a table of n values of the function f(x) 
    close to x = a. 
    """
    horizontal_line = "-" * 31
    
    print(horizontal_line)
    print("  {0:14}  {1:14}".format("x", "f(x)"))
    print(horizontal_line)
    
    for i in range(1, n+1): 
        print("{0:14.10f}  {1:14.10f}".format
              (a - 10**(-i), f(a - 10**(-i))))
    
    print(horizontal_line)

def f_1(x):
    """Calculate a simple rational function of x."""
    return (x**4 - x**3 + x**2 - 1)/(x - 1)

def f_2(x):
    """Calculate the function sin(7x)/x"""
    return math.sin(7*x)/x

#main
print("\nf(x) = (x**4 - x**3 + x**2 - 1)/(x - 1)")
limit_table(f_1, 1, 10)

print("\n\nf(x) = sin(7x)/x")
limit_table(f_2, 0, 10)

#tabulates (x^2 - 1)/(x - 1) near x=1.✓
import math 

def limit_table(f, a, n): 
    """
    Print out a table of n values of the function f(x) 
    close to x = a. 
    """
    horizontal_line = "-" * 31
    
    print(horizontal_line)
    print("  {0:14}  {1:14}".format("x", "f(x)"))
    print(horizontal_line)
    
    for i in range(1, n+1): 
        print("{0:14.10f}  {1:14.10f}".format
              (a + 10**(-i), f(a + 10**(-i))))
    
    print(horizontal_line)

def f_1(x):
    """Calculate a simple rational function of x."""
    return (x**2 - 1)/(x - 1)

#main
print("\nf(x) = (x**2 - 1)/(x - 1)")
limit_table(f_1, 1, 10)

#mutability of sets 
menu = ["spam", "egg", "beans"]
print(menu[0]) #spam
menu[0] = "sausage"
print(menu) #['sausage', 'egg', 'beans']

#menu and food but only change food 
menu = ["spam", "egg", "beans"]
food = list(menu) #put the list()
print(food, menu)
food[2] = "jam"
print(food, menu)

#anonymous function using lambda
limit_table(lambda x : (x**4 - x**3 + x**2 -1)/(x-1), 1, 10)
limit_table(lambda x : math.sin(7*x)/x, 0, 10)




