import math 


def midpoint_approximation(f, N, a, b): 
   """
   Calculate an approximation to int_a^b f(x) 
   with N midpoint-rectangles 
   """
   approximation = 0 
   for i in range(N): 
       approximation += (b - a)/N * f(a + (i + 1/2)*(b - a)/N) 
   return approximation


def f(x): 
  """Calculate x squared."""
  return x**2 


def g(x): 
  """Calculate x squared."""
  return math.exp(x**2) 


print("int_0^1 x**2 dx is roughly {0:.6f}".format( #/i means integral for latex 
  midpoint_approximation(f, 2, 0, 1)))
print("int_0^1 e**(x**2) dx is roughly {0:.6f}".format(
  midpoint_approximation(g, 1000, 0, 1)))

#exercise 9.1
def trapezoidal_approximation(f, N, a, b): 
    """
    Calculate an approximation to int_a^b f(x) 
    with N midpoint-rectangles 
    """
    approximation = 0 
    for i in range(N): 
        approximation += (b - a)/(2*N) * (  f(a + i*(b-a)/N) + f(a + (i+1)*(b-a)/N)  )
    return approximation


def f(x): 
   """Calculate x squared."""
   return x**2 


def g(x): 
   """Calculate x squared."""
   return math.exp(x**2) 


print("int_0^1 x**2 dx is roughly {0:.6f}".format( #/i means integral for latex 
   midpoint_approximation(f, 2, 0, 1)))
print("int_0^1 e**(x**2) dx is roughly {0:.6f}".format(
   midpoint_approximation(g, 1000, 0, 1)))

def test_function(x):
     x = x + 2
     print("Inside the function: x =", x)
     return x
i = 2 
print("Before the function is called: i =", i)
i = test_function(i)
print("After the function is called: i =", i)

#exercise 9.3 recursive function 
def function(n): 
   """Calculate some mysterious functionnrecursively."""
   if n == 0:
      return 1
   return n*functiom(n-1) 

print(function(5))

