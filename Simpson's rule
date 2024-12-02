import math

#from given material
def midpoint_approximation(f, N, a, b): #Midpoint approximation : calculates the area under the curve using rectangles centered at the midpoint of each subinterval.
    """
    Calculate an approximation to int_a^b f(x)
    with N midpoint-rectangles.
    """
    approximation = 0
    for i in range(N):
        approximation += (b - a) / N * f(a + (i + 1/2) * (b - a) / N)
    return approximation

#from exercise 9.1
def trapezium_approximation(f, N, a, b): #trapezium approximation: uses trapezoids to approximate the area under the curve, summing the areas of the trapezoids formed between adjacent points.
    """
    Calculate an approximation to int_a^b f(x)
    with N midpoint-rectangles
    """
    approximation = 0
    for i in range(N):
        approximation += (b - a)/(2*N) * (  f(a + i*(b-a)/N) + f(a + (i+1)*(b-a)/N)  )
    return approximation

#homework
def simpsons_rule(f, N, a, b): #Simpsons rule : combines both the function values at the endpoints and at the midpoint between adjacent points, using a weigted average to provide a more accurate estimate.
    """
    Calculate an approximation to int_a^b f(x)
    using Simpson's Rule with N intervals.
    """
    approximation = 0
    for i in range(N):
        x_i = a + i * (b - a) / N
        x_inc = a + (i + 1) * (b - a) / N
        x_mid = (x_i + x_inc) / 2 #mid between x_i and x_inc
        approximation += (b - a) / (6 * N) * (f(x_i) + 4 * f(x_mid) + f(x_inc))
    return approximation

def f(x):
    """Calculate x squared."""
    return x**2

def g(x):
    """Calculate x cubed."""
    return x**3

def h(x):
    """Calculate x to the fourth power."""
    return x**4

#Constant as stated in the question
N = 10
a, b = 0, 1

print("(i) ∫ 0 to 1 x^2 dx") #f "" these strings are used for formatting
print("Midpoint Approximation: {0:.6f}".format(midpoint_approximation(f, N, a, b)))
print("Trapezium Approximation: {0:.6f}".format(trapezium_approximation(f, N, a, b)))
print("Simpson's Rule: {0:.10f}\n".format(simpsons_rule(f, N, a, b)))

print("(ii) ∫ 0 to 1 x^3 dx")
print("Midpoint Approximation: {0:.6f}".format(midpoint_approximation(g, N, a, b)))
print("Trapezium Approximation: {0:.6f}".format(trapezium_approximation(g, N, a, b)))
print("Simpson's Rule: {0:.10f}\n".format(simpsons_rule(g, N, a, b)))

print("(iii) ∫ 0 to 1 x^4 dx")
print("Midpoint Approximation: {0:.6f}".format(midpoint_approximation(h, N, a, b)))
print("Trapezium Approximation: {0:.6f}".format(trapezium_approximation(h, N, a, b)))
print("Simpson's Rule: {0:.10f}\n".format(simpsons_rule(h, N, a, b)))
