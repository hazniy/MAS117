import math

def infinite_limit_table(f, n):
    """
    Print out a table of n values of the function f(x) 
    """
    horizontal_line = "-" * 31

    print(horizontal_line)
    print("  {0:14}  {1:14}".format("x", "f(x)"))
    print(horizontal_line)

    for i in range(1, n + 1):
        x = 10**i
        value = f(x)
        print("{0:14.2f}  {1:14.9f}".format
            (float(x), value))

    print(horizontal_line)

def g(x):
    return x**(1/x)

def h(x):
    return (1 + 1/x)**x

# Main 
print("\ng(x) = x^(1/x)")
infinite_limit_table(g, 10)  

print("\nh(x) = (1 + 1/x)^x")
infinite_limit_table(h, 10)  
